// script.js

// Function to fade out messages after a certain time
function fadeOutMessages() {
    setTimeout(function() {
        var messages = document.getElementsByClassName('messages');
        for (var i = 0; i < messages.length; i++) {
            messages[i].style.opacity = '0';
            messages[i].style.transition = 'opacity 1s ease-out';
            setTimeout(function() {
                messages[i].style.display = 'none';
            }, 1000); // hide after 1 second
        }
    }, 5000); // fade out after 5 seconds
}

// Call fadeOutMessages when the page loads
window.onload = function() {
    fadeOutMessages();
};
