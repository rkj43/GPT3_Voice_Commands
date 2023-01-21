import requests
import speech_recognition as sr
import pyttsx3
import openai

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the text-to-speech engine
engine = pyttsx3.init()

# Set up the speech recognition object
r = sr.Recognizer()

# Continuously listen for audio input and respond
while True:
    # Listen for audio input
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Transcribe the audio input into text
    text = r.recognize_google(audio)
    print(f"You said: {text}")

    # Use GPT-3 to generate a response based on the input text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the response text from the API response
    response_text = response["choices"][0]["text"]
    print(f"GPT-3 response: {response_text}")

    # Convert the response text to speech
    engine.say(response_text)
    engine.runAndWait()
