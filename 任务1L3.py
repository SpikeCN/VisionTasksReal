import cv2
import numpy as np

# 读取图像并将其转换为灰度图像
image = cv2.imread(r'C:\Users\whisperwindzz\Documents\Tencent Files\2879368507\FileRecv\Lena\Lena.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 将灰度图像分割为上半部分和下半部分
height, width = gray_image.shape[:2]
half_height = height // 2
upper_half = gray_image[:half_height, :]
lower_half = gray_image[half_height:, :]

# 计算上半部分的平均值作为阈值
threshold_value = np.mean(upper_half)

# 对上半部分进行二值化处理
_, binary_upper_half = cv2.threshold(upper_half, threshold_value, 255, cv2.THRESH_BINARY)

# 将上半部分和下半部分合并为最终图像
final_image = np.vstack((binary_upper_half, lower_half))

# 显示最终图像
cv2.imshow("Final Image", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
