document.addEventListener('DOMContentLoaded', function() {
    const messageForm = document.getElementById('messageForm');
    const messageInput = document.getElementById('message');
    const chatbox = document.getElementById('chatbox');

    messageForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const userMessage = messageInput.value.trim();
        if (userMessage) {
            appendMessage('You', userMessage, 'user');
            messageInput.value = '';
            fetchResponse(userMessage);
        }
    });

    function appendMessage(sender, message, className) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', className);
        messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatbox.appendChild(messageElement);
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    function fetchResponse(message) {
        fetch('/api/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        })
        .then(response => response.json())
        .then(data => {
            appendMessage('Bot', data.response, 'bot');
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage('Bot', 'Sorry, there was an error processing your request.', 'bot');
        });
    }
});
