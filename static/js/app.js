const socket = io();
const terminal = document.getElementById('terminal');

socket.on('data', (data) => {
  terminal.textContent += data.message + '
';
  terminal.scrollTop = terminal.scrollHeight;
});

