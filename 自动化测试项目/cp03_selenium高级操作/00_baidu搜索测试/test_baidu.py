from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# 打开百度
driver.get("https://www.baidu.com")
# 浏览器窗口最大化
driver.maximize_window()
# 输入框输入你好世界
driver.find_element(By.ID, "kw").send_keys("你好世界")
# 点击百度一下 点击多次会弹出验证
driver.find_element(By.ID, "su").click()
