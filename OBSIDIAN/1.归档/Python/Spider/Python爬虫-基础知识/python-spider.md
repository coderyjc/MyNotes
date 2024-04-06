# Python爬虫

> [学习文档(https://book.apeland.cn/details/66/)](https://book.apeland.cn/details/66/)

## 爬虫基础简介

爬虫在使用场景中的分类

- 通用爬虫：抓取系统重要组成部分。抓取的是一整张页面数据。
- 聚焦爬虫：是建立在通用爬虫的基础之上。抓取的是页面中特定的局部内容。
- 增量式爬虫：检测网站中数据更新的情况。只会抓取网站中最新更新出来的数据。

robots.txt 规定了哪些数据可以被爬取，哪些不能爬取

http协议：就是服务器和客户端进行数据交互的一种形式。

常用请求头信息
- User-Agent：请求载体的身份标识
- Connection：请求完毕后，是断开连接还是保持连接常用响应头信息

常用的响应头消息
- Content-Type：服务器响应回客户端的数据类型

https协议：安全的超文本传输协议 - 传输的文本进行了加密

加密方式：

- 对称密钥加密
	* “共享密钥加密”，也就是说，客户端将文件加密之后，将密钥和加密后的信息一起传送给服务端，加密和解密的密钥是同一个，这种方式看起来安全，但是仍然有安全隐患。
- 非对称密钥加密
	* 服务端制造密钥对（公钥->用来加密 和 私钥->用来解密），将公钥发送给客户端，客户端使用公钥加密文件，将加密后的文件发送给服务端，服务端用私钥进行解密。
	* 技术难题（缺点）：保证接收端向发送端发出公开秘钥的时候，发送端确保收到的是预先要发送的，而不会被挟持。效率低，处理复杂，影响通信速度
- 证书密钥加密


## requests模块基础

步骤

- 指定url - **这个url一定是通过抓包获取的，直接输入地址栏可能不会达到预期的结果**
- 发起请求
- 获取响应数据
- 持久化存储



爬取搜狗页面的数据：

```python
if __name__ == "__main__":
    # 指定url（通过抓包获取）
    url = "http://www.kekenet.com/";
    # 发起请求
    responce = requests.get(url = url);
    # 设置字符编码
    responce.encoding = 'utf-8'
    # 获取响应数据
    page_text = responce.text
    # 持久化存储
    with open("baidu.txt", 'w', encoding='utf-8') as fp:
        fp.write(page_text);
        fp.close()
    print("Success!")
```

### UA伪装

反爬机制

- User-Agent：请求载体的身份标识，使用浏览器发起的请求，请求载体的身份标识为浏览器，使用爬虫程序发起的请求，请求载体为爬虫程序。
- UA检测：相关的门户网站通过检测请求该网站的载体身份来辨别该请求是否为爬虫程序，如果是，则网站数据请求失败。因为正常用户对网站发起的请求的载体一定是基于某一款浏览器，如果网站检测到某一请求载体身份标识不是基于浏览器的，则让其请求失败。因此，UA检测是我们整个课程中遇到的第二种反爬机制，第一种是robots协议

```python
if __name__ == "__main__":
    url = 'https://www.sogou.com/web'

    # 请求头，里面设置我们的UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    # 处理url中携带的参数-封装到字典中
    kw = input('enter a keyword :')
    # 请求中的参数
    param = {
        'query': kw
    }
    # url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)

    # 如果页面显示乱码，可以加上这一句
    # response.encoding = 'utf-8'

    page_text = response.text
    # 持久化存储
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
        fp.close()
    print("success")
```

### 爬取局部信息（ajax-post）

我们已经知道，百度翻译的单词翻译区是基于ajax的局部刷新实现的

![[python爬虫.imgs/image-20210126171017846.png]]
因此我们可以通过抓包工具来获取发送过来的数据。

![[python爬虫.imgs/image-20210126171319186.png]]
从下方数据包中找到我们需要的dog有关的json数据，可以发现，我们发送的表单数据为 kw:"dog"，因此我们的表单需要一个kw属性的数据，值为我们要查找的数据。

![[python爬虫.imgs/image-20210126171500291.png]]
查看响应，发现里面封装的json数据刚好是我们需要的。

![[python爬虫.imgs/image-20210126171619847.png]]
```python
if __name__ == "__main__":
    # 获取用户输入的关键词
    keyWord = input("enter a word to search: ")
    # 设置UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    # 设置url
    url = "https://fanyi.baidu.com/sug"
    # 将要发送的数据
    data = {
        "kw": keyWord
    }
    # 获取回应的数据
    response = requests.post(url=url, data=data, headers=headers)
    # 将回应的数据转化为json格式
    json_data = response.json()
    # 数据的持久化存储
    fileName = keyWord + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(json_data, fp, ensure_ascii=False)
```

> 扩展：json数据格式与python
>
> 将python 的数据结构转换为json：`json_str = json.dumps(data)` 其中，data是一个json格式的字典类型数据; 将json编码的字符串转化为python格式`data = json.loads(json_str)`
>
> 如果处理的是文件，可以使用dump与loda编码和解析json数据：
>
> ```python
> # Writing JSON data
> with open('data.json', 'w') as f:
>     json.dump(data, f)
> 
> # Reading data back
> with open('data.json', 'r') as f:
>     data = json.load(f)
> ```

### 爬取局部信息（ajax-get）

我们来到 [豆瓣动作电影分类排行榜](https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=) 发现在将页面下拉到最底部的时候会刷新出来由此我们可以判定是ajax动态刷新页面，打开浏览器自带的抓包工具，过滤xhr请求，将页面下拉到最下面之后，我们可以捕获到刷新出来的新的数据的信息。

![[python爬虫.imgs/image-20210126175023398.png]]
在下拉到时候我们可以看到出现这么一条信息，消息头是get方式，链接为`https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=20&limit=20`

因此我们可以查看这个消息头，获取数据格式，我们可以自己设置字典的参数来获取数据

![[python爬虫.imgs/image-20210126175509471.png]]
观察这个链接，发现不止有这几个参数

```python
if __name__ == "__main__":
    # 设置UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    # 设置url
    url = "https://movie.douban.com/j/chart/top_list"
    # 将要发送的数据
    param = {
        # 注意！！！这里的键值对一定要设置正确，拼写、空格都要正确，不要有多余的空格或者少的空格！！！！
        'type': '5',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }
    # 获取回应的数据
    response = requests.get(url=url, headers=headers, params=param)
    # 将回应的数据转化为json格式
    json_data = response.json()
    # 数据的持久化存储
    fp = open("movieRank", 'w', encoding='utf-8')
    json.dump(json_data, fp, ensure_ascii=False)
```

### 综合案例

爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据 [http://scxk.nmpa.gov.cn:81/xk/](http://scxk.nmpa.gov.cn:81/xk/)

具体代码查看`Learning\Python\Spider\01-UsageOfRequest\06-challenge.py`

## 数据解析

聚焦爬虫：爬取页面中指定页面的内容。在聚焦爬虫中要用到数据解析。

数据解析原理概述：

- 解析的局部的文本内容都会在标签之间或者标签对应的属性中进行存储
    1. 进行指定标签的定位
    2. 标签或者标签对应的属性中存储的数据值进行提取（解析）

步骤为：

- 指定url
- 发起请求
- 获取响应数据
- 数据解析
- 持久化存储

### xpath解析【重点】

最常用、最便捷、最高效、最通用。

原理：

1. 实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。
2. 调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。

环境安装：

- `pip install lxml`

实例化一个etree对象 `from lxml import etree`

1. 可以将**本地的html文档**中的源码数据加载到etree对象中：`etree.parse(filePath)`
2. 可以将从**互联网**上获取的源码数据加载到该对象中：`etree.HTML('page_text')`

调用xpath方法进行解析：`xpath('xpath表达式')` 【重点】

xpath表达式(始终返回一个列表)：

- `/`表示的是从根节点开始定位。表示的是一个层级 `elem = tree.xpath('/html/body/h1')`
- `//` 表示可以表示从任意位置开始定位 `headers = tree.xpath('//h1')  # // 表示从任意位置开始定位`
- 属性定位： `//tagName[@attrName="attrValue"]` ，比如 `disp1 = tree.xpath('//div[@class="disp-1"]')` 获取到class 属性为 disp-1 的div元素
- 索引定位： `//tagName[@attrName="attrValue"]/subTagName[index]` ，比如 `disp3 = tree.xpath('//body/div[3]')` 表示获得body标签下的第三个div元素
- 取出文本：
    - `/text()` 取出元素中**直系**的文本元素，比如 `disp1_text = tree.xpath('//div[3]/text()')` 取出了全局第3个div中的文字，返回值为一个列表，要想取得文本，应该去一个下标，也就是 `disp1_text = tree.xpath('//body/text()')[0] `
    - `//text()` 取出元素的所有文本元素，比如`disp_all_text = tree.xpath('//body//text()')`
- 取出标签属性：
    - `/@attrName` ，也会返回一个属性值列表，我们可以去下表来取得元素的属性值。比如`img_src = tree.xpath('//body/img/@src')[0]`

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8"/>
        <title>53</title>
    </head>
    <body>
        <button>替换节点</button>
        <h1>我是标题1</h1>
        <h1>我是标题1</h1>
        <p>我是段落</p>
        <div class="disp-1">this is disp1</div>
        <div class="disp-2">this is disp2</div>
        <div class="disp-3">this is disp3</div>
        <img src="https://hcdn2.luffycity.com/media/frontend/activity/head-logo_1564141048.3435316.svg"  alt="tupian"/>
    </body>
</html>
```

注意：所有xpath表达式中的下标都以1开头，所有的python列表都是以0开头

#### 案例一: 解析58二手房的相关数据



> 从[58二手房网站](https://zz.58.com/ershoufang/)中获取二手房的所有标题和价格



注意：获取到了一个xpath节点之后，再以获取到的这个节点为根节点寻找的时候不能用`/tag/tag...` 而是应该用`./tag/..`， 比如 我们已经找到了 一个div节点，我们要再次寻找这个节点下的第二个div节点，因此我们需要使用`theDiv.xpath('./div[2]')`

源码见 `Learning\Python\Spider\02-DataAnalysis\02-xpath-SecondhandHouse.py`


#### 案例二：4K图片解析下载

> 从[高清壁纸网](http://pic.netbian.com/4kfengjing/)中爬取高清壁纸的缩略图


中文乱码问题的通用解决方案：

`img_name.encode('iso-8859-1').decode('gbk')`

或者直接查看页面元数据的编码方式


创建文件夹和写入图片数据

```python
# 创建文件夹来保存图片
if not os.path.exists('./picLibs'):
    os.mkdir('./picLibs')


# 将图片写入文件
img_data = requests.get(url=total_url, headers=headers).content
img_path = 'picLibs/' + pic_title
with open(img_path, 'wb') as fp:
    fp.write(img_data)
    print(pic_title + ' success')
```

源码见 `Learning\Python\Spider\02-DataAnalysis\03-xpath-PictureDownload.py`

#### 案例三：全国城市名称提取

> 从[中国天气网](https://www.aqistudy.cn/historydata/)爬取中国所有的城市的名称

没有很难的知识点，解析略，源码见`Learning\Python\Spider\02-DataAnalysis\03-xpath-AllPath.py`

## 验证码识别

### 使用工具类和api接口

步骤：

- 将验证码事先下载到本地

- 将本地存储的验证码提交给平台的示例程序进行识别操作

识别平台：`http://www.chaojiying.com/user/` 


具体代码见`Learning\Python\Spider\03-VertifyCodeAnalysis\01-recognizeVertifyCode.py`

### 模拟登录-Cookie

处理cookie的两种操作：

- 手动处理，抓包之后封装到header中【不推荐】
- 自动处理

http/https协议的特性：无状态

同一个文件内，第一次请求登录成功之后，第二次请求登陆后的页面数据失败的原因：服务器不知道这次请求是基于登录状态下的请求。

cookie：用来让服务器记录客户端的相关状态，cookie 的值来自模拟登录post 请求后由服务器创建

session：作用: 发送请求、存储cookie

因此，我们需要创建一个session对象，用session对象进行模拟登录post请求的发送（cookie就会被存储在session中）

session对象对个人主页对应的get请求进行发送（携带了cookie）

---

具体分析方法：

打开古诗文网的登录页面 `https://so.gushiwen.cn/user/login.aspx`,开启捕获数据包，输入密码登录。

可以看到html类型的post请求的数据包名为login，可以猜想就是我们要找的数据包

![[python爬虫.imgs/image-20210128143417376.png]]
查看数据包的消息头、请求数据：

消息头

![[python爬虫.imgs/image-20210128143552885.png]]
数据

![[python爬虫.imgs/image-20210128143535267.png]]
因此，登录行为就是向消息头所在的地址发送表单数据中的数据包`page_data = session.post(url=login_url, headers=headers, data=data).text`

然后获得返回的数据，就是我们想要的页面。

这里要注意一下，应该用同一个session访问，以进行cookie的留存。

具体代码见：`Learning\Python\Spider\03-VertifyCodeAnalysis\02-LoginGithub.py`

### 模拟登录-代理IP

> 这个要钱的，而且比较贵，先不学了吧。

场景：多次请求同一个网站，网站的反爬机制组织我们再次请求这个网站，给我们返回错误结果403（服务器拒绝访问）

代理就是用来破解封IP这种反爬机制的。

代理：代理服务器，它的功能就是代理网络用户去取得网络信息。

作用：

- 突破自身IP访问的限制，访问一些平时不能访问的站点。
- 隐藏真实IP，免受攻击，防止自身IP被封锁

代理IP的类型：

- http：应用到http协议对应的url中
- https：应用到https协议对应的url中

代理IP的匿名度：

- 透明：服务器知道这次请求使用了代理，也知道请求对应的真实ip
- 匿名：知道使用了代理，不知道真实ip
- 高匿：不知道使用了代理，更不知道真实ip

## 高性能异步爬虫

目的：在爬虫中使用异步实现高性能的数据爬取操作

方式：

- 多线程，多进程（不建议使用）：
    - 好处：可以为相关阻塞操作开启线程或者进程
    - 坏处：无法无限制的开启多线程或者多进程
- 线程池、进程池（少用）：
    - 好处：我们可以降低系统对进程或者线程创建和销毁的一个频率，从而很好的降低系统的开销
    - 弊端：池中线程或进程的数量有上限
- 单线程异步协程（**推荐**）

Pool线程池对象一定要放在main函数下面，不放在这里会报错。

```python
from multiprocessing.dummy import Pool

... ...
# 实例化一个线程池对象
pool = Pool(4)  # 表示线程池中有4个线程对象
# 第一个参数为阻塞函数，第二个为可迭代对象
# 函数执行的时候会开辟线程并把可迭代对象中的值依次传入到函数中进行执行
pool.map(get_page, name_list)
```

单线程异步协程：

event_loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足某些条件的时候，函数就会被循环执行。

coroutine：协程对象，我们可以将协程对象注册到事件循环中，它会被事件循环调用。我们可以使用async 关键字来定义一个方法，这个方法在调用时不会立即被执行，而是返回一个协程对象。

task：任务，它是对协程对象的进一步封装，包含了任务的各个状态。

future：代表将来执行或还没有执行的任务，实际上和task 没有本质区别。

async：定义一个协程。

await：用来挂起阻塞方法的执行。

协程相关操作：



### 案例一：爬取梨视频的视频数据

在这个案例中，把写文件功能写成一个函数（因为这个功能比较耗时）。

**这个网站加上了反爬机制，无法破解，故没有做，直接粘贴的教程上的代码**

```python
import requests
import random
from lxml import etree
import re
from fake_useragent import UserAgent
#安装fake-useragent库:pip install fake-useragent
#导入线程池模块
from multiprocessing.dummy import Pool
#实例化线程池对象
pool = Pool()
url = 'http://www.pearvideo.com/category_1'
#随机产生UA
ua = UserAgent().random
headers = {
    'User-Agent':ua
}
#获取首页页面数据
page_text = requests.get(url=url,headers=headers).text
#对获取的首页页面数据中的相关视频详情链接进行解析
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@id="listvideoList"]/ul/li')
detail_urls = []#存储二级页面的url
for li in li_list:
    detail_url = 'http://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    title = li.xpath('.//div[@class="vervideo-title"]/text()')[0]
    detail_urls.append(detail_url)
vedio_urls = []#存储视频的url
for url in detail_urls:
    page_text = requests.get(url=url,headers=headers).text
    vedio_url = re.findall('srcUrl="(.*?)"',page_text,re.S)[0]
    vedio_urls.append(vedio_url) 
#使用线程池进行视频数据下载    
func_request = lambda link:requests.get(url=link,headers=headers).content
video_data_list = pool.map(func_request,vedio_urls)
#使用线程池进行视频数据保存
func_saveData = lambda data:save(data)
pool.map(func_saveData,video_data_list)
def save(data):
    fileName = str(random.randint(1,10000))+'.mp4'
    with open(fileName,'wb') as fp:
        fp.write(data)
        print(fileName+'已存储')
pool.close()
pool.join()
```

## Selenium

### 安装与环境测试

> 源码：GITHUB\Learning\Python\Spider\05-Selenium\01-test.py

安装环境 `pip install selenium`

下载与浏览器对应的驱动，注意查看映射关系

使用步骤：

- 实例化浏览器对象
- 编写自动化操作代码

```python
if __name__ == "__main__":
    #  实例化一个浏览器对象
    bro = webdriver.Firefox(executable_path='./../Utils/geckodriver.exe')
    #  让浏览器发起一个指定的url对应请求 , python程序会自动调用驱动打开浏览器进行一系列操作
    bro.get('http://scxk.nmpa.gov.cn:81/xk/')
    #  获取页面源码
    page_text = bro.page_source
    tree = etree.HTML(page_text)
    #  获取列表块
    list_block = tree.xpath('//ul[@id="gzlist"]/li')
    for items in list_block:
        title = items.xpath('./dl/@title')[0]
        print(title)
    #  关闭浏览器
    bro.quit()
```

### 一些操作

> 源码：GITHUB\Learning\Python\Spider\05-Selenium\02-OtherAutoOperations.py

- 发起请求 `get(url)`
- 标签定位 `find_...系列的方法` 
- 标签交互 `send_keys('xxx')`
- 执行js程序 `execute_sctript('JsCode')`
- 前进和后退 `back(), forward()`
- 关闭浏览器 `quit()`

定位元素：

![[python爬虫.imgs/image-20210129212959044.png]]
```python
if __name__ == "__main__":
    # 注册浏览器
    bro = webdriver.Firefox(executable_path='./../Utils/geckodriver.exe')
    # 获取页面
    bro.get('http://scxk.nmpa.gov.cn:81/xk/')
    # 标签定位 - 查询信息
    enter = bro.find_element_by_id("searchtext")
    # 向文本框中输入 20170002
    enter.send_keys("20170002")
    #  查找搜索按钮
    btn = bro.find_element_by_id('searchInfo')
    #  点击查找按钮按钮
    btn.click()
    #  执行js代码，向下滚动一屏幕的距离
    bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 再次跳转到页面
    bro.get('http://kaifa.baidu.com/home')
    # 回退到上一个页面
    bro.back()
    # 返回到上一个页面
    bro.forward()
    #  关闭浏览器
    bro.quit()
```

### selenuim处理iframe

实现拖动操作（动作链）

> 源码：GITHUB\Learning\Python\Spider\05-Selenium\03-ActionChain.py

如果定位的标签在iframe中，则必须使用`switch_to.frame(id)`

动作链：

- `from selenium.webdriver import ActionChains`
- 实例化一个动作链对象：`action = ActionChains(bro)`
- `click_and_hold(div)` 长按且点击操作
- `move_by_offset(x, y)` 偏移
- `perform()` 立即执行动作链
- ` action.release()` 释放动作链

```python
if __name__ == "__main__":
    bro = webdriver.Firefox(executable_path='./../Utils/geckodriver.exe')
    bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

    #  如果要丁文的标签是iframe标签的话，就必须通过以下方式来转换定位作用域
    #  因为iframe是在html中应用的另一个html，定位的时候是默认的外层的html
    bro.switch_to.frame('iframeResult')
    div = bro.find_element_by_id('draggable')

    # 动作链
    action = ActionChains(bro)
    # 点击长安指定的标签
    action.click_and_hold(div)

    # 模拟人拖动滑块
    for i in range(5):
        # perform() 立即执行动作链
        # move_by_offset(x, y) 偏移
        action.move_by_offset(17, 0).perform()
        # 休眠0.3秒
        sleep(0.1)
    # 释放动作链
    action.release()
    sleep(5)
    bro.quit()
```


### 无头浏览器 + 规避检测

> Learning\Python\Spider\05-Selenium\04-HeadlessBrowser.py

无可视化界面的浏览器

```python
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options

if __name__ == "__main__":
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--disable-gpu')
    bro = webdriver.Firefox(executable_path='./../Utils/geckodriver.exe', firefox_options=firefox_options)
    # ------------无头浏览器-----------
    bro.get("http://kaifa.baidu.com/home")
    print(bro.page_source)
    bro.quit()
```

规避检测，用的时候直接复制就行

火狐的有问题，这个是chrome的 ，火狐的没有add_experimental_option对象实例，所以先用chrome的吧

```python
from selenium import webdriver
# 实现无可视化界面
from selenium.webdriver.chrome.options import Options
# 实现规避建测
from selenium.webdriver import ChromeOptions

if __name__ == "__main__":
    # 实现无可视化操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # 实现规避检测
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    bro = webdriver.Firefox(executable_path='./driver',
                            firefox_options=chrome_options,
                            options=options)

    # ------------无头浏览器 + 规避检测-----------
    bro.get("http://kaifa.baidu.com/home")
    print(bro.page_source)
    bro.quit()
```

