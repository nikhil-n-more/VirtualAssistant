from PyQt5.QtWidgets import QInputDialog
from Utilities.common_methods import instantPrint
from ui import MainWindow, DEFAULT
import os
from gideon import Gideon

class QueryHandler:
    def __init__(self, assistant : Gideon) -> None:
        self.assistant = assistant
    
    def process_command(self, command):
        instantPrint("Command Received : " + command)
        if("what" in command):
            self.whatQuest(command)
        elif('find' in command):
            if('location' in command):
                command = command.replace("location", "")
                command = command.replace("location", "")
                self.assistant.speak("Enter the location")
                location, result = QInputDialog.getText(self, "Location", "Enter location")
                self.assistant.speak("Searching for : " + location)
                if result:
                    self.assistant.search.find_location(location)
                else:
                    self.speak("Sorry could not get that. Please try again later")
            elif("product" in command):
                command = command.replace("find", "")
                command = command.replace("product","")
                self.assistant.speak("Enter the product name")
                product, result = QInputDialog.getText(self, "Product", "Enter product name")
                if result:
                    self.assistant.search.find_product_amazon(product)
        elif('open' in command):
            self.openCommand(command=command)
        elif('play' in command):
            self.playCommand(command=command)
        elif('search' in command):
            self.searchCommand(command=command)
        elif('fetch info' in command or 'fetch information' in command):
            self.fetchInfoCommand(command=command)
        elif('create' in command):
            self.createCommand(command=command)
        elif('install' in command and 'package' in command):
            self.installCommand(command=command)
        elif('download' in command and 'url' in command):
            print("Not available")
        elif('close' in command):
            self.closeCommand()
        else:
            self.searchCommand(command=command)

    def searchCommand(self, command):
        instantPrint(command)
        if('youtube' in command):
            command = command.replace("search", "")
            command = command.replace("youtube", "")
            self.assistant.search.search_youtube(topic=command)
            self.assistant.speak("searching on youtube")
                # print("Searching on youtube")
        else:
            self.assistant.search.search_web(query=command)
            self.assistant.speak("Searching on google")    

    def fetchInfoCommand(self, command):
        command = command.rplace('fetch', '')
        try:
            command = command.replace("info", "")
        except:
            command = command.replace("information", "")
        try:
            info = self.assistant.search.get_information_wiki(topic=command)
            self.assistant.speak(info)
            self.display_command(info)
        except:
            self.assistant.speak("Error getting information")
            # print("Fetching information")

    def playCommand(self, command):
        
        if('youtube' in command):
            command = command.replace("play", "")
            command = command.replace("youtube", "")
            self.assistant.search.search_youtube(topic=command)
            self.assistant.speak("Playing on youtube")
        else:
            print("Playing some beats")

    def remainCommand(self, command=""):
        self.assistant.speak("Could Not recognize your command. Please input it here")
        command,result = QInputDialog.getText(self, "Text Input Dialog", "Enter the command")
        print(command)
            # self.processed = True
        # print("Calling procedures")
        if not self.processed:
            self.process_command(command=command)
            self.processed = True
                # self.assistant.speak("Error getting input")
        else:
            self.assistant.speak("Sorry but I could not recognize your command")
            self.processed = False

    def openCommand(self, command):
        if('youtube' in command):
            self.assistant.search.search_youtube("Operating System")
        elif('classroom' in command):
            self.assistant.search.search_web("https://classroom.google.com/u/0/h")
            self.assistant.speak("Opening Google Classroom")
        elif('mail' in command):
            self.assistant.search.open_mail()
        elif('whatsapp' in command):
            self.assistant.search.open_whatsapp()
        elif('system monitor' in command):
            os.system('gnome-system-monitor')
        elif('code' in command or 'vscode' in command):
            os.system("code")
        else:
            self.assistant.speak("Please try again")
        return 

        if('open this' in command):
            if('terminal' in command):
                print("Opening folder in terminal")
            else:
                print("opening this folder in vscode")
        elif('project' in command):
                command = command.replace('project', '')
                for app in projects:
                    if(app in command):
                        os.system(f'code {app}')
                        print("opening your project in vscode")
                        break
        elif('open my' in command):
            command = command.replace('open', '').replace('my', '')
            if('diary' in command):
                print("you need to first authincate yourself sir")
                return authincate()
        else:
            return "opening this application in vscode"

    def installCommand(self, command):
        if('python package' in command):
            package, result = QInputDialog.getText(self, "Package", "Enter package name")
            self.assistant.commands.installPythonPackage(package=package)
        else:
            package = "gnome-clock"
            package, result = QInputDialog.getText(self, "Package", "Enter package name")
            self.assistant.commands.installPackage(package=package)

    def createCommand(self, command):
        # command = command.replace('create', '')
        try:
            if('project' in command):
                self.createProjectCommand(command=command)
            elif('file' in command):
                self.createFilecommand(command=command)
            elif('folder' in command):
                self.createFolderCommand(command=command)
        except:
            self.assistant.speak("This section required some work")
        # elif('folder' in command):
        #     self.createFolderCommand(command=command)

    def createProjectCommand(self, command):
        # command = command.replace('project','')
        projectType, result = QInputDialog.getText(self, "Text Input Dialog", "Input project type")
        print(projectType)
        if True:
            projectName, result = QInputDialog.getText(self, "Text Input Dialog", "Enter Name of Project")
            if True:
                if(projectType == "flutter"):
                    self.assistant.commands.createFlutterProject(projectName)
                elif(projectType == "django"):
                    self.assistant.commands.createDJangoProject(projectName)
                elif(projectType == "nodejs"):
                    self.assistant.commands.createNodeJsProject(projectName)

    def createFolderCommand(self, command):
        path, result = QInputDialog.getText(self, "Path", "Enter folder path")
        # if result:
        #     os.mkdir(path)
        os.mkdir(path)
        # if('default' in command ):
        #     print("Here you have to save the folder in which you created a file or folder earlier")
        #     print("Enter the name of the folder")
        # else:
        #     print("Specify the path and name of folder")

    def createFilecommand(self, command):
        self.assistant.speak('Enter file name with extension')
        filename, result = QInputDialog.getText(self, "Name", "Enter the filename")
        if('default' in command):
            try:
                os.system(f'touch {os.path.join(DEFAULT, filename)}')
                self.assistant.speak("File created")
            except:
                self.assistant.speak("Error Encountered")
        else:
            foldername, result = QInputDialog.getText(self, "Name", "Enter the folder path")
            # if result:
            os.system(f'touch {os.path.join(foldername, filename)}')
            self.assistant.speak("File created")
