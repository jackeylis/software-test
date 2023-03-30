# 导入selenium中的webdriver类
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
driver = webdriver.Edge()
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(2)
# 点击"百度一下"按钮左边的相机icon
driver.find_element(By.XPATH, "//span[@class='soutu-btn']").click()
# 定位到要上传文件的文件域
up_file = driver.find_element(By.XPATH, "//input[@class='upload-pic']")
# 拼接当前目录下vivo.png文件路径
image_location = os.getcwd() + os.sep + "vivo.jpg"
# 上传文件路径
up_file.send_keys(image_location)
