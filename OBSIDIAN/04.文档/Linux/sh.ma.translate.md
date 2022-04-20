BSD通用命令手册

名称: dash  -- 命令解释器(shell)

概要: 
    dash [-aCefnuvxIimqVEbp] [+aCefnuvxIimqVEbp] [-o option_name] [+o option_name]
          [command_file [argument ...]]
    dash -c [-aCefnuvxIimqVEbp] [+aCefnuvxIimqVEbp] [-o option_name] [+o option_name]
          command_string [command_name [argument ...]]
    dash -s [-aCefnuvxIimqVEbp] [+aCefnuvxIimqVEbp] [-o option_name] [+o option_name]
          [argument ...]


## 介绍

dash 是标准的系统命令解释器。当前版本的dash是正在更改以符合 POSIX 1003.2 和 1003.2a 规范的shell。这个版本有很多特性，这使它在某些地方看起来和 Korn shell 很相似，但它不是 Korn shell 的克隆（请参阅 ksh(1)）。只有POSIX规范设计的特性,加上一些博伯克利的扩展, 正在合并到这个shell中. 这个帮助页面旨在成为一个教程或者这个shell完整的说明


### 概述

shell是一个命令, 这个命令从中断或者文件中读取命令行, 解释他们, 一般用来执行其他命令. 这是在用户登入到系统的时候运行的程序(即便用户能够通过chsh命令选择不同的shell). 

... 

命令能够直接敲在运行的shell中, 也能放在一个文件中, 这个文件能够被shell 直接执行

### 调用
A login shell first reads commands from the files /etc/profile and .profile if they exist.

If the environment variable ENV is set on entry to an interactive shell, or is set in the .profile of a login shell, the shell next reads commands from the file named in ENV.


### 参数列表处理



### 词法结构



### 引号



### 反斜杠



### 单引号



### 双引号



### 逆转单词



### 昵称



### 命令



### 简单命令



### 重定向



### 搜索和执行



### 路径搜索



### 命令退出状态



### 复杂命令



### 管道



### 后台命令 -- &



### 列表 -- 概括地说



### 短路列表运算符



### 控制流



### 函数



### 变量和参数



### 未知参数



### 特殊参数



### 词扩展



### 波浪号扩展(替代用户的主目录)



### 参数扩展



### 命令替代



### 算数扩展



### 空白符分割



### 路径扩展



### shell模式



### 内置的命令





## 退出状态



## 环境变量



## 文件


## 引用




## 历史

## BUGS


THE END



