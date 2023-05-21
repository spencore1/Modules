import speech_recognition as sr 

#create recognizer instance 
r = sr.Recognizer()

#load audio file
with sr.AudioFile('audio_file.wav') as source:
    audio = r.record(source)

#convert speech to text
text = r.recognize_google(audio)
print(text)