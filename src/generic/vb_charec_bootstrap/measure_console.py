# import the necessary packages
from skimage.measure import compare_ssim
import imutils
import cv2
import matplotlib.pyplot as plt
# construct the argument parse and parse the arguments
# load the two input images
# two individual images.
def tight(imageA, imageB):
# convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# what is that shit?
    cnts = imutils.grab_contours(cnts)

# loop over the contours
# save the original buffer under some pickle object?
    for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
# show the output images
    cv2.imshow("Original", imageA)
    cv2.imshow("Modified", imageB)
    cv2.imshow("Diff", diff)
    cv2.imshow("Thresh", thresh)
    cv2.waitKey(0)

def btight(imageA, imageB):
# convert the images to grayscale
# but the pictures are not grayscale at all, though.
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
# imageA and imageB are both 3 channels.
# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# what is that shit?
    cnts = imutils.grab_contours(cnts)

# loop over the contours
# save the original buffer under some pickle object?
# just crop these shits.
    crp = []
    for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
        (x, y, w, h) = cv2.boundingRect(c)
#        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
# show the output images
        cropping = imageA[y:y+h,x:x+w]
        crp.append(cropping.copy())
        cropping = imageB[y:y+h,x:x+w]
        crp.append(cropping.copy())
    return crp

def ctight(imageA, imageB):
# convert the images to grayscale
# but the pictures are not grayscale at all, though.
    clo = len(imageA.shape)
    if clo == len(imageB.shape):
        if clo >=2 :
            pass
        else:
            raise Exception("dimension smaller than 2")
    else:
        raise Exception("dimension not the same")
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
# imageA and imageB are both 3 channels.
# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# what is that shit?
    cnts = imutils.grab_contours(cnts)

# loop over the contours
# save the original buffer under some pickle object?
# just crop these shits.
    crp = []
    for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
        (x, y, w, h) = cv2.boundingRect(c)
#        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
# show the output images
# a is original.
        #    cf = (imageA[y:y+h,x:x+w,:].copy(), imageB[y:y+h,x:x+w,:].copy() )
        cf = (imageA[y:y+h,x:x+w].copy(), imageB[y:y+h,x:x+w].copy())
        crx = {(x,y,w,h):cf}
        crp.append(crx)
    return crp
        # view them altogether?
#        print(x,y,w,h)
#        print(cropping.shape)

def dplot(array):
    width=5
    height=10
    rows = 5
    cols = 10
    axes=[]
    fig=plt.figure()
    for a in range(rows*cols):
#    b = np.random.randint(7, size=(height,width))
        try:
#            print("key",cos[a])
#        b = hs[cos[a]]
            b = array[a]
            axes.append(fig.add_subplot(rows, cols, a+1) )
            subplot_title=("Subplot"+str(a))
            axes[-1].set_title("number "+str(a))
            plt.imshow(b)
        except:
            print("error on key",cos[a])
    fig.tight_layout()    
    plt.show()

"""        cv2.imshow("Original", cropping)
        cv2.waitKey(0)
        cropping = imageB[x:x+w,y:y+h,:]
        print(cropping.shape)
        cv2.imshow("Modified", cropping)"""
#    cv2.imshow("Diff", diff)
#    cv2.imshow("Thresh", thresh)
#        cv2.waitKey(0)

