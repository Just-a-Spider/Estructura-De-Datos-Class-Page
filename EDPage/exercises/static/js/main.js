// main.js

const openNavButton = document.getElementById("openNav");
const closeNavButton = document.getElementById("closeNav");
const navBar = document.getElementById("myNav")
const menuText = document.getElementById("menuText")

// Open the navBar
openNavButton.addEventListener("click", function() {
    navBar.style.width = "55%";
    openNavButton.style.display = "none";
    closeNavButton.style.display = "block";
    menuText.style.display = "block";
});

// Close the navBar
closeNavButton.addEventListener("click", function() {
    closeNavButton.style.display = "none";
    menuText.style.display = "none";
    navBar.style.width = "0";
    openNavButton.style.display = "block";
});
