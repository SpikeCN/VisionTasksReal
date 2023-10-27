import cv2
import numpy as np

# 读取图像并将其转换为灰度图像
image = cv2.imread(r'C:\Users\whisperwindzz\Documents\Tencent Files\2879368507\FileRecv\Lena\Lena.jpg', cv2.IMREAD_GRAYSCALE)
T = 128
# 对灰度图像进行二值化处理
_, binary_image = cv2.threshold(image, T, 255, cv2.THRESH_BINARY)

# 计算矩阵前两行数的平均值和中位数
matrix = np.array(binary_image)
first_two_rows = matrix[:2, :]
average_value = np.mean(first_two_rows)
median_value = np.median(first_two_rows)

# 将小于平均值和中位数的数值置为0，大于等于阈值的数值置为255
threshold_value = 128
thresholded_image = np.where(first_two_rows < threshold_value, 0, 255)

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

# 输出矩阵和阈值图像
print("Matrix:")
print(first_two_rows)
print("Average Value:", average_value)
print("Median Value:", median_value)
print("Thresholded Image:")
print(thresholded_image)
