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
# 进入新闻页面 新版本原因find_elements_by_link_text()不能直接使用  需要更改为driver.find_element(By.LINK_TEXT（'类型'）, "value")
newBtn = driver.find_element(By.LINK_TEXT, "新闻")
newBtn.click()
# 后退
time.sleep(2)
driver.back()
# 前进
time.sleep(2)
driver.forward()
# 刷新页面

time.sleep(2)
driver.refresh()
# 打印页面标题
print(driver.title)
# 关闭浏览器
time.sleep(2)
driver.quit()