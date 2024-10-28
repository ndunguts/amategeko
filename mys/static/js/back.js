// Prevent back navigation after page load
document.addEventListener("DOMContentLoaded", function () {
    history.pushState(null, null, location.href);
    window.onpopstate = function () {
        history.go(0);
    };
});

// Set the initial result count, retrieving it from localStorage if available, or default to 1
let currentResult = localStorage.getItem('currentResult') ? parseInt(localStorage.getItem('currentResult')) : 1;

// Display the initial result count
document.querySelector('.current').textContent = currentResult;

// Select elements
const showAnswerButton = document.querySelector('.btn.start');
const progressBar = document.querySelector('.progress-bar');
const progressText = document.querySelector('.progress-text');

// Set initial progress based on stored currentResult
const initialProgressWidth = (currentResult / 20) * 100;
progressBar.style.width = `${initialProgressWidth}%`;
progressText.textContent = `${Math.round(initialProgressWidth)}%`;

// Add an event listener to the "Show answer" button
showAnswerButton.addEventListener('click', () => {
    if (currentResult < 20) {
        currentResult++;
    } else {
        currentResult = 1;
    }

    // Update the displayed result count and progress bar
    document.querySelector('.current').textContent = currentResult;
    const progressWidth = (currentResult / 20) * 100;
    progressBar.style.width = `${progressWidth}%`;
    progressText.textContent = `${Math.round(progressWidth)}%`;
    
    // Store the updated result count in localStorage
    localStorage.setItem('currentResult', currentResult);
});
