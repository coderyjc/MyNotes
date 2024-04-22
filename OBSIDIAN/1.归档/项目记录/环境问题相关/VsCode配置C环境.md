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

## 方法3（2024.4.22更新）


```json
// tasks.json

{
  // See https://go.microsoft.com/fwlink/?LinkId=733558
  // for the documentation about the tasks.json format
  "version": "2.0.0",
  "tasks": [
      {
          "label": "echo",
          "type": "shell",
          "command": "g++",
          "args": [
              "-g", 
              "${file}", 
              "-o", 
              "${fileBasenameNoExtension}.exe",
              "-fexec-charset=GBK"//解决中文乱码
          ]
      }
  ],
  "presentation": {
      "echo": true,
      "reveal": "always",
      "focus": false,
      "panel": "shared", 
      "showReuseMessage": true,
      "clear": false
  }
}
```


```json
// c_cpp_properties.json

{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceRoot}",
                // "F:\\env\\mingw\\include",
                // "F:\\env\\mingw\\lib\\gcc\\x86_64-w64-mingw32\\8.1.0\\include\\c++",
                // "F:\\env\\mingw\\lib\\gcc\\x86_64-w64-mingw32\\8.1.0\\include\\c++\\x86_64-w64-mingw32",
                // "F:\\env\\mingw\\lib\\gcc\\x86_64-w64-mingw32\\8.1.0\\include\\c++\\backward",
                // "F:\\env\\mingw\\lib\\gcc\\x86_64-w64-mingw32\\8.1.0\\include",
                // "F:\\env\\mingw\\lib\\gcc\\x86_64-w64-mingw32\\8.1.0\\include-fixed",
                // "F:\\env\\mingw\\x86_64-w64-mingw32\\include"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "__GNUC__=6",
                "__cdecl=__attribute__((__cdecl__))"
            ],
            "intelliSenseMode": "msvc-x64",
            "browse": {
                "limitSymbolsToIncludedHeaders": true,
                "databaseFilename": "",
                "path": [
                    "${workspaceRoot}",
                    // "F:\\env\\mingw\\include",
                    // "F:\\env\\mingw\\lib\\gcc\\x86_64-w64-mingw32\\8.1.0\\include\\c++",
                    // "F:\\env\\mingw\\lib\\gcc\\x86_64-w64-mingw32\\8.1.0\\include\\c++\\x86_64-w64-mingw32",
                    // "F:\\env\\mingw\\lib\\gcc\\x86_64-w64-mingw32\\8.1.0\\include\\c++\\backward",
                    // "F:\\env\\mingw\\lib\\gcc\\x86_64-w64-mingw32\\8.1.0\\include",
                    // "F:\\env\\mingw\\lib\\gcc\\x86_64-w64-mingw32\\8.1.0\\include-fixed",
                    // "F:\\env\\mingw\\x86_64-w64-mingw32\\include"
                ]
            }
        }
    ],
    "version": 4
}
```


```json
// launch.json

{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
      {
        "name": "(Windows) Launch",
        "type": "cppvsdbg",
        "request": "launch",
        "program": "cmd",
        "preLaunchTask": "echo",
        "args": [
            "/C",
            "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "&",
            "echo.",
            // "&",
            // "pause" // 黑框一闪而过就释放这里的注释
        ],
        "stopAtEntry": false,
        "cwd": "${workspaceFolder}",
        "environment": [],
        "externalConsole":true
    },
    {
      "name": "(gdb) Launch",
      "type": "cppdbg",
      "request": "launch",
      "program": "${workspaceFolder}/${fileBasenameNoExtension}.exe",
      "args": [],
      "stopAtEntry": false,
      "cwd": "${workspaceFolder}",
      "environment": [],
      "externalConsole": true,
      "MIMode": "gdb",
      "miDebuggerPath": "F:\\env\\mingw\\bin\\g++.exe",// 自己电脑的gdb
      "preLaunchTask": "echo",
      "setupCommands": [
        {
            "description": "Enable pretty-printing for gdb",
            "text": "-enable-pretty-printing",
            "ignoreFailures": true
        }
      ]
    }
  ]
}
```


## 方法2【新版】

在文件夹下创建`.vscode`文件夹，然后创建3个文件。

1. c_cpp_properties.json
2. launch.json
3. tasks.json

1. c_cpp_properties.json

```json
{
    "configurations": [
        {
          "name": "Win32",
          "includePath": ["${workspaceFolder}/**"],
          "defines": ["_DEBUG", "UNICODE", "_UNICODE"],
          "windowsSdkVersion": "10.0.17763.0",
          "compilerPath": "F:\\codeConfiguration\\minGW\\bin\\g++.exe",   /*修改成自己bin目录下的g++.exe，这里的路径和电脑里复制的文件目录有一点不一样，这里是两个反斜杠\\*/
          "cStandard": "c11",
          "cppStandard": "c++17",
          "intelliSenseMode": "${default}"
        }
      ],
      "version": 4
}
```

2. launch.json

```json

{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "g++.exe build and debug active file",
            "type": "cppdbg",
            "request": "launch",
            "program": "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": true,
            "MIMode": "gdb",
            "miDebuggerPath": "F:\\codeConfiguration\\MinGW\\bin\\gdb.exe",		/*修改成自己bin目录下的gdb.exe，这里的路径和电脑里复制的文件目录有一点不一样，这里是两个反斜杠\\*/
            "setupCommands": [
                {
                    "description": "为 gdb 启用整齐打印",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            "preLaunchTask": "task g++"
        }
    ]
}

```

3. tasks.json

```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558 
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
        "type": "shell",
        "label": "task g++",
        "command": "F:\\codeConfiguration\\MinGW\\bin\\g++.exe",	/*修改成自己bin目录下的g++.exe，这里的路径和电脑里复制的文件目录有一点不一样，这里是两个反斜杠\\*/
        "args": [
            "-g",
            "${file}",
            "-o",
            "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "-I",
            "F:\\codeProject\\vsCode",      /*修改成自己放c/c++项目的文件夹，这里的路径和电脑里复制的文件目录有一点不一样，这里是两个反斜杠\\*/
            "-std=c++17"
        ],
        "options": {
            "cwd": "F:\\codeConfiguration\\MinGW\\bin"	/*修改成自己bin目录，这里的路径和电脑里复制的文件目录有一点不一样，这里是两个反斜杠\\*/
        },
        "problemMatcher":[
            "$gcc"
        ],
        "group": "build",
        
        }
    ]
}
```

然后写个hello world进行测试。


应该没问题。


## 方法1【旧版】

### 配置C++环境

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

### 配置构建任务（使用vscode的debug调试）

创建一个tasks.json文件来告诉VS Code如何构建（编译）程序。该任务将调用g++编译器基于源代码创建可执行文件。 按快捷键`Ctrl+Shift+P`调出命令面板，输入tasks，选择“Tasks:Configure Default Build Task”：

![[assets/Pasted image 20230225163408.png]]

![[assets/Pasted image 20230225163510.png]]


在`./.vscode`生成了`task.json`

此时在`hello.cpp`中直接按`F5`可以直接进行调试，

![[assets/Pasted image 20230225164105.png]]

选择：`C++(GDB/LLDB)`

然后产生一个`launch.json`文件

直接替换！！

```ad-warning
title:注意
- miDebuggerPath要换成自己的路径
- preLaunchTask要替换成自己的字段，就是之前配置的tasks.json中的label字段
```

```json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "(gdb) Launch",
      "preLaunchTask": "C/C++: g++.exe build active file",//调试前执行的任务，就是之前配置的tasks.json中的label字段
      "type": "cppdbg",//配置类型，只能为cppdbg
      "request": "launch",//请求配置类型，可以为launch（启动）或attach（附加）
      "program": "${fileDirname}\\${fileBasenameNoExtension}.exe",//调试程序的路径名称
      "args": [],//调试传递参数
      "stopAtEntry": false,
      "cwd": "${workspaceFolder}",
      "environment": [],
      "externalConsole": true,//true显示外置的控制台窗口，false显示内置终端
      "MIMode": "gdb",
      "miDebuggerPath": "F:\\env\\mingw64\\bin\\gdb.exe",
      "setupCommands": [
          {
              "description": "Enable pretty-printing for gdb",
              "text": "-enable-pretty-printing",
              "ignoreFailures": true
          }
      ]
    }
  ]
}
```

最后，打了断点之后能够显示变量和正常运行，即为配置成功

![[assets/Pasted image 20230225164820.png]]
