# SpringMVC

## SpringMVC概述

SpringMVC：是基于spring的一个框架， 实际上就是spring的一个模块， 专门是做web开发的。是servlet的一个升级

Web开发底层是servlet ， 框架是在servlet基础上面加入一些功能，让你做web开发方便。

SpringMVC就是一个Spring。 Spring是容器，ioc能够管理对象，使用< bean >, @Component, @Repository, @Service, @Controller

SpringMVC能够创建对象， 放入到容器中（SpringMVC容器）， springmvc容器中放的是控制器对象，

我们要做的是 使用@Contorller创建控制器对象， 把对象放入到springmvc容器中， 把创建的对象作为控制器使用， 这个控制器对象能接收用户的请求， 显示处理结果，就当做是一个servlet使用。

使用@Controller注解创建的是一个普通类的对象， 不是Servlet。 springmvc赋予了控制器对象一些额外的功能。

Web开发底层是servlet， springmvc中有一个对象是Servlet ： DispatherServlet(中央调度器)

DispatherServlet: 负责接收用户的所有请求， 用户把请求给了DispatherServlet， 之后DispatherServlet把请求转发给我们的Controller对象， 最后是Controller对象处理请求。

### 第一个SpringMVC程序

需求： 用户在页面发起一个请求， 请求交给springmvc的控制器对象，并显示请求的处理结果（在结果页面显示一个欢迎语句）。

**实现步骤：**

1. 新建web maven工程

2. 加入依赖，spring-webmvc依赖，会间接把spring的依赖都加入到项目，jsp，servlet依赖
   
3. 重点： 在web.xml中注册springmvc框架的核心对象DispatcherServlet（注意：只要是SpringMVC的项目，就必须有DispatcherServlet对象，这个对象是衡量程序是不是用了SpringMVC的标准）
	1. DispatcherServlet叫做中央调度器， 是一个servlet， 它的父类是继承HttpServlet
    4. DispatcherServle也叫做前端控制器（front controller）
    1. DispatcherServlet负责接收用户提交的请求， 调用其它的控制器对象，并把请求的处理结果显示给用户

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
<!--pom.xml-->
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

![[SpringMVC.imgs/image-20210111103339072.png]]


注册中央调度器DispatcherServlt，需要在tomcat服务器启动后，创建DispatcherServlet对象的实例。

​    为什么要创建DispatcherServlet对象的实例呢？    因为DispatcherServlet在他的创建过程中， 会同时创建springmvc容器对象，    读取springmvc的配置文件，把这个配置文件中的对象都创建好， 当用户发起请求时就可以直接使用对象了。

```xml
<!--web.xml-->
	<servlet>
        <servlet-name>SpringMVC</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>

        <!--自定义springmvc读取的配置文件的位置-->
        <init-param>
             <!--springmvc的配置文件的位置的属性-->
            <param-name>contextConfigLocation</param-name>
            <!--指定自定义文件的位置, 写在 main/resources 目录中-->
            <param-value>classpath:SpringMVC.xml</param-value>
        </init-param>
        <!--
            load-on-startup:表示tomcat启动后创建对象的顺序。它的值是整数，数值越小，tomcat创建对象的时间越早。 大于等于0的整数。
        -->
        <load-on-startup>1</load-on-startup>
    </servlet>

    <!--
        使用框架的时候， url-pattern可以使用两种值
        1. 使用扩展名方式， 语法 *.xxxx , xxxx是自定义的扩展名。 常用的方式 *.do, *.action, *.mvc等等
           不能使用 *.jsp
           http://localhost:8080/myweb/some.do
        2.使用斜杠 "/"
    -->
    <servlet-mapping>
        <servlet-name>SpringMVC</servlet-name>
        <url-pattern>*.do</url-pattern>
    </servlet-mapping>
```

SpringMVC配置文件 `SpringMVC.xml` , 注册组件扫描器

```xml
    <context:component-scan base-package="com.Jancoyan.*"/>
```

创建发起请求的页面 index.jsp

```jsp
    <p>第一个spring MVC项目</p>
    <a href="some.do">发起some.do请求</a>
```

创建处理器（控制器）类（这样的类可以有很多个）

```java
// com.Jancoyan.Controller.MyController

@Controller
public class MyController {
    // 处理用户提交的请求，使用自定义方法来处理请求


    /**
     * 准备使用doSome方法处理some.do请求。
     * @RequestMapping: 请求映射，作用是把一个请求地址和一个方法绑定在一起, 一个请求指定一个方法处理。
     *  属性： 1. value 是一个String，表示请求的uri地址的（some.do）, value的值必须是唯一的， 不能重复。 在使用时，推荐地址以“/”开头
     *  位置：1.在方法的上面，常用的。2.在类的上面
     *  说明： 使用RequestMapping修饰的方法叫做处理器方法或者控制器方法。使用@RequestMapping修饰的方法可以处理请求的，类似Servlet中的doGet, doPost
     *
     *  返回值：ModelAndView 表示本次请求的处理结果
     *   Model: 数据，请求处理完成后，要显示给用户的数据
     *   View: 视图， 比如jsp等等。
     */
    @RequestMapping(value = "/some.do")
    public ModelAndView doSome(){
        // 处理some.do 相当于service调用处理完成了
        ModelAndView modelAndView = new ModelAndView();
        // 添加数据, 框架最后把他放在request作用域（setAttribute）
        modelAndView.addObject("msg1", "hello,SpringMVC");
        modelAndView.addObject("msg2", "welcome");
        // 指定视图的完整路径, 框架会对视图进行forward处理 request.getRequestDispatcher("/show.jsp").forward()
        modelAndView.setViewName("/show.jsp");
        return modelAndView;
    }
}

```

### 请求处理流程

 1. 发起some.do
 2. tomcat(web.xml--url-pattern知道 *.do的请求给DispatcherServlet)
 3. DispatcherServlet（根据springmvc.xml配置知道 some.do---doSome()）
 4. DispatcherServlet把some.do转发给MyController.doSome()方法
 5. 框架执行doSome（）把得到ModelAndView进行处理， 转发到show.jsp

上面的过程简化的方式  some.do---DispatcherServlet---MyController

![[SpringMVC.imgs/image-20210112095419640.png]]

用户可以直接通过在地址栏敲入show.jsp直接显示页面，但是这时候页面中并没有获取到数据，此时我们需要隐藏显示结果的视图，也就是将show.jsp放入 `webapp/WEB-INF/view` 下面达到隐藏效果，但是此时在控制器中转发的时候要写完整的路径，所以我们要在springmvc配置文件中进行配置**视图解析器**

```xml
<!--SpringMVC.xml-->
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
<!--        前缀:视图文件的路径-->
        <property name="prefix" value="/WEB-INF/view/"/>
<!--        前缀:视图文件的扩展名-->
        <property name="suffix" value=".jsp"/>
    </bean>
```

当配置完视图解析器之后，可以使用逻辑名称（文件名），指定视图，框架会使用视图解析器的前缀 + 逻辑名称 + 后缀 组成完成路径， 这里就是字符连接操作

```java
        modelAndView.setViewName("show");
```

至此，第一个项目已经结束，具体源代码参考 `GITHUB\Learning\JavaWeb\SpringMVC\1.FirstApplication`

### SpringMVC执行流程

![[SpringMVC.imgs/image-20210113162949692.png]]

1. 浏览器提交请求到中央调度器
2. 中央调度器直接将请求转给处理器映射器。
3. 处理器映射器会根据请求，找到处理该请求的处理器，并将其封装为处理器执行链后返回给中央调度器。
4. 中央调度器根据处理器执行链中的处理器，找到能够执行该处理器的处理器适配器。
5. 处理器适配器调用执行处理器。
6. 处理器将处理结果及要跳转的视图封装到一个对象 ModelAndView 中，并将其返回给处理器适配器。
7. 处理器适配器直接将结果返回给中央调度器。
8. 中央调度器调用视图解析器，将 ModelAndView 中的视图名称封装为视图对象。
9. 视图解析器将封装了的视图对象返回给中央调度器
10. 中央调度器调用视图对象，让其自己进行渲染，即进行数据填充，形成响应对象。
11. 中央调度器响应浏览器。

## SpringMVC注解式开发

### @ RequestMapping 定义请求规则

@ RequestMapping 放在类的上面，表示该控制器类中所有的RequestMapping前面都会加上类上面RequestMapping括号中的内容，我们通常根据这个来划分不同的控制器的功能，以及进行模块的迁移。只需要改动控制器类上面的requestMapping，就可以实现模块的迁移

```java
// index.xml
<a href="user/some.do"> 调用user的doSome </a>

// MyController.java
@Controller
@RequestMapping("/user")
public class MyController {

    @RequestMapping(value = "/some.do")
    public ModelAndView doSome(){
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("msg", "Hello");
        modelAndView.setViewName("show");
        return modelAndView;
    }
}
```

---

指定method请求方式

如果前后端的请求方式不同，就会报错。

```java
    // 指定请求方式为 POST，使用RequestMethod中的枚举类型
    @RequestMapping(value = "/some.do", method = RequestMethod.POST) // 在这里写
    public ModelAndView doSome(){
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("msg", "Hello");
        modelAndView.setViewName("show");
        return modelAndView;
    }
```



### 处理器方法的参数

处理器方法可以包含以下四类参数，这些参数会在系统调用时由**系统自动赋值**，即我们可在方法内直接使用。 写在控制器方法的形参列表的位置。

- HttpServletRequest
- HttpServletResponse
- HttpSession
- 请求中所携带的请求参数

前三种在调用的时候系统自动赋值，我们直接在控制器方法中直接赋值即可。

```java
    @RequestMapping(value = "/some.do", method = RequestMethod.POST)
    public ModelAndView doSome(HttpServletRequest request, HttpServletResponse response, HttpSession session){
        ModelAndView modelAndView = new ModelAndView();
        // 直接使用即可
        String name = request.getParameter("name");
        System.out.println(name);
        return modelAndView;
    }
```

第四种有两种方法

- 逐个接收参数
- 对象接受参数

注意：在提交请求参数时，get请求方式中文没有乱码。 使用post方式提交请求，中文有乱码，需要使用过滤器处理乱码的问题。过滤器可以自定义，也可使用框架中提供的过滤器 CharacterEncodingFilter

**逐个接收参数**

逐个接受参数的时候，处理器（控制器）方法的形参名和请求中参数名必须一致。同名的请求参数赋值给同名的形参, 对位置没有要求。

```java
// index.jsp
    <form action="user/addOneByOne.do" method="post">
        增加功能的实现： <br>
        name : <input name="name" type="text"> <br>
        age : <input type="text" name="age"> <br>
        <input type="submit" value="逐个接收addOneByOne.do">
    </form>
// MyController.java
    @RequestMapping(value = "/addOneByOne.do", method = RequestMethod.POST)
    public ModelAndView addOneByOne(String name, int age){
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("name", name);
        modelAndView.addObject("age", age);
        modelAndView.setViewName("show");
        return modelAndView;
    }
// show.jsp
    <h3>获取到的name为 ： ${name}</h3>
    <h3>获取到的age为 ： ${age}</h3>
```

原理解析：

框架接收请求参数，使用request对象接收请求参数的时候，框架会帮我们自动执行以下内容：

`String strName = request.getParameter("name");`
`String strAge = request.getParameter("age");`

springmvc框架通过 DispatcherServlet 调用 MyController的doSome()方法调用方法时，按名称对应，把接收的参数赋值给形参 : doSome（strName，Integer.valueOf(strAge)）框架会提供类型转换的功能，能把String转为 int ，long ， float， double等类型。

但是当我们在前端传入age=“” 年龄为空的时候，会出现400错误，400状态码是客户端错误， 表示提交请求参数过程中，发生了问题。

因为 Integer.valueOf(strAge) 传入一个空的时候，会出现错误。

这个可以JavaScript进行前端校验

---

注意：用get方法进行提交的时候不会出现乱码错误，但是post方法会出现中文乱码，这时候应该使用过滤器：

```xml
<!--    注册声明过滤器，解决post乱码问题-->
    <filter>
        <filter-name>characterEncodingFilter</filter-name>
        <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
<!--        设置项目中使用的字符编码-->
        <init-param>
            <param-name>encoding</param-name>
            <param-value>utf-8</param-value>
        </init-param>
<!--         强制请求对象(HttpServletRequest)使用encoding编码的值-->
        <init-param>
            <param-name>forceRequestEncoding</param-name>
            <param-value>true</param-value>
        </init-param>
<!--        强制应答对象(HttpServletResponse)使用encoding编码的值-->
        <init-param>
            <param-name>forceResponseEncoding</param-name>
            <param-value>true</param-value>
        </init-param>
    </filter>

    <filter-mapping>
        <filter-name>characterEncodingFilter</filter-name>
<!--    /*:表示强制所有的请求先通过过滤器处理。-->
        <url-pattern>/*</url-pattern>
    </filter-mapping>
```

---

**校正请求参数名@RequestParam**

前端的sname赋值给形参name；sage赋值给形参age

@RequestParam: 逐个接收请求参数中， 解决请求中参数名形参名不一样的问题

属性：
1. value 请求中的参数名称
2. required 是一个boolean，默认是true, true：表示请求中必须包含此参数。

位置： 在处理器方法的形参定义的前面

```java
@RequestMapping(value = "/modifyParas.do", method = RequestMethod.POST)
    public ModelAndView modifyParas(@RequestParam(value = "sname", required = true) String name, @RequestParam(value = "sage", required = true) int age){
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("name", name);
        modelAndView.addObject("age", age);
        modelAndView.setViewName("show");
        return modelAndView;
    }
```

**对象接收参数**

先调用无参构造，再用set方法赋值

可以有多个形参对象，他们互不干扰，对象会分别创建然后赋值。

@RequestParam 不能在这种情况下使用。

 处理器方法形参是java对象， 这个对象的属性名和请求中参数名一样的,框架会创建形参的java对象， 给属性赋值。 请求中的参数是name，框架会调用setName()

```java
    @RequestMapping(value = "/addObject", method = RequestMethod.POST)
    public ModelAndView addObj(Student student){
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("name", student.getName());
        modelAndView.addObject("age", student.getAge());
        modelAndView.setViewName("show");
        return modelAndView;
    }
```

源码：`GITHUB\Learning\JavaWeb\SpringMVC\2.Parameters`


### 处理器方法的返回值


p23 -- 32 学完ajax + jquery 再来看

### 解读 < url-pattern />

用户发起的请求是由哪些服务器程序处理的？

```
http://localhost:8080/ch05_url_pattern/index.jsp ：tomcat（jsp会转为servlet）
http://localhost:8080/ch05_url_pattern/js/jquery-3.4.1.js ： tomcat
http://localhost:8080/ch05_url_pattern/images/p1.jpg ： tomcat
http://localhost:8080/ch05_url_pattern/html/test.html： tomcat
http://localhost:8080/ch05_url_pattern/some.do ：  DispatcherServlet（springmvc框架处理的）
```

因此，tomcat本身能处理静态资源的访问， 像html， 图片， js文件都是静态资源

原因：tomcat的web.xml文件有一个servlet 名称是 default ， 在服务器启动时创建的。

```xml
<!--tomcat/conf/web.xml-->
 <servlet>
        <servlet-name>default</servlet-name>
        <servlet-class>org.apache.catalina.servlets.DefaultServlet</servlet-class>
        <init-param>
            <param-name>debug</param-name>
            <param-value>0</param-value>
        </init-param>
        <init-param>
            <param-name>listings</param-name>
            <param-value>false</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <servlet-mapping>
        <servlet-name>default</servlet-name>
        <url-pattern>/</url-pattern>  表示静态资源和未映射的请求都这个default处理
    </servlet-mapping>
```

default这个servlet作用： 

1. 处理静态资源
2. 处理未映射到其它servlet的请求。

使用框架的时候， url-pattern可以使用两种值

1. 使用扩展名方式， 语法 *.xxxx , xxxx是自定义的扩展名。 常用的方式 *.do, *.action, *.mvc 等等，不能使用 *.jsp

2. 使用斜杠 "/"。当你的项目中使用了 / ，它会替代 tomcat中的default。导致所有的静态资源都给DispatcherServlet处理， 默认情况下DispatcherServlet没有处理静态资源的能力。没有控制器对象能处理静态资源的访问。所以静态资源（html，js，图片，css）都是404。       动态资源some.do是可以访问，的因为我们程序中有MyController控制器对象，能处理some.do请求。

#### 静态资源的访问

三种方式：

1. 使用< mvc:default-servlet-handler / >
2. 使用 < mvc: resources /> 【掌握】
3. 声明注解驱动

**使用< mvc:default-servlet-handler / >**

需要在springmvc配置文件加入 < mvc:default-servlet-handler >

原理是： 加入这个标签后，框架会创建控制器对象DefaultServletHttpRequestHandler（类似我们自己创建的MyController），DefaultServletHttpRequestHandler这个对象可以把接收的**所有**请求转发给 tomcat的default这个servlet，为了访问动态资源我们需要 加上 < mvc:annotation-driven / > 来解决问题

直接加上这句话

```xml
<!--SpringMVC.xml-->
    <mvc:default-servlet-handler />
    <!-- default-servlet-handler 和 @RequestMapping注解 有冲突， 需要加入annotation-driven 解决问题-->
    <mvc:annotation-driven />
```

**使用 < mvc: resources /> 【掌握】**

mvc:resources 加入后框架会创建 ResourceHttpRequestHandler这个处理器对象。

让这个对象处理静态资源的访问，不依赖tomcat服务器。

mapping:访问静态资源的uri地址， 使用通配符 **

location：静态资源在你的项目中的目录位置。

images/** : 表示 images/p1.jpg , images/user/logo.gif , images/order/history/list.png， **表示所有字符，可以表示文件、目录、多级目录等

mvc:resources和@RequestMapping有一定的冲突，所以要记得加上注解驱动

```xml
<!--SpringMVC.xml-->
<!--
	images, html, js 都是webapp的直接子目录，和WEB-INF同级 
-->
    <mvc:resources mapping="/images/**" location="/images/" />
    <mvc:resources mapping="/html/**" location="/html/" />
    <mvc:resources mapping="/js/**" location="/js/" />


    <mvc:annotation-driven />
```

使用一条语句解决多种静态资源的访问问题：

首先应该在webapp中新建一个static文件夹，然后将所有静态资源文件夹都放在static文件夹中。

webapp/static/html, webapp/static/js, webapp/static/images 

```xml
<mvc:resources mapping="/static/**" location="/static/" />
<mvc:annotation-driven />
```


## SSM整合开发

### 搭建环境

SSM： SpringMVC + Spring + MyBatis.

SpringMVC: 视图层，界面层，负责接收请求，显示处理结果的。

Spring：业务层，管理service，dao，工具类对象的。

MyBatis：持久层， 访问数据库的

用户发起请求--SpringMVC接收--Spring中的Service对象--MyBatis处理数据

SSM整合也叫做SSI (IBatis也就是mybatis的前身)， 整合中有容器。

1. 第一个容器SpringMVC容器， 管理Controller控制器对象的。
2. 第二个容器Spring容器，管理Service，Dao，工具类对象的

我们要做的把使用的对象交给合适的容器创建，管理。

把Controller还有web开发的相关对象交给springmvc容器，web用的对象写在springmvc配置文件中
service，dao对象定义在spring的配置文件中，让spring管理这些对象。

springmvc容器和spring容器是有关系的，关系已经确定好了。springmvc容器是spring容器的子容器， 类似java中的继承。子可以访问父的内容，在子容器中的Controller可以访问父容器中的Service对象， 就可以实现controller使用service对象

**实现步骤**

0. 使用springdb的mysql库， 表使用student（id auto_increment, name, age）

1. 新建maven web项目

2. 加入依赖springmvc，spring，mybatis三个框架的依赖，jackson依赖，mysql驱动，druid连接池，jsp，servlet依赖

3. 写web.xml，注册DispatcherServlet ,目的：
  1. 创建SpringMVC容器对象，才能创建Controller类对象。
  2. 创建的是Servlet，才能接受用户的请求。
  3. 注册spring的监听器：ContextLoaderListener,目的： 创建spring的容器对象，才能创建service，dao等对象。
  4. 注册字符集过滤器，解决post请求乱码的问题

4. 创建包， Controller包， service ，dao，实体类包名创建好

5. 写springmvc，spring，mybatis的配置文件
	1. springmvc配置文件
	2. spring配置文件
	3. mybatis主配置文件
	4. 数据库的属性配置文件
	
6. 写代码， dao接口和mapper文件， service和实现类，controller， 实体类。

7. 写jsp页面


配置 pom.xml

```xml
    <dependency>
      <groupId>javax.servlet</groupId>
      <artifactId>javax.servlet-api</artifactId>
      <version>3.1.0</version>
      <scope>provided</scope>
    </dependency>
    <!-- jsp依赖 -->
    <dependency>
      <groupId>javax.servlet.jsp</groupId>
      <artifactId>jsp-api</artifactId>
      <version>2.2.1-b03</version>
      <scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-webmvc</artifactId>
      <version>5.2.5.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-tx</artifactId>
      <version>5.2.5.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-jdbc</artifactId>
      <version>5.2.5.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId>
      <artifactId>jackson-core</artifactId>
      <version>2.9.0</version>
    </dependency>
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId>
      <artifactId>jackson-databind</artifactId>
      <version>2.9.0</version>
    </dependency>
    <dependency>
      <groupId>org.mybatis</groupId>
      <artifactId>mybatis-spring</artifactId>
      <version>1.3.1</version>
    </dependency>
    <dependency>
      <groupId>org.mybatis</groupId>
      <artifactId>mybatis</artifactId>
      <version>3.5.1</version>
    </dependency>
    <dependency>
      <groupId>mysql</groupId>
      <artifactId>mysql-connector-java</artifactId>
      <version>5.1.9</version>
    </dependency>
    <dependency>
      <groupId>com.alibaba</groupId>
      <artifactId>druid</artifactId>
      <version>1.1.12</version>
    </dependency>


  <build>
    <resources>
      <resource>
        <directory>src/main/java</directory><!--所在的目录-->
        <includes><!--包括目录下的.properties,.xml 文件都会扫描到-->
          <include>**/*.properties</include>
          <include>**/*.xml</include>
        </includes>
        <filtering>false</filtering>
      </resource>
    </resources>
    <plugins>
      <plugin>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.1</version>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
        </configuration>
      </plugin>
    </plugins>
  </build>
```

配置web.xml

### 整合注解开发

见文件 `Learning\JavaWeb\SpringMVC\3.SSM`

## SpringMVC核心技术

### 请求转发和重定向

![[SpringMVC.imgs/image-20210113103410547.png]]

请求转发的使用情况：因为我们已经配置了视图解析器，所以在跳转的时候我们不能直接通过 setViewName的方式跳转到view目录以外的目录，为了能够跳转到view以外的目录，我们需要用到请求转发操作。

语法：`modelAndView.setViewName("forward:完整目录")`

特点： 不和视图解析器一同使用，就当项目中没有视图解析器

```java
    @RequestMapping(value = "/addOneByOne.do", method = RequestMethod.POST)
    public ModelAndView addOneByOne(String name, int age){
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("name", name);
        modelAndView.addObject("age", age);
        modelAndView.setViewName("forward:/WEB-INF/view/show.jsp"); // 请求转发
        return modelAndView;
    }
```

处理器方法返回ModelAndView,实现重定向redirect

语法：setViewName("redirect:视图完整路径")

redirect特点：不和视图解析器一同使用，就当项目中没有视图解析器

框架对重定向的操作：

1. 框架会把Model中的简单类型的数据，转为string使用，作为hello.jsp的get请求参数使用。目的是在 doRedirect.do 和 hello.jsp 两次请求之间传递数据
2. 在目标hello.jsp页面可以使用参数集合对象 `$ {param}`获取请求参数值`  ${param.myname}`
3. 重定向不能访问/WEB-INF资源

```java
    @RequestMapping(value = "/doRedirect.do")
    public ModelAndView doWithRedirect(String name,Integer age){
        //处理some.do请求了。 相当于service调用处理完成了。
        ModelAndView mv  = new ModelAndView();
        //数据放入到 request作用域
        mv.addObject("myname",name);
        mv.addObject("myage",age);
        //重定向不能访问/WEB-INF资源
        mv.setViewName("redirect:/WEB-INF/view/show.jsp");
        return mv;
    }
```

### 异常处理

代码见`Learning\JavaWeb\SpringMVC\4.Exception`

springmvc框架采用的是统一，全局的异常处理。

把controller的所有异常处理都集中到一个地方。 采用的是aop的思想。把业务逻辑和异常处理代码分开。解耦合。

使用两个注解

1. @ExceptionHandler

2. @ControllerAdvice

异常处理步骤：

1. 新建maven web项目

2. 加入依赖

3. 新建一个自定义异常类 MyUserException , 重写前两个构造方法，即无参构造和String构造，再定义它的子类NameException , AgeException

4. 在controller抛出NameException , AgeException

5. 创建一个普通类，作用全局异常处理类 GlobalExceptionHandler
    1. 在类的上面加入@ControllerAdvice（控制器增强 - 给控制器增加异常处理功能）特点：必须让框架知道这个注解所在的包名（第7步）
    2. 在类中定义方法，方法的上面加入@ExceptionHandler

6. 创建处理异常的视图页面

7. 创建springmvc的配置文件
    1. 组件扫描器 ，扫描@Controller注解
    2. 组件扫描器，扫描@ControllerAdvice所在的包名
    3. 声明注解驱动

关键点：把异常抛出给框架，让框架集中处理这些异常。

创建相关类

```java
// UserException.java
public class UserException extends Exception {
    public UserException(){}
    public UserException(String message) {  super(message);  	}
}
//AgeException.java
public class AgeException extends UserException {
    public AgeException() {  super();   }
    public AgeException(String message) {  super(message);    }
}
//NageException.java 略
// Controller
    @RequestMapping(value = "/addObject", method = RequestMethod.POST)
    public ModelAndView addObj(Student student) throws UserException {
        ModelAndView modelAndView = new ModelAndView();
        if(student.getAge() > 100){
            throw new AgeException();
        }
        if(!student.getName().equals("zs")){
            throw new NameException();
        }
        modelAndView.addObject("name", student.getName());
        modelAndView.addObject("age", student.getAge());
        modelAndView.setViewName("show");
        return modelAndView;
    }

```

全局异常处理类

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    //定义方法，处理发生的异常
    /*
        处理异常的方法和控制器方法的定义一样， 可以有多个参数，可以有ModelAndView,
        String, void,对象类型的返回值

        形参：Exception，表示Controller中抛出的异常对象。
        通过形参可以获取发生的异常信息。

        @ExceptionHandler(异常的class)：表示异常的类型，当发生此类型异常时，
        由当前方法处理
     */
    @ExceptionHandler(value = NameException.class)
    public ModelAndView doNameException(Exception e){
        /*
           异常发生处理逻辑：
           1.需要把异常记录下来， 记录到数据库，日志文件。记录日志发生的时间，哪个方法发生的，异常错误内容。
           2.发送通知，把异常的信息通过邮件，短信，微信发送给相关人员。
           3.给用户友好的提示。
         */
        ModelAndView mv = new ModelAndView();
        mv.addObject("msg","姓名必须是zs，其它用户不能访问");
        mv.addObject("e", e);
        mv.setViewName("nameError");
        return mv;
    }
    @ExceptionHandler(value = AgeException.class)
    public ModelAndView doAgeException(Exception e){
        ModelAndView mv = new ModelAndView();
        mv.addObject("msg","年龄太大了！！！");
        mv.addObject("e", e);
        mv.setViewName("ageError");
        return mv;
    }
    @ExceptionHandler()
    public ModelAndView OtherException(Exception e){
        ModelAndView mv = new ModelAndView();
        mv.addObject("msg","其他异常");
        mv.addObject("e", e);
        mv.setViewName("Others");
        return mv;
    }
}
```

错误视图略。

配置文件的配置

```xml
<!--SpringMVC.xml-->
    <context:component-scan base-package="com.Jancoyan.Handler"/>
    <context:component-scan base-package="com.Jancoyan.Controller"/>
    <mvc:annotation-driven/>
```

### 拦截器

1. 拦截器是springmvc中的一种，需要实现HandlerInterceptor接口。
2. 拦截器和过滤器类似，功能方向侧重点不同。 过滤器是用来过滤器请求参数，设置编码字符集等工作。拦截器是拦截用户的请求，做请求做判断处理的。
3. 拦截器是全局的，可以对多个Controller做拦截。 一个项目中可以有0个或多个拦截器， 他们在一起拦截用户的请求。拦截器常用在：用户登录处理，权限检查， 记录日志。

拦截器的使用步骤：
1. 定义类实现HandlerInterceptor接口
2. 在springmvc配置文件中，声明拦截器， 让框架知道拦截器的存在。

![[SpringMVC.imgs/image-20210113155716488.png]]
实现接口：

```java
// 拦截器类，拦截用户的请求
public class MyInterceptor implements HandlerInterceptor {

    // 预处理方法，最后一个参数是被拦截的控制器对象
    // 返回值 ：请求是否通过的拦截器，true表示通过，可以执行
    // 特点：在控制器方法之前执行的，用户的请求首先到达此方法
    // 在这个方法中可以获取请求的信息， 验证请求是否符合要求。可以验证用户是否登录， 验证用户是否有权限访问某个连接地址（url）。
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        System.out.println("拦截器的MyInterceptor的preHandle()");
        return true;
    }
    
    /*
       postHandle:后处理方法。
       参数：
        Object handler：被拦截的处理器对象MyController
        ModelAndView mv:处理器方法的返回值

        特点：
         1.在处理器方法之后执行的（MyController.doSome()）
         2.能够获取到处理器方法的返回值ModelAndView,可以修改ModelAndView中的数据和视图，可以影响到最后的执行结果。
         3.主要是对原来的执行结果做二次修正，

         ModelAndView mv = MyController.doSome();
         postHandle(request,response,handler,mv);
     */
    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        System.out.println("拦截器的MyInterceptor的postHandle()");

    }

    /*
      afterCompletion:最后执行的方法
      参数
        Object handler:被拦截器的处理器对象
        Exception ex：程序中发生的异常
      特点:
       1.在请求处理完成后执行的。框架中规定是当你的视图处理完成后，对视图执行了forward。就认为请求处理完成。
       2.般做资源回收工作的， 程序请求过程中创建了一些对象，在这里可以删除，把占用的内存回收。
     */
    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        System.out.println("拦截器的MyInterceptor的afterCompletion()");
    }
}

```

修改配置文件：

```xml
    <!--声明拦截器： 拦截器可以有0或多个-->
    <mvc:interceptors>
        <!--声明第一个拦截器-->
        <mvc:interceptor>
            <!--指定拦截的请求uri地址
                path：就是uri地址，可以使用通配符 **
                      ** ： 表示任意的字符，文件或者多级目录和目录中的文件
                http://localhost:8080/myweb/user/listUser.do
                http://localhost:8080/myweb/student/addStudent.do
            -->
            <mvc:mapping path="/**"/>
            <!--声明拦截器对象-->
            <bean class="com.Jancoyan.Handler.MyInterceptor" />
        </mvc:interceptor>
    </mvc:interceptors>

```

拦截器的执行时间：

1. 在请求处理之前， 也就是controller类中的方法执行之前先被拦截。
2. 在控制器方法执行之后也会执行拦截器。
3. 在请求处理完成后也会执行拦截器。

拦截器：看做是多个Controller中公用的功能，集中到拦截器统一处理。使用的AOP的思想

多个拦截器的执行顺序：

![[SpringMVC.imgs/image-20210113155834039.png]]

```
第一个拦截器preHandle=true , 第二个拦截器preHandle=true 

111111-拦截器的MyInterceptor的preHandle()
22222-拦截器的MyInterceptor的preHandle()
=====执行MyController中的doSome方法=====
22222-拦截器的MyInterceptor的postHandle()
111111-拦截器的MyInterceptor的postHandle()
22222-拦截器的MyInterceptor的afterCompletion()
111111-拦截器的MyInterceptor的afterCompletion()

第一个拦截器preHandle=true , 第二个拦截器preHandle=false

111111-拦截器的MyInterceptor的preHandle()
22222-拦截器的MyInterceptor的preHandle()
111111-拦截器的MyInterceptor的afterCompletion()

第一个拦截器preHandle=false , 第二个拦截器preHandle=true|false

111111-拦截器的MyInterceptor的preHandle()
```

**拦截器和过滤器的区别**

1.过滤器是servlet中的对象，  拦截器是框架中的对象

2.过滤器实现Filter接口的对象， 拦截器是实现HandlerInterceptor

3.过滤器是用来设置request，response的参数，属性的，侧重对数据过滤的。  拦截器是用来验证请求的，能截断请求。

4.过滤器是在拦截器之前先执行的。

5.过滤器是tomcat服务器创建的对象, 拦截器是springmvc容器中创建的对象

6.过滤器是一个执行时间点。  拦截器有三个执行时间点

7.过滤器可以处理jsp，js，html等等,  拦截器是侧重拦截对Controller的对象。 如果你的请求不能被DispatcherServlet接收， 这个请求不会执行拦截器内容

8.拦截器拦截普通类方法执行，过滤器过滤servlet请求响应