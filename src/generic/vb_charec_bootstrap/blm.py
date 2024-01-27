import cv2 as cv
import numpy as np

black_screen = np.zeros([50,50,3])

black_screen[:, :, 2] = np.ones([50,50])*64/255.0
cv.imshow("Simple_black", black_screen)
cv.waitKey(0)
cv.destroyAllWindows()
