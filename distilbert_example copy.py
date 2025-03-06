from transformers import DistilBertTokenizer, DistilBertModel

# Load the tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
model = DistilBertModel.from_pretrained("distilbert-base-uncased")

# Example input text
text = "Hello, welcome to the museum demo!"

# Encode the text using the tokenizer
inputs = tokenizer(text, return_tensors="pt")

# Get the model's output
outputs = model(**inputs)

# Print the last hidden states
print(outputs.last_hidden_state)
