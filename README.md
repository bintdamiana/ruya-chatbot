# RUYA Chatbot

RUYA is a multilingual AI chatbot with advanced FAQ matching, text-to-speech (TTS), and speech-to-text (STT) capabilities. It is designed to provide seamless conversational experiences for businesses and developers.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Features
- **FAQ Matching**:
  - Accurate semantic matching using DistilBERT.
  - Pre-trained models for quick deployment.
- **Ruya Chatbot**:
  - Multilingual support for global audiences.
  - Text-to-speech (TTS) and speech-to-text (STT) integration.
  - Customizable to fit your brand and use case.

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

## Contact
For questions, collaborations, or commercial licensing, feel free to reach out:

- Website: [almadisahara.com](https://almadisahara.com)
- Email: bintdamiana@gmail.com

Sahara is happy to assist you with any inquiries or support you may need!