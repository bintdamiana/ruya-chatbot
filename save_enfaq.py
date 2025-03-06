import json

# JSON data as a string
faq_json = '''
{
  "faq": [
    {
      "question": "What is the mission of the museum?",
      "answer": "The Museum celebrates language acquisition, diversity, and preservation, with the goal of educating the public about language's role in society and its universal aspects."
    },
    {
      "question": "What are the main themes of the exhibits?",
      "answer": "Universal Aspects of Language: Common features across all languages. Language in Society: How language shapes culture and identity. Languages of the World: Celebrating global linguistic diversity."
    },
    {
      "question": "What exhibits and programs does the museum offer?",
      "answer": "Languages of Science: Language in the scientific field. What Makes People Laugh?: Humor across languages. Social Justice Poetry: Poetry on social justice in 10 languages. A Virtual Cruise to Puerto Rico: Explore Puerto Rican language and culture. Philogelos: The oldest known joke book."
    },
    {
      "question": "How does the museum promote language education?",
      "answer": "The museum offers interactive exhibits, multimedia content, and community programs to support language learning and preservation."
    },
    {
      "question": "Who can benefit from the museum's programs?",
      "answer": "General public, students, language enthusiasts, and professionals in linguistics and cultural studies."
    },
    {
      "question": "How does the museum serve as a language forum?",
      "answer": "It brings together linguists, policymakers, community leaders, and experts from various fields to discuss the importance of language."
    },
    {
      "question": "How can I get involved?",
      "answer": "Become a member, volunteer, join the Language Leadership Council, or donate."
    },
    {
      "question": "What educational resources does the museum offer?",
      "answer": "Teachers Corner: Resources for educators. Language of the Month: A featured language each month. Immigrant Success Stories: The role of language in immigrant success."
    },
    {
      "question": "What is the museums vision for language education?",
      "answer": "To inspire curiosity and help people discover the wonders of language."
    },
    {
      "question": "How can I stay updated?",
      "answer": "Subscribe to the newsletter, follow on social media, or visit the website for updates."
    }
  ]
}
'''

# Parse the JSON data
faq_data = json.loads(faq_json)

# Save the data to a .json file
with open('faq_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(faq_data, json_file, ensure_ascii=False, indent=4)

print("JSON data has been saved to faq_data.json")
