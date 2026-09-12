# 🎙️ Speech Recognition using Python

A Python speech recognition project that converts spoken Persian language from an audio file into text using the SpeechRecognition library and Google's Speech Recognition service.

## Overview

This project demonstrates how to process an audio file and convert speech into written text.

The program loads a `.wav` audio file, records the audio data using the `SpeechRecognition` library, and sends the audio to Google's Speech Recognition service for transcription.

The project is currently configured to recognize **Persian (Iranian)** speech using the `fa-IR` language setting.

## Features

* 🎙️ Speech recognition
* 🔊 Audio file processing
* 📝 Speech-to-text conversion
* 🇮🇷 Persian language recognition
* 🎧 WAV audio file support
* ☁️ Google Speech Recognition service
* 🐍 Simple Python implementation

## Technologies Used

* Python
* SpeechRecognition
* Google Speech Recognition API

## Input

The program uses a WAV audio file as its input:

```text
tf.wav
```

The audio file contains the speech that will be converted into text.

The current project is configured for Persian speech recognition:

```python
text = r.recognize_google(audio, language='fa-IR')
```

The `fa-IR` language code specifies Persian as the recognition language.


## How It Works

The project follows these main steps:

```text
Load WAV Audio File
        ↓
Create Recognizer
        ↓
Read Audio Data
        ↓
Send Audio to Google
        ↓
Recognize Persian Speech
        ↓
Convert Speech to Text
        ↓
Print Result
```

## Speech Recognition

The `SpeechRecognition` library is used to process the audio.

First, a recognizer object is created:

```python
import speech_recognition as sr

r = sr.Recognizer()
```

The WAV file is then loaded:

```python
voice = sr.AudioFile("tf.wav")
```

The audio data is recorded from the file:

```python
with voice as source:
    audio = r.record(source)
```

The resulting audio object can then be sent to the speech recognition service.

## Google Speech Recognition

The project uses Google's Speech Recognition service to convert the recorded audio into text.

```python
text = r.recognize_google(
    audio,
    language='fa-IR'
)

print(text)
```

The `language='fa-IR'` parameter tells the service to recognize the speech as Persian.

## Output

The program prints the recognized text in the terminal.

For example:

```text
Recognized Text:
سلام، این یک تست می کنیم 1 2 3 تشخیص صدا است.
```

The exact output depends on the content and quality of the input audio.

## Complete Code

```python
import speech_recognition as sr

r = sr.Recognizer()

voice = sr.AudioFile("tf.wav")

with voice as source:
    audio = r.record(source)

print(audio)

text = r.recognize_google(
    audio,
    language='fa-IR'
)

print(text)
```

## Output

The program prints the recognized text in the terminal.

For example:

```text
Recognized Text:
سلام، این یک تست می کنیم 1 2 3 تشخیص صدا است.
```

The exact output depends on the content and quality of the input audio.

## Complete Code

```python
import speech_recognition as sr

r = sr.Recognizer()

voice = sr.AudioFile("tf.wav")

with voice as source:
    audio = r.record(source)

print(audio)

text = r.recognize_google(
    audio,
    language='fa-IR'
)

print(text)
```

## Project Structure

```text
Speech-Recognition/
│
├── tf.wav
├── Farsi_Speech_Recognition.py
├── speech recognition.ipynb
├── requirements.txt
├── LICENSE
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Matin-python/Speech-Recognition.git
```

Go to the project directory:

```bash
cd Speech-Recognition
```

Install the required library:

```bash
pip install SpeechRecognition
```

Or install the dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## How to Run

Make sure the audio file is located in the project directory:

```text
tf.wav
```

Then run the Python script:

```bash
python speech_recognition.py
```

The program will:

1. Create a speech recognizer.
2. Load the WAV audio file.
3. Read the audio data.
4. Send the audio to Google's Speech Recognition service.
5. Recognize the Persian speech.
6. Convert the speech into text.
7. Print the recognized text.

## Requirements

* Python 3
* Internet connection
* A `.wav` audio file
* `SpeechRecognition` library

An internet connection is required because `recognize_google()` uses Google's online speech recognition service.

## Error Handling

The current version of the project assumes that the audio can be successfully recognized.

The `SpeechRecognition` library can raise exceptions when:

* The speech cannot be understood.
* The Google service cannot be reached.
* The audio format is not supported.
* The input audio contains too much noise.

These cases can be handled using exceptions such as:

```python
sr.UnknownValueError
```

and:

```python
sr.RequestError
```

## Future Improvements

* 🎤 Add real-time microphone speech recognition
* 🌍 Support multiple languages
* 🔇 Add noise reduction
* 🎚️ Improve audio preprocessing
* ⏱️ Add real-time transcription
* 💾 Save recognized text to a file
* 📝 Create a graphical user interface
* 🔄 Process multiple audio files
* 📊 Compare recognition accuracy for different audio qualities
* 🛡️ Add complete exception handling

## Contributing

Contributions, suggestions, and bug reports are welcome.

Feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Author

Mohammad Reza Bakhshandeh

Interested in Python, Machine Learning, Deep Learning, Computer Vision, Artificial Intelligence, and Game Development.
