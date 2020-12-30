# debug记录日志

### HTTP Status 500

2020.12.30

错误描述：

<img src="D:\GITHUB\MyNotes\_Typora\Java_Web\SERVLET_JSP\errors.imgs\image-20201230215911751.png" alt="image-20201230215911751" style="zoom:50%;" />

在将相关的信息post到目标jsp文件中之后，在jsp文件中不能取得想要的值，输出之后发现是个空指针，推断是没有传至成功。

错误代码：

```jsp
<body>
    登录 <br>
    <form action="check.jsp" method="post">
        用户名<input type="text" value="uname"> <br>
        密码 <input type="text" value="upwd"> <br>
        <input type="submit" value="登录">
    </form>
</body>
```

原因分析：

查看代码之后，发现input的value属性设置的相关字段，而我们是通过name来获取的，所以在另一个jsp文件中获取不到相关的值，将相关的value改为name，问题解决

