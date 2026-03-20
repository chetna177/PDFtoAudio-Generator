# PDFtoAudio-Generator
📄🔊 PDF to Audio Generator

A Python-based tool that converts text from PDF files into high-quality audio using Google Cloud Text-to-Speech API.

This project extracts text from a PDF and generates an MP3 audio file, making it useful for audiobooks, accessibility, and learning on the go.

🚀 Features

📖 Extract text from PDF files using PyPDF2

🔊 Convert text to natural-sounding speech

☁️ Uses Google Cloud Text-to-Speech API

🎧 Outputs audio in MP3 format

⚡ Simple and easy-to-use Python script

🛠️ Tech Stack

Python 3.x

PyPDF2

Google Cloud Text-to-Speech API

Requests (optional for API handling)

🧠 How It Works

Read PDF

Uses PyPDF2 to extract text from all pages

Process Text

Cleans and prepares text for speech conversion

Convert to Speech

Sends text to Google Cloud TTS API

Save Audio

Writes the output as an MP3 file
⚠️ Limitations

Large PDFs may exceed API text limits

Formatting (tables, images) is not preserved

Requires internet connection for API calls

🔮 Future Improvements

Split large PDFs into chunks

Add multiple language support

Add voice customization (male/female, accents)

Build a GUI using Tkinter or Streamlit
💡 Author

Developed by Chetna Sahu
