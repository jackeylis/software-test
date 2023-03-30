# 导入selenium中的webdriver类
from selenium import webdriver
from selenium.webdriver.common.by import By
# 导入鼠标行动链条类ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
# 打开百度首页
driver.get("https://www.baidu.com/")
time.sleep(2)
# 定位新闻链接
setBtn = driver.find_element(By.LINK_TEXT, "新闻")
# 创建鼠标行动链条类ActionChains对象
ace = ActionChains(driver)
# 在新闻链接鼠标右键
ace.context_click(setBtn).perform()
