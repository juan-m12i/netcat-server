"""
A Flask app that listens for incoming netcat connections and displays the received data in real-time using SocketIO.

This app uses several Python libraries to accomplish its goal:

- Flask: a third-party web framework that makes it easy to build web applications in Python. Flask is used to serve the HTML template and handle HTTP requests.

- Flask-SocketIO: a third-party library that provides SocketIO integration for Flask. SocketIO is used to send the received data to connected clients in real-time.

- socket: a standard Python library that provides low-level network communication. socket is used to listen for incoming netcat connections and receive data.

- threading: a standard Python library that provides multi-threading support. threading is used to spawn a new thread for each incoming netcat connection, so that the app can handle multiple connections simultaneously.

When the app is run, it starts a listener for incoming netcat connections on a specified port. When data is received from a client, the app sends the data to connected clients using SocketIO in real-time. The app also includes a simple HTML template that displays the received data.

Two ports will be open on the server when running this application: the Flask server port, which defaults to 5000, and the netcat listener port, which is set to 12345 by default.

The main execution thread of this app is the Flask server, which listens for incoming HTTP requests and serves the HTML template. When a netcat connection is made, a new thread is spawned to handle the connection and receive data in real-time using SocketIO. The main thread continues to listen for new HTTP requests while the sub-threads handle the netcat connections.
"""

from flask import Flask, render_template
from datetime import datetime
import socket
import threading
import os
from flask_socketio import SocketIO, emit

# Create a Flask app and configure a secret key for security
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")  # TODO: check if this is being used and if it should be, maybe as part of securisation of the server

# Create a SocketIO instance for real-time communication
socketio = SocketIO(app)

# Set the buffer size and port number for the netcat listener
BUFFER_SIZE = 1024

NETCAT_PORT_NUMBER = 12345  # TODO probably move to a config or environment file
FLASK_APP_PORT = 5010  # TODO probably move to a config or environment file


# This function handles incoming netcat connections and displays the
# received data in real-time
def handle_client(client_socket, client_address):
    # Receive data from the client
    data = client_socket.recv(BUFFER_SIZE)
    # Print the received data to the console
    print(f"Received data from {client_address}: {data.decode('utf-8')}")

    # Send the received data to connected clients using SocketIO, along with
    # IP address and timestamp
    socketio.emit("message",
                  {"ip": client_address[0],
                   "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                   "content": data.decode('utf-8')})


# This function starts a listener for incoming netcat connections on the
# specified port
def start_netcat_listener(port):
    print(f"Starting netcat listener on port {port}")
    # Create a socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the specified port
    server_socket.bind(("", port))
    # Listen for incoming connections
    server_socket.listen(1)

    while True:
        # Accept incoming connections and spawn a new thread to handle each one
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(
            target=handle_client, args=(
                client_socket, client_address))
        thread.start()


# Start the netcat listener in a separate thread
# This is important as the server will be both opening the port for the Flask webapp, but also to listen to netcat requests, and this happens in different threads
threading.Thread(
    target=start_netcat_listener,
    args=(
        NETCAT_PORT_NUMBER,
    )).start()


# The only page of the app, using the native Flash method: render_template (see html code including imports in templates/index.html)
@app.route("/")
def index():
    return render_template("index.html")


# This SocketIO event handler runs when a client connects to the server
@socketio.on("connect")
def handle_connect():
    # Send a "Connected" message to the connected client using SocketIO
    emit("message", "Connected")


# This is the entry point when the code is executed from a command line to this file (example python app.py).
# If the module were to be imported into a different module, the code below would be ignored
# This will start the server
if __name__ == "__main__":
    # Start the Flask app with SocketIO support
    # TODO: review how a proper production-grade server could be used instead of werkzeug, specially with unsafe mode
    # host=0.0.0.0 was required to run on docker, but not on local
    socketio.run(app, allow_unsafe_werkzeug=True, port=FLASK_APP_PORT, host='0.0.0.0')


