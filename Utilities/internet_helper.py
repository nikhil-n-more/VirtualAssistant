from speedtest import Speedtest 

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
