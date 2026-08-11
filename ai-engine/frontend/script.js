const API_URL = "http://localhost:8000";

let latestAnalysis = null;


/* =========================================================
   NAVIGATION
========================================================= */

const navItems = document.querySelectorAll(".nav-item");
const pages = document.querySelectorAll(".page");

const pageInfo = {

    overview: {
        title: "Overview",
        subtitle:
            "AI-powered DevOps and platform engineering analysis"
    },

    repository: {
        title: "Repository Analysis",
        subtitle:
            "Analyze GitHub repositories for DevOps issues"
    },

    analysis: {
        title: "Infrastructure Analysis",
        subtitle:
            "Analyze Docker, Kubernetes, Helm and Jenkins"
    },

    fixes: {
        title: "AI Fixes",
        subtitle:
            "Generate improved infrastructure configuration"
    },

    monitoring: {
        title: "Monitoring",
        subtitle:
            "Observe platform and application metrics"
    },

    kubernetes: {
        title: "Kubernetes",
        subtitle:
            "Analyze the live Kubernetes cluster"
    },

    incidents: {
        title: "Incidents",
        subtitle:
            "Generate monitoring and incident reports"
    }

};


function showPage(section) {

    pages.forEach(page => {
        page.classList.remove("active");
    });

    navItems.forEach(item => {
        item.classList.remove("active");
    });

    const page = document.getElementById(section);

    const nav = document.querySelector(
        `.nav-item[data-section="${section}"]`
    );

    if (page) {
        page.classList.add("active");
    }

    if (nav) {
        nav.classList.add("active");
    }

    const info = pageInfo[section];

    if (info) {

        document.getElementById("pageTitle").textContent =
            info.title;

        document.getElementById("pageSubtitle").textContent =
            info.subtitle;
    }
}


navItems.forEach(item => {

    item.addEventListener("click", () => {

        showPage(item.dataset.section);

    });

});


document.querySelectorAll("[data-goto]").forEach(button => {

    button.addEventListener("click", () => {

        showPage(button.dataset.goto);

    });

});


/* =========================================================
   API HEALTH
========================================================= */

async function checkAPI() {

    const dot = document.getElementById("apiDot");
    const status = document.getElementById("apiStatus");

    try {

        const response = await fetch(
            `${API_URL}/health`
        );

        if (!response.ok) {
            throw new Error("API unavailable");
        }

        dot.classList.remove("offline");
        dot.classList.add("online");

        status.textContent = "Connected";

        document.getElementById("overviewApi").textContent =
            "Online";

    } catch (error) {

        dot.classList.remove("online");
        dot.classList.add("offline");

        status.textContent = "Offline";

        document.getElementById("overviewApi").textContent =
            "Offline";
    }
}


checkAPI();


/* =========================================================
   REPOSITORY ANALYSIS
========================================================= */

const analyzeBtn =
    document.getElementById("analyzeBtn");


analyzeBtn.addEventListener(
    "click",
    analyzeRepository
);


async function analyzeRepository() {

    const input =
        document.getElementById("repoUrl");

    const status =
        document.getElementById("analysisStatus");

    const url =
        input.value.trim();


    if (!url) {

        status.textContent =
            "Enter a GitHub repository URL.";

        return;
    }


    if (!url.startsWith("https://github.com/")) {

        status.textContent =
            "Please enter a valid GitHub repository URL.";

        return;
    }


    analyzeBtn.disabled = true;

    analyzeBtn.textContent =
        "Analyzing...";

    status.textContent =
        "Cloning and analyzing repository...";


    try {

        const response = await fetch(
            `${API_URL}/analyze/repository`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    repo_url: url
                })
            }
        );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Repository analysis failed."
            );
        }


        latestAnalysis = data;

        displayRepositoryResults(data);

        status.textContent =
            "Analysis completed successfully.";

        const now =
            new Date().toLocaleString();

        document.getElementById(
            "lastUpdated"
        ).textContent = now;

        document.getElementById(
            "overviewTime"
        ).textContent =
            new Date().toLocaleTimeString(
                [],
                {
                    hour: "2-digit",
                    minute: "2-digit"
                }
            );

        document.getElementById(
            "overviewScore"
        ).textContent =
            data.overall_score ?? "--";


    } catch (error) {

        console.error(error);

        status.textContent =
            `Error: ${error.message}`;

    } finally {

        analyzeBtn.disabled = false;

        analyzeBtn.textContent =
            "Analyze Repository";
    }
}


/* =========================================================
   DISPLAY REPOSITORY RESULTS
========================================================= */

function displayRepositoryResults(data) {

    document
        .getElementById("repositorySummary")
        .classList.remove("hidden");


    const score =
        Number(data.overall_score);


    document.getElementById(
        "overallScore"
    ).textContent =
        Number.isFinite(score)
            ? score
            : "--";


    document.getElementById(
        "scoreRingValue"
    ).textContent =
        Number.isFinite(score)
            ? score
            : "--";


    renderComponentScores(data);

    renderIssues(data);

    renderRecommendations(data);

    updateIssueCount(data);
}


/* =========================================================
   COMPONENT SCORES
========================================================= */

function renderComponentScores(data) {

    const container =
        document.getElementById(
            "componentScores"
        );


    container.innerHTML = "";


    const components = [
        ["Docker", "docker"],
        ["Kubernetes", "kubernetes"],
        ["Terraform", "terraform"],
        ["Helm", "helm"],
        ["Jenkins", "jenkins"]
    ];


    components.forEach(
        ([name, key]) => {

            const component =
                data[key];


            if (!component) {
                return;
            }


            const card =
                document.createElement("div");


            card.className =
                "score-card";


            card.innerHTML = `
                <span>${escapeHtml(name)}</span>

                <strong>
                    ${component.score ?? "N/A"}
                </strong>
            `;


            container.appendChild(card);

        }
    );
}


/* =========================================================
   ISSUES
========================================================= */

function renderIssues(data) {

    const container =
        document.getElementById(
            "issuesContainer"
        );


    container.innerHTML = "";


    const components = [
        ["Docker", "docker"],
        ["Kubernetes", "kubernetes"],
        ["Terraform", "terraform"],
        ["Helm", "helm"],
        ["Jenkins", "jenkins"]
    ];


    components.forEach(
        ([name, key]) => {

            const component =
                data[key];


            if (
                !component ||
                !Array.isArray(component.issues) ||
                component.issues.length === 0
            ) {
                return;
            }


            const group =
                document.createElement("div");


            group.className =
                "issue-group";


            const issues =
                component.issues
                    .map(
                        issue =>
                            `<li>${escapeHtml(issue)}</li>`
                    )
                    .join("");


            group.innerHTML = `
                <div class="issue-title">
                    ${escapeHtml(name)}
                </div>

                <ul class="issue-list">
                    ${issues}
                </ul>
            `;


            container.appendChild(group);

        }
    );


    if (!container.children.length) {

        container.innerHTML =
            "<p>No issues found.</p>";
    }
}


/* =========================================================
   RECOMMENDATIONS
========================================================= */

function renderRecommendations(data) {

    const container =
        document.getElementById(
            "recommendationsContainer"
        );


    container.innerHTML = "";


    let recommendations = [];


    if (Array.isArray(data.recommendations)) {

        recommendations =
            data.recommendations;
    }


    if (!recommendations.length) {

        const components = [
            "docker",
            "kubernetes",
            "terraform",
            "helm",
            "jenkins"
        ];


        components.forEach(key => {

            if (
                data[key] &&
                Array.isArray(
                    data[key].recommendations
                )
            ) {

                recommendations.push(
                    ...data[key].recommendations
                );
            }

        });
    }


    recommendations =
        [...new Set(recommendations)];


    if (!recommendations.length) {

        container.innerHTML =
            "<p>No recommendations available.</p>";

        return;
    }


    const list =
        document.createElement("ul");


    list.className =
        "recommendation-list";


    recommendations.forEach(
        recommendation => {

            const li =
                document.createElement("li");

            li.textContent =
                recommendation;

            list.appendChild(li);

        }
    );


    container.appendChild(list);
}


/* =========================================================
   ISSUE COUNT
========================================================= */

function updateIssueCount(data) {

    let count = 0;


    [
        "docker",
        "kubernetes",
        "terraform",
        "helm",
        "jenkins"
    ].forEach(key => {

        if (
            data[key] &&
            Array.isArray(data[key].issues)
        ) {

            count +=
                data[key].issues.length;
        }

    });


    document.getElementById(
        "issueCount"
    ).textContent = count;
}


/* =========================================================
   INDIVIDUAL ANALYZERS
========================================================= */

document.querySelectorAll(
    ".analyzer-btn"
).forEach(button => {

    button.addEventListener(
        "click",
        async () => {

            await runAnalyzer(
                button.dataset.endpoint,
                button.dataset.name,
                button
            );

        }
    );

});


async function runAnalyzer(
    endpoint,
    name,
    button
) {

    const output =
        document.getElementById(
            "analysisOutput"
        );

    const title =
        document.getElementById(
            "analysisOutputTitle"
        );


    button.disabled = true;

    button.textContent =
        "Running...";


    title.textContent =
        `${name} Analysis`;


    output.textContent =
        "Running analyzer...";


    try {

        const response =
            await fetch(
                `${API_URL}${endpoint}`,
                {
                    method: "POST"
                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                `${name} analysis failed`
            );
        }


        output.textContent =
            JSON.stringify(
                data,
                null,
                2
            );


    } catch (error) {

        output.textContent =
            `Error: ${error.message}`;

    } finally {

        button.disabled = false;

        button.textContent =
            "Analyze";
    }
}


/* =========================================================
   FIXERS
========================================================= */

document.querySelectorAll(
    ".fixer-btn"
).forEach(button => {

    button.addEventListener(
        "click",
        async () => {

            await runFixer(
                button.dataset.endpoint,
                button.dataset.name,
                button
            );

        }
    );

});


async function runFixer(
    endpoint,
    name,
    button
) {

    const output =
        document.getElementById(
            "fixOutput"
        );

    const message =
        document.getElementById(
            "fixMessage"
        );


    button.disabled = true;

    button.textContent =
        "Generating...";


    output.classList.remove(
        "hidden"
    );


    message.textContent =
        `Generating ${name} fix...`;


    try {

        const response =
            await fetch(
                `${API_URL}${endpoint}`,
                {
                    method: "POST"
                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                `${name} fix failed`
            );
        }


        message.innerHTML = `
            <p>
                ${escapeHtml(
                    data.message ||
                    `${name} fix generated successfully.`
                )}
            </p>

            ${
                data.download_url
                    ? `
                        <a
                            class="primary-btn"
                            href="${API_URL}${data.download_url}"
                            target="_blank"
                        >
                            Download Fix
                        </a>
                    `
                    : ""
            }
        `;


    } catch (error) {

        message.textContent =
            `Error: ${error.message}`;

    } finally {

        button.disabled = false;

        button.textContent =
            "Generate Fix";
    }
}


/* =========================================================
   FIX ALL
========================================================= */

document
    .getElementById("fixAllBtn")
    .addEventListener(
        "click",
        async () => {

            const button =
                document.getElementById(
                    "fixAllBtn"
                );

            const output =
                document.getElementById(
                    "fixOutput"
                );

            const message =
                document.getElementById(
                    "fixMessage"
                );


            button.disabled = true;

            button.textContent =
                "Generating...";


            output.classList.remove(
                "hidden"
            );


            message.textContent =
                "Generating all fixes...";


            try {

                const response =
                    await fetch(
                        `${API_URL}/fix/all`,
                        {
                            method: "POST"
                        }
                    );


                const data =
                    await response.json();


                if (!response.ok) {

                    throw new Error(
                        data.detail ||
                        "Fix generation failed"
                    );
                }


                message.textContent =
                    data.message ||
                    "All fixes generated successfully.";


            } catch (error) {

                message.textContent =
                    `Error: ${error.message}`;

            } finally {

                button.disabled = false;

                button.textContent =
                    "Generate All Fixes";
            }

        }
    );


/* =========================================================
   MONITORING
========================================================= */

document
    .getElementById("monitorBtn")
    .addEventListener(
        "click",
        async () => {

            const button =
                document.getElementById(
                    "monitorBtn"
                );

            const output =
                document.getElementById(
                    "monitorOutput"
                );


            button.disabled = true;

            button.textContent =
                "Analyzing...";


            output.textContent =
                "Running monitoring analysis...";


            try {

                const response =
                    await fetch(
                        `${API_URL}/analyze/monitoring`
                    );


                const data =
                    await response.json();


                if (!response.ok) {

                    throw new Error(
                        data.detail ||
                        "Monitoring analysis failed"
                    );
                }


                output.textContent =
                    JSON.stringify(
                        data,
                        null,
                        2
                    );


            } catch (error) {

                output.textContent =
                    `Error: ${error.message}`;

            } finally {

                button.disabled = false;

                button.textContent =
                    "Run Monitoring Analysis";
            }

        }
    );


/* =========================================================
   METRICS
========================================================= */

document
    .getElementById("metricsBtn")
    .addEventListener(
        "click",
        async () => {

            const output =
                document.getElementById(
                    "monitorOutput"
                );


            output.textContent =
                "Loading Prometheus metrics...";


            try {

                const response =
                    await fetch(
                        `${API_URL}/metrics`
                    );


                const data =
                    await response.text();


                if (!response.ok) {

                    throw new Error(
                        "Unable to fetch metrics"
                    );
                }


                output.textContent =
                    data;


            } catch (error) {

                output.textContent =
                    `Error: ${error.message}`;
            }

        }
    );


/* =========================================================
   KUBERNETES
========================================================= */

document
    .getElementById("kubernetesBtn")
    .addEventListener(
        "click",
        async () => {

            const button =
                document.getElementById(
                    "kubernetesBtn"
                );

            const output =
                document.getElementById(
                    "kubernetesOutput"
                );


            button.disabled = true;

            button.textContent =
                "Analyzing...";


            output.textContent =
                "Analyzing live Kubernetes cluster...";


            try {

                const response =
                    await fetch(
                        `${API_URL}/analyze/kubernetes/live`
                    );


                const data =
                    await response.json();


                if (!response.ok) {

                    throw new Error(
                        data.detail ||
                        "Kubernetes analysis failed"
                    );
                }


                output.textContent =
                    JSON.stringify(
                        data,
                        null,
                        2
                    );


            } catch (error) {

                output.textContent =
                    `Error: ${error.message}`;

            } finally {

                button.disabled = false;

                button.textContent =
                    "Analyze Live Cluster";
            }

        }
    );


/* =========================================================
   INCIDENT REPORT
========================================================= */

document
    .getElementById("incidentBtn")
    .addEventListener(
        "click",
        async () => {

            const button =
                document.getElementById(
                    "incidentBtn"
                );

            const output =
                document.getElementById(
                    "incidentOutput"
                );


            button.disabled = true;

            button.textContent =
                "Generating...";


            output.textContent =
                "Generating incident report...";


            try {

                const response =
                    await fetch(
                        `${API_URL}/incident/report`
                    );


                const data =
                    await response.json();


                if (!response.ok) {

                    throw new Error(
                        data.detail ||
                        "Incident report failed"
                    );
                }


                output.textContent =
                    JSON.stringify(
                        data,
                        null,
                        2
                    );


            } catch (error) {

                output.textContent =
                    `Error: ${error.message}`;

            } finally {

                button.disabled = false;

                button.textContent =
                    "Generate Report";
            }

        }
    );


/* =========================================================
   REFRESH
========================================================= */

document
    .getElementById("refreshBtn")
    .addEventListener(
        "click",
        () => {

            checkAPI();

            if (latestAnalysis) {
                displayRepositoryResults(
                    latestAnalysis
                );
            }

        }
    );


/* =========================================================
   HTML ESCAPING
========================================================= */

function escapeHtml(value) {

    const div =
        document.createElement("div");

    div.textContent =
        String(value);

    return div.innerHTML;
}
