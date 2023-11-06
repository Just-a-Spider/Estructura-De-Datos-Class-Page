// snippet.js

const pySnippetBtn = document.getElementById("pySnippetBtn");
const cppSnippetBtn = document.getElementById("cppSnippetBtn");
const pySnippet = document.getElementById("pySnippet");
const cppSnippet = document.getElementById("cppSnippet");
var csrftoken = document.querySelector('[name=csrf-token]').content;

function tryCode() {
    var activeSnippet = document.querySelector('.snippet .active');
    var code = activeSnippet.textContent;
    var language = activeSnippet.id === 'cppSnippetBtn' ? 'cpp' : 'python';
    fetch('/run-code/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Django requires a CSRF token for POST requests
        },
        body: JSON.stringify({ language, code })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Display the output in the browser
        var outputDiv = document.getElementById('output');
        outputDiv.textContent = data.output;
    });
}
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
document.getElementById('tryCode').addEventListener('click', tryCode);
