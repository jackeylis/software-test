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
# 获取百度贴吧a标签文本
a3btn = driver.find_element(By.LINK_TEXT, "贴吧")
# 删除百度贴吧a标签的target属性  让它在当前页面打开 不重新打开新窗口
driver.execute_script('arguments[0].removeAttribute("target")', a3btn)
# 点击百度贴吧
a3btn.click()
