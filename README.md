# netcat-server

This repository contains the implementation of a web application that functions as a [netcat](https://en.wikipedia.org/wiki/Netcat) server. It was built in python with Flask, rendering received data in a retro-style terminal interface.

## Netcat
https://en.wikipedia.org/wiki/Netcat

## Project structure
The main component of the project is the webapp that acts as a friendly user interface for receiving commands from netcat clients. The project also includes a client and installer that is a thing wrapper around netcat to be used in a command line with pre-defined IPs and ports for ease of calling. The ideal scenario for this is having access to a server (either inside of a personal/private network or via a cloud provider) that will be running the application constantly and that can be sent data from any client that has access to the server. This facilitates to get data from the clients to be used for instance with tools like ChatGPT to debug issues in the client more easily, but also just sending an e-mail to an admin, or even googling.

You can read about the thin client [here](/unix_client/Readme.md) .

The rest of the current file regards the server piece of the project.

## Setup

### Via command line on a UNIX system (including WSL)
The recommended approach with python project such as this one would be to create a virtual environment. There are different ways to do this, with venv, virtualenv, virtualenvwrapper.

1. A suggestion using virtualenv would be executing the following (your milleage may vary, please check online and test what is your preferred way of working with virtual environments or go to the Docker option)
```
pip install virtualenv
virtualenv -p python3.9 venv
source venv/bin/activate
```
2. Install the required packages:
```
pip install -r requirements.txt
```
3. Executing the server:
```commandline
python app.py
```
You'll need to note down the IP of the machine where you are running this server code.

### With Docker

1. Ensure Docker and Docker Compose are installed on your machine.

2. Clone this repository and navigate to the project folder.

3. Run `sh build_and_run_docker.sh` to get the image built and the container launched.

5. Open your browser and visit `localhost:5010` on a browser to view the terminal interface.

6. Send messages to the server using netcat from a Linux computer (either with `netcat 192.168.X.X 12345` or using the [client](/unix_client/Readme.md) from this projecT).

## Technologies

- Flask (Python web framework)
- Docker (containerization platform)
- JavaScript libraries for WebSocket communication and terminal UI implementation (e.g., Socket.IO and xterm.js)


## Development and contributing
The main branch will be connected with github actions to create new releases.

- A "pre-release" branch exists for having new features to be bundled together for a new release
- A "development" branch exists for working concurrently on new features and making sure there are no conflicts. It's strongly encouraged to pull from this branch frequently
- New features and issues should be built in new specific branches following the github issue number. Using Github's UI this will look like: 1-add-tests
- Code should be merged to "development" ideally via a Pull Request to be reviewed by someone else
- Feel free to add "TODO" comments when there are obvious improvements or additions to make
- The working practices can evolve to accommodate preferences of contributors


## Use to pipe errors
``` bash
<your command> 2>&1 | wnc
```
