import pytesseract
from PIL import Image
import os
# 定义图片路径
img_pat = os.getcwd() + os.sep + "images" + os.sep + "test.png"
# img_pat = os.getcwd() + os.sep + "images" + os.sep + "vcode.png"
print(img_pat)
# 通过Image的open()方法加载到内存
img = Image.open(img_pat)
print(img)
# 通过图片识别工具识别图片上的文本
text = pytesseract.image_to_string(img)
print(text)
#####################
# 获取验证码中文方法
# 定义图片路径
img_pat = os.getcwd() + os.sep + "images" + os.sep + "chi.png"
print(img_pat)
# 通过Image的open()方法加载到内存
img = Image.open(img_pat)
print(img)
# 通过图片识别工具识别图片上的中文 获取lang="chi_sim"的中文库 获取中文
text = pytesseract.image_to_string(img, lang="chi_sim")
print(text)
