import cv2
import numpy as np

# 读取图像并将其转换为灰度图像
image = cv2.imread(r'C:\Users\whisperwindzz\Documents\Tencent Files\2879368507\FileRecv\Lena\Lena.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 对灰度图像进行二值化处理
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 将二值图像转换为矩阵
matrix = np.array(binary_image)

# 输出矩阵
print("Matrix:")
print(matrix)

# 计算矩阵的平均值和中位数
average_value = np.mean(matrix)
median_value = np.median(matrix)

# 设定阈值为平均值和中位数
threshold_value = int(average_value)  # 平均值作为阈值
thresholded_image = np.where(matrix < threshold_value, 0, 255)

# 将数据类型转换为uint8
thresholded_image = thresholded_image.astype(np.uint8)

# 保存修改后的图像
output_path = r'C:\Users\whisperwindzz\Documents\Tencent Files\2879368507\FileRecv\Lena\Lena_modified.jpg'
cv2.imwrite(output_path, thresholded_image)

# 显示二值化图像
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)

# 显示阈值处理后的图像
cv2.imshow("Thresholded Image", thresholded_image)
cv2.waitKey(0)

# 关闭窗口
cv2.destroyAllWindows()

# 输出平均值、中位数和阈值图像
print("Average Value:", average_value)
print("Median Value:", median_value)
print("Thresholded Image:")
print(thresholded_image)
