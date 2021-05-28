import os
import subprocess
from data import *

class Commands:
    def __init__(self):
        super().__init__()

    def createFlutterProject(self, appName):
        """Creates a new flutter project with given app name

        Args:
            appName (string): [Name of the app to be created]

        Returns:
            [bool]: [True if operation was succesful]
        """        
        try:
            process = subprocess.Popen(['flutter', 'create', os.path.join(FlutterFolder, appName)], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if stdout:
                os.system(f'code {os.path.join(FlutterFolder,appName)}')
                return True
            else:
                return False
        except:
            return False

    def createUnityProject(self, appName):
        return False

    def createDJangoProject(self, appName):
        process = subprocess.Popen(['django-admin', 'startptoject', os.path.join(DJangoFolder, appname)], stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stdout:
            os.system(f'code {os.path.join(DJangoFolder,appName)}')
            return True
        else:
            return False

    def createNodeJsProject(self, appName):
        pass

    def checkVersion(self, applicationName):
        command = applications[applicationName]
        process = subprocess.Popen([command, '--version'], stdout=subprocess.PIPE,stderr = subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stdout:
            stdout = stdout.split('\n')
            stdout = stdout.split('.')
            return stdout
        else:
            return stderr

    def emptyTrash(self):
        try:
            os.system(f'rm -rf {TRASH}')
            return True
        except:
            return False

    def installPythonPackage(self, package):
        print("Package : " + package)
        # print("This will install package using pip")
        try:
            process = subprocess.Popen(['pipe', 'install', package], stdoout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            print(stdout)
            return True
        except:
            return False

    def installPackage(self, package):
        print("Package : " + package)
        # command = ['sudo', 'apt']
        # print("This will try to install package from software center or snap")
        try:
            process = subprocess.Popen(['sudo', 'apt', 'install', packaege], stdoout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if(stdout):
                pass
            else:
                process = subprocess.Popen(['sudo', 'snap', 'install', package], stdoout=subprocess.PIPE, stderr=subprocess.PIPE)
                pass
        except:
            self.speak("Error Installing package using software center")

    def get_closest_command(self):
        pass

    def process_open_command(self, command):
        pass

    def process_search_command(self, command):
        pass

    def process_play_command(self, command):
        pass

    def downloadFromGithub(url=''):
        pass

        