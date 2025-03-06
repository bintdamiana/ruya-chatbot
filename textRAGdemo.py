from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch

# Function to get answers from the FAQ data
def answer_question(question, faq_data, tokenizer, model):
    # Tokenize the input question and context (faq_data)
    inputs = tokenizer(question, faq_data, return_tensors="pt", max_length=512, truncation=True)

    # Get the model's output
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the start and end positions of the answer
    answer_start = outputs.start_logits.argmax()  # Position of the start of the answer
    answer_end = outputs.end_logits.argmax()  # Position of the end of the answer

    # Decode the tokens back into the answer string
    answer_tokens = inputs.input_ids[0][answer_start:answer_end + 1]
    answer = tokenizer.decode(answer_tokens, skip_special_tokens=True)

    return answer

# Step 1: Load the pre-trained DistilBERT model for Question Answering and the tokenizer
model_name = "distilbert-base-uncased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Step 2: Your FAQ data (museum-specific content)
faq_data = """
What is the mission of the museum?
The museum celebrates language acquisition, diversity, and preservation, aiming to educate the public about language’s role in society and its universal aspects.

What are the main themes of the exhibits?
Universal aspects of language, language in society, and global linguistic diversity.

What exhibits and programs does the museum offer?
Virtual field trips, poetry around the world, and the history of words.

How does the museum promote language education?
Interactive exhibits, multimedia content, and community programs support language learning and preservation.

Who can benefit from the museum's programs?
General public, students, language enthusiasts, and professionals in linguistics and cultural studies.

How does the museum serve as a language forum?
It brings together linguists, policymakers, community leaders, and experts to discuss language's importance.

How can I get involved with the museum?
Become a member, volunteer, join the Language Leadership Council, or donate.

What educational resources does the museum offer?
Educational materials, language exploration activities, and cultural insights.

What is the museum's vision for language education?
To inspire curiosity and help people discover the wonders of language.

How can I stay updated on museum activities?
Subscribe to the newsletter, follow on social media, or visit the website for updates.
"""

# Step 3: Interact with the model via text
if __name__ == "__main__":
    print("Museum FAQ System powered by DistilBERT\n")
    print("Type 'exit' to quit the session.\n")

    while True:
        user_question = input("Ask a question about the museum: ")
        if user_question.lower() == 'exit':
            print("Exiting the session. Goodbye!")
            break

        answer = answer_question(user_question, faq_data, tokenizer, model)
        print(f"Answer: {answer}\n")