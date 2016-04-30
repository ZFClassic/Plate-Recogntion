# -*- coding: utf-8 -*-
import cv2
import numpy as np 

img = cv2.imread("car2.jpg")
cv2.imshow("input",img)


# 高斯模糊
blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gaussinan",blur)

# 灰階
gray_img = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)

# 邊緣檢測
sobel_img = cv2.Sobel(gray_img,cv2.CV_8U,1,0,ksize=3)
cv2.imshow("sobel",sobel_img)


img_row , img_col = gray_img.shape #取得圖像的長 寬
color = [32, 96, 160, 224] #將量化後的四個平均值放進一個陣列

for row in range(img_row):
	for col in range(img_col):
		#做量化
		sobel_img[row,col] = color[int(sobel_img[row,col]) / 64]

cv2.imshow("quantization",sobel_img)
cv2.waitKey(0)