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
time.sleep(2)
# 通过id属性定位到百度搜索框
#kwCat = driver.find_element_by_id("kw")
kwCat = driver.find_element(By.ID, "kw")
kwCat.click()
# 在百度搜索框输入内容
kwCat.send_keys("通过id搜索")
