import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# D打开QQ邮箱网站
driver.get("https://ui.ptlogin2.qq.com/cgi-bin/login?style=9&appid=522005705&s_url=https%3A%2F%2Fwap.mail.qq.com%2Flogin%2Flogin%3Fauth_type%3D3&daid=4&hln_css=https%3A%2F%2Fmail.qq.com%2Fzh_CN%2Fhtmledition%2Fimages%2Flogo%2Fqqmail%2Fqqmail_logo_defa ult_200h.png&low_login=1&hln_autologin=%E8%87%AA%E5%8A%A8%E7%99%BB%E5%BD%95&hln_p_tips=%E8%BE%93%E5%85%A5%E5%AF%86%E7%A0%81")
# 窗口最大化
driver.maximize_window()
# 选中账号输入框输入账号
driver.find_element(By.ID, "u").send_keys("908698497")
# 选择密码输入框 输入密码
driver.find_element(By.ID, "p").send_keys("Z1458872271")
# 点击确认按扭进行登录
driver.find_element(By.ID, "go").click()
time.sleep(40)
# # # 点击发送邮件
driver.find_element(By.XPATH, "//*[@id='mailListHeader']/a[2]").click()
# # 收件人
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='tet']/div[1]/div[2]/input").send_keys("2934541262@qq.com")
# 主题
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="mailMainApp"]/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/input').send_keys("测试")
# 内容
time.sleep(1)
driver.find_element(By.ID, "writer_textarea").send_keys("自动化软件测试2022年11月13日")
# 点击发送
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='mailMainApp']/div[1]/div/div/div/div[1]/div[1]/button[2]").click()
time.sleep(2)
# 关闭
driver.quit()


