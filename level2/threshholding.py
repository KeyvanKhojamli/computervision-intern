import cv2

#read image with grayscale
img = cv2.imread('level1\example.jpg' ,cv2.IMREAD_GRAYSCALE)

#trshold image
_,thresh = cv2.threshold(img,50,200,cv2.THRESH_BINARY)


#adaptive thresholding
adaptiveThresha = cv2.adaptiveThreshold(img, 255,
                                      cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY_INV,
                                      7, 3)

#show images
cv2.imshow('image',img)
cv2.imshow('thresh1',thresh)
cv2.imshow('thresh2',adaptiveThresha)
cv2.waitKey(0)
cv2.destroyAllWindows()

#save images
cv2.imwrite('level2/outputs/thresh.jpg',thresh)
cv2.imwrite('level2/outputs/adaptiveThresha.jpg',adaptiveThresha)