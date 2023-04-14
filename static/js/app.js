document.addEventListener("DOMContentLoaded", function () {
  const socket = io.connect(location.protocol + "//" + document.domain + ":" + location.port);
  const tableBody = document.getElementById("data-table").getElementsByTagName("tbody")[0];

  socket.on("connect", function () {
    socket.emit("user_connected");
  });

    socket.on("message", function (data) {
      if (data.ip !== undefined && data.timestamp !== undefined) {
        addRow(data);
      }
    });


  function addRow(data) {
    const row = document.createElement("tr");

    const metadataCell = document.createElement("td");
    metadataCell.innerHTML = `IP: ${data.ip}<br>Timestamp: ${data.timestamp}`;
    metadataCell.className = "align-top";
    metadataCell.classList.add("bg-black", "text-green-400", "font-mono");
    row.appendChild(metadataCell);

    const contentCell = document.createElement("td");
    contentCell.className = "relative max-h-24 p-2 overflow-y-auto break-all";

    if (data.content) {
      contentCell.innerHTML = data.content.replace(/\n/g, "<br>");
    } else {
      contentCell.innerHTML = '';
    }

    const copyButton = document.createElement("button");
    copyButton.className = "absolute top-0 right-0 bg-blue-500 text-white px-2 py-1 text-xs rounded hover:bg-blue-600";
    copyButton.innerHTML = "Copy";
    copyButton.onclick = function () {
      if (data.content) {
        navigator.clipboard.writeText(data.content);
      }
    };
    contentCell.appendChild(copyButton);
    contentCell.classList.add("bg-black", "text-green-400", "font-mono");




    row.appendChild(contentCell);
    tableBody.appendChild(row);
  }
});
