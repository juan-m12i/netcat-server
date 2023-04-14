# netcat-server

This repository contains the implementation of a netcat server built with Flask, rendering received data in a retro-style terminal interface.

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

