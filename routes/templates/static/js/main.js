// ==========================================
// SahyogSetu - Main JavaScript
// ==========================================


// ------------------------------------------
// Auto-hide flash messages
// ------------------------------------------

document.addEventListener("DOMContentLoaded", function () {

    const messages = document.querySelectorAll(".flash-message");

    messages.forEach(function (message) {

        setTimeout(function () {
            message.style.opacity = "0";

            setTimeout(function () {
                message.remove();
            }, 500);

        }, 3000);

    });

});


// ------------------------------------------
// Confirmation before rejecting/deleting
// ------------------------------------------

document.addEventListener("click", function (event) {

    const button = event.target.closest("[data-confirm]");

    if (!button) {
        return;
    }

    const message = button.getAttribute("data-confirm");

    if (!confirm(message)) {
        event.preventDefault();
    }

});


// ------------------------------------------
// Mobile navigation
// ------------------------------------------

const menuButton = document.querySelector(".menu-button");
const navigation = document.querySelector(".navigation");

if (menuButton && navigation) {

    menuButton.addEventListener("click", function () {
        navigation.classList.toggle("active");
    });

}


// ------------------------------------------
// Progress bar animation
// ------------------------------------------

document.addEventListener("DOMContentLoaded", function () {

    const progressBars = document.querySelectorAll("[data-progress]");

    progressBars.forEach(function (bar) {

        const progress = bar.getAttribute("data-progress");

        if (progress !== null) {
            bar.style.width = progress + "%";
        }

    });

});


// ------------------------------------------
// Simple form validation
// ------------------------------------------

document.addEventListener("submit", function (event) {

    const form = event.target;

    if (!form.matches(".validate-form")) {
        return;
    }

    const requiredFields = form.querySelectorAll("[required]");

    let valid = true;

    requiredFields.forEach(function (field) {

        if (!field.value.trim()) {
            field.style.borderColor = "red";
            valid = false;
        } else {
            field.style.borderColor = "";
        }

    });

    if (!valid) {
        event.preventDefault();
        alert("Please fill in all required fields.");
    }

});