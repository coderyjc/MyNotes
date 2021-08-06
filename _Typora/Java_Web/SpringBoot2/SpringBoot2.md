## SpringBoot介绍

> 笔记来源：[千峰教育 - SpringBoot](https://www.bilibili.com/video/BV1ti4y1G7yX?p=1)

### 1.1 引言

> - 为了使用ssm框架去开发，准备ssm框架的模块配置
> - 为了spring 整合第三方框架，单独写xml配置文件
> - 导致ssm项目后期xml文件特别多，维护xml文件的成本很高
> - ssm部署也是很麻烦的，依赖第三方的容器
> - ssm开发方式很笨重

### 1.2 spring boot介绍

> SpringBoot是由Privota团队研发的，SpringBoot并不是一门技术，只是将之前常用的Spring,SpringMVC，data-jpa等常用的框架封装到了一起，并隐藏了这些框架的整合细节，实现敏捷开发
>
> Spring Boot就是一个工具类。

### 1.3 Spring Boot的特点

> 1. Spring Boot项目不需要模板化的配置
> 2. 在Spring Boot 中整合第三方的框架是，只需要导入相应的starter依赖包，就自动整合了
> 3. Spring Boot默认只有一个.properties的配置文件，不推荐使用xml,后期会采用,.java文件去编写配置信息
> 4. SpringBoot工程部署时，采用的是jar包的方式，内部自动依赖Tomcat容器，提供了多环境的配置。
> 5. 后期要学习的微服务框架Spring Cloud需要建立在Spring Boot 的基础上。

## 快速入门

### 项目搭建

![image-20210522195410527](./SpringBoot2.imgs\image-20210522195410527.png)

**选择依赖的时候选择上web**

这三个东西是可以删掉的。

![image-20210522195312814](.\SpringBoot2.imgs\image-20210522195312814.png)

![image-20210522195858611](.\SpringBoot2.imgs\image-20210522195858611.png)

![image-20210522195908996](.\SpringBoot2.imgs\image-20210522195908996.png)

### 目录介绍

1. pom.xml文件
   2. 指定了一个父工程，指定了当前工程中为springboot，帮助我们声明了starter依赖的版本
   2. 项目的元数据：包名，项目名，版本号
   3. 指定了properties信息：指定了java的版本1.8
   4. 导入依赖：默认情况下导入spring-boot-starter, spring-boot-starter-test
   5. 插件：spring-boot-maven-plugin

1. .gittignore文件：默认帮助我们忽略了一些文件和目录

1. src目录
- src
  - main
  	- java 
  		- 包名
  		- 启动类.java   # 需要将controller类，放在启动类的子类包中或者同级包下
  	- resources
  		- static   # 存放静态资源的
  		- templates  # 存储模板页面的
  		- application.porperties  # SpringBoot提供的唯一的配置文件
  - test # 测试用的

### 三种启动方式

1. 运行启动类的main方法即可运行springboot工程
2. 采用maven的命令去运行spring Boot工程  mvn spring-boot:run
3. 采用jar包的方式运行

- 将当前的项目打包成一个jar文件  mvn clean package
- 通过 java -jar jar文件

## 常用注解

### @Configuration和@Bean

之前使用ssm去开发的时候，在xml文件中编写bean标签。

但是spring boot不推荐使用xml文件

@configuration注解相当于beans标签

@Bean注解相当于bean标签

 id="方法名 | 注解中的name属性（优先级更高）"

 class="方法的放回结果"

```java
@Configuration           // 代表当前类是一个配置类
public class UserConfig {

    @Bean(name = "user1")
    public User user(){
        User user = new User();
        user.setId(1);
        user.setName("张三");
        return user;
    }

    /*
    <beans .....>  @Configuration
        @Bean
        <bean id="user1" class"com.gopan.firstspringboot.entity.User">
    </beans>
    */
}
```

### @SpringBootApplication

@SpringBootApplication是一个组合注解

1. @SpringBootConfiguration就是@Comfiguration注解，代表我的启动类就是一个配置类

1. @EnableAutoConfiguration帮你实现自动装配的，SpringBoot工程启动时，运行一个SpringFactoriesLoader的类，加载META-INF/spring.factories配置类（已经开启的），通过SpringFactoriesLoader中的load方法，以For循环的方式，一个一个地加载。

好处：无需编写大量的整合配置信息，只需要按照SpringBoot提供好了约定去整合即可。

坏处：如果导入了starter依赖，那么你就需要填写他必要的配置信息。

手动关闭自动装配指定内容

```java
@SpringBootApplication(exclude = QuartzAutoConfiguration.class)
```

1. @ComponentScan就相当于<context:component-scan basePackage="包名"/>
帮助扫描注解的

## 常用配置

### Spring Boot 的配置文件的格式

SpringBoot的配置文件支持properties和yml,甚至还支持json

更推荐使用yml文件格式：

1. yml文件 会根据换行和缩进帮助咱们管理配置文件的所在位置。

   使用properties文件配置很难管理，需要手动管理

2. yml 文件，相比于properties更轻量级一些

yml文件的劣势：

1. 严格遵循**换行**和**缩进**
2. 在填写value时，一定要在“ ：”后面跟上空格

### 多环境配置

在application.yml文件中添加一个配置项：

```yaml
spring:
 profiles:
   active: 环境名
```
在resource目录下，创建多个application-环境名.yml即可

在部署工程时，通过 java -jar 文件 - - spring.profiles.active = 环境名

举例：

![image-20210522212347297](.\SpringBoot2.imgs\image-20210522212347297.png)

### 引入外部配置文件信息

和传统的ssm的方式一样，通过@value的注解去获取properties/yml文件中的内容

如果在yml文件中需要编写大量的自定义的配置，并且具有统一的前缀时，可以采用下方方式



```java
// com.jancoyan.properties.AliyunProperties

// 这里面的 prefix 是前缀
@ConfigurationProperties(prefix = "aliyun") // 公共前缀
// 声明组件
@Component
// lombok的相关函数
@Data
public class AliyunProperties {
    // 这里面的名字应该和配置文件中的一样
    private String aaaa;
    private String bbbb;
    private String cccc;
    private String dddd;
}
```

```yaml
# application.yml
aliyun:
  aaaa: aaa
  bbbb: aaa
  cccc: ccc
  dddd: ddd
```

```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
</dependency>
```

<img src=".\SpringBoot2.imgs\image-20210522222240546.png" alt="image-20210522222240546" style="zoom: 80%;" />

### SpringBoot中的热加载（热部署）

导入依赖

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <optional>true</optional>
</dependency>
```

然后

![image-20210522222638870](.\SpringBoot2.imgs\image-20210522222638870.png)

然后重启项目

这样在build之后就会自动部署相关的文件，能避免项目的多次重启问题

**通过build重新构建工程**

![image-20210522222854339](.\SpringBoot2.imgs\image-20210522222854339.png)

## 整合MyBatis

复杂的查询不推荐用注解的方式

复杂查询和动态SQL推荐使用xml方式

SpringBoot支持使用注解和xml同时使用。

0.导入依赖

```xml
<!--        mysql驱动-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.21</version>
        </dependency>

<!--        druid和sboot整合的连接-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
            <version>1.1.10</version>
        </dependency>

        <!--        mybatis-->
        <!-- https://mvnrepository.com/artifact/org.mybatis.spring.boot/mybatis-spring-boot-starter -->
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>1.3.2</version>
        </dependency>
```

### xml方式整合

1. 编写配置文件

```java
// 1. 准备实体类

@Data
public class Air {

  private long id;

  private long districtId;

  private java.sql.Date monitorTime;

  private long pm10;

  private long pm25;

  private String monitoringStation;

  private java.sql.Date lastModifyTime;

}
// ----------------------------------------

@Data
public class District {

  private long id;

  private String name;

}
```

```java
// 2.2 准备Mapper接口
public interface AirMapper {
    List<Air> findAll();
}
// 在启动类中添加直接，扫描Mapper接口所在的包
@MapperScan(basePackages = "com.gopan.firstspringboot.mapper")
```

![image-20210522225226184](.\SpringBoot2.imgs\image-20210522225226184.png)

```xml
<!-- 2.3 准备映射文件 -->
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.gopan.firstspringboot.mapper.AirMapper">
<!--    List<Air> findAll();-->
    <select id="findAll" resultType="Air">
        select * from air
    </select>

</mapper>
```

```yaml
# 添加yml文件的配置信息
# Mybatis配置
mybatis:
  # 扫描映射的文件
  mapper-locations: classpath:mapper/*.xml
  # 配置别名扫描的包
  type-aliases-package: com.gopan.firstspringboot.entity
  configuration:
    # 开启驼峰映射
    map-underscore-to-camel-case: true
   # 2.3 指定连接数据库的信息

# 连接数据库的信息
spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql:///air?serverTimezone=UTC # mysql 8 应该在链接的时候加上时区
    username: root
    password: 123456
    type: com.alibaba.druid.pool.DruidDataSource
```

测试

![image-20210522225743071](.\SpringBoot2.imgs\image-20210522225743071.png)

<img src=".\SpringBoot2.imgs\image-20210522225842149.png" alt="image-20210522225842149" style="zoom: 67%;" />

![image-20210522230107069](.\SpringBoot2.imgs\image-20210522230107069.png)



在Mapper接口的位置，直接右键 -> goto -> Test

会自动创建当前的接口的测试类，在test目录下。

让当前的测试类，继承FirstSpringbootApplicationTests测试类（在class前添加，public）

```java
class AirMapperTest extends FirstSpringbootApplicationTests {
    @Autowired
    private AirMapper airMapper;

    @Test
    void findAll() {
        List<Air> list = airMapper.findAll();
        for (Air air : list) {
            System.out.println(air);
        }
    }
}
```

 

### 注解方式整合



创建District的Mapper接口

```java
public interface DistrictMapper {
    List<District> findAll();
}
```

添加Mybatis注解

针对增删改查：@Insert @Delete @Update @Select

还是需要在启动类中添加@MapperScan注解

```java
public interface DistrictMapper {

    @Select("select * from district")
    List<District> findAll();

    @Select("select * from district where id = #{id}")
    District findOneById(@Param("id") Integer id);
}
```

测试，看到执行的sql语句

```yaml
# 查看sql语句
logging:
  level:
    com.gopan.firstspringboot.mapper: DEBUG
```

```java
class DistrictMapperTest extends FirstSpringbootApplicationTests {

    @Autowired
    private DistrictMapper mapper;

    @Test
    void findAll() {
        List<District> list = mapper.findAll();
        for (District district : list) {
            System.out.println(district);
        }
    }

    @Test
    void findOneById() {
        District dis = mapper.findOneById(5);
        System.out.println(dis);
    }
}
```



### 整合PageHelper

导入依赖

```xml
<!-- springboot-pageHelper依赖 -->
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



测试使用

```java
@Test
public void findByPaage(){
    // 1. 执行分页
    PageHelper.startPage(1,1);

    // 2. 执行查询
    List<Air> list = airMapper.findAll();

    // 3. 封装PageInfo对象
    PageInfo<Air> pageInfo = new PageInfo<>(list);

    // 4. 输出
    for (Air air : pageInfo.getList()) {
        System.out.println(air);
    }
}
```

## 整合JSP

导入依赖

```xml
<!--        jsp核心引擎-->
        <dependency>
            <groupId>org.apache.tomcat.embed</groupId>
            <artifactId>tomcat-embed-jasper</artifactId>
        </dependency>
<!--JSTL-->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>jstl</artifactId>
        </dependency>
```

创建webapp和web-inf存放页面

![image-20210523084138269](.\SpringBoot2.imgs\image-20210523084138269.png)

配置视图解析器

![image-20210523084228494](.\SpringBoot2.imgs\image-20210523084228494.png)

![image-20210523084314258](.\SpringBoot2.imgs\image-20210523084314258.png)

