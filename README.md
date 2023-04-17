# netcat-server

This repository contains the implementation of a web application that functions as a [netcat](https://en.wikipedia.org/wiki/Netcat) server. It was built in python with Flask, rendering received data in a retro-style terminal interface.

## Netcat

## Project structure
The main component of the project is the webapp that acts as a friendly user interface for receiving commands from netcat clients. The project also includes a client and installer that is a thing wrapper around netcat to be used in a command line with pre-defined IPs and ports for ease of calling. The ideal scenario for this is having access to a server (either inside of a personal/private network or via a cloud provider) that will be running the application constantly and that can be sent data from any client that has access to the server. This facilitates to get data from the clients to be used for instance with tools like ChatGPT to debug issues in the client more easily, but also just sending an e-mail to an admin, or even googling.
You can read about the thin client [here](/unix_client/Readme.md) 

## Setup

1. Ensure Docker and Docker Compose are installed on your machine.

2. Clone this repository and navigate to the project folder.

3. Copy .env.example to .env and update the values as needed.

4. Run `docker-compose up -d` to build and start the Docker container.

5. Open your browser and visit `localhost:5000` to view the terminal interface.

6. Send messages to the server using netcat from a Linux computer.

## Technologies

- Flask (Python web framework)
- Docker (containerization platform)
- JavaScript libraries for WebSocket communication and terminal UI implementation (e.g., Socket.IO and xterm.js)


## Installing client
 
```
curl -s https://api.github.com/repos/juan-m12i/netcat-server/releases/latest | jq -r '.assets[] | select(.name=="wnc_client.tar.gz") | .browser_download_url'
```
