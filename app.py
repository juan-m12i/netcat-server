from flask import Flask, render_template, request
from datetime import datetime
import socket
import threading
import os
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
socketio = SocketIO(app)

BUFFER_SIZE = 1024
PORT_NUMBER = 12345

def handle_client(client_socket, client_address):
    data = client_socket.recv(BUFFER_SIZE)
    print(f"Received data from {client_address}: {data.decode('utf-8')}")
    socketio.emit("message", {"ip": client_address[0], "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "content": data.decode('utf-8')})



def start_netcat_listener(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", port))
    server_socket.listen(1)

    while True:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

threading.Thread(target=start_netcat_listener, args=(PORT_NUMBER,)).start()

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    emit("message", "Connected")

if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True)
