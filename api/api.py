from flask import Flask, request, jsonify
from cli.cli import MyCLI

app = Flask(__name__)
cli = MyCLI()

@app.route("/api/workspaces", methods=["GET"])
def list_workspaces():
    workspaces = cli.do_list_workspaces("")
    return jsonify(workspaces)

@app.route("/api/workspaces/<workspace>", methods=["GET"])
def get_workspace(workspace):
    workspace_data = cli.do_get_workspace(workspace)
    return jsonify(workspace_data)

@app.route("/api/workspaces/<workspace>/scan", methods=["POST"])
def scan(workspace):
    target = request.json.get("target")
    if not target:
        return jsonify({"error": "Target is missing."}), 400

    cli.do_set_workspace(workspace)
    cli.do_scan(target)

    return jsonify({"status": "success"})

@app.route("/api/workspaces/<workspace>/results", methods=["GET"])
def list_results(workspace):
    results = cli.do_list_results("")
    return jsonify(results)

@app.route("/api/workspaces/<workspace>/report", methods=["GET"])
def generate_report(workspace):
    format = request.args.get("format", "html")
    report = cli.do_generate_report(f"{workspace} -f {format}")
    return report

if __name__ == "__main__":
    app.run(debug=True)