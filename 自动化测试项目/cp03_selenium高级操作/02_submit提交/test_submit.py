# 引入Selenium模块
from selenium.webdriver.common.by import By
from selenium import webdriver
# 引入时间模块
import time
# 启动Chrome浏览器
driver = webdriver.Chrome()
# 打开指定网页
driver.get("https://www.baidu.com")
# 浏览器窗口最大化
driver.maximize_window()
# 设置等待时间单位/s
time.sleep(2)
# 为搜索框设值”submit提交“
driver.find_element(By.ID, "kw").send_keys("submit提交")
# 触发“百度一下”按扭的submit搜索事件
driver.find_element(By.ID, "su").submit()
