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

从插件列表中下载C/C++扩展

![[assets/Pasted image 20230225162343.png]]

先编写测试代码

![[assets/Pasted image 20230225162408.png]]

发现需要配置运行环境

下面我们开始配置运行环境

## 配置C++环境

可以直接在弹出来的窗口中选择`Configure UI`

![[assets/Pasted image 20230225162447.png]]

也可以`Ctrl Shift P`后输入C++，选择`Configure UI`

![[assets/Pasted image 20230225162533.png]]

这里已经自动写好了，默认是gcc的，用来编译C语言代码，可以改成g++，C++兼容C语言

![[assets/Pasted image 20230225162636.png]]

这里IntelliSense代码补全工具写windows-gcc-x64

![[assets/Pasted image 20230225162742.png]]

配置完成后，此时在侧边栏可以发现多了一个.vscode文件夹，并且里面有一个c_cpp_properties.json文件，内容如下，说明上述配置成功。现在可以通过`Ctrl+<`快捷键打开内置终端并进行编译运行了。

目前已经可以进行编译和运行了。

```bash
g++ hello.cpp
./a.exe
```

## 配置构建任务（使用vscode的debug调试）

创建一个tasks.json文件来告诉VS Code如何构建（编译）程序。该任务将调用g++编译器基于源代码创建可执行文件。 按快捷键`Ctrl+Shift+P`调出命令面板，输入tasks，选择“Tasks:Configure Default Build Task”：

![[assets/Pasted image 20230225163408.png]]

![[assets/Pasted image 20230225163510.png]]


在`./.vscode`生成了`task.json`

此时在`hello.cpp`中直接按`F5`可以直接进行调试，

![[assets/Pasted image 20230225164105.png]]

选择：`C++(GDB/LLDB)`

然后产生一个`launch.json`文件

