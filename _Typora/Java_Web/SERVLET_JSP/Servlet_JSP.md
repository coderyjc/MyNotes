## JSP


### JSP 环境

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

a.配置jdk  (必须配置JAVA_HOME)
java_home  classPath  path

b.配置catalina_home  指向 tomcat根目录

检查是否配置成功：
- 双击bin/startup.bat启动tomacat，
- 常见错误： 可能与其他服务的端口号冲突
- tomcat端口号默认8080 （此端口号较为常见，容易冲突），建议修改此端口 （8888或者80）
 
访问本地服务器 `http://localhost:8888/`


常见状态码：

- 200：一切正常
- 300/301: 页面重定向 （跳转）

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
将web项目配置到 webapps以外的目录
conf/server.xml中配置 host标签中：
```html
<!-- 严格区分大小写，并且这两个字段必须写上 -->
<!-- docBase是当项目的实际路径，path是相对webapps的路径 -->
<Context  docBase="D:\study\JspProject"  path="/JspProject"   />
```

b.方式二
D:\study\apache-tomcat-8.5.30\conf\Catalina\localhost
中新建   “项目名.xml”中新增一行：
```html
<Context  docBase="D:\study\JspProject"  path="/JspProject"   />
```

虚拟主机

通过www.test.com访问本机
方法a. conf/server.xml

```xml
  <Engine name="Catalina" defaultHost="www.test.com">
  
	  <Host appBase="D:\study\JspProject" name="www.test.com">
			<Context docBase="D:\study\JspProject"   path="/"/>
	  </Host>
```

方法b.C:\Windows\System32\drivers\etc\host
增加
127.0.0.1       www.test.com


流程：
www.test.com -> host找映射关系 ->server.xml找Engine的defaultHost ->通过"/"映射到D:\study\JspProject
为了后续学习，将以上恢复成默认


JSP执行流程
jsp- java(Servlet文件) -class
D:\study\apache-tomcat-8.5.30\work\Catalina\localhost\JspProject\org\apache\jsp

Jsp 和Servlet 可以相互转换  

因为第一请求服务端 会有翻译 和编译的过程，因此比较慢； 后续访问 可以直接访问class,因此速度较快。但是 如果 服务端修改了代码，则再次访问时  会重新的翻译、编译。

