// main.js

const openNavButton = document.getElementById("openNav");
const closeNavButton = document.getElementById("closeNav");

// Open sidebar
document.getElementById("openNav").addEventListener("click", function() {
    document.getElementById("myNav").style.width = "270px";
});

// Close sidebar
document.getElementById("closeNav").addEventListener("click", function() {
    document.getElementById("myNav").style.width = "0";
});

// Hide the openNav button when the navigation is open
closeNavButton.addEventListener("click", function() {
    openNavButton.style.display = "block";
});

// Show the openNav button when the navigation is closed
openNavButton.addEventListener("click", function() {
    openNavButton.style.display = "none";
});
