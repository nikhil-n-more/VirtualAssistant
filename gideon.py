import pyttsx3
import speech_recognition as sr
from os import remove
from datetime import datetime
from data import STOPWORDS
from Utilities.search_helper import Search
from Utilities.common_methods import instantPrint
from execute import Commands
from textblob import TextBlob
from Utilities.virtual_mouse import VirtualMouse
import json

USERNAME = "Nikhil"

class VirtualAssistant:
    def __init__(self):
        """
        Initializes the Gideon class.

        This method sets up the necessary components for the virtual assistant, such as the speech recognizer,
        speech recognition functionality, commands, and search functionality.

        Parameters:
            None

        Returns:
            None
        """
        super().__init__()
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 900.0
        self.initialize_speech_recognition_functionality()
        # self.speaker = MusicPlayer()
        self.wish_user()
        self.commands = Commands()
        self.search = Search()
        self.virtualMouse = None
        self.load_response_phrases()
        
    def load_response_phrases(self):
        """
        Loads the response phrases from the 'assistant_data.json' file.

        Parameters:
        None

        Returns:
        None
        """
        assistant_data = json.load(open("ApplicationData/assistant_data.json"))
        self.response_phrases = assistant_data["response_phrases"]
        self.voice_options = assistant_data["voice_options"]

    def verify_and_update_voice_options(self):
        """
        Verifies and updates the voice options for the assistant.

        Parameters:
        None

        Returns:
        None
        """
        voices = self.speech_engine.getProperty('voices')
        if len(voices) != len(self.voice_options):
            self.voice_options = voices

    def initialize_speech_recognition_functionality(self):
        """
        Initializes the speech recognition functionality by initializing the speech engine and setting the voice property.

        Parameters:
        None

        Returns:
        None
        """
        self.speech_engine = pyttsx3.init()
        self.switch_voice()

    def switch_voice(self):
        """
        Switches the voice of the assistant to the next available voice in the list of voices.
        """
        voice = self.speech_engine.getProperty('voice')
        voices = self.speech_engine.getProperty('voices')
        index = -1
        for i in range(len(voices)):
            if(voices[i].id == voice):
                index = i
                break
        # if(index == -1):
        #     self.speak("Sorry, I am not able to switch the voice at the moment")
        #     return
        
        index = (index+1)%len(voices)
        self.speech_engine.setProperty('voice', voices[index].id)

    def listen_to_user(self):
        """
        Listens to the user's voice input using the microphone and returns the recognized command.

        Returns:
            str: The recognized command received from the user.
        """
        instantPrint("Listening....")
        command_received = ""
        # self.speaker.stop_music_player()
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=3)
            except:
                self.speak("Please try again")
                # self.listen_user()
            voice_data = ""
            try:
                voice_data = self.recognizer.recognize_google(audio, language='en-in')
            except sr.UnknownValueError:
                self.speak("Sorry. I did not get that")
                # self.listen_user()
            except sr.RequestError:
                self.speak("Sorry. Not able to listen right now")
            except:
                self.speak("please try again")

            instantPrint(f"Captured Command : {voice_data}")
            # corrected_sentence = self.correct_sentence_words(voice_data).lower()
            # print(f"Command with corrected words : {corrected_sentence}")
            # command_received = corrected_sentence
            command_received = voice_data.lower()
        instantPrint(f"Final Command Received : {command_received}")
        return command_received

    def startMusic(self):
        """
        This method starts the music player.
        
        Note: Currently, starting the music player is not supported.
        """
        self.speak("Not Supported...")
        # self.speaker.start_music_player()
    
    def speak(self, audioText):
        """
        Speaks the given audio text using the assistant's speech engine.

        Parameters:
        audioText (str): The text to be spoken by the assistant.

        Returns:
        None
        """
        instantPrint(audioText)
        # Method for the speaking of the assistant
        self.speech_engine.say(audioText) 
        # Blocks while processing all the currently
        # queued commands
        self.speech_engine.runAndWait()

    def wish_user(self):
        """
        Wishes the user based on the current time of the day.

        This method checks the current hour and greets the user accordingly.
        If the hour is between 0 and 12, it wishes "Good Morning".
        If the hour is between 12 and 18, it wishes "Good Afternoon".
        Otherwise, it wishes "Good Evening".
        After greeting, it introduces itself as "Gideon, your personal virtual assistant".

        Parameters:
        None

        Returns:
        None
        """
        hour = int(datetime.now().hour)
        if(hour >=0 and hour<12):
            self.speak("Good Morning Sir")
        elif(hour>=12 and hour<18):
            self.speak("Good Afternoon Sir")
        else:
            self.speak("Good evening sir")
        self.speak("I am Gideon, your personal virtual assistant")
        # self.speak("How may I assist you today")

    def time_taken(self, start=0, finish=0):
        """
        Calculates the time taken between two given timestamps.

        Args:
            start (int): The starting timestamp in seconds.
            finish (int): The finishing timestamp in seconds.

        Returns:
            dict: A dictionary containing the time taken in hours, minutes, and seconds.
        """
        seconds = finish - start                 
        hours = seconds // 3600
        seconds -= hours * 3600 
        minutes = seconds // 60               
        seconds -= minutes * 60              
        return {"hours": hours, "minutes": minutes, "seconds": seconds}

    def remove_stopwords(self, command):
        """
        Removes stopwords from the given command.

        Parameters:
        - command (str): The input command to remove stopwords from.

        Returns:
        - str: The updated command with stopwords removed.
        """
        command_tokens = command.split("\\s+")
        print(command_tokens)
        tokens = [word for word in command_tokens if not word in STOPWORDS]
        command = ""
        for word in tokens:
            command += word
        return command

    def recognize_face(self):
        """
        Recognizes a face using face recognition technology.
        
        This method is currently not supported and will speak a message indicating the same.
        """
        self.speak("Currently Not Supported")
        # self.speak("Getting ready for Face Recognition")
        # self.faceRecognizer = FaceRecognition()
        # self.speak("Hit 'q' to confirm when you have taken clear picture")
        # user = self.faceRecognizer.take_picture()
        # self.speak(f'{user} recognized')
        # self.loggedUser = user

    def correct_sentence_words(self, sentence):
        """
        Corrects the words in a given sentence using TextBlob.

        Args:
            sentence (str): The sentence to be corrected.

        Returns:
            str: The corrected sentence.

        """
        corrected_sentence = TextBlob(sentence).correct()
        return str(corrected_sentence)

    def __del__(self):
        """
        Destructor method for the Gideon class.
        Removes the 'gideon_audio.mp3' file if it exists.

        Raises:
            None

        Returns:
            None
        """
        try:
            remove("gideon_audio.mp3")
        except:
            instantPrint('Junk already cleared')

    def enable_virtual_mouse_mode(self):
        """
        Enables the virtual mouse mode.

        If the virtual mouse is not already initialized, it creates a new instance of the VirtualMouse class and runs it.
        """
        if(self.virtualMouse is None):
            self.virtualMouse = VirtualMouse()
        self.virtualMouse.run()

    
