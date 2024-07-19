import cv2
import mediapipe as mp
import pyautogui
from .hand_tracker_module import HandDetector
import time
import numpy as np


class VirtualMouse():
    def __init__(self, wCam = 640, hCam = 480, smoothening = 7, frameR = 100) -> None:
        self.wCam = wCam
        self.hCam = hCam
        self.smoothening = smoothening
        self.frameR = frameR
        
        self.wScr, self.hScr = pyautogui.size()
        self.detector = HandDetector(maxHands=1)

    def run(self):
        plocX, plocY = 0, 0
        clocX, clocY = 0, 0
        pTime = 0
        cap = cv2.VideoCapture(0)
        cap.set(3, self.wCam)
        cap.set(4, self.hCam)
        while True:
            # 1. Find hand Landmarks
            success, img = cap.read()
            img = cv2.flip(img, 1)
            img = self.detector.findHands(img)
            lmList, bbox = self.detector.findPosition(img)

            # 2. Get the tip of the index and middle fingers
            if len(lmList) > 0:
                x1, y1 = lmList[8][1:]
                x2, y2 = lmList[12][1:]

                # 3. Check which fingers are up
                fingers = self.detector.fingersUp()
                print(fingers, flush=True)

                cv2.rectangle(img, (self.frameR, self.frameR), (self.wCam - self.frameR, self.hCam - self.frameR),
                            (255, 0, 255), 2)
                # 4. Only Index Finger : Moving Mode
                if fingers[1] == 1 :#and fingers[2] == 0:
                    plocX, plocY = self.move_mouse(x1, y1, plocX, plocY, img)

                # 8. Both Index and middle fingers are up : Clicking Mode
                if fingers[1] == 1 and fingers[2] == 1:
                    self.click_mouse(x2, y2, img)

            # 11. Frame Rate
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)

            # 12. Display
            cv2.imshow("Image", img)
            cv2.waitKey(1)

    def move_mouse(self, x1, y1, plocX, plocY, img):
        # 5. Convert Coordinates
        x3 = np.interp(x1, (self.frameR, self.wCam - self.frameR), (0, self.wScr))
        y3 = np.interp(y1, (self.frameR, self.hCam - self.frameR), (0, self.hScr))

        # 6. Smoothen Values
        clocX = plocX + (x3 - plocX) / self.smoothening
        clocY = plocY + (y3 - plocY) / self.smoothening

        # 7. Move Mouse
        pyautogui.moveTo(clocX, clocY)    
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        return clocX, clocY
    
    def click_mouse(self, x2, y2, img):
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        # 9. Find distance between fingers
        length, img, lineInfo = self.detector.findDistance(8, 12, img)
        print(length)

        # 10. Click mouse if distance short
        if length < 40:
            cv2.circle(img, (lineInfo[4], lineInfo[5]),
                    15, (0, 255, 0), cv2.FILLED)
            pyautogui.click()

    def close(self):
        cv2.destroyAllWindows()

def main():
    mouse = VirtualMouse()
    mouse.run()
    time.sleep(5)
    mouse.close()

if __name__ == "__main__":
    main()