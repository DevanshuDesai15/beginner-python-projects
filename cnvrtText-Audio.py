from gtts import gTTS

from playsound import playsound

audio='speech.mp3'
language='en'

sp=gTTS(text="Enter the text to convert it into a video file...", lang=language, slow=False)

sp.save(audio)
playsound(audio)