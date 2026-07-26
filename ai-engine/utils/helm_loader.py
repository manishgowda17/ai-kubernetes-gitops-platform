from pathlib import Path


class HelmLoader:

    def __init__(self, chart_directory):
        self.chart_directory = Path(chart_directory)

    def load_chart(self):

        files = []

        # Load Chart.yaml
        chart = self.chart_directory / "Chart.yaml"

        if chart.exists():
            files.append({
                "filename": "Chart.yaml",
                "content": chart.read_text()
            })

        # Load values.yaml
        values = self.chart_directory / "values.yaml"

        if values.exists():
            files.append({
                "filename": "values.yaml",
                "content": values.read_text()
            })

        # Load templates
        templates = self.chart_directory / "templates"

        if templates.exists():

            for file in sorted(templates.rglob("*")):

                if file.is_file():

                    files.append({
                        "filename": str(file.relative_to(self.chart_directory)),
                        "content": file.read_text()
                    })

        return files
