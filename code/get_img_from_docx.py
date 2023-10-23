import docx2txt

# 提取Word文档中的图片
image_folder = "../source/input_Image"
docx2txt.process("../source/21200107209冯鑫钢.docx", image_folder)

# 遍历图片文件并保存
import os

for image_filename in os.listdir(image_folder):
    if image_filename.endswith(".png"):  # 假设图片格式是PNG
        with open(os.path.join(image_folder, image_filename), "rb") as img_file:
            image_data = img_file.read()
            # 这里可以根据需要保存图片或进行其他操作
