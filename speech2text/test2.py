import speech_recognition as sr
from langdetect import detect
from translate import Translator

r = sr.Recognizer()

mic = sr.Microphone()

transcriptions = {}

recording = False

while True:
    if not recording:
        input("Press Enter to start recording...")
        recording = True
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Recording started. Say something!")
            audio = r.listen(source)
    else:
        input("Press Enter to stop recording...")
        recording = False
        try:
            text = r.recognize_google(audio)
            detected_language = detect(text) 
            transcriptions[detected_language] = text
            print(f'Detected language: {detected_language}')
            print(f'Spoken text ({detected_language}): {text}')
            target_language = input("Select a language code for translation (e.g., en for English): ")
            if target_language:
                try:
                    translator = Translator(to_lang=target_language)
                    translation = translator.translate(text)
                    print(f'Translation to {target_language}: {translation}')
                except ValueError:
                    print(f"Invalid language code: {target_language}")
            else:
                print("No target language selected. Skipping translation.")

        except sr.UnknownValueError:
            detected_language = "Unknown"
            transcriptions[detected_language] = "Could not understand audio"
        except sr.RequestError as e:
            detected_language = "Unknown"
            transcriptions[detected_language] = f"Could not request results from Google Speech Recognition service; {e}"