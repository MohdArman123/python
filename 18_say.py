import cowsay
import pyttsx3  # python text to speech library

engine = pyttsx3.init()   # initialize the library for text to speech
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()