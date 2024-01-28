
## 创建Django项目

```bash
django-admin startproject certificate_analysis
```

命令行工具**django-admin**会在安装Django的时候一起自动安装好。

执行了上面的命令以后，系统会为Django项目生成基础文件夹结构。

```bash
certificate_analysis/                  <-- 高级别的文件夹
 |-- certificate_analysis/             <-- Django项目文件夹
 |    |-- certificate_analysis/
 |    |    |-- __init__.py
 |    |    |-- settings.py
 |    |    |-- urls.py
 |    |    |-- wsgi.py
 |    +-- manage.py
 +-- venv/                  <-- 虚拟环境文件夹
```


-   **manage.py**：使用**django-admin**命令行工具的快捷方式。它用于运行与我们项目相关的管理命令。我们将使用它来运行开发服务器，运行测试，创建迁移等。
-   **__init.py**：这个空文件告诉python这个文件夹是一个python包。
-   **settings.py**：包含了所有的项目配置。
-   **urls.py**：这个文件负责映射我们项目中的路由和路径。例如，如果你想在访问URL `/ about/` 时显示某些内容，则必须先在这里做映射关系。
-   **wsgi.py**：该文件是用于部署的简单网关接口。你可以暂且先不用关心它的内容，就先让他在那里就好了。

django自带了一个简单的网络服务器。在开发过程中非常方便，所以我们无需安装任何其他软件即可在本地运行项目。我们可以通过执行命令来测试一下它：

```bash
python manage.py runserver
```

![[Django-基础知识/assets/Pasted image 20230226085417.png]]

可以看到服务已经启动了

![[Django-基础知识/assets/Pasted image 20230226085425.png]]

`Ctrl + C` 终止服务器

## 新建应用程序

![[Django-基础知识/assets/Pasted image 20230226085704.png]]

新建的应用程序就是上图中黄色的小圆圈，一个Django项目中可以包含多个应用程序

创建名为dashboard的应用程序

```bash
django-admin startapp dashboard
```

dashboard文件夹结构是：

```text
 Directory of D:\code\github\certificate_analysis\certificate_analysis\backend\certificate_analysis\dashboard

02/26/2023  08:58 AM    <DIR>          .
02/26/2023  08:58 AM    <DIR>          ..
02/26/2023  08:58 AM                66 admin.py
02/26/2023  08:58 AM               156 apps.py
02/26/2023  08:58 AM    <DIR>          migrations
02/26/2023  08:58 AM                60 models.py
02/26/2023  08:58 AM                63 tests.py
02/26/2023  08:58 AM                66 views.py
02/26/2023  08:58 AM                 0 __init__.py
               6 File(s)            411 bytes
               3 Dir(s)  478,411,984,896 bytes free

```

下面，我们来探讨每个文件的作用：

-   **migrations/**：在这个文件夹里，Django会存储一些文件以跟踪你在**models.py**文件中创建的变更，用来保持数据库和**models.py**的同步。
-   **admin.py**：这个文件为一个django内置的应用程序**Django Admin**的配置文件。
-   **apps.py**：这是应用程序本身的配置文件。
-   **models.py**：这里是我们定义Web应用程序数据实例的地方。models会由Django自动转换为数据库表。
-   **tests.py**：这个文件用来写当前应用程序的单元测试。
-   **views.py**：这是我们处理Web应用程序请求(request)/响应(resopnse)周期的文件。

现在我们创建了我们的第一个应用程序，让我们来配置一下项目以便启用这个应用程序。

配置一下项目以便启用这个应用程序：要做到这一点，打开**settings.py**并尝试找到`INSTALLED_APPS`变量：

![[Django-基础知识/assets/Pasted image 20230226090151.png]]

以上显示的是已经安装在当前Django项目中的应用程序，如身份验证，会话，静态文件管理（图像，JavaScript，CSS等）等。

要想让我们的应用程序运行，应该先把自己的项目名称添加到配置文件中

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 以下是自定义app
    "dashboard",
]

```

使用前面漫画正方形和圆圈的比喻，黄色的圆圈就是我们的**boards**应用程序，**django.contrib.admin, django.contrib.auth**等就是红色的圆圈。


## Hello World

==创建视图==

编辑应用程序`dashboard`中的`views.py`

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World')
```

视图是接收`httprequest`对象并返回一个`httpresponse`对象的Python函数。接收 _request_ 作为参数并返回 _response_ 作为结果。

这个视图返回一个字符串信息

==告诉服务器什么时候返回这个视图==

应该在项目层面管理url，而不是应用层面。

因此应该在项目管理所在的文件夹编写相关代码。

`urls.py`

```ad-tip
title: django中url、path和re_path
url是Django 1.x中的写法，在Django2.1中，开始舍弃Django1.x中的url写法。
在Django2.x中，描写url配置的有两个函数path和re_path，re_path()函数可以看做是django 1.x中得url函数，即可以在路径中使用正则。
```


```python
from django.contrib import admin
from django.urls import path, re_path

# 导入dashboard应用中的views视图
from dashboard import views


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^admin/', admin.site.urls),
]
```

现在，Django使用**正则表达式**来匹配请求的URL。对于我们的**home**视图，我使用`^$` 正则，它将匹配一个空路径，也就是主页（这个URL：[http://127.0.0.1:8000](https://kgithub.com/http://127.0.0.1:8000) ）。如果我想匹配的URL是 **http://127.0.0.1:8000/homepage/** ，那么我的URL正则表达式就会是：`url(r'^homepage/$', views.home, name='home')`。

