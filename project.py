# -*- coding: utf-8 -*-
import cv2
import numpy as np 

img = cv2.imread("car2.jpg")
cv2.imshow("input",img)
img2 = cv2.imread("3.jpg")

blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gaussinan",blur)

gray_img = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)


sobelx1 = cv2.Sobel(gray_img,cv2.CV_8U,1,0,ksize=3)
sobely1= cv2.Sobel(gray_img,cv2.CV_8U,0,1,ksize=3)
cv2.imshow("soble",sobelx1)
y,x = gray_img.shape #取得圖像的長 寬
color = [32, 96, 160, 224] #將量化後的四個平均值放進一個陣列

for width in range(0, x, 1):
	for length in range(0, y, 1):
		px = sobelx1[length:length+1, width:width+1]
		
		#設一變數px去抓當前像素點位置的顏色值
		sobelx1[length:length+1, width:width+1] = color[int(px) / 124]
		#做量化
cv2.imshow("sobelx",sobelx1)
cv2.waitKey(0)