from flask import Flask, request, jsonify , render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

@app.route('/')
def home():
    return render_template('index.html')  # Make sure this points to the correct HTML file

@app.route('/infer', methods=['POST'])
def infer():
    data = request.get_json()
    model = data['model']
    input_text = data['inputs']

    HF_API_KEY = '<>'  # Secure this appropriately
    HF_API_URL = f"https://api-inference.huggingface.co/models/{model}"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"inputs": input_text}

    response = requests.post(HF_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to retrieve data from the Hugging Face API"}), response.status_code
    logging.debug(f"Request received with model: {model} and text: {input_text}")
    if response.status_code == 200:
        logging.debug("API call successful")
        return jsonify(response.json())
    else:
        logging.error(f"API call failed with status code {response.status_code}")
        return jsonify({"error": "Failed to retrieve data from the Hugging Face API"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
