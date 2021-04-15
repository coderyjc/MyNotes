# SSM整合开发流程框架搭建

> 参考来源: [bilibili - 尚硅谷SSM综合开发项目](https://www.bilibili.com/video/BV17W411g7zP?p=1)

> 说明：
>
> 这是我学习 [bilibili - 尚硅谷SSM综合开发项目](https://www.bilibili.com/video/BV17W411g7zP?p=1) 之后的框架搭建总结报告



[TOC]



## 简介

SSM： SpringMVC + Spring + MyBatis.

SpringMVC: 视图层，也就是界面层，负责接收请求，显示处理结果。

Spring：业务层，管理service，dao，工具类对象的。

MyBatis：持久层， 用来访问数据库

目录结构：

src
    └─main -- Maven主目录
        ├─java
        │  └─com
        │      └─Jancoyan
        │          ├─controller -- 控制器
        │          ├─dao -- DAO接口，负责与数据库的沟通
        │          ├─domain -- 实体类，POJO类所在目录
        │          ├─service  -- 服务类
        │          ├─test -- 测试类，用来测试模块
        │          └─utils -- 工具类，减少代码的重复
        ├─resources
        │  ├─mapper -- MyBatis映射文件
        |  ├─applicationContext.xml -- Spring 配置文件
        |  ├─mybatis.xml -- MyBatis配置文件
        |  └─jdbc.properties -- 数据库连接配置文件
        └─webapp
        |  ├─index.jsp -- 默认访问文件
        |  ├─static -- 存放静态资源比如jQuery.js
        |  └─WEB-INF
        |      ├─views -- 视图文件夹
        |      ├─dispatcherServlet-servlet.xml -- SpringMVC配置文件
        |      └─web.xml -- web项目配置文件
        └─pom.xml -- maven配置文件

## 配置文件

### pom.xml

依赖：

- 分页插件pagehelper
- mybatis逆向工程的mbg
- JSR303数据校验
- jackson
- c3p0连接池
- ssm基础依赖

```xml
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>org.example</groupId>
  <artifactId>ssm</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>war</packaging>


  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
  </properties>

  <!--引入项目依赖的jar包 -->
  <!-- SpringMVC、Spring -->
  <!-- https://mvnrepository.com/artifact/org.springframework/spring-webmvc -->
  <dependencies>

    <!--引入pageHelper分页插件 -->
    <dependency>
      <groupId>com.github.pagehelper</groupId>
      <artifactId>pagehelper</artifactId>
      <version>5.0.0</version>
    </dependency>

    <!-- MBG -->
    <!-- https://mvnrepository.com/artifact/org.mybatis.generator/mybatis-generator-core -->
    <dependency>
      <groupId>org.mybatis.generator</groupId>
      <artifactId>mybatis-generator-core</artifactId>
      <version>1.3.5</version>
    </dependency>

    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-webmvc</artifactId>
      <version>4.3.7.RELEASE</version>
    </dependency>

    <!-- 返回json字符串的支持 -->
    <!-- https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind -->
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId>
      <artifactId>jackson-databind</artifactId>
      <version>2.8.8</version>
    </dependency>

    <!--JSR303数据校验支持；tomcat7及以上的服务器，
    tomcat7以下的服务器：el表达式。额外给服务器的lib包中替换新的标准的el
    -->
    <!-- https://mvnrepository.com/artifact/org.hibernate/hibernate-validator -->
    <dependency>
      <groupId>org.hibernate</groupId>
      <artifactId>hibernate-validator</artifactId>
      <version>5.4.1.Final</version>
    </dependency>


    <!-- Spring-Jdbc -->
    <!-- https://mvnrepository.com/artifact/org.springframework/spring-jdbc -->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-jdbc</artifactId>
      <version>4.3.7.RELEASE</version>
    </dependency>

    <!--Spring-test -->
    <!-- https://mvnrepository.com/artifact/org.springframework/spring-test -->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-test</artifactId>
      <version>4.3.7.RELEASE</version>
    </dependency>


    <!-- Spring面向切面编程 -->
    <!-- https://mvnrepository.com/artifact/org.springframework/spring-aspects -->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-aspects</artifactId>
      <version>4.3.7.RELEASE</version>
    </dependency>

    <!--MyBatis -->
    <!-- https://mvnrepository.com/artifact/org.mybatis/mybatis -->
    <dependency>
      <groupId>org.mybatis</groupId>
      <artifactId>mybatis</artifactId>
      <version>3.4.2</version>
    </dependency>
    <!-- MyBatis整合Spring的适配包 -->
    <!-- https://mvnrepository.com/artifact/org.mybatis/mybatis-spring -->
    <dependency>
      <groupId>org.mybatis</groupId>
      <artifactId>mybatis-spring</artifactId>
      <version>1.3.1</version>
    </dependency>

    <!-- 数据库连接池、驱动 -->
    <!-- https://mvnrepository.com/artifact/c3p0/c3p0 -->
    <dependency>
      <groupId>c3p0</groupId>
      <artifactId>c3p0</artifactId>
      <version>0.9.1</version>
    </dependency>
    <!-- https://mvnrepository.com/artifact/mysql/mysql-connector-java -->
    <dependency>
      <groupId>mysql</groupId>
      <artifactId>mysql-connector-java</artifactId>
      <version>5.1.41</version>
    </dependency>
    <!-- （jstl，servlet-api，junit） -->
    <!-- https://mvnrepository.com/artifact/jstl/jstl -->
    <dependency>
      <groupId>jstl</groupId>
      <artifactId>jstl</artifactId>
      <version>1.2</version>
    </dependency>

    <!-- https://mvnrepository.com/artifact/javax.servlet/javax.servlet-api -->
    <dependency>
      <groupId>javax.servlet</groupId>
      <artifactId>javax.servlet-api</artifactId>
      <version>3.0.1</version>
      <scope>provided</scope>
    </dependency>

    <!-- junit -->
    <!-- https://mvnrepository.com/artifact/junit/junit -->
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.12</version>
    </dependency>
  </dependencies>

  <build>
    <resources>
      <resource>
        <directory>src/main/java</directory>
        <includes>
          <include>**/*.properties</include>
          <include>**/*.xml</include>
        </includes>
      </resource>
      <resource>
        <directory>src/main/resources</directory>
        <includes>
          <include>**/*.xml</include>
          <include>**/*.properties</include>
        </includes>
      </resource>
    </resources>

    <plugins>
      <plugin>
        <artifactId>maven-war-plugin</artifactId>
        <version>2.6</version>
        <configuration>
          <includeEmptyDirectories>true</includeEmptyDirectories>
        </configuration>
      </plugin>
    </plugins>

  </build>
</project>

```





### applicationContext.xml



```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:aop="http://www.springframework.org/schema/aop" xmlns:tx="http://www.springframework.org/schema/tx"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop.xsd http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx.xsd">

<!--    这里配置业务逻辑-->

<!--    配置组件扫描，扫描的包为Controller包下的所有类-->
    <context:component-scan base-package="com.Jancoyan">
        <context:exclude-filter type="annotation" expression="org.springframework.stereotype.Controller"/>
    </context:component-scan>

<!--    配置数据库连接池，这里使用的时c3p0连接池， 从resources目录下的jdbc.properties中读取数据库的配置文件-->
    <context:property-placeholder location="classpath:jdbc.properties" />
    <bean id="pooledDataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
        <property name="jdbcUrl" value="${jdbc.url}"></property>
        <property name="user" value="${jdbc.user}"></property>
        <property name="password" value="${jdbc.password}"></property>
        <property name="driverClass" value="${jdbc.driver}"></property>
    </bean>

<!--    Mybatis 整合=============================================================-->
<!--    自动注入SqlSessioFactory-->
    <bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
        <property name="configLocation" value="classpath:mybatis.xml"></property>
        <property name="dataSource" ref="pooledDataSource"></property>
        <property name="mapperLocations" value="classpath:mapper/*.xml"></property>
    </bean>

<!--    配置扫描器，将mybatis的接口实现加入ioc-->
    <bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
<!--        扫描所有的ioc实现，加入到ioc容器中-->
        <property name="basePackage" value="com.Jancoyan.dao"></property>
    </bean>

<!--    配置可以执行批量操作的SQLSession-->
    <bean class="org.mybatis.spring.SqlSessionTemplate" id="sqlSession">
        <constructor-arg name="sqlSessionFactory" ref="sqlSessionFactory"></constructor-arg>
<!--        BATCH批量执行-->
        <constructor-arg name="executorType" value="BATCH"></constructor-arg>
    </bean>

<!-- 配置事务管理======================================-->
<!--    事务管理器-->
    <bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
<!--        控制数据管理源-->
        <property name="dataSource" ref="pooledDataSource"></property>
    </bean>

<!--    开启基于注解的事务管理-->
    <aop:config>
<!--        切入点表达式-->
        <aop:pointcut id="txPoint" expression="execution(* com.Jancoyan.service..*(..))"/>
<!--        配置事务增强-->
        <aop:advisor advice-ref="txAdvice" pointcut-ref="txPoint"/>
    </aop:config>

<!-- 配置事务增强, 事务如何切入-->
    <tx:advice id="txAdvice">
        <tx:attributes>
<!--            所有方法都事务方法-->
            <tx:method name="*"/>
<!--            get开始的所有方法-->
            <tx:method name="get*" read-only="true"/>
        </tx:attributes>
    </tx:advice>

<!--    spring 的核心点: 数据源,与 mybatis 的整合-->
</beans>
```



### mybatis.xml 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
<!--  数据库字段映射为驼峰式字段-->
    <settings>
        <setting name="mapUnderscoreToCamelCase" value="true"/>
    </settings>

<!--配置类的别名-->
    <typeAliases>
        <package name="com.Jancoyan.domain"/>
    </typeAliases>

<!--    配置分页文件PageHelper-->
    <plugins>
        <plugin interceptor="com.github.pagehelper.PageInterceptor">
            <property name="reasonable" value="true"/>
        </plugin>
    </plugins>
</configuration>
```



### dispatcherServlet-servlet.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:mvc="http://www.springframework.org/schema/mvc"
       xsi:schemaLocation="http://www.springframework.org/schema/mvc http://www.springframework.org/schema/mvc/spring-mvc-4.3.xsd
		http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-3.2.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">

    <!--SpringMVC的配置文件，包含网站跳转逻辑的控制，配置  -->
    <context:component-scan base-package="com.Jancoyan" use-default-filters="false">
        <!--只扫描控制器。  -->
        <context:include-filter type="annotation" expression="org.springframework.stereotype.Controller"/>
    </context:component-scan>

    <!--配置视图解析器，方便页面返回  -->
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/views/"></property>
        <property name="suffix" value=".jsp"></property>
    </bean>

    <!--两个标准配置  -->
    <!-- 将springmvc不能处理的请求交给tomcat -->
    <mvc:default-servlet-handler/>
    <!-- 能支持springmvc更高级的一些功能，JSR303校验，快捷的ajax...映射动态请求 -->
    <mvc:annotation-driven/>

</beans>
```



## 其他



![image-20210408184043139](R:\GITHUB\MyNotes\_Typora\_Docs\SSM开发流程.imgs\image-20210408184043139.png)