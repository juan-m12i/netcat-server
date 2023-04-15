#!/bin/bash

CONFIG_FILE="${HOME}/.wnc_config"

# Set default values if the config file does not exist
if [ ! -f "${CONFIG_FILE}" ]; then
  echo "DEFAULT_IP=192.168.1.100" > "${CONFIG_FILE}"
  echo "DEFAULT_PORT=12345" >> "${CONFIG_FILE}"
fi

# Load config values
source "${CONFIG_FILE}"

set_port() {
  local port=$1
  sed -i "s/DEFAULT_PORT=.*/DEFAULT_PORT=$port/" "${CONFIG_FILE}"
  echo "Default port set to $port"
}

set_ip() {
  local ip=$1
  sed -i "s/DEFAULT_IP=.*/DEFAULT_IP=$ip/" "${CONFIG_FILE}"
  echo "Default IP set to $ip"
}

if [ "$1" = "set-port" ]; then
  if [ -n "$2" ] && [ "$2" -eq "$2" ] 2>/dev/null; then
    set_port "$2"
  else
    echo "Error: Invalid port number"
  fi
  exit
fi

if [ "$1" = "set-ip" ]; then
  if [[ "$2" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    set_ip "$2"
  else
    echo "Error: Invalid IP address"
  fi
  exit
fi

if [ "$1" = "set-address" ]; then
  if [[ "$2" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+$ ]]; then
    IFS=":"
    read -ra ADDR <<< "$2"
    set_ip "${ADDR[0]}"
    set_port "${ADDR[1]}"
  else
    echo "Error: Invalid address format"
  fi
  exit
fi



# Parse arguments
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -ip)
    IP="$2"
    shift # past argument
    shift # past value
    ;;
    -p|-port)
    PORT="$2"
    shift # past argument
    shift # past value
    ;;
    --)
    shift # past the double dash
    NETCAT_ARGS="$*"
    break
    ;;
    *)
    COMMAND="$COMMAND $1"
    shift
    ;;
esac
done

if [ -z "$COMMAND" ]; then
  # If command is not provided, use stdin
  netcat $NETCAT_ARGS $IP $PORT
else
  # If command is provided, execute it and pipe the output to netcat
  eval "$COMMAND" | netcat $NETCAT_ARGS $IP $_PORT
fi



# Use the updated DEFAULT_IP and DEFAULT_PORT variables for netcat
echo -n "$@" | nc "${DEFAULT_IP}" "${DEFAULT_PORT}"
