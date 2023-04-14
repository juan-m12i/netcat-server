"""A simple Flask app that listens for incoming netcat connections and displays the received data in real-time using SocketIO.

This app listens for incoming netcat connections on a specified port and displays the received data in real-time using SocketIO. The app also includes a simple HTML template that displays the received data.

Example usage:
$ python app.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
"""

from flask import Flask, render_template, request
from datetime import datetime
import socket
import threading
import os
from flask_socketio import SocketIO, emit

# Create a Flask app and configure a secret key for security
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Create a SocketIO instance for real-time communication
socketio = SocketIO(app)

# Set the buffer size and port number for the netcat listener
BUFFER_SIZE = 1024
PORT_NUMBER = 12345

# This function handles incoming netcat connections and displays the received data in real-time
def handle_client(client_socket, client_address):
    # Receive data from the client
    data = client_socket.recv(BUFFER_SIZE)
    # Print the received data to the console
    print(f"Received data from {client_address}: {data.decode('utf-8')}")
    # Send the received data to connected clients using SocketIO, along with IP address and timestamp
    socketio.emit("message", {"ip": client_address[0], "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "content": data.decode('utf-8')})

# This function starts a listener for incoming netcat connections on the specified port
def start_netcat_listener(port):
    # Create a socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the specified port
    server_socket.bind(("", port))
    # Listen for incoming connections
    server_socket.listen(1)

    while True:
        # Accept incoming connections and spawn a new thread to handle each one
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

# Start the netcat listener in a separate thread
threading.Thread(target=start_netcat_listener, args=(PORT_NUMBER,)).start()

# This route serves the index.html template
@app.route("/")
def index():
    return render_template("index.html")

# This SocketIO event handler runs when a client connects to the server
@socketio.on("connect")
def handle_connect():
    # Send a "Connected" message to the connected client using SocketIO
    emit("message", "Connected")

# Start the Flask app with SocketIO support
if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True)
