import speech_recognition as sr
from googletrans import Translator
from pydub import AudioSegment
import os

def convert_audio_to_wav(audio_file, wav_file):
    audio = AudioSegment.from_file(audio_file)
    audio.export(wav_file, format="wav")

def recognize_and_translate_speech(audio_file, target_language):
    recognizer = sr.Recognizer()
    translator = Translator()

    def translate_text(text, target_language):
        translation = translator.translate(text, dest=target_language)
        return translation.text
    file_ext = os.path.splitext(audio_file)[-1].lower()
    if file_ext != ".wav":
        wav_file = "temp.wav"
        convert_audio_to_wav(audio_file, wav_file)
        audio_file = wav_file

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        transcribed_text = recognizer.recognize_google(audio_data)
        detected_language = recognizer.detect_google(transcribed_text)

        print(f"Detected Language: {detected_language}")
        print(f"Transcript: {transcribed_text}")
        translated_text = translate_text(transcribed_text, target_language)
        print(f"Translation ({target_language}): {translated_text}")

    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == '__main__':
    audio_file = 'Recording.m4a'
    target_language = 'en' 
    recognize_and_translate_speech(audio_file, target_language)
    
