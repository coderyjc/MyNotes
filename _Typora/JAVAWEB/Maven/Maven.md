# Maven

## 简介



是什么？Maven 是一个项目管理工具



传统的项目开发（没有使用maven）存在的问题

- 有很多模块，模块之间存在关系，手动管理关系比较繁琐
- 需要很多第三方功能，很多jar文件，需要手动从网络上获取所有的jar文件
- 需要管理jar的版本
- 需要管理jar的依赖

使用maven的优点

- 自动管理jar文件
- 自动下载jar文件和源码
- 自动管理jar的依赖和版本
- 自动编译为class
- 测试代码是否正确
- 帮你打包文件形成jar文件或者war文件
- 帮你部署项目



构建：项目的构建。

构建是面向过程的，就是一些步骤，完成项目代码的编译，测试，运行，打包，部署等等。

maven支持的构建包括有：

1. 清理，把之前项目编译的东西删除掉，为新的编译代码做准备。

2. 编译，把程序源代码编译为执行代码，java-class文件批量的，maven可以同时把成千上百的文件编译为class。javac不一样，javac一次编译一个文件。

3. 测试，maven可以执行测试程序代码，验证你的功能是否正确。批量的，maven同时执行多个测试代码，同时测试很多功能。

4. 报告，生成测试结果的文件，测试通过没有。

5. 打包，把你的项目中所有的class文件，配置文件等所有资源放到一个压缩文件中。这个压缩文件就是项目的结果文件，通常java程序，压缩文件是jar扩展名的。对于web应用，压缩文件扩展名是.war

6. 安装，把5中生成的文件war，war安装到本机仓库

7. 部著，把程序安装好可以执行。// 这个用maven比较麻烦，通常手工完成



核心概念：

1. POM。是一个文件，名称是 pom.xml，翻译过来叫做项目对项目模型，maven把一个项目当作一个模型使用，控制maven构建项目的过程，管理jar依赖。
2. 约定的目录结构。maven项目的目录和文件的位置都是规定的。
3. 坐标。是一个唯一的字符串，用来表示资源的。
4. 依赖管理。管理你的项目可以使用的jar文件。
5. 仓库管理（了解）。资源存放的位置
6. 生命周期（了解）。maven工具构建项目的过程就是生命周期。
7. 插件和目标（了解）。执行maven构建的时候用的工具就是插件。
8. 继承。
9. 聚合。



**maven的安装和配置**

下载：直接官网上下载（10M）就行

子目录介绍：

- bin：执行程序，主要是mvn.cmd
- conf：maven本身的配置文件 settings.xml

配置：

在系统的环境变量中的指定一个M2_HOME的名称，指向maven主目录

<img src="D:\GITHUB\MyNotes\_Typora\JAVAWEB\Maven\Maven.assets\image-20201003124003629.png" alt="image-20201003124003629" style="zoom:50%;" />

然后在path中加入bin目录

<img src="D:\GITHUB\MyNotes\_Typora\JAVAWEB\Maven\Maven.assets\image-20201003124039883.png" alt="image-20201003124039883" style="zoom:50%;" />

必须有JAVA_HOME环境变量

<img src="D:\GITHUB\MyNotes\_Typora\JAVAWEB\Maven\Maven.assets\image-20201003124154240.png" alt="image-20201003124154240" style="zoom:50%;" />



出现如下内容说明安装配置正确

<img src="D:\GITHUB\MyNotes\_Typora\JAVAWEB\Maven\Maven.assets\image-20201003124300534.png" alt="image-20201003124300534" style="zoom:50%;" />



## Maven核心概念

### Maven约定目录结构

每一个maven的项目在磁盘中都是一个文件夹

<img src="D:\GITHUB\MyNotes\_Typora\JAVAWEB\Maven\Maven.assets\image-20201003125645297.png" alt="image-20201003125645297" style="zoom:50%;" />

执行tree命令

<img src="D:\GITHUB\MyNotes\_Typora\JAVAWEB\Maven\Maven.assets\image-20201003141751034.png" alt="image-20201003141751034" style="zoom:50%;" />

在main\java中创建了一个package，里面写上测试代码

使用命令行 mvn compile 编译main\java中的**所有**java程序

此时会发现正在下载大量的东西，问题：为什么要下载这些东西？下载了什么？下载完成之后这些东西存到哪里了？

为什么要下载？因为maven工具的执行需要用到很多的插件（java类--jar文件）

下载什么？插件。用来完成某些功能

下载到哪里了？默认放在C盘 \ 用户 \ .m2 \ respository（本机仓库）

执行了mvn compile之后，在项目的根目录下面生成了target目录，编译生成的所有文件都在里面。



