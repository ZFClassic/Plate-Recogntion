# -*- coding: utf-8 -*-
import cv2
import numpy as np 

img = cv2.imread("car2.jpg")
cv2.imshow("input",img)

# 高斯模糊
blur = cv2.GaussianBlur(img,(5,5),0)
# cv2.imshow("gaussinan",blur)

# 灰階
gray_img = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)

# 邊緣檢測
sobel_x = cv2.Sobel(gray_img,cv2.CV_8U,1,0)
sobel_y = cv2.Sobel(gray_img,cv2.CV_8U,0,1)

# dst = cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
# Calculates the weighted sum of two arrays.  src1 權重 alpha . src2 權重 beta.  gamma 為兩數相加之後再加上去的數
dst = cv2.addWeighted(sobel_y,1,sobel_x,1,0)


cv2.imshow("sobel",dst)
cv2.waitKey(0)