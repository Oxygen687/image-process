import cv2
import numpy as np


def img2gray(color_image):
    # 将图像转为灰度

    # 将彩色图片转换为灰度图片
    gray_img = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # 创建一个3通道的黑白 RGB 图片
    bw_rgb_image = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
    return bw_rgb_image


def img_invert(img):
    # 将黑色和白色交换

    inverted_img = cv2.bitwise_not(img)
    return inverted_img


def add_text(img, text):
    # 选择字体和字号
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2

    # 获取文本的大小
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)

    # 计算文本位置（右上角）
    text_x = img.shape[1] - text_size[0] - 30  # 30像素的边距
    text_y = 30  # 30像素的边距

    # 指定文本颜色
    text_color = (0, 0, 255)

    # 在图像上绘制文本
    cv2.putText(img, text, (text_x, text_y), font, font_scale, text_color, font_thickness)
    return img


imageName = "frame_1.jpg"
imgText = "21200107209冯鑫钢"
# 读取图像
image = cv2.imread('../source/input_Image/'+imageName)
# 将图片灰度处理
gray_image = img2gray(image)

inverted_image = img_invert(gray_image)

image_okay = add_text(inverted_image, imgText)
# 保存结果
# cv2.imwrite('../source/output_Image/'+imageName, image_okay)

# 显示结果（可选）
cv2.imshow('image', image_okay)
cv2.waitKey(0)
cv2.destroyAllWindows()
