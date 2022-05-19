Web项目的创建有两种形式：

- Model
- Project

两种形式都可以。

### 下载与安装Tomcat

进入[Tomcat官网](https://tomcat.apache.org/)点击Which version

<img src="IDEA创建Web项目.imgs\image-20210303072152729.png" alt="image-20210303072152729" style="zoom:50%;" />

在这里可以看到Tomcat版本和Java版本的关系

<img src="IDEA创建Web项目.imgs\image-20210303072237806.png" alt="image-20210303072237806" style="zoom: 80%;" />

下载Tomcat 9： 点击Tomcat 9.0 ， 下载  Binary Distributions 的Core 的zip包

<img src="IDEA创建Web项目.imgs\image-20210303072303419.png" alt="image-20210303072303419" style="zoom:67%;" />

然后将下载的zip包解压出来

### Project方式创建Web项目

#### 1. 新建 Java Enterprise Project

   配置 Application Server，选择TomcatServer

<img src="IDEA创建Web项目.imgs\image-20210303071804720.png" alt="image-20210303071804720" style="zoom:50%;" />

Tomcat Home选择刚刚解压的Tomcat文件夹，下面的会自动填充

<img src="IDEA创建Web项目.imgs\image-20210303071930824.png" alt="image-20210303071930824" style="zoom:50%;" />

OK之后选择Web Application 4.0

<img src="IDEA创建Web项目.imgs\image-20210303072427076.png" alt="image-20210303072427076" style="zoom:50%;" />

然后创建好工程，可以看到这样的目录结构：

<img src="IDEA创建Web项目.imgs\image-20210303072507882.png" alt="image-20210303072507882" style="zoom: 80%;" />

#### 2. 配置Tomcat服务器

点击Add Configuration , 点击"+", 找到Tomcat Server , Local 

<img src="IDEA创建Web项目.imgs\image-20210303072656843.png" alt="image-20210303072656843" style="zoom: 80%;" />

添加Artifact

<img src="IDEA创建Web项目.imgs\image-20210303073213741.png" alt="image-20210303073213741" style="zoom:80%;" />

先点击Apply,再点击OK

<img src="IDEA创建Web项目.imgs\image-20210303073454902.png" alt="image-20210303073454902" style="zoom:80%;" />

配置完毕.

测试:

运行或者Debug: 

弹出如下浏览器窗口表示运行成功.

<img src="IDEA创建Web项目.imgs\image-20210303073719079.png" alt="image-20210303073719079" style="zoom:80%;" />

## Module方式创建Web项目

**和Projuct几乎一样**

新建一个Module

<img src="IDEA创建Web项目.imgs\image-20210303074118495.png" alt="image-20210303074118495" style="zoom:80%;" />

创建完成之后可以看到Web是以模块的形式创建好了

<img src="IDEA创建Web项目.imgs\image-20210303074153047.png" alt="image-20210303074153047" style="zoom:80%;" />

接下来的步骤和Project的第2步一模一样