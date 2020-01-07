import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

cap = cv2.VideoCapture('steamboat.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, binary_frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(binary_frame, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        contour_image = np.zeros(binary_frame.shape, dtype=np.uint8)
        for i in range(len(contours)):
            if hierarchy[0][i][3] == -1:
                cv2.drawContours(contour_image, contours, i, 255, 2)
            if hierarchy[0][i][3] != -1:
                cv2.drawContours(contour_image, contours, i, 255, 2)
        cv2.imshow('frame', contour_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
