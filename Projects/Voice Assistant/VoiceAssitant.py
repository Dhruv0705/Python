import pyttsx3 as TTS
import speech_recognition
import webbrowser
import datetime
import pyjokes 
import pyaudio

def SpeechTextRecognizer():
    Recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as Source:
        print("Listening...")
        Recognizer.adjust_for_ambient_noise(Source)
        Audio = Recognizer.listen(Source)
        try:
            print("Recognizing...")
            Data = Recognizer.recognize_google(Audio)
            print(Data)
        except speech_recognition.UnknownValueError:
            print(" I Don't Understand")

SpeechTextRecognizer()
