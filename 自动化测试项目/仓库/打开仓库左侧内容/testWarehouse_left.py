# 导入selenium包里的webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
# 导入时间模块
import time
# 打开Chrome浏览器
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 打开仓库地址
driver.get("http://124.221.224.47:8084/")
# 定位仓库用户名
username = driver.find_element(By.ID, "input-username")
# 清楚仓库用户名输入框内容
username.clear()
# 填写仓库用户名
username.send_keys("administrator")
# 定位仓库密码输入框
password = driver.find_element(By.ID, "input-password")
# 清除仓库密码输入框
password.clear()
# 填写仓库密码
password.send_keys("administrator123")
# 点击仓库登录按扭进行登录
driver.find_element(By.ID, "login-btn").click()
time.sleep(2)
# 打开左侧基本资料下拉框
driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[2]/a').click()
# 打开基本资料下的供应商管理模块
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="sidebar"]/ul/li[2]/ul/li[2]/a').click()
time.sleep(3)
# 关闭
driver.quit()
