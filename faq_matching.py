from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch
from google.cloud import texttospeech
import os


# Initialize Google Cloud TTS client
client = texttospeech.TextToSpeechClient()

# Function to add pauses after every 3 words in SSML format
def add_pauses_to_text(text):
    words = text.split()
    chunks = []
    
    # Split text into chunks of 3 words and insert a pause
    for i in range(0, len(words), 3):
        chunk = ' '.join(words[i:i+3])
        chunks.append(chunk)
    
    # Join all chunks with pauses between them
    ssml_text = ""
    for chunk in chunks:
        ssml_text += f"{chunk}<break time='300ms'/> "  # 300ms pause
    
    return ssml_text

# Function to get answers from the FAQ data and return SSML
def answer_question(question, faq_data):
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

    # Convert answer to SSML format with pauses
    ssml_answer = f"<speak>{add_pauses_to_text(answer)}</speak>"

    return ssml_answer
    
# Step 1: Load the pre-trained DistilBERT model for Question Answering and the tokenizer
model_name = "distilbert-base-uncased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Step 2: Your FAQ data (museum-specific content) with RAG variations
faq_data = """
What is the mission of the museum?
The museum celebrates language acquisition, diversity, and preservation, aiming to educate the public about language’s role in society and its universal aspects.

What is the primary goal of the museum?
The museum celebrates language acquisition, diversity, and preservation, aiming to educate the public about language’s role in society and its universal aspects.

What does the museum aim to achieve?
The museum celebrates language acquisition, diversity, and preservation, aiming to educate the public about language’s role in society and its universal aspects.

What is the museum's purpose?
The museum celebrates language acquisition, diversity, and preservation, aiming to educate the public about language’s role in society and its universal aspects.

What are the main themes of the exhibits?
Universal aspects of language, language in society, and global linguistic diversity.

What are the key themes in the museum's exhibits?
Universal aspects of language, language in society, and global linguistic diversity.

What themes are covered in the museum's exhibits?
Universal aspects of language, language in society, and global linguistic diversity.

What are the central themes of the museum's displays?
Universal aspects of language, language in society, and global linguistic diversity.

What exhibits and programs does the museum offer?
Virtual field trips, poetry around the world, and the history of words.

What can I see or participate in at the museum?
Virtual field trips, poetry around the world, and the history of words.

What kind of exhibits and programs are available at the museum?
Virtual field trips, poetry around the world, and the history of words.

What are the current exhibits and programs offered by the museum?
Virtual field trips, poetry around the world, and the history of words.

How does the museum promote language education?
Interactive exhibits, multimedia content, and community programs support language learning and preservation.

What efforts does the museum make to support language learning?
Interactive exhibits, multimedia content, and community programs support language learning and preservation.

How does the museum encourage language education?
Interactive exhibits, multimedia content, and community programs support language learning and preservation.

What initiatives does the museum have for language education?
Interactive exhibits, multimedia content, and community programs support language learning and preservation.

Who can benefit from the museum's programs?
General public, students, language enthusiasts, and professionals in linguistics and cultural studies.

Who is the museum's target audience?
General public, students, language enthusiasts, and professionals in linguistics and cultural studies.

What groups can take advantage of the museum's programs?
General public, students, language enthusiasts, and professionals in linguistics and cultural studies.

Who are the primary beneficiaries of the museum's programs?
General public, students, language enthusiasts, and professionals in linguistics and cultural studies.

How does the museum serve as a language forum?
It brings together linguists, policymakers, community leaders, and experts to discuss language's importance.

What role does the museum play in language discussions?
It brings together linguists, policymakers, community leaders, and experts to discuss language's importance.

How does the museum facilitate language-related discussions?
It brings together linguists, policymakers, community leaders, and experts to discuss language's importance.

What forums or discussions does the museum host related to language?
It brings together linguists, policymakers, community leaders, and experts to discuss language's importance.

How can I get involved with the museum?
Become a member, volunteer, join the Language Leadership Council, or donate.

What opportunities are there to participate in the museum's activities?
Become a member, volunteer, join the Language Leadership Council, or donate.

How can I contribute to the museum?
Become a member, volunteer, join the Language Leadership Council, or donate.

What ways can I support the museum?
Become a member, volunteer, join the Language Leadership Council, or donate.

What educational resources does the museum offer?
Educational materials, language exploration activities, and cultural insights.

What resources are available for learning about language?
Educational materials, language exploration activities, and cultural insights.

What educational tools does the museum provide?
Educational materials, language exploration activities, and cultural insights.

What resources does the museum offer for educators and students?
Educational materials, language exploration activities, and cultural insights.

What is the museum's vision for language education?
To inspire curiosity and help people discover the wonders of language.

What goals does the museum have for language education?
To inspire curiosity and help people discover the wonders of language.

What is the museum's outlook on language education?
To inspire curiosity and help people discover the wonders of language.

What is the museum's long-term vision for language education?
To inspire curiosity and help people discover the wonders of language.

How can I stay updated on museum activities?
Subscribe to the newsletter, follow on social media, or visit the website for updates.

How can I keep informed about the museum's events?
Subscribe to the newsletter, follow on social media, or visit the website for updates.

What is the best way to stay in the loop with the museum?
Subscribe to the newsletter, follow on social media, or visit the website for updates.

How can I receive updates from the museum?
Subscribe to the newsletter, follow on social media, or visit the website for updates.
"""

# Step 3: Automatically print all questions and their answers
if __name__ == "__main__":
    print("Museum FAQ System powered by DistilBERT and Google Cloud TTS\n")

    # List of questions in the FAQ data
    questions = [
        "What is the mission of the museum?",
        "What is the primary goal of the museum?",
        "What does the museum aim to achieve?",
        "What is the museum's purpose?",
        "What are the main themes of the exhibits?",
        "What are the key themes in the museum's exhibits?",
        "What themes are covered in the museum's exhibits?",
        "What are the central themes of the museum's displays?",
        "What exhibits and programs does the museum offer?",
        "What can I see or participate in at the museum?",
        "What kind of exhibits and programs are available at the museum?",
        "What are the current exhibits and programs offered by the museum?",
        "How does the museum promote language education?",
        "What efforts does the museum make to support language learning?",
        "How does the museum encourage language education?",
        "What initiatives does the museum have for language education?",
        "Who can benefit from the museum's programs?",
        "Who is the museum's target audience?",
        "What groups can take advantage of the museum's programs?",
        "Who are the primary beneficiaries of the museum's programs?",
        "How does the museum serve as a language forum?",
        "What role does the museum play in language discussions?",
        "How does the museum facilitate language-related discussions?",
        "What forums or discussions does the museum host related to language?",
        "How can I get involved with the museum?",
        "What opportunities are there to participate in the museum's activities?",
        "How can I contribute to the museum?",
        "What ways can I support the museum?",
        "What educational resources does the museum offer?",
        "What resources are available for learning about language?",
        "What educational tools does the museum provide?",
        "What resources does the museum offer for educators and students?",
        "What is the museum's vision for language education?",
        "What goals does the museum have for language education?",
        "What is the museum's outlook on language education?",
        "What is the museum's long-term vision for language education?",
        "How can I stay updated on museum activities?",
        "How can I keep informed about the museum's events?",
        "What is the best way to stay in the loop with the museum?",
        "How can I receive updates from the museum?"
    ]
    
    # Loop through each question in the FAQ
    for question in questions:
        print(f"Question: {question}")

        # Get the answer using the model
        ssml_answer = answer_question(question, faq_data)

        # Request synthesis using SSML (Google Cloud TTS)
        synthesis_input = texttospeech.SynthesisInput(ssml=ssml_answer)

        # Set the voice parameters (using en-US-Standard-C)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Standard-C",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )

        # Set the audio encoding (MP3 in this case)
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Synthesize speech
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        # Save the output audio to a file with the question as part of the filename
        output_file = f"audio_{question.replace(' ', '_').replace('?', '').lower()}.mp3"
        with open(output_file, "wb") as out:
            out.write(response.audio_content)

        # Inform the user that the audio has been saved
        print(f"Answer (with SSML and pauses): {ssml_answer}")
        print(f"Audio saved to: {os.path.abspath(output_file)}\n")