import cv2
import numpy as np
from matplotlib import pyplot as plt

#color_Range
color_range_end = [20, 51, 60, 80, 138, 168, 200, 245, 275, 315, 350]

def _colorhist(img, r_x, r_y):

  #convert bgr2hsv
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  h, s, v = cv2.split(hsv)

  #check img size
  (height, width) = h.shape

	#convert pixel point rate to coordinate
  c_x = int(height * r_x)
  c_y = int(width * r_y)

  #check the h value of the pixel
  pixel_h = h[c_x][c_y]

  #check the range
  h_range = pixel_h
  if (pixel_h <= color_range_end[0]) or (pixel_h > color_range_end[10]):
    h_range = 0
  else:
    for i in range(1, 11):
      if pixel_h <= color_range_end[i]:
        h_range = i
        break

	return h_range
