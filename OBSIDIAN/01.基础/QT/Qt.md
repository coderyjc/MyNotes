V:\Environment\Annaconda\python.exe R:/Code/Pycharm/main.py

> Qt 笔记 https://www.bilibili.com/video/BV1g4411H78N



## 1.概述

### 1.1 什么是Qt

Qt是一个跨平台的C＋＋图形用户界面应用程序框架。它为应用程序开发者提供建立艺术级图形界面所需的所有功能。它是完全面向对象的，很容易扩展，并且允许真正的组件编程。

### 1.2 发展史

1991年Qt最早由奇趣科技开发。

1996年进入商业领域，它也是目前流行的Linux桌面环境KDE的基础。

2008年奇趣科技被诺基亚公司收购，Qt称为诺基亚旗下的编程语言

2012年Qt又被Digia公司收购

2014年4月跨平台的集成开发环境Qt Creator3.1.0发布，同年5月20日配发了Qt5.3正式版，至此Qt实现了对iOS、Android、WP等各平台的全面支持。

2019年，Qt团队宣布最新版5.13版本发布。

> Linux 桌面是用Qt做的

### 1.3 平台

Qt支持下述平台：

MS/Windows - 95、98、NT4.0、ME、2000、XP 、 Vista、Win7、win8、win2008、win10

Unix/X11 -Linux、SunSolaris、HP-UX、CompaqTru64 UNIX、IBMAIX、SGI IRIX、FreeBSD、BSD/OS和其它很多X11平台

Macintosh -Mac OS X

> 跨平台的

### 1.4 版本

按照不同的版本发行，分为商业版和开源版。

商业版

- 4I 为商业软件提供开发，他们提供传统商业软件发行版，并且提供在商业有效期内的免费升级和技术支持服务。

开源的 LGPL版本

- “为了开发自有而设计的开放源码软件，它提供了和商业版本同样的功能，在GNU通用公共许可下，它是免费的。

### 1.5 下载和安装

> 版本列表 https://download.qt.io/archive/ 
>
> QtCreater文档 https://doc.qt.io/qtcreator/index.html
>
> 

默认安装(建议组件全部选中)Qt对不同的平台提供了不同版本的安装包,可根据实际情况自行下载安装

本文档使用qt- opensource-windows-x86 new482 opengl5.3.1版本进行讲解

### 1.6 优点和成功案例

**优点**

- 跨平台，几乎支持所有的平台
- 接口简单，容易上手，学习QT框架对学习其他框架有参考意义。
- 一定程度上简化了内存回收机制。
- 开发效率高，能够快速的构建应用程序。
- 有很好的社区氛围，市场份额在缓慢上升。
- 可以进行嵌入式开发。。

**成功案例**

- Linux 桌面环境KDE 

- WPS Office 办公软件
- Skype 网络电话
- Google Earth 谷歌地图
- VLC多媒体播放器
- VixtualBox，虚拟机软件



## 2 创建项目

### 2.1 向导创建

![[image-20211203102638034.png]]
项目目录不能有中文

构建系统简介

- CMake 很常用，功能也很强大，许多知名的项目都是用它，比如 OpenCV 和 VTK，但它的语法繁杂。

- qmake 是针对辅助 Qt 开发的，但也可以在非 Qt 项目使用，特点是语法简单明了，但功能也相对简单。

- Qbs 号称下一代构建工具，也有好多人力捧 Qbs，没用过。

这里可以选择默认的qmake

![[image-20211203103023182.png]]
然后设置类信息，首先Class name是自定义的，而且下面的Header file、Source file和From file的名称会根据自定义的Class name自动修改。

然后是Base class（基类），有三个基类供选择，QMainWindow、QWidget 和 QDialog

QMainWindow 和 QDialog 是 QWidget 的两个派生类，可以理解为都是窗口，但窗口样式不同

- QWidget 最简单的窗口，

- QMainWindow  多了菜单栏、工具栏、状态栏

- QDialog 对话框



![[image-20211203103840665.png]]
这里直接使用了默认的类信息。

![[image-20211203103239075.png]]
这个默认

构建套件默认，如果下载了多个版本的构建套件，可以在这里进行选择

版本控制默认

![[image-20211203103912445.png]]
点击完成，创建完成

![[image-20211203104402973.png]]
### 2.2 .pro文件

相当于 VS 的 .sln 文件 工程文件。



### 2.3 一个最简单的Qt应用程序

```c++
// 自己刚刚生成的类
#include "widget.h"
// 包含一个应用程序类的头文件
#include <QApplication>

// argc 命令行参数的数量
// argv 命令行参数数组
int main(int argc, char *argv[])
{
    // a 应用程序对象，在Qt中，应用程序对象有且仅有一个
    QApplication a(argc, argv);
    // 窗口对象，通过我们自己刚刚生成的类创建
    Widget w;
    // 调用show方法，窗口对象默认不会显示，必须调用这个方法
    w.show();
    // 让应用程序对象进入消息循环机制
    // 当代码阻塞到这一行
    return a.exec();
}
```

### 2.4 命名规范&快捷键











## 3 第一个Qt小程序

### 3.1 按钮的创建









### 3.2 对象模型（对象树）







### 3.3 Qt窗口坐标体系





## 4 信号和槽







