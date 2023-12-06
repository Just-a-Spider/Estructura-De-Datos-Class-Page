const pySnippetBtn = document.getElementById("pySnippetBtn");
const cppSnippetBtn = document.getElementById("cppSnippetBtn");
const pySnippet = document.getElementById("pySnippet");
const cppSnippet = document.getElementById("cppSnippet");
const consoleDiv = document.getElementById("console");
const pyCode = document.getElementById("pyCode");
const cppCode = document.getElementById("cppCode");
const copyBtn = document.getElementById("copyBtn");
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

copyBtn.addEventListener("click", function () {
    if (pySnippetBtn.classList.contains("active")) {
        copyToClipboard(pyCode);
    } else {
        copyToClipboard(cppCode);
    }
});

function copyToClipboard(element) {
    var text = element.textContent;
    var textarea = document.createElement('textarea');
    textarea.textContent = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);

    // Show notification
    var notification = document.getElementById('notification');
    notification.classList.add('notification-visible');

    // Hide notification after 2 seconds
    setTimeout(function() {
        notification.classList.remove('notification-visible');
    }, 2000);
}

// Path: backend/exercises/static/js/submit.js
