from api.api import app
from cli.cli import cli
from database.db import Database
from reports.reports import ReportGenerator

def main():
    # Initialize database.
    database = Database("database.sqlite")

    # Initialize report generator.
    report_generator = ReportGenerator(database)

    # Start API server in background.
    app.run(debug=False)

    # Start CLI.
    cli.cmdloop()

    # Clean up.
    database.close()

if __name__ == "__main__":
    main()