使用mybatis执行插入的时候提交执行两次：

<img src="D:\GITHUB\MyNotes\_Typora\Errors\SsmErrors.imgs\image-20210109090154868.png" alt="image-20210109090154868" style="zoom:50%;" />


springMVC中央调度器的配置文件中加入的注解驱动应该是 springframework的，不然会报错。
也可以在注册驱动之后修改一下beans的前置标签 :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:mvc="http://www.springframework.org/schema/mvc"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/context
       http://www.springframework.org/schema/context/spring-context.xsd
       http://www.springframework.org/schema/mvc
       http://www.springframework.org/schema/mvc/spring-mvc.xsd">
```