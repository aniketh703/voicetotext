import speech_recognition as sr
from translate import Translator
from langdetect import detect

r = sr.Recognizer()

mic = sr.Microphone()

transcriptions = {}

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            detected_language = detect(text) 
            transcriptions[detected_language] = text
            print(f'Detected language: {detected_language}')
            print(f'Spoken text ({detected_language}): {text}')
            target_language = input("Select a language code for translation (e.g., en for English): ")
            if target_language:
                translator = Translator(to_lang=target_language)
                translation = translator.translate(text)
                print(f'Translation to {target_language}: {translation}')
            else:
                print("No target language selected. Skipping translation.")

        except sr.UnknownValueError:
            detected_language = "Unknown"
            transcriptions[detected_language] = "Could not understand audio"
        except sr.RequestError as e:
            detected_language = "Unknown"
            transcriptions[detected_language] = f"Could not request results from Google Speech Recognition service; {e}"
