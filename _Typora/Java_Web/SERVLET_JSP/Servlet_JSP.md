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

<img src="D:\GITHUB\MyNotes\_Typora\Java_Web\SERVLET_JSP\Servlet_JSP.imgs\image-20201231212221241.png" alt="image-20201231212221241" style="zoom:80%;" />

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

<img src="D:\GITHUB\MyNotes\_Typora\Java_Web\SERVLET_JSP\Servlet_JSP.imgs\image-20201231214534665.png" alt="image-20201231214534665" style="zoom: 67%;" />

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



详情见[ＪＤＢＣ详细笔记](../JavaSE_JDBC_JVM/JDBC.md)

## 4. MVC



