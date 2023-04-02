---
url: https://blog.csdn.net/qq_52596258/article/details/121742261
title: Failed to configure a DataSource: ‘url‘ attribute is not specified and no embedde_一宿君的博客 - CSDN 博客
date: 2023-04-02 09:10:04
tag: 剪藏/Debug
summary: 实力踩坑 Failed to configure a DataSource: 'url' attribute is not specified and no embedde1、异常错误日志2、分析原因解决1、异常错误日志Failed to configure a DataSource: 'url' attribute is not specified and no embedded datasource could be configured.翻译就是：无法配置DataSource：未指定'url'
---

- [ ] 已整理

---
### 实力踩坑 Failed to configure a DataSource: 'url' attribute is not specified and no embedde

*   [1、异常错误日志](#1_1)
*   [2、分析原因解决](#2_7)

# 1、异常错误日志

```
Failed to configure a DataSource: 'url' attribute is not specified and no embedded datasource could be configured.

翻译就是：无法配置DataSource：未指定'url'属性，也无法配置嵌入数据源。
```

# 2、分析原因解决

**问题原因: Mybatis 没有找到合适的加载类, 其实是大部分`spring-datasource-url`没有加载成功, 分析原因如下所示：**

*   在没有用到数据库的场景下，DataSourceAutoConfiguration 会自动加寻找资源
    
*   spring-datasource-url 没有配置属性值
    
*   spring-datasource-url 配置的地址格式有问题
    
*   spring-datasource-url 配置的文件没有加载
    

**解决方案如下：**

**方案 1（此方案是在没有用到数据库的场景下使用）**

*   排除此类的 autoconfig。启动以后就可以正常运行。
    
    ```
    @SpringBootApplication(exclude= {DataSourceAutoConfiguration.class})
    ```
    

**方案 2**

*   在 application.properties 或者 application.yml 文件中没有添加数据库配置信息.
    
    ```
    spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
    spring.datasource.url=jdbc:mysql://localhost:3306/compass?useUnicode=true&characterEncoding=utf8
    spring.datasource.username=root
    spring.datasource.password=root
    ```
    

**方案 3**

*   在 spring xml 配置文件中引用了数据库地址 所以需要对冒号`:`等特殊字符进行转义处理. 但是在 application.properties / 或者 application.yml 文件并不需要转义, 错误和正确方法写在下面了。
    
    ```
    //错误示例
    spring.datasource.url = jdbc:mysql\://localhost\:1504/f_me?setUnicode=true&characterEncoding=utf8
    ```
    
    ```
    //正确示例
    spring.datasource.url = jdbc:mysql://localhost:1504/f_me?setUnicode=true&characterEncoding=utf8
    ```
    

**方案 4**

*   yml 或者 properties 文件没有被扫描到, 需要在 pom 文件中添加如下，来保证文件都能正常被扫描到并且加载成功。
    
    ```
    <!-- 如果不添加此节点mybatis的mapper.xml文件都会被漏掉。 -->
    <resources>
        <resource>
            <directory>src/main/java</directory>
            <includes>
                <include>**/*.yml</include>
                <include>**/*.properties</include>
                <include>**/*.xml</include>
            </includes>
            <filtering>false</filtering>
        </resource>
        <resource>
            <directory>src/main/resources</directory>
            <includes>
                <include>**/*.yml</include>
                <include>**/*.properties</include>
                <include>**/*.xml</include>
            </includes>
            <filtering>false</filtering>
        </resource>
    </resources>
    ```
    

**上述根据自己情况而定，重新启动基本就没啥问题了！！！**

![](https://img-blog.csdnimg.cn/9c8367d975594f2286269661cfd912c6.gif#pic_center)

一起学编程，让生活更随和！如果你觉得是个同道中人，欢迎关注博主公众号：【随和的皮蛋桑】。专注于 Java 基础、进阶、面试以及计算机基础知识分享🐳。偶尔认知思考、日常水文🐌。

![](https://img-blog.csdnimg.cn/e8614355b8314ddcb90719e643393bea.png#pic_center)