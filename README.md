# RUYA: Multilingual Chatbot for Inclusive Communication

RUYA is a multilingual AI chatbot designed to enrich user experiences with advanced FAQ matching, text-to-speech (TTS), and speech-to-text (STT) capabilities. With a focus on seamless and inclusive communication, RUYA aims to make every interaction more accessible and engaging. Whether you're a business looking to enhance customer support, an educator aiming to inspire, or a developer seeking to innovate, RUYA is here to help you build meaningful connections in a smarter, more connected world.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Features
- **Multilingual Support**: Engage with users in multiple languages.
- **Advanced FAQ Matching**: Accurate semantic matching using DistilBERT.
- **Text-to-Speech (TTS)**: Convert text responses to spoken words.
- **Speech-to-Text (STT)**: Transcribe spoken words into text.
- **Customizable**: Tailor the chatbot to fit your brand and use case.

## Setup
### Set up a virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Download additional resources (optional):
- For DistilBERT:
  ```bash
  python -m spacy download en_core_web_sm
  ```

## Usage
### FAQ Matching
1. **Navigate to the faqmatch folder**:
   ```bash
   cd faqmatch
   ```
2. **Run the script**:
   ```bash
   python faq_matching.py
   ```

### Ruya Chatbot
1. **Navigate to the ruya folder**:
   ```bash
   cd ruya
   ```
2. **Run the chatbot**:
   ```bash
   python ruya_chatbot.py
   ```

## License
This project is dual-licensed under the following licenses:

- **Open-Source License**: GNU Affero General Public License (AGPL)
  - You are free to use, modify, and distribute this project under the terms of the AGPL.
  - If you modify and distribute this project, you must share your changes under the same license.

- **Commercial License**: Commercial License
  - If you want to use this project without the restrictions of the AGPL, you must purchase a commercial license.
  - Visit [almadisahara.com](https://almadisahara.com) for pricing and terms.

## Acknowledgments

The development of RUYA Chatbot has benefited from the support of several advanced AI models, frameworks, platforms, and technologies. Sahara would like to express sincere gratitude to the following contributors:

- **Moonshot AI**: Kimi intelligent assistant. [Moonshot AI Website](https://www.moonshot.ai )
- **DeepSeek**: Mixture-of-Experts architecture. [DeepSeek Documentation](https://www.deepseek.com )
- **OpenAI's ChatGPT**: Leading AI model. [OpenAI Website](https://www.openai.com )
- **Whisper AI (by OpenAI)**: Speech recognition. [Whisper GitHub Repository](https://github.com/openai/whisper )
- **DistilBERT**: Semantic matching. [Hugging Face Model Page](https://huggingface.co/distilbert-base-uncased )
- **Flask**: Web framework. [Flask Official Website](https://flask.palletsprojects.com )
- **Heroku**: Cloud application platform. [Heroku Official Website](https://www.heroku.com )
- **Text-to-Speech (TTS) and Speech-to-Text (STT) APIs**: Voice-based interactions.

Sahara also extends thanks to mentors Paul Shin and Angie Howard for their invaluable guidance and support throughout this project. Their insights and encouragement have been instrumental in her journey.

## Contact
For questions, collaborations, or commercial licensing, feel free to reach out to Sahara Al-Madi:

- Website: https://almadisahara.com
- Email: bintdamiana@gmail.com

Sahara is happy to assist you with any inquiries or support you may need!