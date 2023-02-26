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

