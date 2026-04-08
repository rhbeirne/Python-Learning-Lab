#4/8 ping reboot server exercise

class Server:
    # This is the blueprint for our servers
    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address
        self.is_online = True  # Servers start online by default

    def ping(self):
        # This method checks the server's status
        if self.is_online:
            print(f"Reply from {self.ip_address}: {self.name} is ONLINE.")
        else:
            print(f"Request timed out: {self.name} is OFFLINE.")

    def reboot(self):
        # Your turn! Complete this method.
        # TODO 1: Print a message saying the server is rebooting.
        # TODO 2: Change self.is_online to False.
        # TODO 3: Print a message saying the server is back online.
        # TODO 4: Change self.is_online to True.
        print("Server is rebooting")
        self.is_online = False
        print("Server is back online")
        self.is_online = True

# --- Main Code ---

# TODO 5: Create a new Server object named "web_server" with the IP "192.168.1.10"
# Example: my_server = Server("Name", "IP")
server1 = Server("web server", "192.168.1.10")
# TODO 6: Create another Server object named "database" with the IP "10.0.0.5"
server2 = Server("database", "10.0.0.5")



# TODO 7: Call the ping() method on your web_server
server1.ping()


# TODO 8: Call the reboot() method on your database server
server2.reboot()