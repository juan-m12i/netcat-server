#!/bin/bash

echo "Starting wnc installation..."

# Default values
DEFAULT_WNC_PATH="/usr/local/bin"
DEFAULT_CONFIG_PATH="${HOME}"
DEFAULT_IP="192.168.1.100"
DEFAULT_PORT="12345"

# Prompt user for installation path
read -p "Enter the path to install wnc (default: ${DEFAULT_WNC_PATH}): " WNC_PATH
WNC_PATH=${WNC_PATH:-$DEFAULT_WNC_PATH}

# Prompt user for config file path
read -p "Enter the path to store the wnc config file (default: ${DEFAULT_CONFIG_PATH}): " CONFIG_PATH
CONFIG_PATH=${CONFIG_PATH:-$DEFAULT_CONFIG_PATH}

# Prompt user for default IP
read -p "Enter the default IP for wnc (default: ${DEFAULT_IP}): " IP
IP=${IP:-$DEFAULT_IP}

# Prompt user for default port
read -p "Enter the default port for wnc (default: ${DEFAULT_PORT}): " PORT
PORT=${PORT:-$DEFAULT_PORT}

# Check if wnc script exists
if [ ! -f "wnc" ]; then
  echo "Error: wnc script not found in the current directory"
  exit 1
fi

# Copy wnc script to the installation path and set execution rights
cp "wnc" "${WNC_PATH}/wnc"
chmod +x "${WNC_PATH}/wnc"

# Create the config file with the provided IP and port
CONFIG_FILE="${CONFIG_PATH}/.wnc_config"
echo "DEFAULT_IP=${IP}" > "${CONFIG_FILE}"
echo "DEFAULT_PORT=${PORT}" >> "${CONFIG_FILE}"

echo "wnc installation complete!"
