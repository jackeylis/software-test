# 导入selenium包里的webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
# 导入时间模块
import time
# 打开Chrome浏览器
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 打开仓库地址
driver.get("http://124.221.224.47:8084/")
time.sleep(30)
# 定位仓库用户名
username = driver.find_element(By.NAME, "input-username")
# 清楚仓库用户名输入框内容
username.clear()
# 填写仓库用户名
username.send_keys("administrator")
# 定位仓库密码输入框
password = driver.find_element(By.NAME, "input-password")
# 清除仓库密码输入框
password.clear()
# 填写仓库密码
password.send_keys("administrator123")
# 点击仓库登录按扭进行登录
driver.find_elements(By.TAG_NAME, 'input')[2].click()
time.sleep(2)
# 打开左侧基本资料下拉框
driver.find_element(By.LINK_TEXT, "基本资料").click()
time.sleep(2)
# 打开基本资料下的供应商管理模块
driver.find_element(By.LINK_TEXT, "供应商管理").click()
time.sleep(3)
# 关闭
driver.quit()

