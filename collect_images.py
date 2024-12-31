import numpy as np
import cv2 as cv
from pathlib import Path

classes = ['A', 'B', 'C', 'D', 'E', 'Like', 'Heart']


def get_image():
    # Class = 'iloveu'
    j = 0
    while (j < len(classes)):
        Path('DATASET/'+classes[j]).mkdir(parents=True, exist_ok=True)
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        i = 0
        while True:

            ret, frame = cap.read()

            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # frame = cv.flip(frame,1)
            i += 1
            if i % 5 == 0:
                cv.imwrite('DATASET/'+classes[j]+'/'+str(i)+'.png', frame)

            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q') or i > 200:
                break
        j += 1
        cap.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    get_image()
