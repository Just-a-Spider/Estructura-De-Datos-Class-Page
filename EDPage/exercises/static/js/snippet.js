const pySnippetBtn = document.getElementById("pySnippetBtn");
const cppSnippetBtn = document.getElementById("cppSnippetBtn");
const pySnippet = document.getElementById("pySnippet");
const cppSnippet = document.getElementById("cppSnippet");
const consoleDiv = document.getElementById("console");
const pyCode = document.getElementById("pyCode");
const cppCode = document.getElementById("cppCode");
// Initially hide the Python snippet
pySnippet.style.display = "none";
pySnippetBtn.classList.remove("active");

pySnippetBtn.addEventListener("click", function () {
    pySnippet.style.display = "block";
    cppSnippet.style.display = "none";
    pySnippetBtn.classList.add("active");
    cppSnippetBtn.classList.remove("active");
    // Send AJAX request to get the console output
    $.ajax({
      url: '/ejecutar/',
      method: 'POST',
      data: {
        code: pyCode.textContent,
        lang: 'python',
        input: $('#input').val()
      },
      success: function(data) {
        if (data.result == 'Input required') {
          $.ajax({
            url: '/ejecutar/',
            method: 'POST',
            data: {
              code: pyCode.textContent,
              lang: 'python',
              input: prompt('Input required')
            },
            success: function(data) {
              console.log('Ejecutando Python');
              consoleDiv.innerHTML = data.result;
            }
          });
        }else{
          console.log('Ejecutando Python');
          consoleDiv.innerHTML = data.result;
        }
      }
    });
      
});

cppSnippetBtn.addEventListener("click", function () {
    pySnippet.style.display = "none";
    cppSnippet.style.display = "block";
    pySnippetBtn.classList.remove("active");
    cppSnippetBtn.classList.add("active");
    // Send AJAX request to get the console output
    $.ajax({
      url: '/ejecutar/',
      method: 'POST',
      data: {
        code: cppCode.textContent,
        lang: 'cpp',
        input: $('#input').val()
      },
      success: function(data) {
        if (data.result == 'Input required') {
          $.ajax({
            url: '/ejecutar/',
            method: 'POST',
            data: {
              code: cppCode.textContent,
              lang: 'cpp',
              input: prompt('Input required')
            },
            success: function(data) {
              console.log('Ejecutando C++');
              consoleDiv.innerHTML = data.result;
            }
          });
        }else{
          console.log('Ejecutando C++');
          consoleDiv.innerHTML = data.result;
        }
      }
    });
});
