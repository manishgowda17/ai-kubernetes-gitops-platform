const analyzeBtn = document.getElementById("analyze-btn");
const dashboard = document.getElementById("dashboard");
const repo=document.getElementById("repo-url").value;

analyzeBtn.addEventListener("click", analyzeRepository);

async function analyzeRepository() {

    analyzeBtn.innerHTML = "Analyzing...";
    analyzeBtn.disabled = true;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/analyze/repository",
            {
                method: "POST"
            }
        );

        const data = await response.json();

        console.log(data);

        dashboard.classList.remove("hidden");

        // Overall Score

        document.getElementById("overall-score").innerText =
            data.overall_score;

        // Health Status

        let status = "Needs Improvement";

        if (data.overall_score >= 80)
            status = "Excellent";

        else if (data.overall_score >= 60)
            status = "Good";

        else if (data.overall_score >= 40)
            status = "Warning";

        document.getElementById("health-status").innerText =
            status;

        // Technology Scores

        document.getElementById("docker-score").innerText =
            data.docker.score;

        document.getElementById("terraform-score").innerText =
            data.terraform.score;

        document.getElementById("kubernetes-score").innerText =
            data.kubernetes.score;

        document.getElementById("helm-score").innerText =
            data.helm.score;

        document.getElementById("jenkins-score").innerText =
            data.jenkins.score;

        // Repository Summary

        document.getElementById("summary-list").innerHTML = `

            <li><strong>Architecture Score :</strong> ${data.repository.architecture_score}</li>

            <li><strong>Security Score :</strong> ${data.repository.security_score}</li>

            <li><strong>Maintainability Score :</strong> ${data.repository.maintainability_score}</li>

            <li><strong>Production Readiness :</strong> ${data.repository.production_readiness}</li>

        `;

        // Recommendations

        const recommendationList =
            document.getElementById("recommendation-list");

        recommendationList.innerHTML = "";

        data.recommendations.forEach(rec => {

            recommendationList.innerHTML +=

                `<li>✅ ${rec}</li>`;

        });

    }

    catch (error) {

        console.error(error);

        alert("Error connecting to backend.");

    }

    analyzeBtn.innerHTML = "Analyze Repository";

    analyzeBtn.disabled = false;

}
document.getElementById("fix-btn")
.addEventListener("click", generateFixes);

async function generateFixes(){

    const response = await fetch(
        "http://127.0.0.1:8000/fix/all",
        {
            method:"POST"
        }
    );

    const data = await response.json();

    alert(data.message);

}
document.getElementById("download-btn")
.addEventListener("click",()=>{

window.location.href=
"http://127.0.0.1:8000/download/all";

});
loader.style.display="block";

/* API */

loader.style.display="none";
await fetch(
"http://127.0.0.1:8000/analyze/repository",
{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

repo_url:repo

})

});
