import speech_recognition as sr

r = sr.Recognizer()

voice = sr.AudioFile("tf.wav")
with voice as source:
    audio = r.record(source)
print(audio)

text = r.recognize_google(audio, language= 'fa-IR')
print(text)