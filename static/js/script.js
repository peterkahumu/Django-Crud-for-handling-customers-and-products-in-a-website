// Function to automatically show messages
function showMessagesAutomatically() {
    // Select messages section
    const messagesSection = document.querySelector('#messages');

    // Check if messages section exists and has children
    if (messagesSection && messagesSection.children.length > 0) {
        // Convert HTMLCollection to array using Array.from()
        Array.from(messagesSection.children).forEach(message => {
            // Add classes for styling (you can customize these classes)
            message.classList.add('notification', 'fadeout');

            // Automatically remove after 5 seconds (adjust timing as needed)
            setTimeout(() => {
                message.remove();
            }, 5000);  // 5000 milliseconds = 5 seconds
        });
    }
}

// Automatically show messages on page load
document.addEventListener('DOMContentLoaded', function() {
    showMessagesAutomatically();
});