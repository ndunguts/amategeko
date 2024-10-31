document.addEventListener('DOMContentLoaded', () => {
    // Initialize currentResult from localStorage or set to 1 by default
    let currentResult = localStorage.getItem('currentResult') ? parseInt(localStorage.getItem('currentResult')) : 1;

    // Check if the page is the start page after the reset
    if (window.location.pathname === '/start_q/') {
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
    const totalQuestions = 20;

    // Function to update the progress display
    function updateProgressDisplay() {
        document.querySelector('.current').textContent = currentResult;
        const progressWidth = (currentResult / totalQuestions) * 100;
        progressBar.style.width = `${progressWidth}%`;
        progressText.textContent = `${Math.round(progressWidth)}%`;
    }

    // Call to update the display initially
    updateProgressDisplay();

    // Function to validate the form
    function validateForm() {
        let radios = document.querySelectorAll('input[name="user_answer"]');
        let isChecked = Array.from(radios).some(radio => radio.checked);
        const errorMessage = document.getElementById('error-message'); // Ensure you have an element for error messages
    
        if (!isChecked) {
            errorMessage.textContent = 'Please select an answer before proceeding.';
            errorMessage.style.color = 'red'; // Optional: Style the error message
            return false;
        } else {
            errorMessage.textContent = ''; // Clear error message if validated
        }
    
        return true;
    }
    

    // Add an event listener to the "Next" button
    showAnswerButton.addEventListener('click', (event) => {
        if (!validateForm()) {
            event.preventDefault();
            return;
        }

        // Increment currentResult
        if (currentResult < totalQuestions) {
            currentResult++;
        } else {
            currentResult = 1; // Reset if maximum reached
        }

        // Store updated currentResult in localStorage
        localStorage.setItem('currentResult', currentResult);
        updateProgressDisplay();
    });

    // Reset functionality for the "Reset" button
    const restButton = document.querySelector('.star');
    restButton.addEventListener('click', () => {
        currentResult = 1;
        localStorage.setItem('currentResult', currentResult);
        updateProgressDisplay();
    });
});
