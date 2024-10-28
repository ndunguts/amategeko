// Initialize currentResult from localStorage or set to 1 by default
let currentResult = localStorage.getItem('currentResult') ? parseInt(localStorage.getItem('currentResult')) : 1;

// Check if the page is the start page after the reset
if (window.location.pathname === '/start_q/') { // Adjust the URL as necessary
    localStorage.removeItem('currentResult'); // Clear the stored value
    currentResult = 1; // Reset to 1
    localStorage.setItem('currentResult', currentResult); // Store the reset value
}

// Display the initial result count
document.querySelector('.current').textContent = currentResult;

// Select elements
const showAnswerButton = document.querySelector('.btn.start');
const progressBar = document.querySelector('.progress-bar');
const progressText = document.querySelector('.progress-text');

// Function to update the progress display
function updateProgressDisplay() {
    document.querySelector('.current').textContent = currentResult;
    const progressWidth = (currentResult / 20) * 100; // Calculate width as a percentage
    progressBar.style.width = `${progressWidth}%`;
    progressText.textContent = `${Math.round(progressWidth)}%`;
}

// Call to update the display initially
updateProgressDisplay();

// Function to validate the form
function validateForm() {
    const radios = document.querySelectorAll('input[name="answer"]');
    let isChecked = Array.from(radios).some(radio => radio.checked); // Check if any radio is selected

    if (!isChecked) {
        alert('Please select an answer before proceeding.');
        return false; // Prevent form submission
    }

    return true; // Allow form submission
}

// Add an event listener to the "Next" button
showAnswerButton.addEventListener('click', (event) => {
    // Validate the form before proceeding
    if (!validateForm()) {
        event.preventDefault(); // Prevent the default action if validation fails
        return; // Exit the function
    }

    // Increment the result count if it's less than 20, otherwise reset to 1
    if (currentResult < 20) {
        currentResult++;
    } else {
        currentResult = 1; // Reset if maximum reached
    }

    // Store the updated result count in localStorage
    localStorage.setItem('currentResult', currentResult);
    updateProgressDisplay(); // Update display after changing currentResult
});

// Reset functionality for the "Rest" button
const restButton = document.querySelector('.start'); // Adjust if necessary to target the correct button
restButton.addEventListener('click', () => {
    currentResult = 1; // Reset to 1
    localStorage.setItem('currentResult', currentResult); // Store the reset value
    updateProgressDisplay(); // Update the display
});
