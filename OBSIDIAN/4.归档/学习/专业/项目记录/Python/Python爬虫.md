背景:

使用自动化框架爬取这种列表, 但是在打开浏览器后, 查找了所有元素, 逐个进行点击

```python

bro = webdriver.Firefox(executable_path='./utils/geckodriver.exe', firefox_binary='U://FireFox/Firefox/firefox.exe')

url = 'https://book.douban.com/subject/5363767/reviews'

bro.get(url)

list_elements = bro.find_elements(by=By.CLASS_NAME, value="unfold")

wait = WebDriverWait(bro, 10)

# 打开每一个节点, 中间显式等待

for element in list_elements:

  sleep(5)

  element.click()

```

![[assets/Pasted image 20220502103241.png]]

报错:

```html

 <a id="toggle-4495930-copy" class="unfold" href="javascript:;"> is not clickable at point (479,887)

because another element <div class="action fixed-action"> obscures it

```

其他元素覆盖到了要点击的元素上面

原因分析:

猜测打开浏览器的时候已经记录下来了此时要找的所有元素的绝对位置, 当点击了展开之后, 浏览器插入了更多的文字, 导致了所有元素的相对位置下移, 在打开页面的时候所记录的所有元素的位置已经不再适用.

![[assets/Pasted image 20220502103732.png]]

![[assets/Pasted image 20220502103737.png]]

  

开启debug, 发现正是如此,

![[assets/Pasted image 20220502103813.png]]

![[assets/Pasted image 20220502103821.png]]

解决方案:

```python

driver.refresh()

```

