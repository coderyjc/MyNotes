```ad-note
更多内容查看https://github.com/pythonzhichan/django-beginners-guide/blob/master/AdvancedConcepts.md
```

我们将从 **myproject** 目录中编写 **urls.py** 开始：

**myproject/urls.py**

```python
urlpatterns = [  
    path("admin/", admin.site.urls),  
    re_path(r'^$', views.home, name='home'),  
    re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics')  
]
```

一个项目可以有很多 **urls.py** 分布在多个应用（app）中。Django 需要一个 **url.py** 作为入口。这个特殊的 **urls.py** 叫做 **根路由配置（root URLconf）**。它被定义在 **settings.py** 中。

**myproject/settings.py**

```python
ROOT_URLCONF = 'myproject.urls'
```

它已经自动配置好了，你不需要去改变它任何东西。

当 Django 接受一个请求(request)， 它就会在项目的 URLconf 中寻找匹配项。他从 `urlpatterns` 变量的第一条开始，然后在每个 `url` 中去匹配请求的 URL。

如果 Django 找到了一个匹配路径，他会把请求(request)发送给 `url` 的第二个参数 **视图函数（view function）**。`urlpatterns` 中的顺序很重要，因为 Django 一旦找到匹配就会停止往后搜索。如果 Django 在 URLconf 中没有找到匹配项，他会通过 **Page Not Found** 的错误处理代码抛出一个 **404** 异常。

这是 `url` 函数的剖析：

```python
def url(regex, view, kwargs=None, name=None):
    # ...
```

-   **regex**： 匹配 URL patterns 的正则表达式。注意：正则表达式会忽略掉 **GET** 或者 **POST** 后面的参数。在一个 **[http://127.0.0.1:8000/boards/?page=2](http://127.0.0.1:8000/boards/?page=2)** 的请求中，只有 **/boards/** 会被处理。
-   **view**： 视图函数被用来处理用户请求，同时它还可以是 **django.conf.urls.include** 函数的返回值，它将引用一个外部的**urls.py**文件，例如，你可以使用它来定义一组特定于应用的 URLs，使用前缀将其包含在根 URLconf 中。我们会在后面继续探讨这个概念。
-   **kwargs**：传递给目标视图函数的任意关键字参数，它通常用于在可重用视图上进行一些简单的定制，我们不是经常使用它。
-   **name:**： 该 URL 的唯一标识符。这是一个非常重要的特征。要始终记得为你的 URLs 命名。所以，很重要的一点是：不要在 views(视图) 或者 templates(模板) 中硬编码 URL，而是通过它的名字去引用 URL。

```ad-tip
如果你想给用户个人主页设置一个很酷的主页的URL，那么避免与静态资源冲突最简单的方法是添加一个前缀，例如：/u/vitorfs，或者像 Medium 一样使用 @ 作为前缀 /@vitorfs/。
```

url解析：

```python
url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics')
```

正则表达式中的 `\d+` 会匹配一个任意大小的整数值。这个整数值用来从数据库中取到 指定的 **Board**。现在注意我们这样写这个正则表达式 `(?P<pk>\d+)`，这是告诉 Django 将捕获到的值放入名为 **pk** 的关键字参数中。

这个pk必须和视图函数中的参数pk相对应。

```python
def board_topics(request, pk):
    # do something...
```

```ad-note
PK or ID？ PK 表示主键（Primary key），这是访问模型的主键ID的简写方法，所有Django模型都有这个属性，更多的时候，使用pk属性和使用id是一样的，这是因为如果我们没有给model定义主键时，Django将自动创建一个 AutoField 类型的字段，名字叫做 id，它就是主键。  
如果你给model定义了一个不同的主键，例如，假设 email 是你的主键，你就可以这样访问：obj.email 或者 obj.pk，二者是等价的。
```

## 使用URLs API 


urls.py

```python
from django.contrib import admin  
from django.urls import path, re_path  
  
from boards import views  
  
urlpatterns = [  
    path("admin/", admin.site.urls),  
    re_path(r'^$', views.home, name='home'),  
    re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics')  
]
```


在boards/views.py中创建视图函数

```python
def board_topics(req, pk):  
    board = Board.objects.get(pk=pk)  
    return render(req, 'topics.html', {'board': board})
```


在 **templates** 目录中，创建一个名为 **topics.html** 的模板

```html
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{ board.name }}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        <li class="breadcrumb-item">Boards</li>
        <li class="breadcrumb-item active">{{ board.name }}</li>
      </ol>
    </div>
  </body>
</html>
```

浏览器访问http://127.0.0.1:8000/boards/1/应该出现以下页面：

![[Django-基础知识/assets/Pasted image 20230226140423.png]]

## 创建404的响应

编辑测试单元

test.py

```python
class BoardTopicTests(TestCase):  
    def setUp(self):  
        Board.objects.create(name='Django', description='Django Board')  
  
    def test_board_topics_view_success_status_code(self):  
        url = reverse('board_topics', kwargs={'pk': 1})  
        resp = self.client.get(url)  
        self.assertEquals(resp.status_code, 200)  
  
    def test_board_topics_view_not_found_status_code(self):  
        url = reverse('board_topics', kwargs={'pk': 99})  
        resp = self.client.get(url)  
        self.assertEquals(resp.status_code, 404)  
  
    def test_board_topics_url_resolves_board_topics_view(self):  
        view = resolve('/boards/1/')  
        self.assertEquals(view.func, board_topics)
```


这里需要注意几件事情。这次我们使用了 `setUp` 方法。在这个方法中，我们创建了一个 **Board** 实例来用于测试。我们必须这样做，因为 Django 的测试机制不会针对当前数据库跑你的测试。运行 Django 测试时会即时创建一个新的数据库，应用所有的model(模型)迁移 ，运行测试完成后会销毁这个用于测试的数据库。

因此在 `setUp` 方法中，我们准备了运行测试的环境，用来模拟场景。

-   `test_board_topics_view_success_status_code` 方法：测试 Django 是否对于现有的 **Board** 返回 status code(状态码) 200(成功)。
-   `test_board_topics_view_not_found_status_code` 方法：测试 Django 是否对于不存在于数据库的 **Board** 返回 status code 404(页面未找到)。
-   `test_board_topics_url_resolves_board_topics_view`  方法：测试 Django 是否使用了正确的视图函数去渲染 topics。

现在来运行一下测试：

```text
python manage.py test
```

输出了错误

![[Django-基础知识/assets/Pasted image 20230226141740.png]]

![[Django-基础知识/assets/Pasted image 20230226141743.png]]

看到了一个错误：“boards.models.DoesNotExist: Board matching query does not exist.”

在 `DEBUG=False` 的生产环境中，访问者会看到一个 **500 Internal Server Error** 的页面。但是这不是我们希望得到的。

我们想要一个 **404 Page Not Found** 的页面。让我们来重写我们的视图函数。

views.py

```python
from django.shortcuts import render
from django.http import Http404
from .models import Board

def home(request):
    # code suppressed for brevity

def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})
```

重新测试一下

![[Django-基础知识/assets/Pasted image 20230226142022.png]]

现在是404了

![[Django-基础知识/assets/Pasted image 20230226142033.png]]

 Django 有一个快捷方式去得到一个对象，或者返回一个不存在的对象 404。

因此让我们再来重写一下 **board_topics** 函数：

```python
from django.shortcuts import render, get_object_or_404
from .models import Board

def home(request):
    # code suppressed for brevity

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
```

依然成功

## 创建导航链接

![[Django-基础知识/assets/Pasted image 20230226142407.png]]

boards/test.py

```python
class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
```

现在我们同样在 **HomeTests** 中添加了 **setUp** 方法。这是因为我们现在需要一个 **Board** 实例，并且我们将 **url** 和 **response** 移到了 **setUp**，所以我们能在新测试中重用相同的 response。

这里的新测试是 **test_home_view_contains_link_to_topics_page**。我们使用 **assertContains** 方法来测试 response 主体部分是否包含给定的文本。我们在测试中使用的文本是 `a` 标签的 `href` 部分。所以基本上我们是在测试 response 主体是否包含文本 `href="/boards/1/"`。

![[Django-基础知识/assets/Pasted image 20230226144137.png]]

现在进行测试是报错的，因为我们的html模版中还没有写相关的逻辑

接下来编写index.html，更改tbody标签的内容

```html
<!-- code suppressed for brevity -->
<tbody>
  {% for board in boards %}
    <tr>
      <td>
        <a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a>
        <small class="text-muted d-block">{{ board.description }}</small>
      </td>
      <td class="align-middle">0</td>
      <td class="align-middle">0</td>
      <td></td>
    </tr>
  {% endfor %}
</tbody>
<!-- code suppressed for brevity -->
```

始终使用 `{% url %}` 模板标签去写应用的 URL。第一个参数是 URL 的名字(定义在 URLconf， 即 **urls.py**)，然后你可以根据需求传递任意数量的参数。

现在已经可以点击链接了。

![[Django-基础知识/assets/Pasted image 20230226144557.png]]

## 创建返回链接

可以先写测试

```python
def test_board_topics_view_contains_link_back_to_homepage(self):  
    board_topics_url = reverse('board_topics', kwargs={'pk': 1})  
    resp = self.client.get(board_topics_url)  
    homepage_url = reverse('home')  
    self.assertContains(resp, 'href="{0}"'.format(homepage_url))
```

当然现在也是不行的，因为我们还没有创建相关的模版引擎

修改topics.html

```html
{% load static %}  
<!DOCTYPE html>  
<html>  
  <head>  
      <title>{{ board.name }}</title>  
      <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">  
      <!-- code suppressed for brevity -->  
  </head>  
  <body>  
    <div class="container">  
      <ol class="breadcrumb my-4">  
        <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>  
        <li class="breadcrumb-item active">{{ board.name }}</li>  
      </ol>  
    </div>  
  </body>  
</html>
```

重新打开得到：

![[Django-基础知识/assets/Pasted image 20230226145243.png]]

| **主键 自增字段** |                                                                     |
| ----------------- |:-------------------------------------------------------------------:|
| 正则表达式        |                            `(?P<pk>\d+)`                            |
| 举例              | `url(r'^questions/(?P<pk>\d+)/$', views.question, name='question')` |
| 有效 URL          |                          `/questions/934/`                          |
| 捕获数据          |                          ` {'pk': '934'}`                           |


| **Slug 字段** |
| ------------- |:-------------:|
| 正则表达式 | `(?P<slug>[-\w]+)` |
| 举例 | `url(r'^posts/(?P<slug>[-\w]+)/$', views.post, name='post')` |
| 有效 URL| `/posts/hello-world/` |
|捕获数据|`{'slug': 'hello-world'}`|

| **有主键的 Slug 字段** |
| ------------- |:-------------:|
| 正则表达式    |  `(?P<slug>[-\w]+)-(?P<pk>\d+)` | 
| 举例     |`url(r'^blog/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', views.blog_post, name='blog_post')`  |
| 有效 URL|`/blog/hello-world-159/`  |
|捕获数据|`{'slug': 'hello-world', 'pk': '159'}`|


| **Django 用户名** |
| ------------- |:-------------:|
| 正则表达式    | `(?P<username>[\w.@+-]+)` | 
| 举例     |`url(r'^profile/(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile')` |
| 有效 URL|`/profile/vitorfs/` |
|捕获数据|` {'username': 'vitorfs'}`|


| **Year** |
| ------------- |:-------------:|
| 正则表达式    |  `(?P<year>[0-9]{4})` | 
| 举例     | `url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive, name='year')` |
| 有效 URL| `/articles/2016/` |
|捕获数据| `{'year': '2016'}`|


|**Year / Month**|
| ------------- |:-------------:|
| 正则表达式    |  `(?P<year>[0-9]{4})/(?P<month>[0-9]{2})` | 
| 举例     |  `url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive, name='month')`|
| 有效 URL| `/articles/2016/01/` |
|捕获数据| `{'year': '2016', 'month': '01'}`|

