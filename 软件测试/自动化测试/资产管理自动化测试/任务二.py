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
driver.find_element(By.ID, "input-username").click()
# 清楚仓库用户名输入框内容
# 清空输入框
driver.find_element(By.ID,'input-username').clear()
# 输入用户名
driver.find_element(By.ID, 'input-username').send_keys('administrator')
driver.find_elements(By.TAG_NAME, 'input')[1].clear()
# 输入密码
driver.find_elements(By.TAG_NAME, 'input')[1].send_keys('administrator123')
# # 点击登录
driver.find_element(By.CSS_SELECTOR, '#login-btn').click()
time.sleep(3)
driver.quit()
