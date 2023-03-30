# 导入selenium中的webdriver类
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
driver = webdriver.Edge()
# 打开当前路径下的page.html页面
driver.get(os.getcwd() + os.sep + "page.html")
driver.maximize_window()
time.sleep(2)
# 点击alert弹窗
driver.find_element(By.ID, "alertBtn").click()
# 处理弹窗确认
time.sleep(2)
driver.switch_to.alert.accept()
# 点击prompt弹窗
time.sleep(2)
driver.find_element(By.ID, "promptBtn").click()
# 处理弹窗输入框输入内容
time.sleep(2)
driver.switch_to.alert.send_keys("prompt内容")
driver.switch_to.alert.accept()
time.sleep(2)
driver.switch_to.alert.accept()
# 点击confirm弹窗
time.sleep(2)
driver.find_element(By.ID, "confirmBtn").click()
# 获取弹窗提示信息
time.sleep(2)
print(driver.switch_to.alert.text)
# 处理弹窗取消
time.sleep(2)
driver.switch_to.alert.dismiss()
# 退出浏览器
time.sleep(2)
driver.quit()
