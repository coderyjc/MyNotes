# SERVLET&&JSP

## 1. JSP 环境

动态网页。

区分动态和静态：动态和静态不是“会不会动”，而是是否随着时间、地点、用户操作的改变而改变

动态网页需要使用到服务端脚本语言（JSP）


架构。

BS架构：Browser Server

BS缺点：网页不美观，有时候响应比较慢

CS结构：Client Server

CS架构的缺点：

- 如果软件升级，则所有用户的软件都需要升级
- 维护麻烦：需要维护每一台客户端软件
- 每一个客户都需要安装客户端软件

注意：BS和CS各有优势

JSP是基于BS架构的。

tomcat解压后目录：

- bin:可执行文件（startup.bat    shutdown.bat）
- conf:配置文件（server.xml）
- lib：tomcat依赖的jar文件
- log:日志文件（记录出错等信息）
- temp:临时文件
- webapps：可执行的项目（将我们开发的项目 放入该目录）
- work:存放由jsp翻译成的java,以及编辑成的class文件(jsp  ->java ->class)

配置tomcat

a.配置jdk  (必须配置JAVA_HOME)  java_home  classPath  path

b.配置catalina_home  指向 tomcat根目录

检查是否配置成功：
- 双击bin/startup.bat启动tomacat，
- 常见错误： 可能与其他服务的端口号冲突
- tomcat端口号默认8080 （此端口号较为常见，容易冲突），建议修改此端口 （8888或者80）

访问本地服务器 `http://localhost:8888/`


常见状态码：

- 200：一切正常
- 300/301: 页面重定向 （跳转），3开头的

- 404:资源不存在 
- 403：权限不足 （如果访问a目录，但是a目录设置 不可见）
- 500：服务器内部错误（代码有误）

其他编码：积累



jsp：在html中嵌套的java代码 

 在项目/WEB-INF/web.xml中设置 默认的 初始页面
```html
    <welcome-file-list>
        <!-- 这里写页面的名称 -->
        <welcome-file>index.jsp</welcome-file>
    </welcome-file-list>
```

虚拟路径：服务器默认访问的项目

a.方式一

将web项目配置到 webapps以外的目录 conf/server.xml 中配置 host标签中：

```html
<!-- 严格区分大小写，并且这两个字段必须写上 -->
<!-- docBase是当项目的实际路径，path是相对webapps的路径 -->
<Context  docBase="D:\study\JspProject"  path="/JspProject"   />
```

b. 方式二

`D:\study\apache-tomcat-8.5.30\conf\Catalina\localhost`中新建   “项目名.xml”中新增一行：

```html
<Context  docBase="D:\study\JspProject"  path="/JspProject"   />
```

虚拟主机

域名解析过程

<img src="Servlet_JSP.imgs\image-20201128231321842.png" alt="image-20201128231321842" style="zoom:100%;" />

通过www.test.com访问本机



方法a. conf/server.xml

```xml
  <Engine name="Catalina" defaultHost="www.test.com">
  
	  <Host appBase="D:\study\JspProject" name="www.test.com">
			<Context docBase="D:\study\JspProject"   path="/"/>
	  </Host>
```

方法b.

在`C:\Windows\System32\drivers\etc\host`增加 127.0.0.1

www.test.com

流程：

www.test.com -> host找映射关系 -> server.xml找Engine的defaultHost ->通过"/"映射到D:\study\JspProject 为了后续学习，将以上恢复成默认

JSP执行流程

<img src="Servlet_JSP.imgs\image-20201128231352392.png" alt="image-20201128231352392" style="zoom:75%;" />

jsp- java(Servlet文件) -class  

`D:\study\apache-tomcat\work\Catalina\localhost\JspProject\org\apache\jsp`

Jsp 和Servlet 可以相互转换  

因为第一请求服务端 会有翻译 和编译的过程，因此比较慢； 后续访问 可以直接访问class,因此速度较快。但是 如果 服务端修改了代码，则再次访问时  会重新的翻译、编译。

浏览器可以直接访问 WebContent中的文件，例如http://localhost:8888/MyJspProject/index1.jsp
其中的index1.jsp就在WebContent目录中；但是WEB-INF中的文件  无法通过客户端（浏览器）直接访问，只能通过请求转发来访问

注意：并不是 任何的内部跳转都能访问WEB-INF；原因是 跳转有2种方式：请求转发 、重定向



统一字符集编码

a.编码分类：

设置jsp文件的编码（jsp文件中的pageEncoding属性）：  jsp -> java  

设置浏览器读取jsp文件的编码（jsp文件中content属性）

一般将上述设置成 一致的编码，推荐使用UTF-8

文本编码：

i.将整个项目中的文件 统一设置 （推荐）

ii.设置 某一个项目

iii.设置单独文件



JSP的页面元素： HTML  java代码（脚本Scriptlet）、指令、注释

**a.脚本Scriptlet**

```jsp
	i.    
		<%
				局部变量、java语句
		%>

	ii.
		<%!
				全局变量、定义方法
		%>
	
	iii.
	
		<%=输出表达式 %>
```

一般而言，修改web.xml、配置文件、java  需要重启tomcat服务 但是如果修改 Jsp\html\css\js ，不需要重启

注意，out.println()不能回车； 要想回车：“< br/ >”，即out.print() <%= %> 可以直接解析html代码

**b.指令**

page指令

<%@ page  ....%>

page指定的属性：

language: jsp页面使用的脚本语言

import:导入类

pageEncoding:jsp文件自身编码  jsp ->java

contentType:浏览器解析jsp的编码

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"  import="java.util.Date" %>
```

**c.注释**

```jsp
	html注释<!-- -->  ,可以被客户 通过浏览器查看源码 所观察到
	java注释//     /*...*/
	jsp注释<%-- --%>
```

JSP九大内置对象（自带的，不需要new 也能使用的对象）

- out：输出对象，向客户端输出内容
- request：请求对象；存储“客户端向服务端发送的请求信息”

    - request对象的常见方法：
    - String getParameter(String name) :根据请求的字段名key （input标签的name属性值） ，返回字段值value （input标签的value属性值）
    - String[] getParameterValues(String name): 根据请求的字段名key ，返回多个字段值value  （checkbox）
    - void setCharacterEncoding("编码格式utf-8") ：设置post方式的请求编码  （tomcat7以前默认iso-8859-1，tomcat8以后改为了utf-8）
    - getRequestDispatcher("b.jsp").forward(request,response) ;  ：请求转发 的方式跳转页面   A - > B
    - ServletContext getServerContext():获取项目的ServletContext对象
- pageContext  JSP页面容器
- session   会话对象
- appliation 全局对象
- response  响应对象
- config  配置对象（服务器配置信息）
- page   当前JSP页面对象（相当于java中的this）
- exception 异常对象



`http://localhost:8888/MyJspProject/show.jsp?uname=aa&upwd=123&uage=22&uhobbies=%E7%AF%AE%E7%90%83`

连接/文件？参数名1=参数值1 & 参数名2=参数值2 & 参数名1=参数值1 

get提交方式:  method="get" 和 地址栏 、超链接`(<a href="xx"></a>)`请求方式 默认都属于get提交方式 `<a href="#" method="get">`

get与post请求方式的区别：

a. get方式 在地址栏显示 请求信息  (但是地址栏能够容纳的 信息有限，4-5KB；如果请求数据存在大文件，图片等会出现地址栏无法容纳全部的数据而出错) ；*post不会显示*

b. 文件上传操作，必须是post

**推荐使用post**

统一请求的编码 request

get方式请求 如果出现乱码，解决方案：

a.统一每一个变量的 编码 （不推荐）

```java
	new String(  旧编码，新编码);
	name = new String(name.getBytes("iso-8859-1"),"utf-8");
```

b. 修改server.xml ，一次性的 更改tomcat默认get提交方式的编码 （utf-8） 建议 使用tomcat时， 首先在server.xml中 统一get方式的编码.. URIEncoding="UTF-8"

post 设置字符编码  request.setCharacterEncoding("utf-8") ;

## 2. Response/Cookie/Session

### 2.1 response (响应对象)

提供的方法：

- void addCookie( Cookie cookie ); 服务端向客户端增加cookie对象
- void sendRedirect(String location ) throws IOException; :页面跳转的一种方式（重定向）
- void setContetType(String type):设置服务端响应的编码（设置服务端的contentType类型）

示例：登陆

login.jsp  -> check.jsp  ->success.jsp

|			|请求转发	|		重定向|
|---------|--------|-------------|
|地址栏是否改变	|	不变(check.jsp)	|	改变(success.jsp)|
|是否保留第一次请求时的数据|		保留|			不保留|
|请求的次数		|1			|2|
|跳转发生的位置	|	服务端	|客户端发出的第二次跳转|

重定向：`response.sendRedirect("success.jsp");//页面跳转：重定向， 导致数据丢失`

请求转发：`request.getRequestDispatcher("success.jsp").forward(request, response); // 不会导致数据丢失`

请求次数的问题

<img src="Servlet_JSP.imgs\image-20201230222208422.png" alt="image-20201230222208422" style="zoom:50%;" />



转发、重定向：

转发：

张三（客户端）     ->    【 服务窗口 A （服务端 ）    ->  服务窗口B   这个过程张三是不知道的】

重定向：

张三（客户端）    -> 	服务窗口 A （服务端 ） ->去找B

张三（客户端）    -> 	服务窗口 B （服务端 ） ->结束

### 2.2 Cookie(服务端 -> 客户端)

Cookie（客户端，不是内置对象）: Cookie是由服务端生成的 ，再发送给客户端保存。相当于**本地缓存**的作用： 客户端(hello.mp4,zs/abc)->服务端(hello.mp4；zs/abc)

作用：提高访问服务端的效率，但是安全性较差。
```java
Cookie：	name = value

// Cookie 对象的方法：
javax.servlet.http.Cookie
public Cookie(String name,String value)
String getName(); // 获取name
String getValue(); // 获取value
void setMaxAge(int expiry); //设置最大有效期 （秒）
```

服务端准备Cookie：`response.addCookie(Cookie cookie)`

页面跳转（转发，重定向）

客户端获取cookie:  `request.getCookies();`

a.服务端增加cookie :response对象；客户端获取对象：request对象

b.不能直接获取某一个单独对象，只能一次性将全部的cookie拿到

通过F12可以发现  除了自己设置的Cookie对象外，还有一个name为 JSESSIONID的cookie

建议 cookie只保存  英文数字，否则需要进行编码、解码

**案例: 使用Cookie实现  记住用户名  功能**

<img src="Servlet_JSP.imgs\image-20201231212221241.png" alt="image-20201231212221241" style="zoom:80%;" />

第一次登录的时候客户端将信息发送给服务端，服务端产生Cookie，并通过重定向将其发送到客户端主机进行保存，当客户端再次登录的时候读取本地cookie进行用户名的填充

> 代码详情见: `Learning\JavaWeb\Jsp&Servlet\2.3_记住密码`

```jsp
// login.jsp

    <%!
       String uname;
    %>
    <%
        Cookie[] cookies = request.getCookies();
        for (Cookie cookie :
                cookies) {
            if (cookie.getName().equals("uname")){
                uname = cookie.getValue();
                System.out.print(uname);
            }
        }
    %>
    <form action="check.jsp" method="post">
        用户名<input type="text" name="uname" value="<%=uname == null ? "" : uname%>"> <br>
        密码 <input type="text" name="upwd"> <br>
        <input type="submit" value="登录">
    </form>


// check.jsp

<%
    request.setCharacterEncoding("utf-8") ;
    String name = request.getParameter("uname");
    String pwd = request.getParameter("upwd");

    //将用户名加入到cookie中

    Cookie cookie1 = new Cookie("uname", name);
    response.addCookie(cookie1);
    response.sendRedirect("success.jsp");
%>

// success.jsp

<font color="red"> 登录成功, 欢迎你 </font>

```


### 2.3 session(服务端)

session :会话

a.浏览网站：开始-关闭

b.购物：  浏览、付款、退出

c.电子邮件：浏览、写邮件、退出

开始-结束- 表示一段会话



session机制：

<img src="Servlet_JSP.imgs\image-20201231214534665.png" alt="image-20201231214534665" style="zoom: 67%;" />

客户端第一次请求服务端时，（jsessionid-sessionid）服务端会产生一个session对象（用于保存该客户的信息）； 并且每个session对象 都会有一个唯一的 sessionId( 用于区分其他session); 

服务端会产生一个cookie，并且该cookie的 name = JSESSIONID , value=服务端sessionId的值；

然后 服务端会在 响应客户端的同时 将该cookie发送给客户端，至此，客户端就有了一个cookie(JSESSIONID)；

因此，客户端的cookie就可以和服务端的session一一对应（JSESSIONID - sessionID）

客户端第二/n次请求服务端时:服务端会先用客户端cookie中的 JSESSIONID  去服务端的session中匹配 sessionid, 如果匹配成功（cookie  jsessionid == sesion sessionid），说明此用户不是第一次访问, 无需登录；



例子：

客户端： 顾客（客户端）

服务端: 存包处   -  商场(服务端)

顾客第一次存包：商场 判断此人是 之前已经存过包（通过你手里是否有钥匙）。 如果是新顾客（没钥匙） ，分配一个钥匙 给该顾客； 钥匙 会和 柜子 一一对应；

 第 2/n 次 存包：商场 判断此人是 之前已经存过包（通过你手里是否有钥匙）。 如果是老顾客（有钥匙），则不需要分配；该顾客手里的钥匙 会 和柜子 自动一一对应。



session总结 :

a. session存储在服务端

b. session是在 同一个用户（客户）请求时 共享

c. 实现机制：第一次客户请求时 产生一个sessionid 并复制给 cookie的jsessionid 然后发给客户端。最终通过session的sessionid 和 cookie的jsessionid 实现一一对应，并且通常来说是和一个浏览器进行对应的。



session方法：

```java
String getId() :获取sessionId  
boolean isNew() :判断是否是 新用户（第一次访问）
void invalidate():使 session 失效 （退出登录、注销）
void setAttribute();
Object getAttribute();
void setMaxInactiveInterval(秒) ：设置最大有效 非活动时间 
int getMaxInactiveInterval():获取最大有效 非活动时间 
```

示例：登录

客户端在第一次请求服务端时，如果服务端发现 此请求没有 JSESSIONID,则会创建一个 name = JSESIONID 的 cookie  并返回给客户端

> 代码详情见 `Learning\JavaWeb\Jsp&Servlet\2.3_持久登录`

```jsp
// 详情见 ：

// login.jsp

<form action="check.jsp" method="post">
        用户名<input type="text" name="uname"> <br>
        密码 <input type="text" name="upwd"> <br>
        <input type="submit" value="登录">
</form>

// check.jsp

<%
        request.setCharacterEncoding("utf-8") ;
        String name = request.getParameter("uname");
        String pwd = request.getParameter("upwd");
        if(name.equals("zs") && pwd.equals("asd")){ // 假设这时候姓名 zs 密码 asd
            // 只有登录成功的时候才会把 姓名和密码 添加到 session 里面
            session.setAttribute("uname", name);
            session.setAttribute("pwd", pwd);
            session.setMaxInactiveInterval(10);
            request.getRequestDispatcher("success.jsp").forward(request, response);
        }else{
            response.sendRedirect("login.jsp");
        }
%>

// success.jsp

<%
        String name = (String) session.getAttribute("uname");
        // 如果用户没有登录，则直接通过地址栏访问 success.jsp, 必然访问到name的值
        // 如果没有就会获取到空值 null
        if (name == null) {
            response.sendRedirect("login.jsp");
        } else {
            out.print(name);
        }
%>
```

Cookie：

a.不是内置对象，要使用必须new

b.但是，服务端会**自动**生成一个(服务端自动new一个cookie也只会new这一个Cookie) name=JSESIONID的cookie  并返回给客户端



cookie和session的区别：
| | session	 |cookie|
| --- |----- | --- |
|保存的位置|	服务端	|	客户端|
|安全性| 较安全|较不安全|
|保存的内容| Object| String|



appliation 全局对象

String getContextPath()	虚拟路径

String getRealPath(String name): 绝对路径（虚拟路径 相对的绝对路径）



四种范围对象（小->大）

| 对象名      | 说明                       | 作用范围     |
| ----------- | -------------------------- | ------------ |
| pageContext | JSP页面容器   （page对象） | 当前页面有效,页面跳转后无效 |
|request  | 请求对象		 | 同一次请求有效，请求转发后有效，重定向后无效 |
|session  | 会话对象		| 同一次会话有效，无论怎么跳转，都有效；关闭/切换浏览器后无效 ； 从 登陆->退出 之间 全部有效 |
|appliation| 全局对象		| 全局有效（整个项目有效）切换浏览器 仍然有效；关闭服务、其他项目 无效  ->  想要多个项目共享、重启后仍然有效 ：使用JNDI |



以上4个对象共有的方法：

```java
Object getAttribute(String name):根据属性名，或者属性值

void setAttribute(String name,Object obj) :设置属性值（新增，修改）

void setAttribute("a","b") ;//如果a对象之前不存在，则新建一个a对象 ；a之前已经存在，则将a的值改为b

void removeAttribute(String name)：根据属性名，删除对象
```

1.以上的4个范围对象，通过 setAttribute()复制，通过getAttribute()取值；

2.以上范围对象，**尽量使用最小的范围**。因为 对象的范围越大，造成的性能损耗越大。

## 3. JDBC

基础知识详情见[ＪＤＢＣ详细笔记](../JavaSE_JDBC_JVM/JDBC.md)

### Jsp访问数据库

```jsp
 <!-- index.jsp -->
	<form action="check.jsp">
      用户名 <input name="name" type="text" value="name"> <br>
      密码 <input name="pwd" type="password" value="pwd"> <br>
      <input type="submit" value="登录"/>
    </form>

<!-- check.jsp -->
    <%
        String uname = request.getParameter("name");
        String upassword = request.getParameter("pwd");

        Class.forName("com.mysql.jdbc.Driver");
        String url = "jdbc:mysql://localhost:3306/spring";
        String name = "root";
        String pwd = "333";

        Connection conn = null;
        PreparedStatement ps = null;

        conn = DriverManager.getConnection(url, name, pwd);
        String sql = "select * from t_user where id = ? and password = ?";
        ps = conn.prepareStatement(sql);
        ps.setString(1, uname);
        ps.setString(2, upassword);
        ResultSet resultSet = ps.executeQuery();
        if (resultSet.next()){
            out.print("登录成功");
        }else{
            out.print("登录失败");
        }
    %>
```

### JavaBean

将 jsp中 登录操作的代码  转移到了LoginDao.java；其中LoginDao类 就称之为JavaBean。

JavaBean的作用：

a.减轻的jsp复杂度 

b.提高代码复用（以后任何地方的 登录操作，都可以通过调用LoginDao实现）

JavaBean（就是一个Java类）的定义：满足一下2点 ，就可以称为JavaBean

1. public 修饰的类  ,public 无参构造
2. 所有属性(如果有) 都是private，并且提供set/get   (如果boolean 则get 可以替换成is)

使用层面，Java分为2大类：

1. 封装业务逻辑的JavaBean (LoginDao.java封装了登录逻辑)可以将jsp中的JDBC代码，封装到Login.java类中 （Login.java）
2. 封装数据的JavaBean   （实体类，Student.java  Person.java ）对应于数据库中的一张表

Login login = new Login(uname,upwd) ;//即用Login对象 封装了2个数据（用户名 和密码）

封装数据的JavaBean 对应于数据库中的一张表   (Login(name,pwd))

封装业务逻辑的JavaBean 用于操作 一个封装数据的JavaBean 

可以发现，JavaBean可以简化 代码(jsp->jsp+java)、提供代码复用(LoginDao.java)

## 4. MVC

### 介绍以及原理

M：Model 模型  ：一个功能。用JavaBean实现。

V：View 视图： 用于展示、以及与用户交互。使用html  js  css jsp jquery等前端技术实现

C：Controller 控制器 ：接受请求，将请求跳转到模型进行处理；模型处理完毕后，再将处理的结果返回给 请求处 。 可以用jsp实现，  但是一般建议使用 Servlet实现控制器。

<img src="Servlet_JSP.imgs\image-20210107173548122.png" alt="image-20210107173548122" style="zoom:50%;" />

对于MVC的理解：

<img src="Servlet_JSP.imgs\image-20210107190727777.png" alt="image-20210107190727777" style="zoom:50%;" />

Jsp->Java(Servlet)->JSP

Servlet：

Java类必须符合一定的 规范，才是一个servlet：

1. 必须继承  javax.servlet.http.HttpServlet
2. 重写其中的 doGet() **或** doPost()方法

 doGet()： 接受 并处 所有get提交方式的请求

 doPost()：接受 并处 所有post提交方式的请求



Servlet要想使用，必须配置

Serlvet2.5：web.xml

Servle3.0： @WebServlet

servlet映射关系

servlet2.5 映射关系

<img src=".\Servlet_JSP.imgs\image-20210107212542020.png" alt="image-20210107212542020" style="zoom:50%;" />

servlet3.0映射关系

<img src="Servlet_JSP.imgs\image-20210107212621395.png" alt="image-20210107212621395" style="zoom:50%;" />

项目的根目录：WebContent 、src

< a href="WelcomeServlet" >所在的jsp是在 WebContent目录中，因此 发出的请求WelcomeServlet  是去请求项目的根目录。

Servlet流程：请求 ->< url-pattern > -> 根据< servlet-mapping >中的< servlet-name > 去匹配  < servlet > 中的< servlet-name >，然后寻找到< servlet-class >，求中将请求交由该< servlet-class >执行。



纯手工方法创建第一个Servlet

步骤：

- 编写一个类，继承HttpServlet

- 重写doGet()、doPost()方法

- 编写web.xml 中的servlet映射关系

    ```xml
    <!--项目/web/WEB-INF/web.xml-->
        <servlet>
            <servlet-name>LoginServlet</servlet-name>
            <servlet-class>LoginServlet</servlet-class>
        </servlet>
    
        <servlet-mapping>
            <servlet-name>LoginServlet</servlet-name>
            <url-pattern>/src/LoginServlet</url-pattern>
        </servlet-mapping>
    ```

    ```java
    //项目/src/LoginServlet
    public class LoginServlet extends HttpServlet {
    
        @Override
        protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
            System.out.println("Hello");
        }
    
        @Override
        protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
            System.out.println("Hello");
        }
    }
    ```

    ```jsp
    <!--项目/web/index.jsp-->
        <form action="src/LoginServlet" method="post">
          用户名 <input name="name" type="text" value="name"> <br>
          密码 <input name="pwd" type="password" value="pwd"> <br>
          <input type="submit" value="登录"/>
        </form>
    ```

    

借助于Eclipse快速生成Servlet

直接新建Servlet即可！（继承、重写、web.xml  可以借助Eclipse自动生成）

Servlet3.0，与Servlet2.5的区别：

Servlet3.0不需要在web.xml中配置，但 需要在 Servlet类的定义处之上编写 注解@WebServlet("url-pattern的值") 

匹配流程：  请求地址 与@WebServlet中的值 进行匹配，如果匹配成功 ，则说明 请求的就是该注解所对应的类



项目根目录：WebContent、src（所有的构建路径）

例如：WebContent中有一个文件index.jsp  /  src中有一个Servlet.java  

如果: index.jsp中请求 < a href="abc" >... < /a > ，则 寻找范围：既会在src根目录中找  也会在WebContent根目录中找

如果：index.jsp中请求< a href="a/abc" >< /a >，寻找范围：先在src或WebContent中找a目录，然后再在a目录中找abc

web.xml中的 /:代表项目根路径  http://localhost:8888/Servlet25Project/

jsp中的/: 服务器根路径  http://localhost:8888/

构建路径、WebContent: 根目录



Servlet生命周期：5个阶段 

- 加载
- 初始化： init()  ，该方法会在 Servlet被加载并实例化的以后执行
- 服务  ：service() ->doGet()  doPost()
- 销毁  ：destroy()，  Servlet被系统回收时执行
- 卸载



init():

	a.默认第一次访问 Servlet时会被执行 （只执行这一次）
	
	b.可以修改为 Tomcat启动时自动执行
	
		i.Servlet2.5：  web.xml

```xml
<servlet>

  	<load-on-startup>1</load-on-startup>
</servlet>			
<!--其中的“1”代表第一个。-->
```

ii.Servlet3.0

```java
	@WebServlet( value="/WelcomeServlet" ,loadOnStartup=1  )
```


service() ->doGet()  doPost() ：调用几次，则执行几次

destroy()：关闭tomcat服务时，执行一次。

---

Servlet API ： 由两个软件包组成： 对应于HTTP协议的软件包、对应于除了HTTP协议以外的其他软件包

即Servlet  API可以适用于 任何 通信协议。 

我们学习的Servlet,是位于javax.servlet.http包中的类和接口，是基础HTTP协议。



Servlet继承关系

<img src="Servlet_JSP.imgs\image-20210107214739439.png" alt="image-20210107214739439" style="zoom:50%;" />

ServletConfig:接口 

ServletContext getServletContext():获取Servlet上下文对象   application

String  getInitParameter(String name):在当前Servlet范围内，获取名为name的参数值（初始化参数）



ServletContext中的常见方法(application)：

- getContextPath():相对路径

- getRealPath()：绝对路径

- setAttribute() 、getAttribute()  --->  String getInitParameter(String name); 在当前Web容器范围内，获取名为name的参数值（初始化参数）



Servlet3.0方式 给当前Servlet设置初始值：@WebServlet( .... , initParams= {@WebInitParam(name="serveltparaname30",value="servletparavalue30")   }   )

注意，此注解只 隶属于某一个具体的Servlet ，因此无法为 整个web容器设置初始化参数 （如果要通过3.0方式设置 web容器的初始化参数，仍然需要在web.xml中设置）

HttpServletRequest中的方法：(同request)，例如setAttrite()、getCookies()、getMethod()
HttpServletResponse中的方法：同response

Servlet使用层面：Eclipse中在src创建一个Servlet，然后重写doGet()  doPost()就可以  （doGet() doPost()只需要编写一个）。

### 三层架构

三层组成:

- 表示层（USL，User Show，Layer 视图层）
    - 前台：对应MVC中的View，用于和用户进行交互，界面的显示【jsp\js\html\css\jquery...】位置：web
    - 后台：对应于MVC的Controller，用于控制跳转，调用业务逻辑层【Servlet\SpringMVC】位置：xxx.servlet包内
- 业务逻辑层（BLL, Business Logic Layer，Service层）
    - 接受表示层的请求，调用
    - 组装数据访问层，逻辑性的操作（增删改查）
    - 一般位于 xxx.service 包内（xxx.manager  xx.bll）
- 数据访问层（DAL，Data Access Layer，DAO层）
    - 直接访问数据库的操作，原子性的操作【增删改查】
    - 一般位于 xxx.dao 包内

三层之间的关系示例

<img src="Servlet_JSP.imgs\image-20210108084353250.png" alt="image-20210108084353250" style="zoom: 67%;" />



三层架构和MVC的关系

<img src="Servlet_JSP.imgs\image-20210108081315318.png" alt="image-20210108081315318" style="zoom:50%;" />

jsp内置对象如何在servlet中获取？

```java
PrintWrite out = responce.getWrite(); // 获取out对象
Session session = request.getSession(); // 获取session对象
Application app = request.getServletContext(); // 获取application对象
```



<img src="Servlet_JSP.imgs\image-20210108081939431.png" alt="image-20210108081939431" style="zoom:50%;" />

### MVC优化

源码见：`Learning\JavaWeb\Jsp&Servlet`

加入接口，为service、dao加入接口

建议面向接口开发：先接口-再实现类

接口与实现类的命名规范

- 接口：interface，	起名格式： `I实体类Service` 比如`IStudentService`、	`IStudentDao`	

- 实现类：implements	起名格式  `实体类ServiceImpl` 比如`StudentServiceImpl`、`StudentDaoImpl`

- 接口所在的包：  xxx.service		xx.dao

- 实现类：起名格式：`实体类层所在包名Impl` 比如：`StudentServiceImpl`、`StudentDaoImpl`

- 实现类所在的包：xxx.service.impl  xx.dao.impl

以后使用接口/实现类时，推荐写法：

接口 x = new 实现类();

IStudentDao studentDao = new StudentDaoImpl();

DBUtil 通用的数据库帮助类，可以简化Dao层的代码量，帮助类 一般建议写在  xxx.util包

方法重构：  将多个方法 的共同代码 提炼出来，单独写在一个方法中，然后引入该方法即可


Web调试：与java代码的调试 区别：启动方式不同

index.jsp ->index_jsp.java ->index_jsp.class 

jsp->java->class
jsp翻译成的Java 以及编译后的class文件 存在于tomcat中的work目录中



**dao和DBUtil的区别：**

dao 是处理特定 类的 数据库操作类：

DBUtil是通用  数据库操作类



#### 分页

要实现分页，必须知道  某一页的 数据 从哪里开始 到哪里结束

页面大小：每页显示的数据量

假设每页显示10条数据



mysql分页：

**mysql : 从0开始计数**

分页：

第n页的数据：  第(n - 1) * 10 + 1条  -- 第n * 10条

MYSQL实现分页的sql：

limit  开始,多少条

```sql
-- 第0页
select * from student limit 0,10 ;
-- 第1页
select * from student limit 10,10 ;
-- 第2页
select * from student limit  20,10 ;
-- 第n页
select * from student limit n*10,10
```

mysql的分页语句：

select * from student limit 页数*页面大小,页面大小




oracle分页：

**sqlserver/oracle:从1开始计数**

```sql
select *from student  where sno >=(n-1)*10+1 and sno <=n*10 ; 
-- 此种写法的前提：必须是Id连续 ，否则 无法满足每页显示10条数据

select rownum,t.*from student t where rownum >=(n-1)*10+1 and rownum <=n*10  order by sno;
--1.如果根据sno排序则rownum会混乱（解决方案：分开使用->先只排序，再只查询rownum） 2.rownum不能查询>的数据 

-- ORACLE\sqlserver都是从1开始计数：  (n-1)*10+1    ---  n*10 

-- 【最终版本】优化：

select * from 
(
	select rownum r, t.* from
	(select s.* from student s order by sno asc) t 		
	where rownum<=n*10 
)
where r>=(n - 1) * 10 + 1;

-- 也就是说

select *from 
(
	select rownum r, t.* from
	(select s.* from student s order by sno asc) t 		
	where  rownum<=页数*页面大小 
)

where r >= (页数-1)*页面大小+1  ;	
```



SQLServer分页：  3种分页sql

row_number()	over(字段) ;

```sql
sqlserver2003:top  --此种分页SQL存在弊端（如果id值不连续，则不能保证每页数据量相等）

select top 页面大小 * from student where id not in 
( select top (页数-1)*页面大小 id from student  order by sno asc )


sqlserver2005之后支持：

select * from 
(
select row_number()  over (sno order by sno asc) as r, * from student
where r<=n*10 
)
where r>=(n-1) *10+1 and  ;	

-- SQLServer此种分页sql与oralce分页sql的区别： 
-- 1.rownum  ，row_number()   
-- 2.oracle需要排序（为了排序，单独写了一个子查询），但是在sqlserver 中可以省略该排序的子查询  因为sqlserver中可以通过over直接排序

-- sqlserver2012之后支持：offset fetch next only

select * from student  oreder by sno 
offset (页数-1)*页面大小+1  rows fetch next 页面大小  rows only ;
```

## 5. 上传与下载

1.上传文件

a.引入2个jar

apache: commons-fileupload.jar组件

commons-fileupload.jar依赖 commons-io.jar



b.

代码：

前台jsp：

< input type="file"  name="spicture"/ >

表单提交方式**必须为post**

在表单中必须增加一个属性 **entype="multipart/form-data"**

后台servlet：
	

注意的问题：

上传的目录  upload ：

1.如果修改代码，则在tomcat重新启动时会被删除

原因：当修改代码的时候,tomcat会重新编译一份class 并且重新部署（重新创建各种目录）
	

2.如果不修改代码，则不会删除
原因： 没有修改代码，class仍然是之前的class

因此，为了防止 上传目录丢失： a.虚拟路径	b.直接更换上传目录 到非tomcat目录

限制上传：类型、大小
注意 对文件的限制条件 写再parseRequest之前


2.下载：不需要依赖任何jar	
	a.请求（地址a  form），请求Servlet	
	b.Servlet通过文件的地址  将文件转为输入流 读到Servlet中
	c.通过输出流 将 刚才已经转为输入流的文件  输出给用户
注意：下载文件 需要设置2个 响应头：
response.addHeader("content-Type","application/octet-stream" );//MIME类型:二进制文件（任意文件）
response.addHeader("content-Disposition","attachement;filename="+fileName );//fileName包含了文件后缀：abc.txt
		
1.下载时 ，文件名乱码问题：
edge：

URLEncoder.encode(fileName,"UTF-8") 



firefox：
给文件名 加：
前缀   =?UTF-8?B?

String构造方法
Base64.encode   
后缀   ?=
示例：
	response.addHeader("content-Disposition","attachment;filename==?UTF-8?B?"+   new String(  Base64.encodeBase64(fileName.getBytes("UTF-8"))  ) +"?=" );//fileName包含了文件后缀：abc.txt
		

2

EL ：为了消除jsp中的Java代码

语法：
${EL表达式}
a.EL不需要导包
b.在el中调用属性，其实是调用的getXxx()方法

${范围.对象.属性.属性的属性 }

操作符：操作：属性，不是对象
. : 使用方便
[] : 如果是常量属性，需要使用双引号/单引号 引起来;比点操作符更加强大


[]强大之处：
a.可以容纳一些 特殊符号 （.  ?   -）
b.[]可以容纳 变量属性 （可以动态赋值）
String x = "a";
${requestScope.a}等价于${requestScope["a"]}等价于${${requestScope[x]}

c.可以处理数组
${requestScope.arr[0] }



普通对象、map中的变量


通过EL获取JSP  九大内置对象

${pageContext }
${pageContext.request }
${pageContext.sessoin }





JSTL：比EL更加强大
需要引入2个jar ：jstl.jar   standard.jar
引入tablib  :
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>    
其中prefix="c" :前缀

核心标签库：  通用标签库、条件标签库  迭代标签库

a.通用标签库
< c:set >赋值
i:
在某个作用域之中（4个范围对象），给某个变量赋值
	<%-- 
		request.setAttribute("name", "zhangsan") ;
	--%>
		<c:set var="name"    value="zhangsan"   scope="request"/>
		${requestScope.name }

<c:set var="变量名"    value="变量值"   scope="4个范围对象的作用域"/>


ii:
给普通对象赋值
在某个作用域之中（4个范围对象），给某个对象的属性复制 （此种写法，不能指定scope属性）

		<c:set target="${requestScope.student}" property="sname"  value="zxs" />

给map对象赋值
		<c:set target="${requestScope.countries}" property="cn"  value="中国" />

<c:set target="对象" property="对象的属性"  value="赋值" />
		

注意 <c:set>可以给不存在的变量赋值 （但不能给不存在的对象赋值）



<c:out>  ：显示
true:<c:out value='<a href="https://www.baidu.com">百度</a>' default="当value为空的，显示的默认值" escapeXml="true" />
false：	<c:out value='<a href="https://www.baidu.com">百度</a>' escapeXml="false" />
		


<c:remove >：删除属性
<c:remove var="a" scope="request"/>


选择：
if(boolean)
单重选择
<c:if test="" >


if else if... esle if... else  /switch

<c:choose>
	<c:when test="...">   </c:when>
	<c:when test="...">   </c:when>
	<c:when test="...">   </c:when>
	<c:otherwise>   </c:otherwise>
</c:choose>


在使用 test="" 一定要注意后面是否有空格
例如：test="${10>2 }"   true
     test="${10>2 } "  非true

循环（迭代标签库）
for(int i=0;i<5;i++)
	<c:forEach  var="name" items="${requestScope.names }" >
		-${name }-
	</c:forEach>


for(String str:names)
	<c:forEach  var="student" items="${requestScope.students }" >
		${student.sname }-${student.sno }
	
	</c:forEach>



过滤器：
实现一个Filter接口
init()、destroy() 原理、执行时机 同Servlet
配置过滤器，类似servlet
通过doFilter()处理拦截，并且通过chain.doFilter(request, response);放行


filter映射

只拦截 访问MyServlet的请求
	<url-pattern>/MyServlet</url-pattern>
拦截一切请求（每一次访问 都会被拦截）
<url-pattern>/*</url-pattern>


通配符

dispatcher请求方式：
REQUEST：拦截HTTP请求 get post
FORWARD：只拦截 通过 请求转发方式的请求

INCLUDE:只拦截拦截通过 request.getRequestDispatcher("").include()  、通过<jsp:include page="..." />此种方式发出的请求
ERROR：只拦截<error-page>发出的请求


过滤器中doFilter方法参数：ServletRequest
在Servlet中的方法参数：HttpServletRequest

过滤器链
可以配置多个过滤器，过滤器的先后顺序 是由 <filter-mapping>的位置 决定

















