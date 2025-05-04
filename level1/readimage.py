import cv2
#read an image using opencv
img = cv2.imread('level1\example.jpg')

#display the image in a window
cv2.imshow('image', img)

#gray scale the image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#display the gray scale image in a window   
cv2.imshow('gray image', img_gray)

#save the gray scale image
cv2.imwrite('level1\example_gray.jpg', img_gray)

# Wait for a key press and close the window
cv2.waitKey(0)  