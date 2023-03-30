from selenium import webdriver #导入selenium模块
from time import sleep #导入time
driver = webdriver.Chrome() #打开Chrome浏览器
driver.maximize_window() #窗口最大化
driver.get("https://www.baidu.com/") #打开百度网站
print(driver.title) #打印百度标题
sleep(3) #打开百度网站控制时间
driver.get("https://www.baidu.com/")
print(driver.title)