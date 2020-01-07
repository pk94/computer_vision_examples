import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import cv2

def detect_plate(img):
    car_img_copy = frame.copy()
    car_rect = plate_cascade.detectMultiScale(car_img_copy, scaleFactor=1.2, minNeighbors=3)
    for (x, y, w, h) in car_rect:
        roi = car_img_copy[y:y+h, x:x+w, :]
        for i in range(1, 10):
            roi = cv2.blur(roi, (10, 10))
        car_img_copy[y:y + h, x:x + w, :] = roi
    return car_img_copy

plate_cascade = cv2.CascadeClassifier('russ_plate.xml')

cap = cv2.VideoCapture('russ_plate.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        plate_img = detect_plate(frame)
        cv2.imshow('frame', plate_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
