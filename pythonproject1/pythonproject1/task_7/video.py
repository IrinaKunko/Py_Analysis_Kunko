import cv2 as cv
from resize import resizing

cap =cv.VideoCapture('video_1.mp4')

while cap.isOpened():
    read, frame = cap.read()
    if not read:
        print('Неводможно получить кадр. Выход')
        break
    frame = resizing(frame, 400)
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()