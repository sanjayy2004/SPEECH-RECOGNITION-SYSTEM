import speech_recognition as sr

# Create a recognizer instance
recognizer = sr.Recognizer()

# Load the audio file
with sr.AudioFile("sample.wav.wav") as source:
    print("Listening...")
    audio_data = recognizer.record(source)
    print("Recognizing...")

# Try to convert speech to text using Google Web Speech API
try:
    text = recognizer.recognize_google(audio_data)
    print("Transcription:", text)
except sr.UnknownValueError:
    print("Speech was unclear.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
