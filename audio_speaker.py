import pyttsx3

class play_audio():
    def __init__(self,voice='female',speakstatus=True):
        self.voice='female'
        self.speakstatus=speakstatus
        self.speakWords={'1':'one',
                         '2':'two',
                         '3':'three',
                         '4':'four',
                         '5':'five',
                         '6':'six',
                         '7':'seven',
                         '8':'eight',
                         '9':'nine',
                         '0':'zero'}
        self.engine=pyttsx3.init()
        V=self.engine.getProperty('voices')
        self.engine.setProperty('voice',V[1].id)

    def speak(self,content):
        if self.speakstatus==True:
            self.engine.say(self.speakWords[content])
            self.engine.runAndWait()


if __name__=='__main__':
    ob=play_audio()
    ob.speak('1')