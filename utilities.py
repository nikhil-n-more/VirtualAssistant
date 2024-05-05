from speedtest import Speedtest 
from pywhatkit import playonyt, search, info, text_to_handwriting, image_to_ascii_art, sendwhatmsg
import json 
from urllib.request import urlopen
from datetime import datetime
from psutil import virtual_memory, cpu_percent
import cv2
# import face_recognition as fr
import os
import numpy as np
import webbrowser

class Internet:
    """Class consisting of methods to get internet speeds
    """    
    def __init__(self):
        super().__init__()
        self.speed_test = Speedtest()
        self.speed_test.get_best_server()

    def get_upload_speed(self):
        """Returns Upload speed of the internet

            Return Type : String
        """        
        speed = str(round(self.speed_test.upload() / (10**6), 2)) + " Mbit/s"
        return speed

    def get_download_speed(self):
        """Returns Download speed of internet

            Return Type : String
        """        
        speed = str(round(self.speed_test.download() / (10**6), 2)) + " Mbit/s"
        return speed

    def get_ping(self):
        """Return Ping of the internet connection

            Return Type : String
        """        
        self.speed_test.get_best_server()
        ping = str(self.speed_test.results.ping) + " ms"
        return ping

class Search:
    def __init__(self):
        super().__init__()

    def get_information_wiki(self, topic, lines=2):
        """Gets the information regarding topic from wikipedia

        Args:

            topic : topic to be searched

            lines (int, optional): Lines of information needed. Defaults to 2.

        Returns:

            string containing information
        """        
        information = info(topic, lines=lines)
        return information

    def search_web(self, query):
        """Searches for the query on google

        Opens up browser window ,if a window is already open then
        opens new tab in it

        Args:

            query : topic to be searched
        """        
        search(query)

    def search_youtube(self, topic):
        """Plays closest choice to the topic on YouTube on new browser window

        Args:

            topic : topic to be searched and played
        """        
        playonyt(topic)

    def find_product_amazon(self, product):
        """Searches for a product on amazon on new browser window

        Args:

            product : Name of product to be searched
        """        
        product_link = "https://www.amazon.in/s?k=" + product;
        self.WebBrowser(product_link)

    def find_product_flipkart(self, product):
        """Searches for specific product on flipkart on new browser window

        Args:

            product : Name of product to be searched
        """        
        product_link = "https://www.flipkart.com/search?q=" + product;
        self.WebBrowser(product_link)

    def find_location(self, location):
        """Searches for provided location on new browser window

        Args:

            location (string): location to be searched
        """        
        location_link = "https://google.nl/maps/place/" + location + "/&amp"
        self.WebBrowser(location_link)

    def open_mail(self):
        """Opens up mainbox in existing browser window
        """        
        self.WebBrowser("https://mail.google.com/mail/u/0/")

    def open_whatsapp(self):
        """Opens web whatsapp
        """        
        self.WebBrowser("https://web.whatsapp.com/")

    def WebBrowser(self,url):
        webbrowser.get().open(url)
        # speak(message)

class UserAccess:
    def __init__(self):
        super().__init__()
        self.location_url = 'http://ipinfo.io/json'
        self.openweather_api_key = "96592338a19378689751668cd2f00029"
        self.openweather_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.total_ram = virtual_memory().total
        self.get_location()

    def get_location(self):
        data = json.load(urlopen(self.location_url))
        # self.IP = data['ip']
        # self.organisation = data['org']
        # self.city = data['city']
        # self.country = data['country']
        # self.region = data['region']
        # self.city = data['city'].decode("utf-8").encode("windows-1252").decode("utf-8")
        self.city = "Amalner"
        instantPrint(self.city)
        return {
            "IP" : data['ip'],
            "Organisation" : data['org'],
            "City" : data['city'],
            "Country" : data['country'],
            "Region" : data['region'],
        }

    def get_weather_info(self):
        self.get_location()
        complete_url = self.openweather_url + "appid=" + self.openweather_api_key + "&q=" + self.city
        data = json.load(urlopen(complete_url))
        if(data["cod"] == "404"):
            print("City not found")
            return 
        y = data["main"]
        # self.temperature = y["temp"] - 273
        # self.pressure = y["pressure"]
        # self.humidity = y["humidity"]
        # self.weather_description = y["weather"][0]["description"]
        return {
            "Temperature" : round(y["temp"],2),
            "Pressure" : round(y["pressure"],2),
            "Humidity" : round(y["humidity"],2),
            "Description" : data["weather"][0]["description"],
        }

    def get_current_time(self):
        today = datetime.today()
        return {
            "Hour" : today.time().hour,
            "Minute" : today.time().minute,
            "Second" : today.time().second,
        }

    def get_current_date(self):
        today = datetime.today() 
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        months = ["Jan.", "Feb.", "Mar.", "April", "May", "June", "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]
        return {
            "year" : str(today.date().year),
            "month" : months[today.date().month - 1],
            "day" : str(today.date().day),
            "weekday" : weekdays[today.weekday()],
        }

    def get_system_usage(self):
        cpu = cpu_percent()
        ram_usage = virtual_memory().percent
        return {
            "cpu_percent" : cpu,
            "ram_percent" : ram_usage,
        }

class Applications:
    def __init__(self):
        super().__init__()

    def open(self):
        pass

    def open_folder(self):
        pass

class funtools:
    def __init__(self):
        super().__init__()

    def get_in_handwriting(self, text, path="handwritten.png", color=[0,0,138]):
        text_to_handwriting(text, path, color)        
        instantPrint("done")

    def pic_to_ascii(self, inpath, outpath="ascii_art.png"):
        image_to_ascii_art(inpath, outpath)
        instantPrint("Done")

class extras:
    def __init__(self):
        super().__intit__()

def instantPrint(text : str):
    print(f"\n{text}", flush=True)
    print("-" * 50, flush=True)

# class FaceRecognition:
#     def __init__(self):
#         super().__init__()
#         path = 'users/'
#         images = []
#         self.classNames = []
#         self.encodings = []
#         # Available images
#         myList = os.listdir(path)
#         for cl in myList:
#             curImage = cv2.imread(os.path.join(path, cl))
#             # Append the images to list
#             images.append(curImage)
#             # Append image names to list
#             # name = os.path.spl
#             self.classNames.append(os.path.splitext(cl)[0])
#         self.compute_encodings(images)
    
#     def compute_encodings(self, imageList):
#         for image in imageList:
#             image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#             curEncode = fr.face_encodings(image)[0]
#             self.encodings.append(curEncode)

#     def take_picture(self):
#         name = "Unknown user"
#         cap = cv2.VideoCapture(0)
#         face_names = []
#         face_locations = []
#         face_encodings = []
#         process_this_frame = True
#         while True:
#             ret, frame = cap.read()
#             small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
#             rgb_small_frame = small_frame[:, :, ::-1]
            
#             if process_this_frame:
#                 face_locations = fr.face_locations(rgb_small_frame)
#                 face_encodings = fr.face_encodings(rgb_small_frame)
#                 face_names = []
#                 for face_encoding in face_encodings:
#                     matches = fr.compare_faces(self.encodings, face_encoding)
#                     # name = "Unknown user"
#                     face_distances = fr.face_distance(self.encodings, face_encoding)
#                     best_match_index = np.argmin(face_distances)
#                     if matches[best_match_index]:
#                         name = self.classNames[best_match_index]
#                     face_names.append(name)
#             process_this_frame = not process_this_frame

#             for (top, right, bottom, left), name in zip(face_locations, face_names):
#                 top *= 4
#                 right *= 4
#                 bottom *= 4
#                 left *= 4        

#                 cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#                 cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

#                 font = cv2.FONT_HERSHEY_DUPLEX
#                 cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                
#             cv2.imshow("Recognizer", frame)

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#         cap.release()
#         cv2.destroyAllWindows()
#         return name



# if __name__ == '__main__':
#     face = FaceRecognition()
#     print(face.take_picture())
