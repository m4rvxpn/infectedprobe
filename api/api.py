from flask import Flask, request, jsonify
from cli.cli import MyCLI
from database.db import Database
from reports.reports import ReportGenerator

app = Flask(__name__)
cli = MyCLI()
database = Database("database.sqlite")
report_generator = ReportGenerator(database)

@app.route("/api/workspaces", methods=["GET"])
def list_workspaces():
    workspaces = database.execute("SELECT * FROM workspaces")
    return jsonify(workspaces)

@app.route("/api/workspaces/<workspace>", methods=["GET"])
def get_workspace(workspace):
    workspace_data = {}
    # Code to get workspace data from SQLite database.
    return jsonify(workspace_data)

@app.route("/api/workspaces/<workspace>/scan", methods=["POST"])
def scan(workspace):
    # Code to run scans and input data to Metasploit database.
    cli.onecmd(f"use {workspace}")
    cli.onecmd("set_credentials")
    cli.onecmd("scan")
    database.commit()
    return jsonify({"status": "success"})

@app.route("/api/workspaces/<workspace>/results", methods=["GET"])
def list_results(workspace):
    results = database.execute(f"SELECT * FROM {workspace}_hosts")
    return jsonify(results)

@app.route("/api/workspaces/<workspace>/report", methods=["GET"])
def generate_report(workspace):
    report_format = request.args.get("format", "html")
    if report_format == "html":
        report = report_generator.generate_html_report(workspace)
        return report
    elif report_format == "csv":
        report = report_generator.generate_csv_report(workspace)
        return report
    elif report_format == "json":
        report = report_generator.generate_json_report(workspace)
        return jsonify(report)
    else:
        return jsonify({"error": f"Invalid report format: {report_format}"}), 400

if __name__ == "__main__":
    app.run(debug=True)
