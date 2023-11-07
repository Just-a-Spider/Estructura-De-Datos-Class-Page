const pySnippetBtn = document.getElementById("pySnippetBtn");
const cppSnippetBtn = document.getElementById("cppSnippetBtn");
const pySnippet = document.getElementById("pySnippet");
const cppSnippet = document.getElementById("cppSnippet");

// Create a WebSocket connection
var socket = new WebSocket('ws://localhost:8000/ws/code_run/');

socket.onopen = function(e) {
  console.log("[open] Connection established");
};

socket.onmessage = function(event) {
  console.log(`[message] Data received from server: ${event.data}`);
};

socket.onerror = function(error) {
  console.log(`[error] ${error.message}`);
};

// Initially hide the Python snippet
pySnippet.style.display = "none";
pySnippetBtn.classList.remove("active");

pySnippetBtn.addEventListener("click", function () {
    pySnippet.style.display = "block";
    cppSnippet.style.display = "none";
    pySnippetBtn.classList.add("active");
    cppSnippetBtn.classList.remove("active");
});

cppSnippetBtn.addEventListener("click", function () {
    pySnippet.style.display = "none";
    cppSnippet.style.display = "block";
    pySnippetBtn.classList.remove("active");
    cppSnippetBtn.classList.add("active");
});

function sendActiveSnippet() {
    const activeSnippet = document.querySelector(".active-snippet");
    const snippetType = activeSnippet.id === "pySnippet" ? "python" : "cpp";
    const snippetCode = activeSnippet.textContent.trim();

    // Send the snippet data to the server over the WebSocket connection
    socket.send(JSON.stringify({
        type: snippetType,
        code: snippetCode,
    }));
}