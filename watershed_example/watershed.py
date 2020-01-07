import numpy as np
import matplotlib as plt
from matplotlib import cm
import cv2

def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)

def mouse_callback(event, x, y, flags, params):
    global marks_updated
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_img, (x,y), 5, (current_marker), -1)
        cv2.circle(img_copy, (x,y), 5, colors[current_marker], -1)
        marks_updated = True


n_markers = 10
current_marker = 1
marks_updated = False

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)

img = cv2.imread('parrot.jpg')
img_copy = np.copy(img)
marker_img = np.zeros(img.shape[:2], dtype=np.int32)
segments = np.zeros(img.shape, dtype=np.uint8)

colors = []
for i in range(10):
    colors.append(create_rgb(i))

while True:
    cv2.imshow('Segments', segments)
    cv2.imshow('Image', img_copy)
    k = cv2.waitKey(1)

    if k == 27:
        break
    elif k == ord('c'):
        img_copy = np.copy(img)
        marker_img = np.zeros(img.shape[:2], dtype=np.int32)
        segments = np.zeros(img.shape, dtype=np.uint8)
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))
    if marks_updated:
        marker_img_copy = marker_img.copy()
        cv2.watershed(img, marker_img_copy)
        segments = np.zeros(img.shape, dtype=np.uint8)
        for color_ind in range(n_markers):
            segments[marker_img_copy == color_ind] = colors[color_ind]
        marks_updated = False

cv2.destroyAllWindows()

