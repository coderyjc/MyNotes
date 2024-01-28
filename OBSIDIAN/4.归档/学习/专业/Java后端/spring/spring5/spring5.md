
> 目前最新版本是Spring6，此版本暂且停止更新

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

### 入门案例

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

![[Spring5.imgs/image-20210104163554079.png]]

IOC过程

![[Spring5.imgs/image-20210104164919877.png]]

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

#### **基于XML注入属性**

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

#### **其他类型的XML注入**

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

#### **FactoryBean**

Spring有两种类型的bean, 一种事普通bean，另一种是工厂bean

普通bean：在配置文件中定义的bean类型就是返回类型

工厂bean：在配置文件中定义的bean类型可以和返回类型不一样，具体返回内容在接口实现中的getObject中进行定义。

```java
// MyBean.java
public class MyBean implements FactoryBean<Book> {

    @Override
    public Book getObject() throws Exception {
        Book book = new Book();
        // 设置属性
        book.setName(Collections.singletonList("<Hello>"));
        return book;
    }
    // 省略其他两个空函数
}

// bean.xml
<bean name="myBean" class="com.Jancoyan.spring.Factory.MyBean"></bean>

// test.java
ApplicationContext context = new ClassPathXmlApplicationContext("bean.xml");
Book book = context.getBean("myBean", Book.class);
```

#### **bean的作用域**

在Spring里面设置创建的bean是单实例还是多实例（默认是单实例，也就是说，每一次用bean获取实例的时候都是获取的同一个实例对象），如何设置多实例还是单实例？

- 在配置文件的bean标签中通过设置属性 scope 进行设置
    - singleton ： 默认，单实例，**加载配置文件**的时候就会加载单实例对象。
    - prototype：手动设置，多实例，在**调用getBean方法**的时候创建多实例对象。

#### **bean生命周期**

1. 通过构造器创建bean实例（无参构造）
2. 为bean的属性设置值和对其他bean的引用（调用set方法）
3. 调用bean的初始化方法（需要进行配置）
    1. 配置初始化方法：设置bean标签的init-method属性值为初始化方法名
4. bean可以使用（对象获取到了）
5. 当容器关闭的时候，调用bean的销毁方法（需要自己配置销毁方法）
    1. 配置销毁方法：设置bean标签的destory-method值为销毁方法名

加上bean的后置处理器之后，生命周期变为7步

1. 通过构造器创建bean实例（无参构造）
2. 为bean的属性设置值和对其他bean的引用（调用set方法）
3. 把bean的实例传递bean后置处理器的方法
4. 调用bean的初始化方法（需要进行配置）
    1. 配置初始化方法：设置bean标签的init-method属性值为初始化方法名
5. 把bean的实例传递bean后置处理器的方法
6. bean可以使用（对象获取到了）
7. 当容器关闭的时候，调用bean的销毁方法（需要自己配置销毁方法）
    1. 配置销毁方法：设置bean标签的destory-method值为销毁方法名

在初始化之前和之后会分别将bean传给后置处理器，后置处理器会对所有配置文件中的bean进行后置处理器的添加。

后置处理器实现：写一个类继承BeanPostProcessor 并Override里面的两个方法，然后在配置文件中写上这个类的bean，spring会自动将其识别为后置处理器（因为实现了BeanPostProcessor接口）

```java
public class MyBeanPost implements BeanPostProcessor {
    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        return bean;
    }
    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        return bean;
    }
}
```

```xml
    <bean name="myBeanPost" class="com.Jancoyan.spring.Factory.MyBean"></bean>
```

#### **xml方式的自动装配**

手动装配：在xml配置文件中bean中设置property标签，手动设置值

自动装配：根据指定的装配规则（属性名称或者属性类型），Spring自动将匹配的属性值进行注入

<mark>在实际开发中使用比较少, 不再演示</mark>

#### **引入外部属性文件（数据库配置）**

1. 直接配置数据库信息

    1. 配置德鲁伊连接池
    2. 引入德鲁伊连接池的jar包`druid.jar`

    ```xml
    <bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource">
     <property name="driverClassName" value="com.mysql.jdbc.Driver"></property>
     <property name="url"
    value="jdbc:mysql://localhost:3306/userDb"></property>
     <property name="username" value="root"></property>
     <property name="password" value="root"></property>
    </bean>
    ```

2. 引入外部属性文件配置数据库连接池

创建外部属性文件，properties文件，写数据库信息（键值对的方式写数据库信息）

把外部的properties属性文件引入到spring文件中，引入context名称空间。

```xml
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:p="http://www.springframework.org/schema/p"
 xmlns:util="http://www.springframework.org/schema/util"
 xmlns:context="http://www.springframework.org/schema/context"
 xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
 http://www.springframework.org/schema/util
http://www.springframework.org/schema/util/spring-util.xsd
 http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context.xsd">
```

然后在spring配置文件中使用标签引入外部属性文件

```xml
<!--引入外部属性文件-->
<context:property-placeholder location="classpath:jdbc.properties"/>
<!--配置连接池-->
<bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource">
 <property name="driverClassName" value="${prop.driverClass}"></property>
 <property name="url" value="${prop.url}"></property>
 <property name="username" value="${prop.userName}"></property>
 <property name="password" value="${prop.password}"></property>
</bean>
```

### 2.4 IOC 操作 Bean 管理（基于注解）

什么是注解

- 注解是代码特殊标记，格式：@注解名称(属性名称=属性值, 属性名称=属性值..) 

使用注解，注解作用在类上面，方法上面，属性上面

使用注解目的：简化 xml 配置

Spring针对Bean管理中创建对象提供注解

1. @Comment 普通的
2. @Service  建议用在业务逻辑层
3. @Controller 建议用在web层
4. @Repository 建议用在DAO层

这四个注解功能是一样的，都可以用来创建Bean实例，这是我们习惯把不同的注解用在不同的层中，以便调理清晰

#### 基于注解方式的对象的创建

步骤

1. 引入依赖 `spring-aop.jar`
2. 开启组件扫描 - 引入context名称空间

```xml
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:p="http://www.springframework.org/schema/p"
 xmlns:util="http://www.springframework.org/schema/util"
 xmlns:context="http://www.springframework.org/schema/context"
 xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
 http://www.springframework.org/schema/util
http://www.springframework.org/schema/util/spring-util.xsd
 http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context.xsd">

    <!-- 开启组件扫描
 		1 如果扫描多个包，包和包之间用逗号隔开
		2 扫描包的上层目录
	-->
<context:component-scan base-package="com.Jancoyan.spring.Factory, com.Jancoyan.spring.bean"></context:component-scan>
```

3. 创建类，在类上面添加创建对象注解

```java
// 注解里面value属性值可以不写
// 如果不写，默认值是类名称的首字母小写形式
@Component( value = "userService")
public class Book {
    private String name;
}
```

设置哪些注解进行扫描和不进行扫描：

```xml
<!--示例 1
 use-default-filters="false" 表示现在不使用默认 filter，自己配置 filter
 context:include-filter ，设置扫描哪些内容
-->
<context:component-scan base-package="com.atguigu" use-defaultfilters="false">
 <context:include-filter type="annotation"

expression="org.springframework.stereotype.Controller"/>
</context:component-scan>
<!--示例 2
 下面配置扫描包所有内容
 context:exclude-filter： 设置哪些内容不进行扫描
-->
<context:component-scan base-package="com.atguigu">
 <context:exclude-filter type="annotation"

expression="org.springframework.stereotype.Controller"/>
</context:component-scan>
```

#### 基于注解实现属性注入

1. @AutoWired：根据属性类型进行自动装配

    1. 把service和dao对象创建，在service和dao类添加创建对象注释
    2. 在service中注入dao对象，在service类添加dao类型属性，在属性上面使用注解（不需要添加set方法）

    ```java
    @Service("userService")
    public class UserService {
    	// 定义dao类型属性
        // 不需要添加set方法
        // 添加注入属性注解 autowired
        @Autowired
        private UserDao userDao;
    
        public void add() {
            System.out.println("Service add...");
            userDao.test();
        }
    }
    ```

2. @Qualifier：根据属性名称进行注入

    1. 应该和@AutoWire一起使用

    ```java
    // UserDao
    @Component("userDao_1")
    public class UserDao implements Dao {
        @Override
        public void test() {
            System.out.println("UserDao....");
        }
    }
    
    // Service
    @Component("userService")
    public class UserService {
        // 如果这个接口有多个实现类就不知道找哪个实现类
        // value值就是将这个实现类找到
        @Autowired
        @Qualifier(value = "userDao_1") // 根据名称进行注入
        private Dao userDao;
    
        public void add() {
            System.out.println("Service add...");
            userDao.test();
        }
    }
    ```

3. @Resource：可以根据类型注入，也能根据属性名称注入

    1. <mark>不建议使用</mark>
    2. 类型注入直接加@Resource
    3. 名称注入加上@Resource（name = ""） 名称写对象名

4. @Value：注入普通类型属性

    ```java
    @Service
    public class Book {
        @Value("<马保国>")
        private String name;
    }
    ```


#### 完全注解开发

1. 创建配置类，替代xml配置文件

@Configuration
@ComponentScan(basePackages = "com.Jancoyan.spring")
public class SpringConfig {
}

```java
2. 编写测试类

java
public static void main(String[] args) {
    ApplicationContext context = new
 AnnotationConfigApplicationContext(SpringConfig.class);
        UserService userService = context.getBean("userService", UserService.class);
        userService.add();
}
```

`ApplicationContext context = new
 AnnotationConfigApplicationContext(SpringConfig.class);`

## 3. AOP

#### 3.1 概念和原理

什么是 AOP ？面向切面编程（方面）

利用 AOP 可以对业务逻辑的各个部分进行隔离，从而使得 业务逻辑各部分之间的耦合度降低，提高程序的可重用性，同时提高了开发的效率。

通俗描述：不通过修改源代码方式，在主干功能里面添加新功能 

使用登录例子说明 AOP：

![[Spring5.imgs/image-20210105160436913.png]]

AOP底层使用动态代理

- 有接口情况，使用JDK动态代理
    - 创建接口实现类代理对象增强类的方法

![[Spring5.imgs/image-20210105161355902.png]]
- 没有接口情况，使用CGLIB动态代理

![[Spring5.imgs/image-20210105161457964.png]]
AOP（JDK动态代理）

<mark>可以不掌握，我们有专门的封装类</mark>

使用JDK动态代理，使用Proxy类里面的方法创建代理对象

1. 调用newProxyInstance方法，其中有三个参数；1、类加载器；2、增强方法所在的类，这个类实现的接口，支持多个接口；3、实现接口InvocationHandler，创建代理对象，写增强的方法

创建接口，定义方法

创建接口实现类，实现方法

使用Proxy类创建接口代理对象

```java
//UserDao
public interface UserDao {
    int add(int a, int b);
    void update(String id);
}
//UserDaoImpl
public class UserDaoImpl implements UserDao {
    @Override
    public int add(int a, int b) {
        return a + b;
    }

    @Override
    public void update(String id) {
        System.out.println("update...");
    }
}
//JDK动态代理
public class JDKProxy {
    public static void main(String[] args) {
        // 创建接口实现类的代理对象
        Class[] interfaces = {UserDao.class};
        UserDaoImpl userDao = new UserDaoImpl();
        UserDao dao = (UserDao) Proxy.newProxyInstance(JDKProxy.class.getClassLoader(), interfaces, new UserDaoProxy(userDao));
        int rst = dao.add(1, 4);
        System.out.println(rst);
    }
}

// 创建代理对象代码
class UserDaoProxy implements InvocationHandler{
    private Object object;
    // 1、 把创建的是谁的代理对象， 把这个“谁”传递进来
    // 有参构造传递
    public UserDaoProxy(Object obj){
        this.object = obj;
    }

    // 增强的部分
    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        //方法之前处理
        System.out.println("Pre...  当前执行的方法是" + method.getName() + " 传递的参数是..." + Arrays.toString(args));

        // 被增强的方法执行
        Object res = method.invoke(object, args);

        if(method.getName().equals("add")){
        // 如果是add方法进行怎样的处理。。。
        }else {
        }

        //方法之后处理
        System.out.println("After... " + res);

        return res;
    }
}
```

<mark>以上内容可以不掌握</mark>



Spring框架一般都是基于AspectJ实现AOP操作

什么是AspectJ？AspectJ不是Spring的组成部分，一般把AspectJ和Spring框架一起使用进行AOP操作

基于AspectJ实现AOP操作：

- 基于xml配置文件实现
- 基于注解方式实现（使用）

引入依赖： 

![[Spring5.imgs/image-20210106092108559.png]]
切入点表达式：

作用：知道对哪个类里面的哪个方法进行增强

语法：`execution([权限修饰符][返回类型][类全路径][方法名称]([参数列表]))`

例1:  com.Jancoyan.Spring.dao.UserDao里面的 add() 进行增强

`* com.Jancoyan.Spring.dao.UserDao.add(..)` * 表示所有的修饰符， .. 表示方法中的所有参数

例2: com.Jancoyan.Spring.dao.UserDao里面的 所有方法 进行增强

`* com.Jancoyan.Spring.dao.UserDao.*(..)` * 表示所有的修饰符， .. 表示方法中的所有参数

例3:  com.Jancoyan.Spring.dao里面的 所有类的 所有方法 进行增强

`* com.Jancoyan.Spring.dao.*.*(..)` * 表示所有的修饰符， .. 表示方法中的所有参数




#### 3.2 操作术语

1. 连接点：类中能被增强的方法
2. 切入点：实际被增强的方法
3. 通知（增强）：实际增强的部分
    1. 前置通知 、之前执行
    2. 后置通知 、之后执行
    3. 环绕通知 、之前和之后都执行
    4. 异常通知 、异常的时候才通知
    5. 最终通知 、类似于finally
4. 切面：是一个动作。将通知应用到切入点的过程

#### 3.3 AspectJ注解

1. 创建类，在类中创建方法

2. 创建增强类，编写增强逻辑

    1. 在增强类里面创建方法，让不同的方法代表不同的通知类型

3. 进行通知的配置

    1. 在spring配置文件中开启注解扫描

    引入名称空间context和aop

    `<context:component-scan base-package="com.Jancoyan.spring.Bean"></context:component-scan>`

    1. 使用注解创建User和UserProxy对象（@Component）
    2. 在增强类上面添加注解 @Aspect
    3. 在spring配置文件中开启生成代理对象

    `<aop:aspectj-autoproxy></aop:aspectj-autoproxy>`

4. 配置不同类型的通知
   
    1. 在增强类的里面，在作为通知方法上面添加通知类型注解，使用切入点表达式配置

```java
// User.java
@Component
public class User {
    public void add(){
        System.out.println("add....");
    }
}
// UserProxy.java
// 增强的类
@Component
@Aspect
public class UserProxy {
    // 前置通知
    @Before(value = "execution(* com.Jancoyan.spring.Bean.User.add(..))")
    public void before(){
        System.out.println("before...");
    }
}
// bean.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop.xsd
       http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">

<!--    开启注解扫描-->
    <context:component-scan base-package="com.Jancoyan.spring.Bean"></context:component-scan>
<!--    开启Aspect生成代理对象-->
    <aop:aspectj-autoproxy></aop:aspectj-autoproxy>
</beans>
// Test.java
public class Test {
    public static void main(String[] args) {
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean.xml");
        User user = context.getBean("user", User.class);
        user.add();
    }
}
```



正常情况下不同类型的通知的输出时机：

- 环绕之前
- before
- add
- 环绕之后
- after
- afterReturning

【Afterthrowing】在抛出异常之前执行

如果有了异常，则执行顺序为：

- 环绕之前
- before
- after
- afterthrowing

相同切入点的抽取：

```java
//相同切入点抽取
@Pointcut(value = "execution(* com.atguigu.spring5.aopanno.User.add(..))")
public void pointdemo() {
}
//前置通知
//@Before 注解表示作为前置通知
@Before(value = "pointdemo()")
public void before() {
	System.out.println("before.........");
}
```

一个方法的多个增强类，设置他们的优先级  - 在增强类上面添加注解 @Order(数字)  数字越小越高

```java
@Aspect
@Component
@Order(0) // 设置优先级
public class PersonProxy {
    @Before(value = "execution(* com.Jancoyan.spring.Bean.User.add(..))")
    public void before(){
        System.out.println("Person before,,,");
    }
}
```


#### 3.4 AspectJ配置文件

<mark>实际开发中少使用，作为了解即可</mark>

1、创建两个类，增强类和被增强类，创建方法

2、在 spring 配置文件中创建两个类对象

```xml
<!--创建对象-->
<bean id="book" class="com.atguigu.spring5.aopxml.Book"></bean>
<bean id="bookProxy" class="com.atguigu.spring5.aopxml.BookProxy"></bean>
```

3、在 spring 配置文件中配置切入点

```xml
<!--配置 aop 增强-->
<aop:config>
 <!--切入点-->
 <aop:pointcut id="p" expression="execution(*
com.atguigu.spring5.aopxml.Book.buy(..))"/>
 <!--配置切面-->
 <aop:aspect ref="bookProxy">
 <!--增强作用在具体的方法上-->
 <aop:before method="before" pointcut-ref="p"/>
 </aop:aspect>
</aop:config>
```

## 4. JDBC Template

### 原理和概念

什么是 JdbcTemplate ？Spring 框架对 JDBC 进行封装，使用 JdbcTemplate 方便实现对数据库操作



1. 引入相关jar包

![[Spring5.imgs/image-20210106104856037.png]]
2. 在spring配置文件中配置数据库连接池

```xml
<!-- 数据库连接池 -->
<bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource"
 destroy-method="close">
 <property name="url" value="jdbc:mysql:///user_db" />
 <property name="username" value="root" />
 <property name="password" value="root" />
 <property name="driverClassName" value="com.mysql.jdbc.Driver" />
</bean>
```

3. 配置jdbcTemplate对象，注入DataSource

```xml
<!-- JdbcTemplate 对象 -->
<bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate">
 <!--注入 dataSource-->
 <property name="dataSource" ref="dataSource"></property>
</bean>
```

4. 创建service类和dao类，在dao注入jdbcTemplate对象

```xml
<!-- 组件扫描 -->
<context:component-scan base-package="com.atguigu"></context:component-scan>
```

```java
// Service
@Service
public class BookService {
 //注入 dao
 @Autowired
 private BookDao bookDao;
}

// dao
@Repository
public class BookDaoImpl implements BookDao {
 //注入 JdbcTemplate
 @Autowired
 private JdbcTemplate jdbcTemplate;
}
```

### 单一操作

```xml
<!--bean.xml-->

<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop.xsd
       http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">

<!--   开启注解扫描-->
    <context:component-scan base-package="com.Jancoyan.spring.Bean"></context:component-scan>

<!--    数据库连接池-->
    <bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource" destroy-method="close">
        <property name="url" value="jdbc:mysql://localhost:3306/spring" />
        <property name="username" value="root" />
        <property name="password" value="333"/>
        <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
    </bean>

<!--    配置JdbcTemplate对象，注入DataSource-->
    <bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate">
        <property name="dataSource" ref="dataSource"></property>
    </bean>

<!--    组件扫描-->
    <context:component-scan base-package="com.Jancoyan.spring"></context:component-scan>


</beans>
```

#### 增删改

使用 `jdbcTemplate.update(sql, args);`

- 第一个参数：sql语句
- 第二个参数：sql语句中占位符代表的元素，类型为 Object[]

```java
//test
public class Test {
    public static void main(String[] args) {
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean.xml");
        Service service = context.getBean("service", Service.class);
        Student student = new Student();
        student.setId("123");
        student.setName("123");
        service.add(student);
        student.setName("hahaha");
        service.update(student);
        service.delete("123");        
    }
}

// service
@org.springframework.stereotype.Service
public class Service {
    @Autowired
    private BookDao bookDao;
    public void add(Student student){
        bookDao.add(student);
    }
    public void delete(String id){
        bookDao.delete(id);
    }
    public void update(Student student){
        bookDao.update(student);
    }
}

// dao

@Repository
public class BookDaoImpl implements BookDao {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    // 增加操作
    @Override
    public void add(Student student) {
        // 1.创建sql
        String sql = "insert into t_student values(?, ?)";
        // 调用方法实现
        Object[] args = {student.getId(), student.getName()};
        // 返回成功的结果数量
        int rst = jdbcTemplate.update(sql, args);
        System.out.println("增加" + rst);
    }

    // 删除操作
    @Override
    public void delete(String id) {
        String sql = "delete from t_student where id = ?";
        int rst = jdbcTemplate.update(sql, id);
        System.out.println("删除"  +  rst);
    }

    // 修改操作
    @Override
    public void update(Student student) {
        String sql = "update t_student set name = ? where id = ?";
        Object[] args = {student.getName(), student.getId()};
        int update = jdbcTemplate.update(sql, args);
        System.out.println("修改" + update);
    }
}
```

#### 返回某个值的查询

调用函数`jdbcTemplate.queryForObject(String sql,Class class)`

- 第一个参数：sql语句
- 第二个参数：返回结果的结果类

```java
    public int totalNumber(){
        String sql = "select count(*) from t_student";
        return jdbcTemplate.queryForObject(sql, Integer.class);
    }
```

#### 返回对象的查询

调用函数 `jdbcTemplate.queryForObject(String sql, new BeanPropertyRowMapper<返回类型>(返回类型Class), 参数列表)`

- 第一个参数：sql语句
- 第二个参数：new BeanPropertyRowMapper<返回类型>(返回类型的Class)
- 第三个参数：sql中的占位符，类型为 Object[]，可以没有

```java
    @Override
    public Student selectStudent(String id){
        String sql = "select * from t_student where id = ?";
        return jdbcTemplate.queryForObject(sql, new BeanPropertyRowMapper<Student>(Student.class), id);
    }
```

#### 返回集合的查询

调用函数 `jdbcTemplate.query(sql, new BeanPropertyRowMapper<Student>(Student.class),参数列表)`

- 第一个参数：sql语句
- 第二个参数：new BeanPropertyRowMapper<返回类型>(返回类型的Class)
- 第三个参数：sql中的占位符，类型为 Object[]，可以没有

```java
    @Override
    public List<Student> selectStudent(){
        String sql = "select * from t_student";
        return jdbcTemplate.query(sql, new BeanPropertyRowMapper<Student>(Student.class));
    }
```

### 批量操作

调用函数`jdbcTemplate.batchUpdate(String sql, List<Object[]> batchArgs)`

- 第一个参数为sql语句
- 第二个为sql中的参数, List\<Object\> 类型

```java
//批量添加
@Override
public void batchAddBook(List<Object[]> batchArgs) {
	String sql = "insert into t_book values(?,?,?)";
	int[] ints = jdbcTemplate.batchUpdate(sql, batchArgs);
	System.out.println(Arrays.toString(ints));
}

// 批量修改
@Override
public void batchUpdateBook(List<Object[]> batchArgs) {
	String sql = "update t_book set username=?, ustatus=? where user_id=?";
	int[] ints = jdbcTemplate.batchUpdate(sql, batchArgs);
	System.out.println(Arrays.toString(ints));
}

// 批量删除
@Override
public void batchDeleteBook(List<Object[]> batchArgs) {
	String sql = "delete from t_book where user_id=?";
	int[] ints = jdbcTemplate.batchUpdate(sql, batchArgs);
	System.out.println(Arrays.toString(ints));
}
```

## 5. Transaction Management

### 概述

web应用三层架构：web层、service层、dao层

建议将事务添加到service层中

有两种方式

- 编程式事务管理【不使用】
- 声明式事务管理【使用】
    - 基于注解方式【使用】
    - 基于xml配置文件方式

总结： 使用**注解声明式事务管理**

底层使用到了AOP

事务管理的API

- 提供一个接口事务管理器，这个接口针对不同的框架实现了不同的实现类

### 注解声明式事务管理

1. 在配置文件中配置事务管理器

```xml
<!--    创建事务管理器-->
    <bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
<!--        注入数据源-->
        <property name="dataSource" ref="dataSource"></property>
    </bean>
```

2. 在配置文件中开启事务注解

    1. 开启名称空间 `tx`

    ```xml
    <beans xmlns="http://www.springframework.org/schema/beans"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xmlns:context="http://www.springframework.org/schema/context"
     xmlns:aop="http://www.springframework.org/schema/aop"
     xmlns:tx="http://www.springframework.org/schema/tx"
     xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd
     http://www.springframework.org/schema/context
    http://www.springframework.org/schema/context/spring-context.xsd
     http://www.springframework.org/schema/aop
    http://www.springframework.org/schema/aop/spring-aop.xsd 
                         http://www.springframework.org/schema/tx
    http://www.springframework.org/schema/tx/spring-tx.xsd">
    ```

    2. 开启事务注解

    ```xml
    <!--开启事务注解-->
        <tx:annotation-driven transaction-manager="transactionManager"></tx:annotation-driven>
    ```

3. 在service类上面（获取service类的方法上面添加事务注解

    1. @Transactional 可以添加到类上或者方法上
    2. 如果添加到类上，表示类中的所有的方法添加了事务
    3. 如果添加到了方法上，表示方法添加了事务

```java
@Service
@Transactional
public class UserService {

    @Autowired
    private UserDao userDao;

    public void transfer(){
        userDao.reduceMoney();
        System.out.println(10/0); //模拟异常
        userDao.addMoney();
        System.out.println("转账成功");
    }

}
```

### 相关参数设置

在 @Transactional 中可以配置和事务相关的参数

![[Spring5.imgs/image-20210107082520535.png]]
比如:

```java
@Transactional(propagation = Propagation.REQUIRED, isolation = Isolation.DEFAULT, timeout = 10, readOnly = true, rollbackFor = Exception.class)
```

#### propagation：事务传播行为

- 多事务方法之间进行调用的时候事务如何管理

记住前两个

![[Spring5.imgs/image-20210107083445897.png]]
![[Spring5.imgs/image-20210107083102949.png]]


#### isolation：事务隔离级别

事务有特性成为隔离性，多事务操作之间不会产生影响。不考虑隔离性产生很多问题

有三个读问题：脏读、不可重复读、虚（幻）读

- 脏读：一个未提交事务读取到另一个未提交事务的数据

- 不可重复读：一个未提交事务读取到另一提交事务修改数据

- 虚读：一个未提交事务读取到另一提交事务添加数据

解决：通过设置事务隔离级别，解决读问题

![[Spring5.imgs/image-20210107083220682.png]]
#### timeout：超时时间

事务需要在一定时间内进行提交，如果不提交进行回滚

默认值是 -1 也就是不允许超时，设置时间以秒单位进行计算

#### readOnly：是否只读

读：查询操作，写：添加修改删除操作

readOnly 默认值 false，表示可以查询，可以添加修改删除操作

设置 readOnly 值是 true，设置成 true 之后，只能查询

#### rollbackFor：回滚

设置出现哪些异常进行事务回滚

#### noRoolbackFor：不回滚

设置出现哪些异常不进行事务回滚

### 完全注解开发

创建配置类，使用配置类替代xml配置文件

```java
@Configuration //配置类
@ComponentScan(basePackages = "com.Jancoyan") //组件扫描
@EnableTransactionManagement //开启事务
public class TxConfig {
    //创建数据库连接池
    @Bean
    public DruidDataSource getDruidDataSource() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName("com.mysql.jdbc.Driver");
        dataSource.setUrl("jdbc:mysql:///user_db");
        dataSource.setUsername("root");
        dataSource.setPassword("root");
        return dataSource;
    }
    //创建 JdbcTemplate 对象
    @Bean
    public JdbcTemplate getJdbcTemplate(DataSource dataSource) {
        //到 ioc 容器中根据类型找到 dataSource
        JdbcTemplate jdbcTemplate = new JdbcTemplate();
        //注入 dataSource
        jdbcTemplate.setDataSource(dataSource);
        return jdbcTemplate;
    }
    //创建事务管理器
    @Bean
    public DataSourceTransactionManager
    getDataSourceTransactionManager(DataSource dataSource) {
        DataSourceTransactionManager transactionManager = new
                DataSourceTransactionManager();
        transactionManager.setDataSource(dataSource);
        return transactionManager;
    }
}    
```

创建对象的时候使用

```java
ApplicationContext context = new AnnotationConfigApplicationContext();
```

## 6. Spring 5 new features

### 自带通用的日志封装

Spring5整合了log4j2。

![[Spring5.imgs/image-20210107141845730.png]]2. 创建log4j2.xml 配置文件，必须是这个名字，不能是别的。
3. 把下面代码复制过去

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--日志级别以及优先级排序: OFF > FATAL > ERROR > WARN > INFO > DEBUG > TRACE >
ALL -->
<!--Configuration 后面的 status 用于设置 log4j2 自身内部的信息输出，可以不设置，
当设置成 trace 时，可以看到 log4j2 内部各种详细输出-->
<configuration status="INFO">
 <!--先定义所有的 appender-->
  <appenders>
 <!--输出日志信息到控制台-->
  <console name="Console" target="SYSTEM_OUT">
 <!--控制日志输出的格式-->
    <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %-
5level %logger{36} - %msg%n"/>
   </console>
 </appenders>
 <!--然后定义 logger，只有定义 logger 并引入的 appender，appender 才会生效-->
 <!--root：用于指定项目的根日志，如果没有单独指定 Logger，则会使用 root 作为
默认的日志输出-->
   <loggers>
     <root level="info">
     <appender-ref ref="Console"/>
   </root>
 </loggers>
</configuration>
```

### @Nullable 注解

@Nullable 注解可以使用在方法上面，属性上面，参数上面，表示方法返回可以为空，属性值可以 为空，参数值可以为空

### 核心容器支持函数式编程风格

```java
//函数式风格创建对象，交给 spring 进行管理
@Test
public void testGenericApplicationContext() {
 //1 创建 GenericApplicationContext 对象
 GenericApplicationContext context = new GenericApplicationContext();
 //2 调用 context 的方法对象注册
 context.refresh();
 context.registerBean("user1",User.class,() -> new User());
 //3 获取在 spring 注册的对象
 // User user = (User)context.getBean("com.atguigu.spring5.test.User");
 User user = (User)context.getBean("user1");
 System.out.println(user);
}
```
