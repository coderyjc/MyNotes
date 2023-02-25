```ad-note
https://zhuanlan.zhihu.com/p/87864677
```

## 安装MinGW编译器

### 方法一：下载安装器在线安装

可以在MinGW[官网地址下载](https://sourceforge.net/projects/mingw-w64/files/mingw-w64/mingw-w64-release/)，也可以直接下载：[MinGW直接下载](https://nchc.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe)

下载参数如下：

![[assets/Pasted image 20230225124610.png]]

确保路径中不包含**空格**和**中文**字符

![[assets/Pasted image 20230225124739.png]]

安装成功即可

但是我在安装的时候安装失败了（科学上网也不行），报错如下，因此尝试离线安装

![[assets/Pasted image 20230225125231.png]]

### 方法二：离线安装

直接在官网下载离线安装包，或者[点击直接下载](https://altushost-swe.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-win32/seh/x86_64-8.1.0-release-win32-seh-rt_v6-rev0.7z)

下载完之后直接解压到文件夹即可。

然后将 `{安装路径}\mingw64\bin`添加到环境变量

检测：

cmd中输入`gcc -v`出现下列文字说明配置正确。

![[assets/Pasted image 20230225125919.png]]

## VsCode安装C++扩展



## 配置C++环境



