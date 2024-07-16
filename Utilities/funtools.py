from pywhatkit import text_to_handwriting, image_to_ascii_art
from Utilities.common_methods import instantPrint

class funtools:
    def __init__(self):
        super().__init__()

    def get_in_handwriting(self, text, path="handwritten.png", color=[0,0,138]):
        text_to_handwriting(text, path, color)        
        instantPrint("done")

    def pic_to_ascii(self, inpath, outpath="ascii_art.png"):
        image_to_ascii_art(inpath, outpath)
        instantPrint("Done")