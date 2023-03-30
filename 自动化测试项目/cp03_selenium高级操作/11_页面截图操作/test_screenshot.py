# 导入selenium中的webdriver类
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(2)
# 获取截图并指定路径和图片名称
driver.get_screenshot_as_file("C:/Users/90869/Desktop/软件测试/软件测试实验报告/自动化测试/03_img_selenium高级操作/11_页面截图处理/baidu.jpg")
# driver.get_screenshot_as_file("C:/Users/Administrator/Desktop/jQuery-5/baidu.png")
time.sleep(2)
driver.quit()
