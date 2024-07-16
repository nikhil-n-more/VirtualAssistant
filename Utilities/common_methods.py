import os
import math

def instantPrint(text : str):
    print(f"\n{text}", flush=True)
    print("-" * 50, flush=True)

def createFileWithFolderIfNotExists(path : str) -> bool:
    try:
        createFolderIfNotExists(path)
        if(not os.path.isfile(path)):
            with open(path, 'w') as f:
                pass
        return True
    except:
        return False
    
def createFolderIfNotExists(path : str) -> bool:
    os.makedirs(path, exist_ok=True)
    return True

def removeSpecialCharactersAndSpaces(text : str) -> str:
    text = ''.join(e for e in text if e.isalnum())
    return text.replace(" ", "")

def measure_distance_between_two_points(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)