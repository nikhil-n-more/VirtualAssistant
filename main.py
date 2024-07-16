# from time import time
# from ui import MainWindow
# from PyQt5.QtWidgets import QApplication
# import sys
# from Utilities.common_methods import instantPrint
import pyttsx3

if __name__ == '__main__':
    speech_engine = pyttsx3.init()
    voices = speech_engine.getProperty('voices') 
    voicer = speech_engine.getProperty('voice')
    print(voicer)
    print("-----------------------")
    for voice in voices: 
        # to get the info. about various voices in our PC  
        print("Voice:") 
        print("ID: %s" %voice.id) 
        print("Name: %s" %voice.name) 
        print("Age: %s" %voice.age) 
        print("Gender: %s" %voice.gender) 
        print("Languages Known: %s" %voice.languages) 


    # app = QApplication(sys.argv)

    # start = time()
    # window = MainWindow()
    # window.setup_Full_UI()
    # window.show()
    # window.assistant.recognize_face()
    # window.assistant.speak("I am ready to roll sir")
    # # window.enable_inputs()
    # finish = time()
    # instantPrint(f"Time Taken : {str(window.assistant.time_taken(start=start, finish=finish))}")

    # sys.exit(app.exec_())
