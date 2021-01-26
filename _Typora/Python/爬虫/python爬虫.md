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

<img src="D:\GITHUB\MyNotes\_Typora\Python\爬虫\python爬虫.imgs\image-20210126171017846.png" alt="image-20210126171017846" style="zoom:50%;" />

因此我们可以通过抓包工具来获取发送过来的数据。

<img src="D:\GITHUB\MyNotes\_Typora\Python\爬虫\python爬虫.imgs\image-20210126171319186.png" alt="image-20210126171319186" style="zoom:50%;" />

从下方数据包中找到我们需要的dog有关的json数据，可以发现，我们发送的表单数据为 kw:"dog"，因此我们的表单需要一个kw属性的数据，值为我们要查找的数据。

<img src="D:\GITHUB\MyNotes\_Typora\Python\爬虫\python爬虫.imgs\image-20210126171500291.png" alt="image-20210126171500291" style="zoom:50%;" />

查看响应，发现里面封装的json数据刚好是我们需要的。

<img src="D:\GITHUB\MyNotes\_Typora\Python\爬虫\python爬虫.imgs\image-20210126171619847.png" alt="image-20210126171619847" style="zoom:50%;" />

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

<img src="D:\GITHUB\MyNotes\_Typora\Python\爬虫\python爬虫.imgs\image-20210126175023398.png" alt="image-20210126175023398" style="zoom:50%;" />

在下拉到时候我们可以看到出现这么一条信息，消息头是get方式，链接为`https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=20&limit=20`

因此我们可以查看这个消息头，获取数据格式，我们可以自己设置字典的参数来获取数据

<img src="D:\GITHUB\MyNotes\_Typora\Python\爬虫\python爬虫.imgs\image-20210126175509471.png" alt="image-20210126175509471" style="zoom: 67%;" />

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

### 正则表达式







### bs4解析







### xpath解析【重点】



