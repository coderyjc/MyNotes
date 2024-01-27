```ad-note
<u>参考</u>了 [bilibili -【尚硅谷】IDEA2022全新版教程，兼容JDK17（快速上手Java开发利器）](https://www.bilibili.com/video/BV1CK411d7aA)

并非直接CV，而是手动复现了所有的操作，并在其基础上进行了**补充和改写**。

```

#软件/IDEA

> 主要内容包括：安装与卸载、运行程序、jdk配置、编辑器设置、工程管理、代码模版使用、快捷键、调试、工程管理、数据库相关内容。
>
> IDEA插件会单独开一个栏目。

# IDEA使用教程

## 卸载和安装

### 卸载

0. 保存配置文件。（可选）

配置文件：IDEA文件根目录的 `IDEA\bin\IdeaConfig\config\options`

插件：IDEA文件根目录的 `IDEA\bin\IdeaConfig\config\plugins`

或者直接从IDEA中导出：

![image-20221130211059399](assets/image-20221130211059399.png)

直接从IDEA导出可以选择更多的选项。

1. 卸载软件。

**如果下载的是免安装版本，则不会显示在电脑系统的“应用程序”中，这时候直接删除整个文件夹即可。**

如果下载的是安装版，则直接从控制面板-卸载程序即可。

![image-20221130211703333](assets/image-20221130211703333.png)

2. 删除残留配置文件

`C:\Users\{电脑用户名}\AppData\Local\JetBrains`

`C:\Users\{电脑用户名}\AppData\Roaming\JetBrains`

### 安装

官方网站：https://www.jetbrains.com/zh-cn/idea/download/

破解办法自行百度，或者下载社区版，支持正版，人人有责。

IDEA 分为两个版本： 旗舰版(Ultimate) 和 社区版(Community) 。

IDEA的大版本每年迭代一次，大版本下的小版本（如：2022.x）迭代时间不固定，一般每年3-4个小版本，目前最新的版本是2022.4。

---

安装步骤：

1. 欢迎界面

![image-20221130212440314](assets/image-20221130212440314.png)

2. 选择路径

![image-20221130212550093](assets/image-20221130212550093.png)

3. 选项

![image-20221130212747408](assets/image-20221130212747408.png)

按照自己的喜好选择，一般来说选择添加到PATH

4. 开始菜单中创建的文件夹的名称为JetBrains，就是下图

![image-20221130213046789](assets/image-20221130213046789.png)

5. 开始安装，安装完成

![image-20221130213022978](assets/image-20221130213022978.png)

---

第一次使用：

是否发送数据？默认选不发送

![image-20221130213216287](assets/image-20221130213216287.png)

是否导入原来的配置文件？

如果在以前导出了相关的配置文件，则可以在这里导入。一般名为`settings.zip`

![image-20221130213312661](assets/image-20221130213312661.png)

这里为了演示，我就不导入了。

然后就ok了。

> 激活问题请自己解决。

### 一些问题

问题描述1：2022.1启动不了，双击桌面图标，没有响应。

问题描述2：进入到安装目录...\IntelliJ IDEA 2022.1.2\bin，打开CMD。输入idea，发现报错。

解决办法：

打开`C:\Users\｛用户名｝\AppData\Roaming\JetBrains\IntelliJIdea2022.1\idea64.exe.vmoptions`这个文件。

删除最后一行以`-javaagent`开头的一行配置

原因：之前使用过的比如2021.2.2版本，是破解版。新版IEDA把现有的启运参数也都复制过去了。又因为最新的IDEA，不兼容pojie程序-javaagent:D:\develop_tools\IDEA\IntelliJ IDEA 2021.2.2\bin\jetbrains-agent.jar了，所以报错了，所以JVM结束了，所以没有启动画面。

## 示例程序

### 新建工程

![image-20221130215144461](assets/image-20221130215144461.png)



![image-20221130215556659](assets/image-20221130215556659.png)

项目创建完成，开始创建java文件

![image-20221130215702493](assets/image-20221130215702493.png)

![image-20221130215733733](assets/image-20221130215733733.png)



### 编写代码

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```


### 运行

因为在创建项目的时候已经设置了jdk了，因此不用再重复设置了。

可以点击方法旁边的运行，来运行项目

![image-20221130215923390](assets/image-20221130215923390.png)

也可以点击工具栏中的运行。

![image-20221130215939214](assets/image-20221130215939214.png)



## JDK相关设置

查看项目的jdk

![image-20221130220033129](assets/image-20221130220033129.png)

![image-20221130220112858](assets/image-20221130220112858.png)

Language level 语言级别是什么：

我们可以使用高版本的jdk，但是使用低版本的语言规范，这个时候虽然使用了新版本的jdk，但是无法使用新版本的语法特性。这个语言级别就是语言规范。

## 详细设置

显示工具栏

![image-20221201104442153](assets/image-20221201104442153.png)

打开详细配置

![image-20221201104500251](assets/image-20221201104500251.png)

详细配置设置

![image-20221201104636721](assets/image-20221201104636721.png)

### 系统设置

#### 默认启动项配置

![image-20221201104846063](assets/image-20221201104846063.png)

如果去掉Reopen last project on startup前面的对勾，每次启动IDEA就会出现如下界面

![image-20221201104945855](assets/image-20221201104945855.png)

#### 取消自动更新

Settings-->Appearance & Behavior->System Settings -> Updates

![image-20221201105102710](assets/image-20221201105102710.png)

建议检查IDE更新的√去掉

检查插件更新的√选上

### 主题设置

**整体主题**

![image-20221201105303600](assets/image-20221201105303600.png)

默认提供4个主题：2白1黑1高对比度。

**菜单和窗口字体大小**

![image-20221201105455046](assets/image-20221201105455046.png)

![image-20221201105557255](assets/image-20221201105557255.png)



**设置背景图**

![image-20221201105912758](assets/image-20221201105912758.png)

效果：

![image-20221201105931374](assets/image-20221201105931374.png)

### 编辑器字体设置

#### 编辑器主题设置

![image-20221201110550838](assets/image-20221201110550838.png)



#### 字体大小

![image-20221201111030533](assets/image-20221201111030533.png)

![image-20221201110913046](assets/image-20221201110913046.png)

#### 详细字体设置：以注释为例

![image-20221201111240818](assets/image-20221201111240818.png)



### 行号和方法分隔符

![image-20221201111409015](assets/image-20221201111409015.png)

![image-20221201111444183](assets/image-20221201111444183.png)

### 代码提示

![image-20221201164053546](assets/image-20221201164053546.png)



### 自动导包

默认需要自己手动导包，Alt+Enter快捷键

![image-20221201164245625](assets/image-20221201164245625.png)

![image-20221201164444787](assets/image-20221201164444787.png)



### 字符编码（全都改成UTF-8）

![image-20221201164554131](assets/image-20221201164554131.png)

![image-20221201164637002](assets/image-20221201164637002.png)

> 字符编码也可以针对文件设置，也是这个步骤，当导入了外部的Java文件，而文件产生了乱码的时候，可以按照这个步骤进行修改。

### 类的头部注释信息

![image-20221201164903582](assets/image-20221201164903582.png)

```java
/**
* ClassName: ${NAME}
* Package: ${PACKAGE_NAME}
* Description: 
* @Author Yan Jingcun
* @Create ${DATE} ${TIME} 
* @Version 1.0   
*/
```

常用的预设变量：

```
${PACKAGE_NAME} - the name of the target package where the new class or interface will 
be created. 
${PROJECT_NAME} - the name of the current project. 
${FILE_NAME} - the name of the PHP file that will be created. 
${NAME} - the name of the new file which you specify in the New File dialog box during 
the file creation. 
${USER} - the login name of the current user. 
${DATE} - the current system date.
${TIME} - the current system time. 
${YEAR} - the current year. 
${MONTH} - the current month. 
${DAY} - the current day of the month. 
${HOUR} - the current hour. 
${MINUTE} - the current minute. 
${PRODUCT_NAME} - the name of the IDE in which the file will be created. 
${MONTH_NAME_SHORT} - the first 3 letters of the month name. Example: Jan, Feb, etc. 
${MONTH_NAME_FULL} - full name of a month. Example: January, February, etc.
```



### 自动编译

![image-20221201165040509](assets/image-20221201165040509.png)



### 省电模式

![image-20221201165108344](assets/image-20221201165108344.png)



### 取消双击shift搜索

![image-20221201165238821](assets/image-20221201165238821.png)



### 其他

是否在单行显式编辑器选项卡（建议去掉勾选）

![image-20221201165514155](assets/image-20221201165514155.png)



## 工程和模块管理

### 项目结构

Project - Module — Package — Class

也就是说：

- 一个project中可以创建多个module
- 一个module中可以创建多个package
- 一个package中可以创建多个class

![image-20221201165616453](assets/image-20221201165616453.png)

在 IntelliJ IDEA 中Project是最顶级的结构单元，然后就是Module。目前，主流的大型项目结构基本都是多Module的结构，这类项目一般是按功能划分的，比如：user-core-module、user-facade-module和user-hessian-module等等，模块之间彼此可以相互依赖，有着不可分割的业务关系。因此，对于一个Project来说：

- 当为单Module项目的时候，这个单独的Module实际上就是一个Project。
- 当为多Module项目的时候，多个模块处于同一个Project之中，此时彼此之间具有互相依赖的关联关系。
- 当然多个模块没有建立依赖关系的话，也可以作为单独一个“小项目”运行。

### 创建模块

建议创建“Empty空工程”，然后创建多模块，每一个模块可以独立运行，相当于一个小项目。

1. 先创建空工程

![image-20221201171316110](assets/image-20221201171316110.png)

2. 创建模块

![image-20221201171650971](assets/image-20221201171650971.png)

![image-20221201171737755](assets/image-20221201171737755.png)

### 删除模块

![image-20221201171849880](assets/image-20221201171849880.png)

移出之后是在本项目中删除了这个项目

但是这个文件夹还在

因此还要把这个文件夹删除

![image-20221201171948501](assets/image-20221201171948501.png)

### 导入其他外部模块

直接复制的时候不会被IDEA标志为本项目的模块，而是以文件夹的形式呈现。

![image-20221201172228830](assets/image-20221201172228830.png)

应该在Project Structure中导入

![image-20221201172528383](assets/image-20221201172528383.png)

![image-20221201172331694](assets/image-20221201172331694.png)

![image-20221201172406695](assets/image-20221201172406695.png)

![image-20221201172429711](assets/image-20221201172429711.png)

然后一路Next下去。

如果文件存在的时候，可以选择Overwrite



## 代码模版的使用

### 查看Postfix Completion模板(后缀补全)

![image-20221201173411749](assets/image-20221201173411749.png)

### 查看Live Templates模板(实时模板)

这个2022.4版本没有，可能已经删除了，就不写了。

### 常用代码模版

1、非空判断 

- 变量.null：if(变量 == null)
- 变量.nn：if(变量 != null)
- 变量.notnull：if(变量 != null)
- ifn：if(xx == null)
- inn：if(xx != null)

2、遍历数组和集合 

- 数组或集合变量.fori：for循环
- 数组或集合变量.for：增强for循环
- 数组或集合变量.forr：反向for循环
- 数组或集合变量.iter：增强for循环遍历数组或集合

3、输出语句 

- sout：相当于System.out.println
- soutm：打印当前方法的名称
- soutp：打印当前方法的形参及形参对应的实参值
- soutv：打印方法中声明的最近的变量的值
- 变量.sout：打印当前变量值
- 变量.soutv：打印当前变量名及变量值

4、对象操作 

创建对象

- Xxx.new.var ：创建Xxx类的对象，并赋给相应的

变量

- Xxx.new.field：会将方法内刚创建的Xxx对象抽取

为一个属性

强转

- 对象.cast：将对象进行强转
- 对象.castvar：将对象强转后，并赋给一个变量

5、静态常量声明 

- psf：public static final
- psfi：public static final int
- psfs：public static final String
- prsf：private static final

### 自定义代码模版

**自定义后缀补全模版**

![image-20221201181208657](assets/image-20221201181208657.png)

![image-20221201181707456](assets/image-20221201181707456.png)

EXPR是事先要输入的表达式，比如这样设置之后，我需要先输入类型比如`Stirng`，然后输入`.list`

![image-20221201181817560](assets/image-20221201181817560.png)

然后回车或者tab就能自动补全代码。

**自定义Live Templates**

定义`sop`为`System.out.println();`语句

1. 添加自定义代码片段组

![image-20221201182132267](assets/image-20221201182132267.png)

2. 在组中添加新模板

![image-20221201182256933](assets/image-20221201182256933.png)

![image-20221201182357869](assets/image-20221201182357869.png)

![image-20221201182450298](assets/image-20221201182450298.png)

在文件中输入`sop`

![image-20221201182528230](assets/image-20221201182528230.png)

然后输入回车即可。

## 快捷键

### 查看快捷键

**已知快捷键操作名，未知快捷键**

![image-20221201183600931](assets/image-20221201183600931.png)

**已知快捷键，不知道对应的操作名**

![image-20221201183701913](assets/image-20221201183701913.png)

### 自定义快捷键

![image-20221201183837058](assets/image-20221201183837058.png)

### 使用其他平台的快捷键

![image-20221201183934845](assets/image-20221201183934845.png)

## 断点调试

### Debug步骤

Debug(调试)程序步骤如下：

1、添加断点

2、启动调试

3、单步执行

4、观察变量和执行流程，找到并解决问题

---

**1. 添加断点**

![image-20221201184912622](assets/image-20221201184912622.png)

> 也可以用 Ctrl + F8 添加或删除断点

**2. 启动调试**

![image-20221201185005627](assets/image-20221201185005627.png)

> 也可以用Shift + F9开启断点

**3. 单步执行**

![image-20221201185130569](assets/image-20221201185130569.png)

> 在debug的过程中可以动态打断点。

**4. 观察执行情况，找出问题**

### 多种debug情况介绍

#### 行断点

断点打在代码所在的行上。执行到这一行时，会停下来。

#### 方法断点

断点设置在方法的签名上，默认当进入时，断点可以被唤醒。

也可以设置在方法退出时，断点也被唤醒

![image-20221201185620024](assets/image-20221201185620024.png)

在多态的场景下，在父类或接口的方法上打断点，会自动调入到子类或实现类的方法

```java
/**
 * ClassName: Hello
 * Package: PACKAGE_NAME
 * Description:
 *
 * @Author Yan Jingcun
 * @Create 2022/12/1 18:15
 * @Version 1.0
 */
public class Hello {
    public static void main(String[] args) {
        //1.
        Son instance = new Son();
        instance.test();
        //2.
        Father instance1 = new Son();
        instance1.test();
        //3.
        Consumer con = new ConsumerImpl();
        con.accept("hello");
    }
}

class Father{
    public void test(){ // 【断点】
        System.out.println("Father : test");
    }
}
class Son extends Father{
    public void test(){ // 【断点】
        System.out.println("Son : test");
    }
}
interface Consumer{
    void accept(String str);
}
class ConsumerImpl implements Consumer{
    @Override
    public void accept(String str) {
        System.out.println("ConsumerImple:" + str);
    }
}
```



#### 字段断点

在**类的属性**声明上打断点，默认对属性的修改操作进行监控

![image-20221201190625104](assets/image-20221201190625104.png)

```java
import java.util.function.Consumer;

/**
 * ClassName: Hello
 * Package: PACKAGE_NAME
 * Description:
 *
 * @Author Yan Jingcun
 * @Create 2022/12/1 18:15
 * @Version 1.0
 */
public class Hello {
    public static void main(String[] args) {
        Person p1 = new Person(20);
        p1.setAge(p1.getAge() + 1);
        p1.setAge(p1.getAge() + 1);
        p1.setAge(p1.getAge() + 1);
        p1.setAge(p1.getAge() + 1);
    }
}

class Person{
    public Person(int age) {
        this.age = age;
    }

    private int age;

    public void setAge(int age) {
        this.age = age;
    }

    public int getAge() {
        return age;
    }
}
```



#### 条件断点

针对上述代码，在满足i == 3的条件下，执行断点。

```java
public class Hello {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            int target = i + 2;
        }
    }
}
```



![image-20221201190759993](assets/image-20221201190759993.png)

![image-20221201191041354](assets/image-20221201191041354.png)



#### 异常断点

对异常进行跟踪。如果程序出现指定异常，程序就会执行断点，自动停住。

![image-20221201191300276](assets/image-20221201191300276.png)

打上勾之后就可以实现异常断点了。

![image-20221201191335815](assets/image-20221201191335815.png)



#### 线程调试

当线程的名称为`Thread2`的时候，进入断点。

```java
    public static void main(String[] args) {
        test("Thread1");
        test("Thread2");
    }
    public static void test(String threadName) {
        new Thread(
                () -> System.out.println(Thread.currentThread().getName()),
                threadName
        ).start();
    }
```

![image-20221201191631368](assets/image-20221201191631368.png)

表达式为`Thread.currentThread().getName().equals("Thread2")`

![image-20221201191719845](assets/image-20221201191719845.png)

#### 强制结束

Ctrl+F2强制结束调试。

![image-20221201191823296](assets/image-20221201191823296.png)

右键之后ForceReturn可以结束当前线程。

### 自定义调试数据视图

![image-20221201215124992](assets/image-20221201215124992.png)

![image-20221201215251325](assets/image-20221201215251325.png)



### 常见问题

问题：使用Step Into时，会出现无法进入源码的情况。如何解决？

方案1：使用 force step into 即可

方案2：点击Setting -> Build,Execution,Deployment -> Debugger -> Stepping

把Do not step into the classess中的java.*、javax.* 取消勾选即可。

![image-20221201215410841](assets/image-20221201215410841.png)



## 创建不同类型的工程

### 创建Java工程

在【示例程序】中已经演示了创建Project的方法，在【工程和模块管理】中已经演示了创建Module的方法。

下面演示创建包的方法：

![image-20221201215728634](assets/image-20221201215728634.png)

输入报名后即可创建，多级package使用点号连接。`top.evilemperor.demo`

![image-20221201215812539](assets/image-20221201215812539.png)

### 创建JavaWeb工程

1. 创建新模块

![image-20221201220017372](assets/image-20221201220017372.png)

2. 选中当前创建的工程，添加框架支持：

![image-20221201220105686](assets/image-20221201220105686.png)

3. 选择：Web Application，选择Create web.xml，如下：

![image-20221201220159855](assets/image-20221201220159855.png)

4. 配置web工程并运行

![image-20221201220309012](assets/image-20221201220309012.png)

![image-20221201220350741](assets/image-20221201220350741.png)

配置tomcat

![image-20221201220519113](assets/image-20221201220519113.png)

![image-20221201220537718](assets/image-20221201220537718.png)

![image-20221201220654891](assets/image-20221201220654891.png)

运行效果

![image-20221201220747355](assets/image-20221201220747355.png)

#### 乱码问题的解决

问题：

![image-20221201220820815](assets/image-20221201220820815.png)

解决：

0. 确保IDEA控制台的字符集编码和tomcat输出的字符集编码是一样的(最好是UTF-8)

IDEA:

![image-20221201222431888](assets/image-20221201222431888.png)

tomcat:

在文件`apache-tomcat-8.5.42\conf\logging.properties`中，确保以下所有字符集都是UTF-8

![image-20221201222518377](assets/image-20221201222518377.png)

1. 点击Help => Edit custom VM Options，在最后面添加`-Dfile.encoding=UTF-8`

![image-20221201221004268](assets/image-20221201221004268.png)

![image-20221201220948166](assets/image-20221201220948166.png)

2. 在当前Tomcat实例中配置 VM option，添加`-Dfile.encoding=UTF-8`

![image-20221201221117212](assets/image-20221201221117212.png)

在第二步的Startup/Connection页签的Run和Debug添加一个key为`JAVA_TOOL_OPTIONS`，value为`-Dfile.encoding=UTF-8`的环境变量

![image-20221201221218316](assets/image-20221201221218316.png)

3. 重启IDEA

成功。

![image-20221201223249234](assets/image-20221201223249234.png)

### 创建Maven Java工程

读者自行下载Maven和配置

配置结果举例:

![image-20221201223313715](assets/image-20221201223313715.png)



1. 创建maven模块（项目），选择一套模版。

![image-20221201223744340](assets/image-20221201223744340.png)

![image-20221201224006902](assets/image-20221201224006902.png)

然后点击创建即可。

2. 添加缺少的资源目录

给main和text目录下添加resources目录，并设置为资源目录

![image-20221201224239447](assets/image-20221201224239447.png)

Maven的Java目录结构：

```
工程名
     src
     ----main
     --------java
     --------resources
     ----test
     --------java
     --------resources
     pom.xml
```

- main目录用于存放主程序。
- test目录用于存放测试程序。
- java目录用于存放源代码文件。
- resources目录用于存放配置文件和资源文件。

3. 测试

第1步：创建Maven的核心配置文件pom.xml（已创建）

第2步：编写主程序代码

第3步：编写测试代码

第4步：运行几个基本的Maven命令

![image-20221201224517830](assets/image-20221201224517830.png)

比如运行了打包package

![image-20221201224804770](assets/image-20221201224804770.png)

#### 报错：不再支持源选项 5。请使用 7 或更高版本。

pom.xml文件中的properties标签改成如下样式：

```xml
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.encoding>UTF-8</maven.compiler.encoding>
    <java.version>1.8</java.version>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
  </properties>
```



### 创建Maven Web工程

![image-20221201224949630](assets/image-20221201224949630.png)

直接创建即可。

然后进行配置，选择对应的artifact即可，然后进行相关的配置即可。

![image-20221201233102233](assets/image-20221201233102233.png)

问题：如果deployment中不显示刚刚创建的artifact，则重新加载一下项目即可。

![image-20221201233037428](assets/image-20221201233037428.png)

![image-20221201233213060](assets/image-20221201233213060.png)



由于现在jsp早就淘汰了，就不写下面的了。

## 关联数据库

### 关联方式

显示数据库

![image-20221201233239845](assets/image-20221201233239845.png)

添加数据库

![image-20221201233309950](assets/image-20221201233309950.png)

![image-20221201233408970](assets/image-20221201233408970.png)



### 常用操作

![image-20221201233449937](assets/image-20221201233449937.png)

也可以展示ER图并导出

![image-20221201233509135](assets/image-20221201233509135.png)





