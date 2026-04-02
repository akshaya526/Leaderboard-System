# Secure Distributed Leaderboard System using TCP with SSL/TLS

---

## Objective

The objective of this project is to design and implement a secure leaderboard system using socket programming.
The system allows multiple clients to update and retrieve scores in real time using TCP communication secured with SSL/TLS.

---

## Features

* TCP socket communication
* SSL/TLS secure data transfer
* Multi-client support using multithreading
* GUI-based client interface
* Real-time leaderboard updates using broadcast
* Input validation and error handling

---

## Architecture

Multiple clients communicate with the server over secure TCP (SSL).
The server maintains the leaderboard and sends updates to all connected clients.

---

## Protocol Design

* UPDATE name score → update score
* GET → retrieve leaderboard

---

## How to Run

### Generate SSL Certificate

```
openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key
```

### Run Server

```
python server_secure.py
```

### Run Clients (multiple instances)

```
python gui.py
```

---

## Performance Evaluation

The system was tested with multiple clients.
As the number of clients increased, response time slightly increased due to thread handling and network overhead, but the system remained stable.

---

## Security

SSL/TLS is used to encrypt communication between client and server.
A self-signed certificate is used for secure data transmission.
The connection was verified using SSLSocket.

---

## Testing

* Tested with multiple concurrent clients
* Verified real-time updates
* Handled invalid inputs
* Tested client disconnections
* Verified secure communication

---

## Screenshots

Add screenshots of:

* GUI running
* Multiple clients
* Server terminal
* SSL proof
* Performance output

---

## Conclusion

The project demonstrates secure socket communication, multi-client handling, and real-time leaderboard updates using TCP and SSL/TLS.
