## 项目创建（一）IDEA联网方式创建

![[assets/Pasted image 20230104103133.png]]

点击Next时，Idea需要联网状态才可以进入到后面那一页，如果不能正常联网，就无法正确到达右面那个设置页了，会一直**联网**转转转。

![[assets/Pasted image 20230104102946.png]]


开发控制器类

`package com.jancoyan.springbootbasicquickstart01.controller;`

```java
@RestController  
@RequestMapping("/user")  
public class UserController {  
  
    @GetMapping()  
    public String getById(){  
        System.out.println("springboot is running...");  
        return "springboot is running...";  
    }  
  
}
```
测试

![[assets/Pasted image 20230104104432.png]]


## 项目创建（二）官网创建

官网提供了[项目创建工具](https://start.spring.io/)（idea的就是调用官网提供的项目创建工具）

![[assets/Pasted image 20230104104736.png]]

填写基本信息

![[assets/Pasted image 20230104104800.png]]

添加依赖

点击生成之后解压到项目文件夹

![[assets/Pasted image 20230104104906.png]]

![[assets/Pasted image 20230104104920.png]]

这时候还不是项目的模块之一，需要添加进项目

打开项目结构

![[assets/Pasted image 20230104105106.png]]

导入模块

![[assets/Pasted image 20230104105128.png]]

![[assets/Pasted image 20230104105152.png]]

![[assets/Pasted image 20230104110432.png]]

直接导入即可

## 项目创建（三）阿里云镜像

创建工程时，切换选择starter服务路径，然后手工输入阿里云地址即可，地址：[http://start.aliyun.com](http://start.aliyun.com/)或[https://start.aliyun.com](https://start.aliyun.com/)

切换源

![[assets/Pasted image 20230104110723.png]]

填写相关信息

![[assets/Pasted image 20230104110802.png]]

选择web应用程序

![[assets/Pasted image 20230104110833.png]]


点击创建即可


## 项目创建（四）手动添加依赖



## SpringBoot简介




