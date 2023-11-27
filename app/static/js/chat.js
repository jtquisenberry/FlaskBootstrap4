const chatForm = document.getElementById('chat-form');
const promptInput = document.getElementById('prompt');
const responseInput = document.getElementById('response');
const submitButton = document.getElementById('submit');
const clearButton = document.getElementById('clear');
const resultDiv = document.getElementById('result');

chatForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const message = promptInput.value;
  fetch('/api/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message })
  })
    .then(response => response.json())
    .then(data => {
      // resultDiv.innerHTML = data.result;
      responseInput.value = data.result;
    });
});

clearButton.addEventListener('click', () => {
  promptInput.value = '';
  resultDiv.innerHTML = '';
});
