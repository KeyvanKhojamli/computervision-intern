import cv2

#read an image using opencv
img = cv2.imread('level1\example.jpg')

#blur the image using Gaussian blur
img_Gblur = cv2.GaussianBlur(img, (15, 15), 0)
#blur the image using median blur
img_Mblur = cv2.medianBlur(img, 15)
#blur the image average blur
img_Ablur = cv2.blur(img, (15, 15))

#display the image and blur images 
cv2.imshow('image', img)
cv2.imshow('Gaussian blur image', img_Gblur)
cv2.imshow('Median blur image', img_Mblur)
cv2.imshow('Average blur image', img_Ablur)

#wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
