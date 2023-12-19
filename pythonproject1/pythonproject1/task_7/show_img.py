import cv2 as cv
import resize

img = cv.imread('img_1.jpg')
if img is None:
    raise Exception('Фото отсутствует')
res_img = resize.resizing(img, new_width=400)
cv.imshow('show img', res_img)


cv.waitKey(0)