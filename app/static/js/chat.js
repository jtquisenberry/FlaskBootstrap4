const chatForm = document.getElementById('chat-form');
const messageInput = document.getElementById('message');
const submitButton = document.getElementById('submit');
const clearButton = document.getElementById('clear');
const resultDiv = document.getElementById('result');

chatForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const message = messageInput.value;
  fetch('/api/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message })
  })
    .then(response => response.json())
    .then(data => {
      resultDiv.innerHTML = data.result;
    });
});

clearButton.addEventListener('click', () => {
  messageInput.value = '';
  resultDiv.innerHTML = '';
});
