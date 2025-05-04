import cv2

#read an image using opencv
img = cv2.imread('level1\example.jpg')

#print th size of the image
print('Original image size:', img.shape)

#resize the image 
img_resized = cv2.resize(img, (200, 200))
print('Resized image size:', img_resized.shape)

#display the resized image  and orginal image in a window
cv2.imshow('Resized image', img_resized)
cv2.imshow('Original image', img)    

#cut the image to 320*440 pixels from the ROI
img_cut = img[0:320, 200:640]
print('Cut image size:', img_cut.shape)

#display the cut image in a window
cv2.imshow('Cut image', img_cut)

# Wait for a key press and close the windows
cv2.waitKey(0)