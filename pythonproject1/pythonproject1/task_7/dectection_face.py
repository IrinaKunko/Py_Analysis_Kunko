import detect
import cv2 as cv

img = cv.imread('img2.jpg')
if img is None:
    raise Exception('Фото отсутствует')
detect.detect_and_dispay(img)
# cv.imshow('show img', res_img)
# cv.imshow('show img', img)

cv.waitKey(0)