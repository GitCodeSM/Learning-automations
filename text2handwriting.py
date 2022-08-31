# using open-cv2 for converting input text to handwriting

import time
print(time.asctime())
import pywhatkit as kit
import cv2
Handwritten = input("Enter your text to convert in handwriting: ")
kit.text_to_handwriting(Handwritten, save_to = "pythoncoding.png", rgb = (255, 0, 0))
img = cv2.imread("pythoncoding.png")
cv2.imshow("Python Coding", img)
cv2.waitKey(1)
cv2.destroyAllWindows()
print('code finished')
