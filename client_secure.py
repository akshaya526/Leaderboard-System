import socket
import ssl
import threading
import time


class SecureClient:
    def __init__(self, callback):
        self.callback = callback
        self.start_time = None

        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = context.wrap_socket(raw_socket, server_hostname="localhost")

        # Change IP if using different system
        self.client.connect(("127.0.0.1", 5000)) # mine is 10.75.232.163

        threading.Thread(target=self.receive, daemon=True).start()

    def receive(self):
        while True:
            try:
                data = self.client.recv(4096).decode()
                if data:
                    end = time.time()

                    if self.start_time:
                        print("Response time:", round(end - self.start_time, 4), "seconds")
                        self.start_time = None  # reset

                    print("Received from server:\n", data)
                    self.callback(data)

            except:
                break

    def update_score(self, name, score):
        self.client.send(f"UPDATE {name} {score}".encode())

    def get_leaderboard(self):
        self.start_time = time.time()   
        print("Request sent...")
        self.client.send("GET".encode())