document.addEventListener("DOMContentLoaded", function () {
  const socket = io.connect(location.protocol + "//" + document.domain + ":" + location.port);
  const terminalOutput = document.getElementById("terminal-output");
  const terminalInput = document.getElementById("terminal-input");

  socket.on("connect", function () {
    socket.emit("user_connected");
  });

  socket.on("message", function (msg) {
    terminalOutput.innerHTML += msg + "\n";
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
  });

  terminalInput.addEventListener("keypress", function (event) {
    if (event.keyCode === 13) { // Enter key
      event.preventDefault();
      const inputValue = event.target.value.trim();
      if (inputValue) {
        socket.emit("filter_data", inputValue);
      }
      event.target.value = "";
    }
  });
});
