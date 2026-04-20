#Library

print("--- Ticket-118: Fleet Report Generator ---")
from datetime import datetime

class ReportGenerator:

    def __init__(self, filename):
        self.filename = filename
        
    def write_report(self, offline_servers):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "w") as file:
            file.write(f"--- Offline Server Report: {current_time} ---\n")
            for s in offline_servers:
                file.write(s + "\n")

# --- Testing the Generator ---
# Here is a mock list of offline servers
crashed_servers = ["DB-01", "Mail-Gateway", "Auth-Server"]

my_reporter = ReportGenerator("Library_exercise/fleet_report.txt")
my_reporter.write_report(crashed_servers)

print("Script finished! Check your local folder for the new file.")