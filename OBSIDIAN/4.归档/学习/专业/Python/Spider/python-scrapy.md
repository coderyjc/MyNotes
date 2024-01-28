## Scrapy框架

### 环境安装

是什么？ 爬虫中封装好的一个明星框架，功能: 高性能的持久化存储，高性能的数据解析，分布式处理

安装：max / linux `pip install scrapy`

windows安装

- `pip install wheel`
- 下载twisted 下载地址为http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted  下载文件`ad3‑2.2.1‑cp37‑cp37m‑win_amd64.whl` cp37表示python3.7，win_amd64表示win64
- 在有这个轮子的资源管理器页面打开cmd执行`pip install Twisted‑17.1.0‑cp36‑cp36m‑win_amd64.whl`
- `pip install pywin32`
- `pip install scrapy`

测试：在终端里录入scrapy指令，没有报错即表示安装成功！

scrapy使用流程：

- 创建工程：`scrapy startproject ProName`
- 进入工程目录：`cd ProName`
- 创建爬虫文件：`scrapy genspider spiderName www.xxx.com`
- 编写相关操作代码
- 执行工程：`scrapy crawl spiderName`

scrapy在执行的时候会有很多日志信息，如果不想看，可以在配置文件`project/settings.py` 中第23行附近加上这句话`LOG_LEVEL = 'ERROR' # 只显示指定类型的日志信息`

请求头的改变：settings.py中，17行的useragent注释解开，然后加上自己的请求头即可

### Scrapy实现数据解析与数据持久化

`scrapy genspider spiderName www.xxx.com` 创建爬虫文件之后，会在spider中自动生成一个爬虫文件，其中的parse方法就是用来处理数据的。

```python
class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        all_data = []
        for div in div_list:
            # xpath返回的是列表，返回的是Selector类型对象
            # 使用 extract() 提取data中的字符串
            title = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            # 列表调用了extract表示将每一个select对象中的data字符串提取出来，返回列表
            content = div.xpath('./a[1]/div/span/text()').extract()
            content = ''.join(content)
            all_data.append({
                "author": title,
                "content": content
            })
        return all_data
```

---

持久化方法：

- 基于终端指令的持久化
    - 只能持久化到文件
    - 只能将返回值持久化，我们要对清洗后的数据进行封装
    - 高效便捷，但局限性强（文件类型有限）
- 基于管道的持久化

基于终端指令的持久化：

爬虫文件中的parse方法必须有返回值

`scrapy crawl 爬虫名称 -o 路径`

```text
scrapy crawl 爬虫名称 -o xxx.json
scrapy crawl 爬虫名称 -o xxx.xml
scrapy crawl 爬虫名称 -o xxx.csv
```

举例`D:\GITHUB\Learning\Python\Spider\06-Scrapy\QiuBai>scrapy crawl qiubai -o ./qiubai.csv`

---

基于管道的持久化，流程：

1. 数据解析
2. 在item类中定义相关的属性,  实现`items.py`, 属性格式：`name = scrapy.Field()`
3. 将解析的数据封装存储到item类型的对象中
4. 将item类型的对象提交给管道进行持久化存储的操作 `piplines.py`
5. 在管道类的ptocess_item中接收爬虫文件提交过来的item对象，然后编写持久化存储的代码将item对象中存储的数据进行持久化存储
6. `settings.py`配置文件中开启管道

源码见：`GITHUB\Learning\Python\Spider\06-Scrapy\BasedOnPipline`

```python
#  spider.py


import scrapy

#  注意，这里在导包的时候要将项目的目录mark为Source Root
from BasedOnPipline.items import BasedonpiplineItem

class QiubaiSpider(scrapy.Spider):
    name = 'BasedOnPipline'
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            # xpath返回的是列表，返回的是Selector类型对象
            # 使用 extract() 提取data中的字符串
            title = div.xpath('./div[1]/a[2]/h2/text() | ./div[1]/span/h2/text()')[0].extract()
            # 列表调用了extract表示将每一个select对象中的data字符串提取出来，返回列表
            content = div.xpath('./a[1]/div/span/text()').extract()
            content = ''.join(content)
            item = BasedonpiplineItem()
            item['author'] = title
            item['content'] = content
            yield item  # 提交item
```

```python
# items.py

class BasedonpiplineItem(scrapy.Item):
    author = scrapy.Field()
    content = scrapy.Field()
```

```python
# puplines.py


class BasedonpiplinePipeline:
    fp = None

    # 重写父类的一个方法没这份方法只在开始爬虫的时候调用一次
    def open_spider(self, spider):
        print("start.....")
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')

    # 用来处理item类型的对象的
    # 该方法可以接受爬虫文件提交的item对象
    # 每接受一次参数都会调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ' : ' + content + '\n')
        return item

    def close_spider(self, spider):
        print('the end...')
        self.fp.close()
```

注意：

- settings.py 里面要设置userAgent 和 ITEM_PIPELINES

面试题：

如果最终需要将爬取到的数据值一份存储到磁盘文件，一份存储到数据库中，则应该如何操作scrapy？

答：管道文件中的代码为：

```python
#该类为管道类，该类中的process_item方法是用来实现持久化存储操作的。
class DoublekillPipeline(object):
	def process_item(self, item, spider):
	#持久化操作代码 （方式1：写入磁盘文件）
	return item
    #如果想实现另一种形式的持久化操作，则可以再定制一个管道类：
class DoublekillPipeline_db(object):
    def process_item(self, item, spider):
    #持久化操作代码 （方式2：写入数据库）
    return item
```

settings.py 中开启管道操作的代码:

```python
#下列结构为字典，字典中的键值表示的是即将被启用执行的管道文件和其执行的优先级。
ITEM_PIPELINES = {
 'doublekill.pipelines.DoublekillPipeline': 300,
  'doublekill.pipelines.DoublekillPipeline_db': 200,
}

#上述代码中，字典中的两组键值分别表示会执行管道文件中对应的两个管道类中的process_item方法，实现两种不同形式的持久化操作。
```

#### 练习 - 基于Spider的全站数据爬取

题目：爬取小说 [临渊行](http://www.paoshuzw.com/27/27256/)  的所有章节内容

源码见 `GITHUB\Learning\Python\Spider\06-Scrapy\Alldata

### Scrapy五大核心组件

![[python爬虫.imgs/image-20210208170904800.png]]
- 引擎(Scrapy)
  - 用来处理整个系统的数据流处理, 触发事务(框架核心)
- 调度器(Scheduler)
  - 用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回. 可以想像成一个URL（抓取网页的网址或者说是链接）的优先队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址
- 下载器(Downloader)
  - 用于下载网页内容, 并将网页内容返回给蜘蛛(Scrapy下载器是建立在twisted这个高效的异步模型上的)
- 爬虫(Spiders)
  - 爬虫是主要干活的, 用于从特定的网页中提取自己需要的信息, 即所谓的实体(Item)。用户也可以从中提取出链接,让Scrapy继续抓取下一个页面
- 项目管道(Pipeline)
  - 负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。

### 请求传参

- 在某些情况下，我们爬取的数据不在同一个页面中，例如，我们爬取一个电影网站，电影的名称，评分在一级页面，而要爬取的其他电影详情在其二级子页面中。这时我们就需要用到请求传参。
- 请求传参的使用场景
  - 当我们使用爬虫爬取的数据没有存在于同一张页面的时候，则必须使用请求传参

```python
# -*- coding: utf-8 -*-
import scrapy
from bossPro.items import BossproItem
class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position=']
    url = 'https://www.zhipin.com/c101010100/?query=python&page=%d'
    page_num = 2
   #回调函数接受item
    def parse_detail(self,response):
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        # print(job_desc)
        item['job_desc'] = job_desc
        yield item
    #解析首页中的岗位名称
    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        for li in li_list:
            item = BossproItem()
            job_name = li.xpath('.//div[@class="info-primary"]/h3/a/div[1]/text()').extract_first()
            item['job_name'] = job_name
            # print(job_name)
            detail_url = 'https://www.zhipin.com'+li.xpath('.//div[@class="info-primary"]/h3/a/@href').extract_first()
            #对详情页发请求获取详情页的页面源码数据
            #手动请求的发送
            #请求传参：meta={}，可以将meta字典传递给请求对应的回调函数
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        #分页操作
        if self.page_num <= 3:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
```

- 增加并发：
  - 默认scrapy开启的并发线程为32个，可以适当进行增加。在settings配置文件中修改CONCURRENT_REQUESTS = 100值为100,并发设置成了为100。
- 降低日志级别：
  - 在运行scrapy时，会有大量日志信息的输出，为了减少CPU的使用率。可以设置log输出信息为INFO或者ERROR即可。在配置文件中编写：LOG_LEVEL = ‘INFO’
- 禁止cookie：
  - 如果不是真的需要cookie，则在scrapy爬取数据时可以禁止cookie从而减少CPU的使用率，提升爬取效率。在配置文件中编写：COOKIES_ENABLED = False
- 禁止重试：
  - 对失败的HTTP进行重新请求（重试）会减慢爬取速度，因此可以禁止重试。在配置文件中编写：RETRY_ENABLED = False
- 减少下载超时：
  - 如果对一个非常慢的链接进行爬取，减少下载超时可以能让卡住的链接快速被放弃，从而提升效率。在配置文件中进行编写：DOWNLOAD_TIMEOUT = 10 超时时间为10s

### 图片数据爬取

- 在scrapy中我们之前爬取的都是基于字符串类型的数据，那么要是基于图片数据的爬取，那又该如何呢？
  - 其实在scrapy中已经为我们封装好了一个专门基于图片请求和持久化存储的管道类ImagesPipeline，那也就是说如果想要基于scrapy实现图片数据的爬取，则可以直接使用该管道类即可。
- ImagesPipeline使用流程
  - 在配置文件中进行如下配置：
    IMAGES_STORE = ‘./imgs’：表示最终图片存储的目录

```python
# pipline.py

from scrapy.pipelines.images import ImagesPipeline
  import scrapy
  class ImgproPipeline(object):
      item = None
      def process_item(self, item, spider):
          # print(item)
          return item
  #ImagesPipeline专门用于文件下载的管道类，下载过程支持异步和多线程
  class ImgPipeLine(ImagesPipeline):
      #对item中的图片进行请求操作
      def get_media_requests(self, item, info):
          yield scrapy.Request(item['src'])
      #定制图片的名称
      def file_path(self, request, response=None, info=None):
          url = request.url
          file_name = url.split('/')[-1]
          return file_name
      def item_completed(self, results, item, info):
          return item  #该返回值会传递给下一个即将被执行的管道类
```

### selenium的应用

- 在通过scrapy框架进行某些网站数据爬取的时候，往往会碰到页面动态数据加载的情况发生，如果直接使用scrapy对其url发请求，是绝对获取不到那部分动态加载出来的数据值。但是通过观察我们会发现，通过浏览器进行url请求发送则会加载出对应的动态加载出的数据。那么如果我们想要在scrapy也获取动态加载出的数据，则必须使用selenium创建浏览器对象，然后通过该浏览器对象进行请求发送，获取动态加载的数据值。

  #### 案例分析：

- 需求：爬取网易新闻的国内板块下的新闻数据

- 需求分析：当点击国内超链进入国内对应的页面时，会发现当前页面展示的新闻数据是被动态加载出来的，如果直接通过程序对url进行请求，是获取不到动态加载出的新闻数据的。则就需要我们使用selenium实例化一个浏览器对象，在该对象中进行url的请求，获取动态加载的新闻数据。

  #### selenium在scrapy中使用的原理分析：

- 当引擎将国内板块url对应的请求提交给下载器后，下载器进行网页数据的下载，然后将下载到的页面数据，封装到response中，提交给引擎，引擎将response在转交给Spiders。Spiders接受到的response对象中存储的页面数据里是没有动态加载的新闻数据的。要想获取动态加载的新闻数据，则需要在下载中间件中对下载器提交给引擎的response响应对象进行拦截，切对其内部存储的页面数据进行篡改，修改成携带了动态加载出的新闻数据，然后将被篡改的response对象最终交给Spiders进行解析操作。

  #### selenium在scrapy中的使用流程：

- 重写爬虫文件的构造方法，在该方法中使用selenium实例化一个浏览器对象（因为浏览器对象只需要被实例化一次）

- 重写爬虫文件的closed(self,spider)方法，在其内部关闭浏览器对象。该方法是在爬虫结束时被调用

- 重写下载中间件的process_response方法，让该方法对响应对象进行拦截，并篡改response中存储的页面数据

- 在配置文件中开启下载中间件
