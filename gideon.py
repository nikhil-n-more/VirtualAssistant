import pyttsx3
import speech_recognition as sr
from os import remove
from datetime import datetime
# from play_music import MusicPlayer
from time import sleep
from data import STOPWORDS
from utilities import Search, instantPrint
from execute import Commands

USERNAME = "Nikhil"

class Gideon:
    def __init__(self):
        super().__init__()
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 900.0
        self.initialize_speech_recognition_functionality()
        # self.speaker = MusicPlayer()
        self.wish_user()
        self.commands = Commands()
        self.search = Search()
        # sp = spacy.load('en_core_web_sm')
        # self.stop_words = sp.Defaults.stop_words

    def initialize_speech_recognition_functionality(self):
        self.speech_engine = pyttsx3.init()
        # getter method(gets the current value
        # of engine property)
        voices = self.speech_engine.getProperty('voices')
        
        # setter method .[0]=male voice and 
        # [1]=female voice in set Property.
        self.speech_engine.setProperty('voice', voices[0].id)

    def listen_to_user(self):
        instantPrint("Listening....")
        # self.speaker.stop_music_player()
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source,timeout=3)
            except:
                self.speak("Please try again")
                # self.listen_user()
            voice_data = ""
            try:
                voice_data = self.recognizer.recognize_google(audio,language='en-in')
            except sr.UnknownValueError:
                self.speak("Sorry. I did not get that")
                # self.listen_user()
            except sr.RequestError:
                self.speak("Sorry. Not able to listen right now")
            except:
                self.speak("please try again")
            voice_data = voice_data.lower()
            # voice_data = remove_stopwords(voice_data)
            return voice_data

    def startMusic(self):
        self.speak("Not Supported...")
        # self.speaker.start_music_player()
    
    def speak(self, audioText):
        instantPrint(audioText)
        # Method for the speaking of the assistant
        self.speech_engine.say(audioText) 
        # Blocks while processing all the currently
        # queued commands
        self.speech_engine.runAndWait()

    def wish_user(self):
        hour = int(datetime.now().hour)
        if(hour >=0 and hour<12):
            self.speak("Good Morning Sir")
        elif(hour>=12 and hour<18):
            self.speak("Good Afternoon Sir")
        else:
            self.speak("Good evening sir")
        self.speak("I am gideon. your personal virtual assistant")
        # self.speak("How may I assist you today")

    def time_taken(self,start=0,finish=0):
        seconds = finish - start                 
        hours = seconds//3600
        seconds -= hours * 3600 
        minutes = seconds // 60               
        seconds -= minutes * 60              
        return {"hours":hours,"minutes":minutes,"seconds":seconds}

    def remove_stopwords(self, command):
        tokens = [word for word in command if not word in STOPWORDS]
        command = ""
        for word in tokens:
            command += word
        return command

    def recognize_face(self):
        self.speak("Currently Not Supported")
        # self.speak("Getting ready for Face Recognition")
        # self.faceRecognizer = FaceRecognition()
        # self.speak("Hit 'q' to confirm when you have taken clear picture")
        # user = self.faceRecognizer.take_picture()
        # self.speak(f'{user} recognized')
        # self.loggedUser = user

    def __del__(self):
        try:
            remove("gideon_audio.mp3")
        except:
            print('Junk already cleared')
