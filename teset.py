import cv2
import numpy as np
from pynput.keyboard import Controller, Key
import time

#keyboard
keyboard = Controller()

#webcam
cap = cv2.VideoCapture(0)

# color arrays
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

lower_blue = np.array([94, 80, 2])
upper_blue = np.array([126, 255, 255])

while True:
    #frame read
    ret, frame = cap.read()
    if not ret:
        break

    # cv shit idk take from internet xD
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # mask red and blue
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # pixel count
    red_count = np.sum(mask_red)
    blue_count = np.sum(mask_blue)

    # if red count is higher space
    if red_count > blue_count:
        keyboard.press(Key.space)
        keyboard.release(Key.space)
     

    # if blue is higher
    elif blue_count > red_count:
        keyboard.press('b')
        keyboard.release('b')
          # Tuş basışlarını yavaşlatmak için bekleme

    # Show cam for debug
    cv2.imshow("Frame", frame)
    cv2.imshow("red",mask_red)
    cv2.imshow("blue", mask_blue)

    # q breaks the code
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# relese
cap.release()
cv2.destroyAllWindows()
