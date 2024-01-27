from measure_console import btight, dplot
import cv2

imageA = cv2.imread("buf0.png")
imageB = cv2.imread("buf1.png")
crx = btight(imageA,imageB)
dplot(crx)
