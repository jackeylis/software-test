# 引入Selenium模块
from selenium.webdriver.common.by import By
from selenium import webdriver
# 引入时间模块
import time
# 启动Chrome浏览器
driver = webdriver.Chrome()
# 浏览器窗口最大化
driver.maximize_window()
# 打开指定网页
driver.get("https://mail.qq.com/")
# 框架切换 切换到表单所在框架form里面
driver.switch_to.frame("login_frame")
driver.find_element(By.ID, "u").send_keys("908698497")
# 从frame表单切换会主页面
driver.switch_to.default_content()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "客服中心").click()
