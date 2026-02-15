# Gemini Voice Assistant (Raspberry Pi Edge Prototype)

An edge-based voice assistant prototype built on Raspberry Pi 3B+ using Google Gemini API.

This project demonstrates:

- Real-time speech-to-text input
- API-based LLM interaction
- Lightweight edge device deployment
- Continuous voice interaction loop
- Python-based system integration

---

## Architecture Overview

USB Microphone  
→ Speech Recognition  
→ Google Gemini API (gemini-2.5-flash)  
→ Real-time text response  

Designed as a minimal edge AI system running on constrained hardware.

---

## Purpose

This project was built as an infrastructure-focused prototype to explore:

- AI integration on edge devices
- Lightweight LLM usage
- Python-based automation workflows
- API key management via environment variables
- Raspberry Pi system constraints and optimization

⚠️ This is a learning / experimentation project — not a production assistant.

---

## Technical Stack

- Python 3.9+
- Google Gemini API
- SpeechRecognition library
- Raspberry Pi OS
- USB Microphone input

---

## Installation

```bash
pip install -r requirements.txt
export GOOGLE_API_KEY="YOUR_API_KEY"
python3 assistant.py
