import cv2
import numpy as np
#以下是平均绝对值算法的实现流程

#定义MAD函数
def MAD(image1,image2):
    diff = np.abs(image1 - image2) #abs获取绝对值
    return np.mean(diff)  #mean对差异数组求平均

#读取两幅图片
image1 = cv2.imread(r'C:\Users\whisperwindzz\Documents\Tencent Files\2879368507\FileRecv\Aanda\A.jpg')
image2 = cv2.imread(r'C:\Users\whisperwindzz\Documents\Tencent Files\2879368507\FileRecv\Aanda\1a.jpg')
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# 将彩色图像转换为灰度图像
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


#调用MAD函数读取相似度
similarity = MAD(image1,image2)
print('similarity',similarity)

# 框选匹配部分
match_region = cv2.absdiff(gray_image1, gray_image2)
_, match_region = cv2.threshold(match_region, 50, 255, cv2.THRESH_BINARY)
match_region = cv2.cvtColor(match_region, cv2.COLOR_GRAY2BGR)
output = cv2.bitwise_and(image1, match_region)

# 显示结果图像
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Match Region', match_region)
cv2.imshow('Output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
