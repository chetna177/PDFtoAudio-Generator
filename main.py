import PyPDF2
import requests
from google.cloud import texttospeech

texts =""
with open("AtomicHabit.pdf","rb") as file:
    reader = PyPDF2.PdfReader(file)


    for page in reader.pages:

        texts += page.extract_text()


print(texts)

with open("text.txt","w") as file1:
    data=file1.write(texts)




url = "https://cloudresourcemanager.googleapis.com/v3/projects"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "projectId": "chetna-project-2026-111",
    "displayName": "PDFtoAUDIO",
    "labels": {
        "environment": "production",
        "costcenter": "marketing"
    }
}

response = requests.post(url, headers=headers, json=data)
# print(response.json())


client = texttospeech.TextToSpeechClient()

# Input text
synthesis_input = texttospeech.SynthesisInput(
    text=texts
)

# Voice settings
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Audio config
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Request
response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

# Save audio file
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)

print("Audio file generated: output.mp3")