async function loadModel() {
    const model = document.getElementById('modelSelector').value;
    const inputText = document.getElementById('inputText').value;

    // Configure the fetch request to send data to your Flask server
    const response = await fetch('/infer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({model: model, inputs: inputText})
    });

    // Handle the response from the server
    if (response.ok) {
        const result = await response.json();
        document.getElementById('output').innerText = JSON.stringify(result.generated_text, null, 2);
    } else {
        // If the server responds with an error, display a generic error message
        const errorMsg = await response.text();
        document.getElementById('output').innerText = 'Error: Unable to fetch the model results. ' + errorMsg;
    }
}

// Optional: Add an event listener for the button click if not using inline 'onclick' attribute
document.addEventListener('DOMContentLoaded', function() {
    const inferenceButton = document.getElementById('modelInferenceButton');
    if (inferenceButton) {
        inferenceButton.addEventListener('click', loadModel);
    }
});
