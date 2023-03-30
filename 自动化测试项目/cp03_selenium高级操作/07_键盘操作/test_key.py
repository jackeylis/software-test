# 导入selenium中的webdriver类
from selenium import webdriver
from selenium.webdriver.common.by import By
# 导入键盘类Keys
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()
# 打开百度首页
driver.get("https://www.baidu.com/")
time.sleep(2)
kwCtl = driver.find_element(By.ID, "kw")
kwCtl.send_keys("你好世界")
# ctrl + A 全选
kwCtl.send_keys(Keys.CONTROL, "A")
# ctrl + C
# ctrl + X