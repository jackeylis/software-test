# 导入selenium中的webdriver类
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()
# 打开指定页面
driver.get("https://www.163.com/news/article/GUL80F9C000189FH.html?clickfrom=w_yw")
driver.maximize_window()
time.sleep(3)
js_code = 'var scrollHeight = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);'
js_code += 'window.scrollTo(0, scrollHeight)'
# 通过js代码实现页面滚动条滑动到页底
driver.execute_script(js_code)
