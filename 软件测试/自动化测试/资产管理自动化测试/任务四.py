# 导入selenium包里的webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
# 导入时间模块
import time
# 引⼊unittest
import unittest
# 引⼊ddt
import ddt
# 打开浏览器
driver = webdriver.Chrome()
#窗口最大化
driver.maximize_window()
# 浏览器打开指定网址
driver.get('http://124.221.224.47:8084/')
# 智能时间等待30秒
driver.implicitly_wait(30)
# 定位元素
username = driver.find_element(By.XPATH, '//*[@id="input-username"]')
# 清空输入框
username.clear()
# 输入用户名
username.send_keys('administrator')
password = driver.find_element_(By.CSS_SELECTOR, '#input-password')
password.clear()
# 输入密码
password.send_keys('administrator123')
# 点击登录
driver.find_element(By.CLASS_NAME, 'btn-primary').click()
