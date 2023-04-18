# WNC Client and Installer

This repository contains the WNC (Wrapped Netcat) client and installer for Unix-based systems. The WNC client allows you to send logs or any other content to a remote server using netcat.

## Installation

### With git
To install the WNC client, follow these steps:

1. Clone this repository or download the installer script and the WNC client script.
2. Run the installer script to set up the WNC client on your system.

### With comand line
Run the following script
```commandline
curl -L -O $(curl -s https://api.github.com/repos/juan-m12i/netcat-server/releases/latest | jq -r '.assets[] | select(.name=="wnc_client.tar.gz") | .browser_download_url') && tar xzf wnc_client.tar.gz && ./unix_client/install_wnc.sh
```

## Usage

After installing the WNC client, you can use it to send logs or any other content to a remote server with a simple command:



You can also configure the default IP address and port used by the WNC client using the following commands:



For more advanced usage, you can pass additional arguments to the netcat command used by the WNC client.
