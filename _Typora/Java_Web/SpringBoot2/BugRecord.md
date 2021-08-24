# Bug记录



## maven错误

### Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.22.2

pom.xml中加入以下代码

```xml


<build>
    <plugins>

        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>2.22.2</version>
            <configuration>
                <skipTests>true</skipTests>
            </configuration>
        </plugin>
    </plugins>

</build>

</project>

```





## 资源路径错误

### 路径访问全解

#### 不使用模板引擎的时候

![image-20210824225157238](BugRecord.imgs/image-20210824225157238.png)



case1：

![image-20210824225213525](BugRecord.imgs/image-20210824225213525.png)



case2：

![image-20210824225224036](BugRecord.imgs/image-20210824225224036.png)



case3：

![image-20210824225233916](BugRecord.imgs/image-20210824225233916.png)



1. “spring.mvc.static-path-pattern”
spring.mvc.static-path-pattern代表的含义是我们应该以什么样的路径来访问静态资源，换句话说，只有静态资源满足什么样的匹配条件，Spring Boot才会处理静态资源请求，以官方配置为例：

这表示只有静态资源的访问路径为/resources/**时，才会处理请求

spring.mvc.static-path-pattern=/resources/**，

假定采用默认的配置端口，那么只有请求地址类似于“http://localhost:8080/resources/jquery.js”时，Spring Boot才会处理此请求，处理方式是将根据模式匹配后的文件名查找本地文件，那么应该在什么地方查找本地文件呢？这就是“spring.resources.static-locations”的作用了。



2. “spring.resources.static-locations”

  “spring.resources.static-locations”用于告诉Spring Boot应该在何处查找静态资源文件，这是一个列表性的配置，查找文件时会依赖于配置的先后顺序依次进行，默认的官方配置如下：

spring.resources.static-locations=classpath:/static,classpath:/public,classpath:/resources,classpath:/META-INF/resources

继续以上面的请求地址为例，“http://localhost:8080/resources/jquery.js”就会在上述的四个路径中依次查找是否存在“jquery.js”文件，如果找到了，则返回此文件， 否则返回404错误。

#### 使用模板引擎的时候

1. 引入jar包(当引入这个jar包的时候 默认的静态根目录变成了templates)

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

步骤二：application.yml只需要加(开发时禁用缓存)

```yml
spring:
   thymeleaf:
     cache: false
```

![image-20210824225415734](BugRecord.imgs/image-20210824225415734.png)![image-20210824225434314](BugRecord.imgs/image-20210824225434314.png)





### SpringBoot整合jsp的时候访问不到静态资源

springboot 默认的静态资源的值有四个：

- *classpath:/META-INF/resources/*
- *classpath:/resources/*
- *classpath:/static/*
- *classpath:/public/*

如果你没有特别配置静态资源的位置，那么默认的静态资源的位置就是resource 下面的static文件夹，毕竟不用自己新建文件夹

那么你的页面引入的静态文件可以这么写：

` <script type="text/javascript" src="/js/jquery.min.js"></script> `

这样就需要在static下面创建js文件夹，将jqeruy.js放在这个js文件夹下面

![image-20210523141031182](R:\GITHUB\MyNotes\_Typora\Java_Web\SpringBoot2\BugRecord.imgs\image-20210523141031182.png)



## 整合pagehelper的时候查询查询了所有的数据，而不是进行了分页

在SSM中整合pagehelper只需要导入一个依赖，但是Springboot中需要导入三个依赖

```xml
<dependency>
    <groupId>com.github.pagehelper</groupId>
    <artifactId>pagehelper</artifactId>
    <version>5.1.4</version>
</dependency>
<dependency>
    <groupId>com.github.pagehelper</groupId>
    <artifactId>pagehelper-spring-boot-starter</artifactId>
    <version>1.2.5</version>
</dependency>
<dependency>
    <groupId>com.github.pagehelper</groupId>
    <artifactId>pagehelper-spring-boot-autoconfigure</artifactId>
    <version>1.2.5</version>
</dependency>
```

导入这三个插件就可以了



