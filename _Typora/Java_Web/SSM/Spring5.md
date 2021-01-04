# Spring 5

## 1. Spring Concepts

### 基本概念

Spring 是轻量级的开源的 JavaEE 框架 

Spring 可以解决企业应用开发的复杂性 

Spring 有两个核心部分：IOC 和 Aop 

- IOC：控制反转，把创建对象过程交给 Spring 进行管理 

- Aop：面向切面，不修改源代码进行功能增强

Spring 特点

- 方便解耦，简化开发 
- Aop 编程支持
- 方便程序测试 
- 方便和其他框架进行整合 
- 方便进行事务操作
- 降低 API 开发难度

### 入门案例：

1. 创建普通Java工程
2. 导入Spring5相关jar包
3. 创建普通类和普通返回方法
4. 创建Spring配置文件，在配置文件里创建对象，配置文件是.xml格式

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:p="http://www.springframework.org/schema/p"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<!--配置User对象创建-->
    <bean id="user" class="com.Jancoyan.spring.User"></bean>

</beans>
```

5. 编写测试代码

## 2. IOC

### 2.1 IOC 底层原理 

#### 什么是 IOC 

（1）控制反转，把对象创建和对象之间的调用过程，交给 Spring 进行管理 

（2）使用 IOC 目的：为了耦合度降低 

（3）做入门案例就是 IOC 实现

#### 底层原理

xml解析、工厂模式、反射

工厂模式：

<img src="D:\GITHUB\MyNotes\_Typora\Java_Web\SSM\Spring5.imgs\image-20210104163554079.png" alt="image-20210104163554079" style="zoom:50%;" />

IOC过程

<img src="D:\GITHUB\MyNotes\_Typora\Java_Web\SSM\Spring5.imgs\image-20210104164919877.png" alt="image-20210104164919877" style="zoom:50%;" />

### 2.2 IOC 接口（BeanFactory）

1、IOC 思想基于 IOC 容器完成，IOC 容器底层就是对象工厂 

2、Spring 提供 IOC 容器实现两种方式：（两个接口）

1. BeanFactory：IOC 容器基本实现，是 Spring 内部的使用接口，**不提供**开发人进行使用。加载配置文件时候不会创建对象，在获取对象（使用）才去创建对象 

2. ApplicationContext：BeanFactory 接口的子接口，提供更多更强大的功能，一般由开发人 员进行使用。加载配置文件时候就会把在配置文件对象进行创建【这种方式比较好，因为在web项目中我们推荐把耗费时间和资源的操作在项目启动的时候进行处理，节约时间而不是节约空间】

### 2.3 IOC 操作 Bean 管理（基于 xml） 

Bean管理指的是两个操作 : Spring 创建对象、Spring注入属性

Bean管理操作由两种方式实现: 基于XML配置文件实现、基于注解实现

**创建对象**

```XML
// bean.xml
<!--配置User对象创建-->
<bean id="user" class="com.Jancoyan.spring.User"></bean>
```

方式：

- 在Spring配置文件中，使用bean标签，标签里面添加对应属性，就可以实现对象创建
- 在 bean 标签有很多属性，介绍常用的属性
    - id ： 唯一的标识，在获取实例的时候将id传入`User user = context.getBean("user", User.class);`
    - class ：类的全路径（也就是包的路径）
- 创建对象的时候，**默认**执行**无参构造**完成对象的创建（没有无参构造就会报错）

**基于XML注入属性**

DI：依赖注入（注入属性），需要在创建对象的基础之上完成

1. set函数进行注入

    1. 创建类，定义属性和set方法（最原始的方法，不再演示）

    2. 在 spring 配置文件配置对象创建，配置属性注入

    ```xml
    <!--配置User对象创建-->
    <bean id="user" class="com.Jancoyan.spring.User">
    <!--name 为要注入的属性名， value为属性值-->
          <property name="name" value="张三"></property>
           <property name="age" value="15"></property>
    </bean>
    ```

2. 有参构造进行注入

    1. 使用有参构造创建类（最原始的方法，不再演示）

    2. 在spring配置文件中进行配置

    ```xml
    <!--配置User对象创建-->
    <bean id="user" class="com.Jancoyan.spring.User">
    <!--name 为要注入的属性名， value为属性值-->
         <constructor-arg name="name" value="张三"></constructor-arg>
         <constructor-arg name="age" value="15"></constructor-arg>
    </bean>
    ```

**其他类型的XML注入**

1. 字面量

    1. null值

        ```xml
    <property name="name">
          <null/>
        </property>
        ```
        
    2. 属性值包含特殊符号，比如 引号

        1. 转义 `&lt;&dt`等
        2. 写道CDATA中

        ```xml
        <property name="name">
         <!--此时姓名为带引号的 “张三” -->
        <value><![CDATA["张三"]]></value>
        </property>
        ```
    
2. 注入属性 - 外部bean

    1. 直接new外部bean的对象`UserDao userDao = new UserDaoImpl();` （传统方法不再演示）
    2. 在xml文件中配置后注入（有参构造或者set）
    ```xml
    <!--定义属性、生成set方法、在配置文件中用ref把其他对象注入进来-->
    <!--    1. service和dao对象创建-->
    <bean id="userService" class="com.Jancoyan.spring.service.UserService">
<!--    2. 注入userDao对象
    name属性：类里面属性的名称
    ref属性：创建userDao对象bean标签的id值-->
        <property name="userDao" ref="userDaoImpl"></property>
    </bean>
    <bean id="userDaoImpl" class="com.Jancoyan.spring.dao.UserDaoImpl"></bean>

    ```

3. 注入属性 - 内部bean

   一对多的关系（一个部门多个员工，一个员工一个部门）

   ```xml
   <!--    内部bean-->
    <bean id="emp" class="com.Jancoyan.spring.bean.Employee">
   <!--        设置两个普通的属性-->
   <property name="name" value="lisi"></property>
   <property name="gender" value="nan"></property>
   <!--        设置对象类型属性-->
   <property name="dept">
         <bean id="dept" class="com.Jancoyan.spring.bean.Dept">
                <property name="dname" value="HR"></property>
         </bean>
   </property>
   </bean>
   ```

4. 注入属性 - 级联bean

	使用ref属性关联外部的bean
	```xml
<!--    级联bean-->
   <bean id="emp" class="com.Jancoyan.spring.bean.Employee">
<!--        设置两个普通的属性-->
   <property name="name" value="lisi"></property>
   <property name="gender" value="nan"></property>
<!--        设置对象类型属性-->
   <property name="dept" ref="dept"></property>
   </bean>
   <bean id="dept" class="com.Jancoyan.spring.bean.Dept">
        <property name="dname" value="HR"></property>
   </bean>
   ```

5. IOC操作Bean管理，xml注入集合属性

第一种方法都是直接用set方法进行赋值，不再演示，以下是xml配置属性
	
```xml
    <bean id="stu" class="com.Jancoyan.spring.sets.Stu">
<!--数组类型属性注入-->
        <property name="courses">
            <array>
                <value>Java</value>
                <value>Oracle</value>
            </array>
        </property>
<!--list 类型注入-->
        <property name="list">
            <list>
                <value>张三</value>
                <value>小三子</value>
            </list>
        </property>
<!--map类型注入-->
        <property name="map">
            <map>
                <entry key="Java" value="java"></entry>
                <entry key="MySQL" value="mysql"></entry>
            </map>
        </property>
<!--set类型注入-->
        <property name="set">
            <set>
                <value>Java</value>
                <value>Python</value>
            </set>
        </property>
    </bean>
```

提出问题: 

- 能不能在集合中使用引用类型? --在集合中设置对象类型的值

- 能不能引用公共的集合，使得多个类都可以引用这个集合对象？ -- 把集合注入部分提取出来

6. 在集合中设置对象类型的值

```xml

    <bean id="stu" class="com.Jancoyan.spring.sets.Stu">
<!--list 类型注入-->
        <property name="list">
            <list>
                <ref bean="java"></ref>
                <ref bean="python"></ref>
            </list>
        </property>
    </bean>

<!--事先声明两个Course类-->
    <bean id="java" class="com.Jancoyan.spring.sets.Course">
        <property name="name" value="JAVA"></property>
        <property name="id" value="1"></property>
    </bean>
    <bean id="python" class="com.Jancoyan.spring.sets.Course">
        <property name="name" value="PYTHON"></property>
        <property name="id" value="2"></property>
    </bean>
```

7. 提取集合注入部分

首先修改beans标签

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:p="http://www.springframework.org/schema/p"
       xmlns:util="http://www.springframework.org/schema/util"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
 http://www.springframework.org/schema/util
http://www.springframework.org/schema/util/spring-util.xsd">
```

配置文件配置方式：

先用util相关标签设置属性， 再用ref进行引用

```xml
    <util:list id="bookList">
        <value>斗罗大陆</value>
        <value>斗破苍穹</value>
    </util:list>

    <bean name="book" class="com.Jancoyan.spring.bean.Book">
        <property name="name" ref="bookList"></property>
    </bean>
```



### 2.4 IOC 操作 Bean 管理（基于注解）



## 3. AOP





## 4. JDBC Template





## 5. Transaction Management





## 6. Spring 5 new features

