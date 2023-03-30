# 导入selenium包里的webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
# 导入时间模块
import time
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
driver = webdriver.Chrome()
# 浏览器窗口最大化
driver.maximize_window()
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
driver.get("https://www.baidu.com")
# 睡眠2秒
time.sleep(1)
# 通过xpath_link_text定位打开hao123
driver.find_element(By.PARTIAL_LINK_TEXT, "hao").click()
time.sleep(2)
# 关闭
driver.quit()
