# 导入selenium中的webdriver类
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
# 打开QQ登录页面

driver.get("https://mail.qq.com/")
# 切换到表单所在框架iframe里页面
# 点击账号或密码登录
# 输入账号
text = driver.find_element(By.ID, "u")
text.click()
text.clear()
text.send_keys("22354687786")
# 输入密码
driver.find_element(By.ID, "p").send_keys("TestPassWord")
# 从表单所在框架iframe里页面切换回主页面
