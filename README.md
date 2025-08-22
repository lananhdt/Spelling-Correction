# 📝 Spelling Correction

A contextual spelling correction system using spaCy embeddings and contextualSpellCheck for real-time English sentence correction.

## 🎯 Project Overview
�
This project builds a real-time contextual spelling correction system that:

- Uses spaCy pre-trained language model (`en_core_web_md`) for word embeddings and context understanding
- Integrates contextualSpellCheck to detect and correct spelling mistakes in English sentences
- Leverages contextual embeddings instead of simple dictionary lookup for more accurate correction
- Provides a user-friendly Streamlit interface for interactive text input and visualization
- Displays corrected text, suggestions, and token-level analysis in real-time

## 🏗️ Architecture

- **Language Model**: spaCy (`en_core_web_md`) for tokenization and contextual word embeddings
- **Spell Checking Engine**: contextualSpellCheck integrated into spaCy pipeline for error detection and correction
- **Web Framework**: Streamlit for the interactive user interface
- **Data Processing**: spaCy pipeline for text preprocessing and token analysis
- **Input**: User-typed English sentences via text input box
- **Visualization**: Streamlit components (expander, success message) for showing corrections, suggestions, and token breakdown

## 🚀 Quick Start

> **💡 Want to try it first?** Check out the [live demo](#-live-demo) above for instant access without any setup!

### Local Setup

```bash
# Clone the repository
git clone https://github.com/lananhdt/Spelling-Correction
cd Spelling-Correction

# Install dependencies
pip install -r requirements.txt

# Start the Streamlit app
streamlit run app.py
```

## 📋 Prerequisites

- Python 3.8+
- Git
- Dependencies listed in `requirements.txt`:
  - `spacy==3.7.2`
  - `contextualSpellCheck==0.4.4`
  - `streamlit==1.46.1`
- Download spaCy model before first use:
```bash
python -m spacy download en_core_web_md
```

## 🎮 Features

### 🔍 Correction Workflow

- **Real-time Input**: Users can type or paste text directly into the web app
- **Contextual Spell Checking**:
  - Detects common spelling mistakes
  - Uses contextual understanding (via `spacy` + `contextualSpellCheck`) to suggest corrections
- **Automatic Correction**: Provides corrected output instantly
- **Interactive Mode**: Users can compare original vs corrected text

### 🎨 User Interface

- Streamlit-based simple UI
- Input text box for raw text
- Real-time display of corrected sentences
- Highlighted corrections for better visualization

### 🧠 AI Features

- Uses **spaCy NLP pipeline** with pre-trained English model (`en_core_web_md`)
- **contextualSpellCheck** for context-aware spelling correction
- Supports sentence-level correction instead of just word-level

## 📁 Project Structure

```text
Spelling-Correction/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
└── README.md               # This file
```
