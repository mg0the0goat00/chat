// Get references to the chatbot elements
const container = document.querySelector('#container');
const inputField = document.createElement('input');
const sendBtn = document.createElement('button');
const messagesList = document.createElement('ul');
const apiKey = 'YOUR_API_KEY'; // Replace with your actual API key

// Set up the input field and send button
inputField.id = 'input-field';
inputField.placeholder = 'Ask me anything!';
inputField.addEventListener('keyup', event => {
    if (event.code === 'Enter') {
        sendMessage();
    }
});

sendBtn.id = 'send-btn';
sendBtn.innerText = 'Send';
sendBtn.addEventListener('click', () => {
    sendMessage();
});

// Append the input field and send button to the container
container.appendChild(inputField);
container.appendChild(sendBtn);

// Set up the messages list
messagesList.id = 'messages';
container.appendChild(messagesList);

/**
 * Fetches a response from the OpenAI ChatGPT API and appends it to the messages list
 */
async function sendMessage() {
    // Remove the input field value after sending the message
    inputField.value = '';

    // Get the user's message
    const userMessage = inputField.value;

    // Display the user's message in the messages list
    messagesList.innerHTML += `<li><strong>You:</strong> ${userMessage}</li>`;

    try {
        // Fetch a response from the OpenAI ChatGPT API
        const response = await fetch(`https://api.openai.com/v1/chat/completions`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`,
            },
            body: JSON.stringify({
                model: 'text-davinci-03',
                prompt: userMessage,
            }),
        });

        // Parse the response JSON
        const jsonResponse = await response.json();
        const aiResponse = jsonResponse?.choices?.?.message?.content ?? '';

        // Display the AI's response in the messages list
        messagesList.innerHTML += `<li><strong>ChatBot:</strong> ${aiResponse}</li>`;
    } catch (error) {
        console.error('Error fetching response:', error);
    }
}
