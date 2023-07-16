import pyttsx3

# Initialize pyttsx3 engine
# wrap the pyttsx3 initialization code in a class
# so that it can be used in other files
class TextToSpeech():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        # using the voice of male
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()