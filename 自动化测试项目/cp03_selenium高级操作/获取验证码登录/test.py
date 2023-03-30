from selenium import webdriver
import pytesseract
import re
from PIL import Image
from selenium.webdriver.common.by import By
from time import sleep
import os
driver = webdriver.Chrome()
driver.get("https://captcha7.scrape.center/")
driver.maximize_window()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[1]/div/div/input').send_keys("admin")
sleep(1)
driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[2]/div/div/input').send_keys("admin")
sleep(1)
auth_stet = "./images/auth.png"

driver.find_element(By.ID, "captcha").screenshot(auth_stet)
# 读取验证码
# 加载图片到内存
sleep(2)
img = Image.open(auth_stet)
text = pytesseract.image_to_string(img)
print(text)
final_text = "".join(re.findall("\w", text)).strip("_")
print(final_text)
sleep(1)
driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[3]/div/div/div[1]/div/input').send_keys(final_text)
sleep(2)
driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[4]/div/button').click()
sleep(10)
driver.quit()
