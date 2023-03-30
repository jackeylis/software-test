# 引入Selenium模块
from selenium.webdriver.common.by import By
from selenium import webdriver
# 引入时间模块
from time import sleep
# 启动Chrome浏览器
driver = webdriver.Chrome()
# 隐性等待10秒(容易产生假死现象)
driver.implicitly_wait(10)
# 强制等待
sleep(10)
