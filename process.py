
applications = ["vscode", "android studio", "visual studio code",]

projects = ["flutter", "django", "node", "nodejs", ""]

questions = ["what is", "what's", "whats", "which", "why", ]
what = ["what is", "what's", "whats",]

def process():
    # if('safeguard' in command):
    #     return select the folder to be safeguarded
    if(word in command for word in what):
        for word in what:
            try:
                command = command.remove(word)
            except:
                continue
        whatQuest(command)
    elif('open' in command):
        if('open this' in command):
            if('terminal' in command):
                return "Opening folder in terminal"
            else:
                return "opening this folder in vscode"
        elif('project' in command):
                command = command.remove('project')
                for app in projects:
                    if(app in command):
                        return "opening your project in vscode"
        elif('open my' in command):
            command = command.remove('open').remove('my')
            if('diary' in command):
                print("you need to first authincate yourself sir")
                return authincate()
        else:
            return "opening this application in vscode"
    elif('install' in command and 'package' in command):
        command = command.remove('install')
        if('python package' in command):
            command = command.remove('python package')
            return installPython()
        else:
            command = command.remove('package')
            return installPackage()
    elif('download' in command and 'url' in command):
        # return "Enter the github from where this is to be installed"
        downloadGithub()
    elif('play' in command):
        if('youtube' in command):
            print("Play something on youtube")
        else:
            print("Playing some beats")
    elif('search' in command):
        if('search this' in command):
            return "Not yet implemented"
        elif('youtube' in command):
            print("Searching on youtube")
            return
        else:
            print("Searching on google")
    elif('fetch info' in command or 'fetch information' in command):
        command = command.remove('fetch')
        print("Fetching information")
    elif('create' in command):
        command = command.remove('create')
        if('project' in command):
            command = command.remove('project')
            folder = word in command for word in projects
            if folder:
                createProject(typeOfProject=folder)
            else:
                print("I could not get what type of project you want to create")
                print("Please enter it in this one")
        elif('folder' in command):
            if('default' in command ):
                print("Here you have to save the folder in which you created a file or folder earlier")
                print("Enter the name of the folder")
            else:
                print("Specify the path and name of folder")
        elif('file' in command):
            if('default' in command):
                print('Enter file name with extension')
            else:
                print('Enter folder location')
    elif('close' in command):
        if('close this' in command):
            # return "Closing the current application"
            closeThis()
        else:
            return "closing the folders"
    else:
        # return "Need to match this to closest command possible"
        print("Could not identify your command")
        print("Enter the command in this box")
        popupWindow = createPopUpWidget()
        popupWindow.show()
        text = popupwindow.getinput()
        
def authincate():
        # take picture
        # validate the owner
        # input password
        # if mismatch then ask for private questions
        # if fail then discard the access token
        print('''# take picture
        # validate the owner
        # input password
        # if mismatch then ask for private questions
        # if fail then discard the access token
        ''')

def safeguard():
        # search for a way to lock folders by password in python
        # input password should be hashed by SHA256 algorithm for more security
    print('''# search for a way to lock folders by password in python
        # input password should be hashed by SHA256 algorithm for more security
        ''')

def installPackage(package):
        print("Package : " + package)
        print("This will try to install package from software center or snap")

def installPython(package):
        print("Package : " + package)
        print("This will install package using pip")

def downloadGithub():
        print("Enter the url please")

def closeThis():
        print("This will detect cross on system and then click on it to close it")

def whatQuest(command):
        if('location' in command):
            print("This should up pop up a window showing the location")
        elif('name' in command):
            print("My name is gideon")
        elif('favorite' in command):
            if('color' in command):
                print("My favorite color is Blue. Same as my creator")
            elif('food' in command):
                print("My favorite food is NLP which my dumb creator hasn't given me")
                print("He just feeds me with hardcode command")
            elif('time pass' in command or 'pass time'):
                print("My favorite pass time is watching you love me")
            elif('time' in command):
                from time import time 
                print(time())
            elif('destination' in command):
                print("My favorite destination is your heart. And I wanna always live in there atleast till I get my next handsome user ")
            elif('work' in command):
                print("My favorite and only work is to help you excel")
            else:
                print('Are you sure of what you are asking. If you are then try typing it here')
        else:
            print("Sorry but I may not have enough resources to aid in you in this question")
            print("Searching on web")

    if __name__ == "__main__":
        print("Try to find a way for getting documentation from ubuntu")

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

    def createPopUpWidget(self, title="", extra=False):
        box = QWidget()
        vbox = QVBoxLAyout()
        # hbox = QHBoxLayout()
        # inputName = QWidget()
        # label1 = QLabel("Name : ")
        # input1 = QLineEdit()
        # input1.setPlaceholderText("Enter the name of the file/app to be created")
        # hbox.addWidget(label1)
        # hbox.addWidget(input1)
        # inputName.setLayout(hbox)
        widget = self.createWidget(label="Name : ", placeholderText="Enter the name of file/app")
        vbox.addWidget(widget)
        if(extras):
            # inputPlace = QWidget()
            # hbox2 = QHBoxLayout()
            # label2 = QLabel("Path : ")
            # input2 = QLineEdit()
            # input2.setPlaceholderText("Enter the path of the folder")
            # hbox2.addWidget(label2)
            # hbox2.addWidget(input2)
            # inputPlace.setLayout(hbox2)
            widget2 = self.createWidget(label="Path : ", placeholderText="Enter the path of folder")
            vbox.addWidget(widget2)
        box.setLayout(vbox)
        return box

    def createWidget(self, label="Name", placeholderText="Enter the name of file/app"):
        inputName = QWidget()
        hbox = QHBoxLayout()
        label1 = QLabel(label)
        input1 = QLineEdit()
        input1.setPlaceholderText(placeholderText)
        hbox.addWidget(label1)
        hbox.addWidget(input1)
        inputName.setLayout(hbox)
        return inputName
