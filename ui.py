from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, QLabel, QWidget, QPushButton, QDial, QGroupBox, QLineEdit, QTextEdit, QMessageBox, QInputDialog
import sys
from PyQt5.QtCore import QSize, Qt        
from PyQt5.QtGui import QFont, QIcon, QPixmap
import requests
import json
from Utilities.internet_helper import Internet
from Utilities.user_access_helper import UserAccess
from gideon import VirtualAssistant as Gideon
from time import sleep, time
import sys
import os
from query_handler import QueryHandler
from section_data_handler import SectionDataHandler

# from data import *
what = ["what is", "what's", "whats", "wht"]
DEFAULT = "~/Documents/workspace/"
gideon = ['gideon', 'didion', 'vdo', 'video']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.assistant = Gideon()
        self.queryHandler = QueryHandler()
        self.sectionDataHandler = SectionDataHandler()
        print("\nVirtual Assistant Initialized")
        print("\n...............................\n")
        self.processed = False

    def setup_Full_UI(self):
        # self.assistant.speak("Hello Sir, I am gideon. Your personal virtual assistant")
        self.assistant.speak("Initialising my user interface for you")
        window = QWidget(self)
        self.setCentralWidget(window)
        window.setStyleSheet('background-color : rgb(0, 0, 0)')
        self.setGeometry(100, 50, 1680, 900)
        self.setWindowTitle("Gideon-Virtual Assistant")
        # Won't work on ubuntu, and probably not on unix systems
        self.setWindowIcon(QIcon("img/gideon_icon.jpg"))
        self.setMinimumWidth(1000)
        self.assistant.speak("Main Window Intialized. Creating sections")
        # self.setMinimumHeight(900)
        hbox = QHBoxLayout()
        self.create_sections()
        hbox.addWidget(self.first_section)
        hbox.addWidget(self.second_section)
        hbox.addWidget(self.third_section)
        window.setLayout(hbox)
        self.assistant.speak("All the sections initialized")
        self.initialize_helpers()
        print("Initialization Complete")
        print("\n................................\n")
        
    def create_sections(self):
        self.first_section = QWidget()
        self.first_section.setStyleSheet('background-color : rgb(0,0,0)')
        self.first_section.setMaximumWidth(350)
        self.second_section = QWidget()
        self.second_section.setStyleSheet('background-color : rgb(128, 255, 170)')
        self.third_section = QWidget()
        self.third_section.setStyleSheet('background-color : rgb(255, 255, 128)')
        self.third_section.setMaximumWidth(350)
        self.third_section.setMinimumWidth(350)

    def initialize_helpers(self):
        self.assistant.speak("Initializing helper methods. Be patient")
        #self.internet = Internet()
        # print("\nInternet Info agent initialized")
        self.user = UserAccess()
        print("\nWeather Info agent initialized")
        # self.assistant.speak("Setting up left window")
        # self.setupLeftWindow()
        # self.assistant.speak("Left Window set up completed")
        self.assistant.speak("Setting up right window")
        self.setupRightWindow()
        self.assistant.speak("Right Window set up completed")
        self.assistant.speak("Updating Internet speed. This my take a while")
        #self.updateNetSpeed()
        self.assistant.speak("Internet spead measured")
        self.assistant.speak("Setting up central window")
        self.setupCentralWindow()
        self.assistant.speak("Central Window set up completed")
        self.assistant.speak("Getting weather forecast info")
        self.updateWeather()
        self.assistant.speak("Getting weather forecast for your area")
        self.updateDate()
        self.updateTime()
        
    def setupCentralWindow(self):
        self.second_section.setStyleSheet("""
        margin: 0px;
        color: white;
        border: 1px solid white;
        """)
        vbox = QVBoxLayout()
        welcome = QLabel("Gideon Welcomes You")
        welcome.setFont(QFont("Sanserif", 14, weight=QFont.Bold))
        welcome.setStyleSheet("""
        color : rgb(255,255,255);
        background-color: rgb(138, 0, 230);
        """)
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setMaximumHeight(80)

        self.widgetDateTime = QWidget()
        self.widgetDateTime.setMaximumHeight(80)
        hbox_datetime = QHBoxLayout()
        self.date = QLabel("Date")
        self.date.setFont(QFont("Sanserif", 12, weight=QFont.Bold))
        self.date.setAlignment(Qt.AlignCenter)
        # self.date.setPlainText("Date")
        self.time = QLabel("Time")
        self.time.setFont(QFont("Sanserif", 12, weight=QFont.Bold))
        self.time.setAlignment(Qt.AlignCenter)
        # self.time.setPlainText("Time")
        hbox_datetime.addWidget(self.date)
        hbox_datetime.addWidget(self.time)
        self.widgetDateTime.setLayout(hbox_datetime)

        self.weather = QWidget()
        self.weather.setMaximumHeight(200)
        vbox_weather = QVBoxLayout()
        weather_label = QLabel("Weather Forecast")
        weather_label.setFont(QFont("Sanserif", 12))
        weather_label.setStyleSheet("""
        color: white;
        border: 1px solid white;
        margin: 0;
        background-color: rgb(46, 184, 184);""")
        weather_label.setAlignment(Qt.AlignCenter)
        weather_label.setMaximumHeight(40)
        vbox_weather.addWidget(weather_label)

        temp_widget = QWidget()
        hbox_temp = QHBoxLayout()
        self.temp = QLabel("Getting Temperature...")
        self.temp.setFont(QFont("Sanserif", 12, weight=QFont.Bold))
        self.temp.setAlignment(Qt.AlignCenter)
        # self.temp.setPlainText("Getting Temperature...")
        self.pressure = QLabel("Getting Pressure...")
        self.pressure.setFont(QFont("Sanserif", 12, weight=QFont.Bold))
        self.pressure.setAlignment(Qt.AlignCenter)
        # self.pressure.setPlainText("Getting Pressure...")
        hbox_temp.addWidget(self.temp)
        hbox_temp.addWidget(self.pressure)
        temp_widget.setLayout(hbox_temp)

        desc_widget = QWidget()
        hbox_desc = QHBoxLayout()
        self.humidity = QLabel("Getting Humidity...")
        self.humidity.setFont(QFont("Sanserif", 12, weight=QFont.Bold))
        self.humidity.setAlignment(Qt.AlignCenter)
        # self.humidity.setPlainText("Getting Humidity...")
        self.description = QLabel("Getting Description...")
        self.description.setFont(QFont("Sanserif", 12, weight=QFont.Bold))
        self.description.setAlignment(Qt.AlignCenter)
        # self.description.setPlainText("Getting Description...")
        hbox_desc.addWidget(self.humidity)
        hbox_desc.addWidget(self.description)
        desc_widget.setLayout(hbox_desc)

        vbox_weather.addWidget(temp_widget)
        vbox_weather.addWidget(desc_widget)
        self.weather.setLayout(vbox_weather)

        # Empty Widget
        empty_widget = QWidget()
        hbox_text = QHBoxLayout()
        self.instruction_area = QTextEdit()
        self.instruction_area.setPlainText('Instructions will appear here')
        hbox_text.addWidget(self.instruction_area)
        empty_widget.setLayout(hbox_text)

        # Listen widget
        listner_widget = QWidget()
        listner_widget.setMaximumHeight(60)
        hbox_listen = QHBoxLayout()
        self.listenArea = QLineEdit("")
        self.listenArea.setPlaceholderText("Enter Something if I can't get you")
        self.listenArea.setMinimumHeight(40)
        self.listenArea.setMinimumWidth(50)
        self.listen = QPushButton("Speak")
        self.listen.setIcon(QIcon("img/speak.png"))
        self.listen.setMinimumHeight(40)
        self.listen.setMinimumWidth(60)
        self.listen.setIconSize(QSize(40,40))
        self.listen.setStyleSheet("""
        margin: 0px;
        color: white;
        border: 1px solid white;
        background-color: rgb(255, 102, 0);""")
        self.listen.clicked.connect(self.assistentListening)
        hbox_listen.addWidget(self.listenArea)
        hbox_listen.addWidget(self.listen)
        listner_widget.setLayout(hbox_listen)

        vbox.addWidget(welcome)
        vbox.addWidget(self.widgetDateTime)
        vbox.addWidget(self.weather)
        vbox.addWidget(empty_widget)
        vbox.addWidget(listner_widget)
        self.second_section.setLayout(vbox)
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Central Window SetUp Completed")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    def setupLeftWindow(self):
        self.first_section.setStyleSheet("""
        margin: 0px;
        border: 1px solid white;
        color: white;
        background-color: black;""")
        
        vbox = QVBoxLayout()
        
        self.app_shortcut_button = QPushButton("           Add Terminal Shortcut")
        self.app_shortcut_button.setMaximumHeight(50)
        self.app_shortcut_button.setIcon(QIcon("img/add.jpg"))
        self.app_shortcut_button.setIconSize(QSize(50,50))
        self.app_shortcut_button.setStyleSheet("""
        background-color: rgb(102, 0, 102);
        color: white;
        border: 1px solid white;""")
        # Set Up Set-Alarm Widget
        alarm_set_widget = QWidget()
        # alarm_set_widget.setStyleSheet('background-color : white')
        hbox_alarm_set = QHBoxLayout()
        clock = QDial()
        hbox_alarm_set.addWidget(clock)
        alarm_info = QWidget()
        vbox_info = QVBoxLayout()
        time_label = QLabel("Time Shall Be showed")
        zone_label = QLabel("AM PM shall be showed")
        vbox_info.addWidget(time_label)
        vbox_info.addWidget(zone_label)
        alarm_info.setLayout(vbox_info)
        hbox_alarm_set.addWidget(alarm_info)
        alarm_set_widget.setLayout(hbox_alarm_set)

        # Set Up Alarm-Show Widget
        # Alarm 1 Set Up
        alarm1 = QWidget()
        alarm1.setMaximumHeight(70)
        # alarm1.setStyleSheet('background-color : white')
        hbox_alarm1 = QHBoxLayout()
        label1 = QLabel("Alarm Will Show up here")
        hbox_alarm1.addWidget(label1)
        alarm1.setLayout(hbox_alarm1)

        # Alarm 2 Set Up
        alarm2 = QWidget()  
        alarm2.setMaximumHeight(70) 
        # alarm2.setStyleSheet('background-color : white')  
        hbox_alarm2 = QHBoxLayout()
        label2 = QLabel("Alarm Will Show up here")
        hbox_alarm2.addWidget(label2)
        alarm2.setLayout(hbox_alarm2)

        # Alarm 3 Set Up
        alarm3 = QWidget() 
        alarm3.setMaximumHeight(70)
        # alarm3.setStyleSheet('background-color : white')
        hbox_alarm3 = QHBoxLayout()
        label3 = QLabel("Alarm1 Will Show up here")
        hbox_alarm3.addWidget(label3)
        alarm3.setLayout(hbox_alarm3)

        # Alarm 4 Set Up
        alarm4 = QWidget()
        alarm4.setMaximumHeight(70) 
        # alarm4.setStyleSheet('background-color : white')
        hbox_alarm4 = QHBoxLayout()
        label4 = QLabel("Alarm1 Will Show up here")
        hbox_alarm4.addWidget(label4)
        alarm4.setLayout(hbox_alarm4)

        # Alarm 5 Set Up
        alarm5 = QWidget()
        alarm5.setMaximumHeight(70)
        # alarm5.setStyleSheet('background-color : white')
        hbox_alarm5 = QHBoxLayout()
        label5 = QLabel("Alarm1 Will Show up here")
        hbox_alarm5.addWidget(label5)
        alarm5.setLayout(hbox_alarm5)

        # Add all the widgets created to VBoxLayout
        vbox.addWidget(self.app_shortcut_button)
        vbox.addWidget(alarm_set_widget)
        vbox.addWidget(alarm1)
        vbox.addWidget(alarm2)
        vbox.addWidget(alarm3)
        vbox.addWidget(alarm4)
        vbox.addWidget(alarm5)
        self.first_section.setLayout(vbox)
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Left Window SetUp Completed")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    def setupRightWindow(self):
        self.third_section.setStyleSheet("""
        margin: 0px;
        background-color: black;
        border: 1px solid white;
        color: white;""")
        self.third_section.setFont(QFont('Sanserif', 14))
        vbox = QVBoxLayout()

        # News Section
        self.newsGroupBox = QGroupBox("News")
        vbox_news = QVBoxLayout()
        news = self.getLatestNews()
        for i in range(5):
            label = QTextEdit()
            label.setPlainText(news[i]['title'])
            vbox_news.addWidget(label)

        # self.newsGroupBox.setStyleSheet("""
        # border: 1px solid rgb(26, 140, 255);
        # color: white""")
        # self.newsGroupBox.setStyleSheet('color : white')
        # self.newsGroupBox.setFont(QFont('Sanserif', 14))
        self.newsGroupBox.setLayout(vbox_news)

        # Net Speed Section
        netGroupBox = QGroupBox("Net Speed")
        netGroupBox.setMaximumHeight(200)
        netGroupBox.setMinimumHeight(200)
        # netGroupBox.setStyleSheet("""
        # border: 1px solid rgb(26, 140, 255);
        # color: white""")
        # netGroupBox.setFont(QFont("Sanserif", 14))
        vbox_net = QVBoxLayout()

        ping_widget = QWidget()   
        # ping_widget.setStyleSheet("""
        # border: 1px solid rgba(26, 140, 255, 0);
        # """)
        hbox_ping = QHBoxLayout()
        self.ping = QTextEdit()
        self.ping.setPlainText("0 ms")
        self.refresh = QPushButton("Refresh")
        self.refresh.setIcon(QIcon("img/refresh.png"))
        self.refresh.setIconSize(QSize(40,40))
        self.refresh.setMinimumHeight(40)
        # self.refresh.clicked.connect(self.refresh_data)
        self.refresh.setStyleSheet("""
        background-color: rgb(102, 0, 102);
        color:white;
        border: 1px solid white;""")
        hbox_ping.addWidget(self.ping)
        hbox_ping.addWidget(self.refresh)
        ping_widget.setLayout(hbox_ping)

        speed_widget = QWidget()
        # speed_widget.setStyleSheet("""
        # border: 1px solid rgba(26, 140, 255, 0);
        # """)
        hbox_speed = QHBoxLayout()
        self.upload = QTextEdit()
        self.upload.setPlainText("U: 0.0 Mbit/s")
        self.download = QTextEdit()
        self.download.setPlainText("D: 0.0 Mbit/s")
        hbox_speed.addWidget(self.upload)
        hbox_speed.addWidget(self.download)
        speed_widget.setLayout(hbox_speed)
        vbox_net.addWidget(speed_widget)
        vbox_net.addWidget(ping_widget)
        netGroupBox.setLayout(vbox_net)

        vbox.addWidget(self.newsGroupBox)
        # self.updateNetSpeed()
        vbox.addWidget(netGroupBox)
        self.third_section.setLayout(vbox)
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Right Window SetUp Completed")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    def getLatestNews(self):
        url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=')
        url +='6303b4d484db41fcb55671d77e06466e'
        try:
            response = requests.get(url)
        except:
            print("Check Your Internet Connection")
        news = json.loads(response.text)
        # print(news)
        # for new in news['articles']:
        #     print('\n................................................')
        #     print(str(new['title']))
        #     print(str(new['description']))
        print("\n...........................\nObtained Latest News")
        return news['articles']

    def updateNetSpeed(self):
        self.ping.setPlainText("Updating...")
        self.upload.setPlainText("Updating...")
        self.download.setPlainText("Updating...")
        latest_ping = "Ping\n" + str(self.internet.get_ping())   
        self.ping.setPlainText(latest_ping)
        latest_upload_speed = "Upload\n" + str(self.internet.get_upload_speed()) 
        self.upload.setPlainText(latest_upload_speed)
        latest_download_speed = "Download\n" + str(self.internet.get_download_speed())
        self.download.setPlainText(latest_download_speed)
        print("\n................................\nNet Speed Updated")
        
    def updateWeather(self):
        self.temp.setText("Updating...")
        self.pressure.setText("Upating...")
        self.humidity.setText("Updating...")
        self.description.setText("Updating...")
        weatherInfo = self.user.get_weather_info()
        latest_temperature = "Temperature (in Kelvin) : " + str(weatherInfo['Temperature']) + " K"
        self.temp.setText(latest_temperature)
        latest_pressure = "Pressure : " + str(weatherInfo['Pressure']) + " hPa"
        self.pressure.setText(latest_pressure)
        latest_humidity = "Humidity : " + str(weatherInfo['Humidity']) + " %"
        self.humidity.setText(latest_humidity)
        latest_description = "Description : " + str(weatherInfo['Description'])
        self.description.setText(latest_description)
        print("\n.....................................\nWeather Forcast Updated")

    def updateDate(self):
        data = self.user.get_current_date()
        latest_date = data["day"] + " " + data["month"] + " , " + data["year"]
        self.date.setText(latest_date)
        self.time.setText(data["weekday"])

    def updateTime(self):
        pass
        # data = self.user.get_current_time()
        # latest_time = str(data["Hour"]) + " : " + str(data["Minute"]) + " : " + str(data["Second"])
        # self.time.setText(latest_time)

    def refresh_data(self):
        self.updateNetSpeed()
        self.updateWeather()
        self.updateTime()

    def assistentListening(self):
        command = self.assistant.listen_to_user()
        command = self.assistant.remove_stopwords(command) 
        self.processed = False
        print(command)
        if command:
            self.display_command(command)
            self.process_command(command)
        # while True:
        #     command = self.assistant.listen_to_user()
        #     command = self.assistant.remove_stopwords(command) 
        #     if('gideon' not in command):
        #         continue
        #     print(command)
        #     if command:
        #         self.display_command(command)
        #         self.process_command(command)
    
    def process_command(self, command):
        if("what" in command):
            self.whatQuest(command)
        print("Command Received : " + command)
        if('find' in command):
            if('location' in command):
                command = command.replace("location", "")
                self.assistant.speak("Enter the location")
                location, result = QInputDialog.getText(self, "Location", "Enter location")
                if result:
                    self.assistant.search.find_location(product)
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
            self.remainCommand()

    def whatQuest(self, command):
        if('location' in command):
            self.display_location()
        elif('name' in command):
            # print("My name is gideon")
            self.assistant.speak("My name is Gideon")
        elif('favorite' in command):
            if('color' in command):
                self.assistant.speak("My favorite color is Navy Blue. Same as my creator")
            elif('food' in command):
                self.assistant.speak("My favorite food is NLP which my dumb creator hasn't given me")
            elif('time pass' in command or 'pass time'):
                self.assistant.speak("My favorite pass time is you asking me questions")
            elif('time' in command):
                print(time())
            elif('destination' in command):
                self.assistant.speak("My favorite destination is your heart. And I wanna always live in there atleast till I get my next handsome user ")
            elif('work' in command):
                self.assistant.speak("My favorite and only work is to help you excel")
            else:
                self.assistant.speak('Are you sure of what you are asking. If you are then try typing it here')
        else:
            self.assistant.speak("Sorry but I may not have enough resources to aid in you in this question")
            # self.remainCommand()

    def display_location(self):
        location = self.user.get_location()
        self.assistant.speak("Displaying your location details")
        msg = QMessageBox()
        msg.setWindowTitle("Location Detail")
        msg.setText(f'\tLocation : {location["City"]}\t')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDetailedText(f' IP Adress : {location["IP"]} \n Organisation : {location["Organisation"]} \n City : {location["City"]} \n Country : {location["Country"]} \n Region : {location["Region"]}\n')
        x = msg.exec_()

    def display_command(self, command):
        text = self.instruction_area.toPlainText()
        self.instruction_area.setPlainText(text + "\n" + command)

    def enable_inputs(self):
        self.refresh.clicked.connect(self.refresh_data)
        self.listen.clicked.connect(self.assistentListening)

    def searchCommand(self, command):
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

    def createCommand(self, command):
        # command = command.replace('create', '')
        try:
            if('project' in command):
                self.createProjectCommand(command=command)
            elif('file' in command):
                self.createFilecommand(command=command)
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

    def closeCommand(self):
        self.assistant.speak("Thanks for choosing me")
        self.assistant.speak("Initializing self destruction")
        self.assistant.speak("Desctruction failed. Please close the terminal window")

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
        # else:
        #     self.assistant.speak("Sorry but I could not recognize your command")
        #     self.processed = False

    def openCommand(self, command):
        if('youtube' in command):
            self.assistant.saerch.search_youtube("Operating System")
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

    def closeEvent(self, event):
        self.assistant.speak("Thanks for choosing me")
        self.assistant.speak("Initializing self destruction")
        self.assistant.speak("Desctruction failed. Please close the terminal window")
        event.accept()

    
