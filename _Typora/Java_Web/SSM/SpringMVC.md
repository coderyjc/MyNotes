# SpringMVC

## SpringMVC概述

SpringMVC：是基于spring的一个框架， 实际上就是spring的一个模块， 专门是做web开发的。是servlet的一个升级

web开发底层是servlet ， 框架是在servlet基础上面加入一些功能，让你做web开发方便。

SpringMVC就是一个Spring。 Spring是容器，ioc能够管理对象，使用< bean >, @Component, @Repository, @Service, @Controller

SpringMVC能够创建对象， 放入到容器中（SpringMVC容器）， springmvc容器中放的是控制器对象，

我们要做的是 使用@Contorller创建控制器对象， 把对象放入到springmvc容器中， 把创建的对象作为控制器使用， 这个控制器对象能接收用户的请求， 显示处理结果，就当做是一个servlet使用。

使用@Controller注解创建的是一个普通类的对象， 不是Servlet。 springmvc赋予了控制器对象一些额外的功能。

  web开发底层是servlet， springmvc中有一个对象是Servlet ： DispatherServlet(中央调度器)

  DispatherServlet: 负责接收用户的所有请求， 用户把请求给了DispatherServlet， 之后DispatherServlet把请求转发给我们的Controller对象， 最后是Controller对象处理请求。

### 第一个SpringMVC程序

需求： 用户在页面发起一个请求， 请求交给springmvc的控制器对象，并显示请求的处理结果（在结果页面显示一个欢迎语句）。

**实现步骤：**

1. 新建web maven工程
2. 加入依赖
   spring-webmvc依赖，会间接把spring的依赖都加入到项目，jsp，servlet依赖
   
3. 重点： 在web.xml中注册springmvc框架的核心对象DispatcherServlet（注意：只要是SpringMVC的项目，就必须有DispatcherServlet对象，这个对象是衡量程序是不是用了SpringMVC的标准）
	1. DispatcherServlet叫做中央调度器， 是一个servlet， 它的父类是继承HttpServlet
  	2. DispatcherServle也叫做前端控制器（front controller）
	3. DispatcherServlet负责接收用户提交的请求， 调用其它的控制器对象，并把请求的处理结果显示给用户

4. 创建一个发起请求的页面 index.jsp

5. 创建控制器(处理器)类
	1. 在类的上面加入@Controller注解，创建对象，并放入到springmvc容器中
	2. 在类中的方法上面加入@RequestMapping注解。

6. 创建一个作为结果的jsp，显示请求的处理结果。

7. 创建springmvc的配置文件（spring的配置文件一样）
	1. 声明组件扫描器， 指定@Contorller注解所在的包名
	2. 声明视图解析器。帮助处理视图的。

加入依赖：

```xml
    <dependency>
      <groupId>javax.servlet</groupId>
      <artifactId>javax.servlet-api</artifactId>
      <version>3.1.0</version>
      <scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-webmvc</artifactId>
      <version>5.2.5.RELEASE</version>
    </dependency>
```

更改web版本为4.0

<img src="D:\GITHUB\MyNotes\_Typora\Java_Web\SSM\SpringMVC.imgs\image-20210111103339072.png" alt="image-20210111103339072" style="zoom:50%;" />







## 【重点】SpringMVC注解式开发











## 【重点】SSM整合开发









## SpringMVC核心技术







