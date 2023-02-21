import csv
import json
import sqlite3

class ReportGenerator:
    def __init__(self, database):
        self.database = database

    def generate_html_report(self, workspace):
        # Connect to SQLite database
        conn = sqlite3.connect(self.database)
        c = conn.cursor()

        # Fetch data from database
        c.execute("SELECT * FROM scans WHERE workspace = ?", (workspace,))
        rows = c.fetchall()

        # Generate HTML report
        html = "<html><body>"
        html += f"<h1>Scan Report for {workspace}</h1>"
        html += "<table>"
        html += "<tr><th>Target</th><th>Port</th><th>Service</th><th>Result</th></tr>"
        for row in rows:
            html += f"<tr><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"
        html += "</table>"
        html += "</body></html>"

        # Save report to file
        with open(f"{workspace}_report.html", "w") as f:
            f.write(html)

        # Close database connection
        conn.close()

    def generate_csv_report(self, workspace):
        # Connect to SQLite database
        conn = sqlite3.connect(self.database)
        c = conn.cursor()

        # Fetch data from database
        c.execute("SELECT * FROM scans WHERE workspace = ?", (workspace,))
        rows = c.fetchall()

        # Generate CSV report
        with open(f"{workspace}_report.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Target", "Port", "Service", "Result"])
            for row in rows:
                writer.writerow(row[1:])

        # Close database connection
        conn.close()

    def generate_json_report(self, workspace):
        # Connect to SQLite database
        conn = sqlite3.connect(self.database)
        c = conn.cursor()

        # Fetch data from database
        c.execute("SELECT * FROM scans WHERE workspace = ?", (workspace,))
        rows = c.fetchall()

        # Generate JSON report
        data = [{"target": row[1], "port": row[2], "service": row[3], "result": row[4]} for row in rows]
        with open(f"{workspace}_report.json", "w") as f:
            json.dump(data, f, indent=2)

        # Close database connection
        conn.close()
