import cv2 as cv
import sys
import copy
import json

img_path = sys.argv[1]
output_path = img_path.split('.')
output_img_path = output_path.copy()
output_data_path = output_path

output_img_path.insert(len(output_path) - 1, 'output')
output_img_path = '.'.join(output_img_path)
output_data_path[-1] = 'json'
output_data_path = '.'.join(output_data_path)

img = cv.imread(img_path)
one_channel_img = copy.deepcopy(img)

def get_one_channel2(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pixel = one_channel_img[i, j]
            pixel[1] = (pixel[1] - pixel[2]) if pixel[1] > pixel[2] else 0
            pixel[1] = (pixel[1] - pixel[0]) if pixel[1] > pixel[0] else 0

    one_channel_img = one_channel_img[:,:,1]
    return one_channel_img

def get_one_channel1(img):
    one_channel_img = img[:,:,2]
    denoised_image = cv.fastNlMeansDenoising(one_channel_img, h=150)
    return denoised_image

def get_one_channel3(img):
    one_channel_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return one_channel_img

one_channel_img = get_one_channel3(img)
cv.imwrite('5_meters_g.jpg', one_channel_img)
circles = cv.HoughCircles(one_channel_img, cv.HOUGH_GRADIENT, 1.2, 5, param1 = 48, param2 = 13, minRadius = 4, maxRadius = 10)

if circles is None:
    print('none circles is found')
    quit()

output_data = []
for x, y, r in circles[0]:
    x, y, r = list(map(int, [x, y, r]))
    output_data.append((x, y))
    cv.circle(img, (x, y), r, (0, 255, 0), 4)

cv.imwrite(output_img_path, img)
output_data_file = open(output_data_path, 'w')
output_data_text = json.dumps(output_data)
output_data_file.write(output_data_text)
