[TOC]



------

使用时发现的Selenium元素定位的代码运行之后会报错，发现是Selenium更新到新版本（4.x版本）后，以前的一些常用的代码的语法发生了改变，当然如果没有更新过或是下载最新版本的Selenium是不受到影响的，还可以使用以前的写法。接下来就是讨论有关于新版本后Selenium定位元素代码的新语法。

## 改动一：executable_path

旧版本Selenium代码：

```python
from selenium import webdriver
driver=webdriver.Chrome(executable_path='/home/yan/Python/chromeselenium/chromeselenium/chromedriver')
12
```

executable_path是我们Selenium驱动的存放路径，只有使用executable_path指定出该路径，Selenium才能正常工作，但是Selenium经过版本更新之后，在使用如上写法时，系统就会报错executable_path has been deprecated, please pass in a Service object,如下所示：

```python
DeprecationWarning: executable_path has been deprecated, please pass in a Service object
  driver = webdriver.Chrome(executable_path="/home/yan/Python/chromeselenium/chromeselenium/chromedriver")
12
```

意思是：executable_path已被弃用，请传入一个Service对象，于是我们就需要修改为如下代码：

新版本Selenium代码：

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 新增

service = Service(executable_path='/home/yan/Python/chromeselenium/chromeselenium/chromedriver')

driver = webdriver.Chrome(service=service)

driver.get("网址")
12345678
```

## 改动二：Selenium定位元素代码

在旧版本中，我们大多数都是使用以下代码来进行元素的定位
旧版本Selenium元素定位代码：

```python
# 以下inputTag任选其一，其他注释掉
inputTag = driver.find_element_by_id("value")  # 利用ID查找

inputTags = driver.find_element_by_class_name("value")  # 利用类名查找

inputTag = driver.find_element_by_name("value")  # 利用name属性查找

inputTag = driver.find_element_by_tag_name("value")  # 利用标签名查找

inputTag = driver.find_element_by_xpath("value")  # 利用xpath查找

inputTag = driver.find_element_by_css_selector("value")  # 利用CSS选择器查找
123456789101112
```

在版本没有更新前我们使用的都是**driver.find_element_by_方法名(”value”)**,**方法名就是by_id、by_class_name、by_name等等，而"value",则是传入的值**，以百度搜索框为例，右键点击百度搜索框点击检查则可看其HTML源代码中属性**id=”kw“**，以旧版本的写法使用id值查找搜索框应该是：

```python
inputTag = driver.find_element_by_id("kw")
1
```

![](img\百度.png)

在版本没有更新之前，通常情况下运行都是能够正确定位到对应的元素，但是Selenium经过版本升级之后，运行后会报错,以driver.find_element_by_id(“value”)为例（其他报错也是类似下面的报错信息），运行后会报错，如下：
![](img\报错信息.png)

根据官方最新文档，将代码进行修改，修改后的格式由 driver.find_element_by_方法名(”value”)变为 **driver.find_element(By.方法名, “value”)**，具体改动如下：

新版本Selenium代码：
首先在文件头部引入如下代码

```python
from selenium.webdriver.common.by import By
1
```

而后做如下修改：

```python
# inputTag = driver.find_element_by_id("value")  # 利用ID查找
# 改为：
inputTag = driver.find_element(By.ID, "value")

# inputTags = driver.find_element_by_class_name("value")  # 利用类名查找
# 改为：
inputTag = driver.find_element(By.CLASS_NAME, "value")

# inputTag = driver.find_element_by_name("value")  # 利用name属性查找
# 改为：
inputTag = driver.find_element(By.NAME, "value")

# inputTag = driver.find_element_by_tag_name("value")  # 利用标签名查找
# 改为：
inputTag = driver.find_element(By.TAG_NAME, "value")

# inputTag = driver.find_element_by_xpath("value")  # 利用xpath查找
# 改为：
inputTag = driver.find_element(By.XPATH, "value")

# inputTag = driver.find_element_by_css_selector("value")  # 利用CSS选择器查找
# 改为：
inputTag = driver.find_element(By.CSS_SELETOR, "value")
1234567891011121314151617181920212223
```

修改完之后即可使用selenium进行自动化工作！

