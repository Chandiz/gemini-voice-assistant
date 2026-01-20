# Gemini Voice Assistant (Raspberry Pi)

A simple voice-based AI assistant built on a Raspberry Pi using Google's Gemini API.
The device listens through a USB microphone, sends speech to Gemini, and prints responses in real time.

> ⚠️ This is a learning / prototype project, not a production assistant.

---

## Features

- Continuous voice interaction
- USB microphone support
- Google Gemini API integration
- Lightweight (Raspberry Pi 3B+ compatible)

---

## Requirements

- Python 3.9+
- Google Gemini API key
- USB microphone
- Internet connection

---

## Installation

```bash
pip install -r requirements.txt

## Set your API key:

export GOOGLE_API_KEY="YOUR_API_KEY"

## Run

python3 assistant.py 2>/dev/null


## Notes

Uses the gemini-2.5-flash model (free tier has request limits)

Audio output (text-to-speech) and LEDs were intentionally removed

Designed for experimentation and learning