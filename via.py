import openai
import speech_recognition as sr

# Sets up the OpenAI API client
openai.api_key = "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"

# Creates a recognizer instance
r = sr.Recognizer()

# Configures the microphone as the audio source
mic = sr.Microphone()

# Configures the speech recognition request
languages = ['en-US', 'es-MX', 'fr-FR'] # List of language codes
transcriptions = {}

# Starts listening to the microphone and transcribing in real-time
with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    while True:
        audio = r.listen(source)
        for lang in languages:
            try:
                text = r.recognize_google(audio, language=lang)
                transcriptions[lang] = text
                response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=f"Translate '{text}' to Spanish", # Change to desired output language
                    max_tokens=60,
                    n=1,
                    stop=None,
                    temperature=0.5,
                )
                translation = response.choices[0].text
                print(f'Original ({lang}): {text}')
                print(f'Translation: {translation}')
            except sr.UnknownValueError:
                transcriptions[lang] = "Could not understand audio"
            except sr.RequestError as e:
                transcriptions[lang] = f"Could not request results from Google Speech Recognition service; {e}"