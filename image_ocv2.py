'''
Image editing: writing text on image
'''

# importing cv2 from opencv2
import cv2

my_image = cv2.imread("pexels-louis-2101187.png",1)     #(flag = 0 or 1 or -1)
window_name = "My Window"
org = (100,50)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (0, 255, 0)
thickness = 2
cv2.putText(my_image, "The cherry blossoms ^.^", org, font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow(window_name, my_image)
cv2.waitKey(0)
cv2.destroyAllWindows()