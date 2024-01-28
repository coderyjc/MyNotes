
## pip 使用清华源安装

### 临时

```bash
pip install ** -i <https://pypi.yuna.tsinghua.edu.en/simple>
```

### 永久

```bash
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

永久的设置会在路径`C:\Users\Administrator\AppData\Roaming\pip`中创建文件`pip.ini`

内容为：

```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

因此我们可以在这个目录中创建文件并写入文本

> 在使用清华源进行下载的软件包的时候可能会遇到如下问题：
> Could not fetch URL https://pypi.tuna.tsinghua.edu.cn/simple/asgiref/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.tuna.tsinghua.edu.cn', port=443): Max retries ex
ceeded with url: /simple/asgiref/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
> 出现这种问题是因为证书不安全，如下解决方法：


增加--trusted-host pypi.douban.com

```bash
pip install xxx --trusted-host pypi.tuna.tsinghua.edu.cn
```



## 软件包下载问题

如果直接pip下载慢的话，直接登录所在的软件包管理网站，在目录中查找想要的whl文件，然后使用迅雷新建下载任务，然后下载。

软件包网站：

https://www.lfd.uci.edu/~gohlke/pythonlibs/

https://pypi.org/project/

比如我要找`ruamel.yaml.clib==0.2.4`可以直接在页面中搜索`ruamel.yaml.clib`

![[assets/Pasted image 20230126000543.png]]