from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

app = Flask(__name__)

# Load the fine-tuned DistilBERT model and tokenizer
model_name = "./fine_tuned_model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Your FAQ data
faq_data = """
What is the mission of the museum?
The National Museum of Language celebrates language acquisition, diversity, and preservation, aiming to educate the public about language’s role in society and its universal aspects.
...
"""

@app.route('/')
def index():
    return render_template('indexruya.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    inputs = tokenizer(user_input, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    predicted_label = torch.argmax(outputs.logits).item()
    response = faq_data[predicted_label]  # Replace with your logic to fetch the correct answer
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)