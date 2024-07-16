import webbrowser
from pywhatkit import info, search, playonyt

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
