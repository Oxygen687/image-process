import cv2
import numpy
# 导入PIL库 加载字体和绘制文本
from PIL import Image, ImageDraw, ImageFont


def img2gray(color_image):
    # 将彩色图片转换为灰度图片
    gray_img = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # 创建一个3通道的黑白 RGB 图片
    bw_rgb_image = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
    return bw_rgb_image


def img_invert(img):
    # 将黑色和白色交换
    inverted_img = cv2.bitwise_not(img)
    return inverted_img


def cv2ImgAddText(img, text, textColor=(255, 128, 64), fontSize=20):
    if isinstance(img, numpy.ndarray):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)

    # 因此计算图片占用像素宽度pixel pixel*fontSize即为字符串占用的像素宽度
    pixel = 3
    for i in text:
        if i.isascii():
            pixel += 0.5
        else:
            pixel += 1
    pixel *= fontSize

    # 设置字体
    fontPath = "../source/font/SanJiZhiHeiTi-2.ttf"
    # 字体的格式
    fontStyle = ImageFont.truetype(fontPath, fontSize)
    # 文本位置
    text_position = (image.shape[1] - pixel, 50)  # 10像素的边距
    # 绘制文本
    draw.text(text_position, text, fill=textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)


if __name__ == '__main__':
    for i in range(1, 39):
        imageName = f"image{i}.png"  # 待处理的图片
        # 读取图像
        image = cv2.imread('../source/input_Image/'+imageName)

        # 将图片灰度处理
        gray_image = img2gray(image)
        # 将图片的黑白反转
        inverted_image = img_invert(gray_image)

        # 为图片添加文本
        imgText = "21200107208"  # 要写入图片的文本
        image_okay = cv2ImgAddText(inverted_image,  imgText)
        # 保存结果
        cv2.imwrite('../source/output_Image/'+imageName, image_okay)

        # 显示结果（可选）
        # cv2.imshow('My Report Picture', image_okay)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
