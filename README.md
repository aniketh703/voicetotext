# voicetotext
# Speech Recognition and Translation in Python
This Python script uses the `speech_recognition` library to recognize spoken text and the `translate` library to translate it into a target language. It also includes language detection using the `cld2-cffi` library.
## Prerequisites
Before running the script, you need to install the required libraries. You can install them using pip:
pip install speechrecognition translate cld2-cffi
Usage:
Run the Python script:
python speech_recognition_translation.py
The script will listen to your microphone input and recognize spoken text.
It will detect the language of the spoken text using cld2-cffi and print the detected language.
The detected text in the original language will be displayed.
You will be prompted to select a target language for translation (e.g., en for English).
If you choose a target language, the script will translate the text into the selected language using the translate library and display the translation.
You can repeat the process as many times as needed.
Supported Languages
The script supports various languages for speech recognition and translation. You can specify the target language code during translation.
Customization
To add or modify the list of supported languages, update the languages list in the code.
You can customize the behavior of the script by modifying the code to fit your specific use case.
Acknowledgments
This script uses the speech_recognition, translate, and cld2-cffi libraries. Thank you to the developers of these libraries for their contributions.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Author
Aniketh vustepalle
#There are also other files in another folder make sure you check them out.
