Django已经配置了Django Admin，这个应用程序列出的INSTALLED_APPS

现在，我们将配置 Django Admin 来维护我们应用程序的版块。

我们首先创建一个管理员帐户：

```bash
python manage.py createsuperuser
```

按照说明操作

```text
Username (leave blank to use 'administrator'):
Email address: coderyjc@163.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

在浏览器访问 http://localhost:8000/admin/

输入用户名和密码

![[Django-基础知识/assets/Pasted image 20230226125944.png]]

它已经配置了一些功能。在这里，我们可以添加用户和组的权限管理，这些概念在后面我们将探讨更多。

添加Board模型非常简单。打开boards目录中的admin.py文件，并添加以下代码：

boards/admin.py

```python
from django.contrib import admin
from .models import Board

admin.site.register(Board)
```

保存admin.py文件，然后刷新网页浏览器中的页面：

![[Django-基础知识/assets/Pasted image 20230226130453.png]]

添加一个项目

![[Django-基础知识/assets/Pasted image 20230226130554.png]]

![[Django-基础知识/assets/Pasted image 20230226130604.png]]

检查一下是否正常：

![[Django-基础知识/assets/Pasted image 20230226130616.png]]