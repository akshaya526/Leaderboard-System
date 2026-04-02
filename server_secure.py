import socket
import ssl
import threading

HOST = "0.0.0.0"
PORT = 5000

leaderboard = {}
clients = []
lock = threading.Lock()


def get_leaderboard():
    sorted_board = sorted(leaderboard.items(),
                          key=lambda x: x[1],
                          reverse=True)

    result = ""
    for i, (name, score) in enumerate(sorted_board, 1):
        result += f"{i}. {name} - {score}\n"
    return result


def broadcast():
    data = get_leaderboard()
    for c in clients:
        try:
            c.send(data.encode())
        except:
            pass


def handle_client(conn, addr):
    print(f"Client connected: {addr}")

    #  SSL PROOF
    print("Socket type:", type(conn)) 

    clients.append(conn)

    while True:
        try:
            data = conn.recv(1024).decode()

            if not data:
                break

            if data.startswith("UPDATE"):
                _, name, score = data.split()

                if not score.isdigit():
                    print("Invalid score received")
                    continue

                with lock:
                    leaderboard[name] = int(score)

                print(f"Updated: {name} → {score}")
                broadcast()

            elif data == "GET":
                print("GET received from client") 
                conn.send(get_leaderboard().encode())

        except:
            print("Client disconnected")
            break

    clients.remove(conn)
    conn.close()


#  SSL setup
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("server.crt", "server.key")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

secure_server = context.wrap_socket(server, server_side=True)

print("Secure Server Running...")

while True:
    conn, addr = secure_server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()