# 导入selenium中的webdriver类
from selenium import webdriver
from selenium.webdriver.common.by import By
# 导入键盘类select
from selenium.webdriver.support.select import Select
import os
import time
driver = webdriver.Chrome()
driver.maximize_window()
# 打开当前路径page.html页面
driver.get(os.getcwd() + os.sep + "page.html")
# 定位到指定的select元素
sel = driver.find_element(By.ID, "sel")
# 传入select元素对象
options = Select(sel)
# 选择option选项value值为2的元素
time.sleep(2)
options.select_by_value("2")
sel.click()
# 选择选项内容为"贵港市"的元素
time.sleep(2)
options.select_by_visible_text("贵港市")
sel.click()
sel.click()
# 选择选项索引值为"3"的元素，索引从"0"开始
time.sleep(2)
options.select_by_index(3)
sel.click()
sel.click()