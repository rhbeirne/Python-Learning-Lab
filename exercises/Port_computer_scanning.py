#Exercise

import platform
import os
import shutil
import socket
import requests
import json

print("--- IT Automation Capstone: Phase 1 ---")
print("Gathering System Health Data...")

# We've automated the hardware checks for you!
os_name = platform.system()
cpu_cores = os.cpu_count()
disk_info = shutil.disk_usage("/")
free_gb = round(disk_info.free / 1073741824, 2) # round() keeps the decimals clean!

print(f"System: {os_name} | Cores: {cpu_cores} | Free Space: {free_gb}GB")

print("\nScanning Local Web Port (80)...")

# METHOD USED: socket.socket() -> Creates a new network socket (our digital "hand" used to knock on doors).
# TODO 1: Create a new socket: s = socket.socket()
s = socket.socket()


# METHOD USED: .connect_ex((ip, port)) -> Tries to connect to the target. Returns 0 if the door is OPEN, or an error number if CLOSED.
# TODO 2: Knock on the door using connect_ex(). Save it to 'port_result'.
# Example: port_result = s.connect_ex(("127.0.0.1", 80))
port_result = s.connect_ex(("127.0.0.1", 80))



# TODO 3: Write an if/else statement:
# If port_result is exactly 0, create a variable called: web_status = "Online"
# Else, create the variable as: web_status = "Offline"
if port_result == 0:
    web_status = "Online"
else:
    web_status = "Offline"


# TODO 4: Print out the 'web_status' variable so we can verify it!
print(f"Web Server Status: {web_status}")

print("\n--- IT Automation Capstone: Phase 2 ---")
print("Packaging Data for IT Dashboard...")

# TODO 5: Create a dictionary called 'server_payload'.
# Add four keys to it: "os", "cores", "storage", and "web_server".
# Set their values to the variables we just created (os_name, cpu_cores, free_gb, web_status).
server_payload = {"os":os_name, "cores":cpu_cores, "storage":free_gb, "web_server":web_status }


# TODO 6: Print your 'server_payload' dictionary to make sure everything is packaged correctly before sending!

print(server_payload)

print("\n--- IT Automation Capstone: Phase 3 ---")
print("Transmitting to Dashboard...")

dashboard_url = "https://api.it-dashboard.local/v1/health-report"

# METHOD USED: requests.post(url, json=dict) -> Packages a Python dictionary into JSON text and sends it to a server.
# METHOD USED: requests.exceptions.ConnectionError -> A specific error triggered when the target server is down or unreachable.

try:
    response = requests.post(dashboard_url, json=server_payload)
    print(f"Report Sent! Receipt: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("Warning: Dashboard API is unreachable. Saving report locally.")