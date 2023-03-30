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
driver.find_element(By.LINK_TEXT, "新闻").click()
time.sleep(2)
# 获取当前窗口名称
print(driver.current_window_handle)
# 获取全部窗口名称(窗口序列号)
print(driver.window_handles)
# 获取第二个窗口的名称（窗口序列号）
print(driver.window_handles[1])
# 切换到第二个窗口（百度新闻窗口）
driver.switch_to.window(driver.window_handles[1])
# 关闭
driver.find_element(By.LINK_TEXT, "中美元首会晤 两国元首握手合影").click()
time.sleep(3)
driver.quit()
