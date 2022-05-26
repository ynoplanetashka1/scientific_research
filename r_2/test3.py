import cv2 as cv

img = cv.imread('25_meters.jpg')
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pixel = img[i, j]
        pixel[1] = (pixel[1] - pixel[2]) if pixel[1] > pixel[2] else 0

img = img[:,:,1]
cv.imwrite('25_meters_t.jpg', img)
