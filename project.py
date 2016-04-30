# -*- coding: utf-8 -*-
import cv2
import numpy as np 


img = cv2.imread("car2.jpg")
# cv2.imshow("input",img)

# 高斯模糊
blur = cv2.GaussianBlur(img,(5,5),0)
# cv2.imshow("gaussinan",blur)

# 灰階
gray_img = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)

# 邊緣檢測
sobel_x = cv2.Sobel(gray_img,cv2.CV_16S,1,0)
sobel_y = cv2.Sobel(gray_img,cv2.CV_16S,0,1)

# in the case of 8-bit input images it will result in truncated derivatives.
# 官方說明 CV_8U 計算完會有一部分被截去 所以使用 CV_16S
# 使用完CV_16S的參數要再轉換回8bit不然會全黑或全灰

sobel_x = cv2.convertScaleAbs(sobel_x)   
sobel_y = cv2.convertScaleAbs(sobel_y)

# dst = cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
# Calculates the weighted sum of two arrays.  src1 權重 alpha . src2 權重 beta.  gamma 為兩數相加之後再加上去的數
dst = cv2.addWeighted(sobel_y,1,sobel_x,1,0)

img_row , img_col = dst.shape #取得圖像的長 寬
color = [32, 96, 160, 224] #將量化後的四個平均值放進一個陣列


for row in range(img_row):
	for col in range(img_col):
		#做量化
		dst[row,col] = color[int(dst[row,col]) / 64]


cv2.imshow("sobel",dst)
# cv2.imwrite("car2_optimization.jpg",dst)
cv2.waitKey(0)




# 輸出兩張圖片可用
# from matplotlib import pyplot as plot
# plot.subplot(2,1,1),plot.xticks([]),plot.yticks([])
# plot.title("Original"),plot.imshow(img)
# plot.subplot(2,1,2),plot.xticks([]),plot.yticks([])
# plot.title("Sobel"),plot.imshow(dst,cmap = 'gray')
# plot.show()