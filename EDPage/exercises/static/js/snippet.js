// snippet.js

const pySnippetBtn = document.getElementById("pySnippetBtn");
const cppSnippetBtn = document.getElementById("cppSnippetBtn");
const pySnippet = document.getElementById("pySnippet");
const cppSnippet = document.getElementById("cppSnippet");

// Initially hide the C++ snippet
cppSnippet.style.display = "none";
cppSnippetBtn.classList.remove("active");


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
