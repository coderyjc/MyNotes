# Tomcat

## Tomcat基础

### 概念

1）. 软件架构
1. C/S： 客户端/服务器端 ‐‐‐‐‐‐‐‐‐‐‐‐> QQ , 360 ....
2. B/S： 浏览器/服务器端 ‐‐‐‐‐‐‐‐‐‐‐‐> 京东， 网易 ， 淘宝 ， 传智播客官网

2）. 资源分类

1. 静态资源： 所有用户访问后，得到的结果都是一样的，称为静态资源。静态资源可以直接被浏览器解析。* 如： html,css,JavaScript，jpg

2. 动态资源: 每个用户访问相同资源后，得到的结果可能不一样 , 称为动态资源。动态资源被访问后，需要先转换为静态资源，再返回给浏览器，通过浏览器进行解析。* 如：servlet/jsp,php,asp....

3）. 网络通信三要素

1. IP：电子设备(计算机)在网络中的唯一标识。
2. 端口：应用程序在计算机中的唯一标识。 0~65536
3. 传输协议：规定了数据传输的规则

1. 基础协议：
1. tcp : 安全协议，三次握手。 速度稍慢
2. udp：不安全协议。 速度快

### web服务器

概念

```
1）. 服务器：安装了服务器软件的计算机
2）. 服务器软件：接收用户的请求，处理请求，做出响应
3）. web服务器软件：接收用户的请求，处理请求，做出响应。在web服务器软件中，可以部署web项目，让用户通过浏览器来访问这些项目
```

常见的web服务器软件

```
1). webLogic：oracle公司，大型的JavaEE服务器，支持所有的JavaEE规范，收费的。
2). webSphere：IBM公司，大型的JavaEE服务器，支持所有的JavaEE规范，收费的。
3). JBOSS：JBOSS公司的，大型的JavaEE服务器，支持所有的JavaEE规范，收费的。
4). Tomcat：Apache基金组织，中小型的JavaEE服务器，仅仅支持少量的JavaEE规范servlet/jsp。开源的，免费的。
```



### Tomcat目录结构

### Tomcat启动和停止

启动之前必须确保**电脑中已经装了 jdk！并且已经配置了JAVA_HOME环境变量，并将其添加到了PATH中**

像这样：

![image-20201001191313299](D:\GITHUB\MyNotes\_Typora\JAVAWEB\Tomcat\Tomcat.assets\image-20201001191313299.png)

![image-20201001191335261](D:\GITHUB\MyNotes\_Typora\JAVAWEB\Tomcat\Tomcat.assets\image-20201001191335261.png)

<img src="D:\GITHUB\MyNotes\_Typora\JAVAWEB\Tomcat\Tomcat.assets\image-20201001191443194.png" alt="image-20201001191443194" style="zoom:50%;" />

（Tomcat是使用Java语言开发的）

启动 双击`bin/startup.bat`文件

访问 `http://localhost:8080`

停止 双击`bin/shutdown.bat` 文件（或者直接关闭已经打开的cmd窗口）

