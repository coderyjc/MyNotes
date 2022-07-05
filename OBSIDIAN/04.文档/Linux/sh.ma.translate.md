> 在学习OS的时候翻译了一下linux系统的 man.sh 
> 
> 源文档中分段较少, 我在原文的基础上对段落结构进行了略微分段, 并使用markdown对原文进行了略微排版, 以获得更好的阅读体验. 如有歧义, 请以官方文档为主.
> 
> 官方文档获取方法: 在linux系统终端输入`man sh`命令.
>
> 本人英语和计算机水平有限, 错误之处还请指出. 不胜感激.
> 
> 非商用转载请注明来源.


# BSD通用命令手册

名称: dash  -- 命令解释器(shell)

概要: 

```bash
    dash [-aCefnuvxIimqVEbp] [+aCefnuvxIimqVEbp] [-o option_name] [+o option_name] [command_file [argument ...]]
    dash -c [-aCefnuvxIimqVEbp] [+aCefnuvxIimqVEbp] [-o option_name] [+o option_name] command_string [command_name [argument ...]]
    dash -s [-aCefnuvxIimqVEbp] [+aCefnuvxIimqVEbp] [-o option_name] [+o option_name] [argument ...]
```

**介绍**

dash 是本系统的标准命令解释器. dash当前版本的正在进行修改以符合POSIX1003.2和1003.2a对于shell的规范. 

这个版本有很多特性, 这些特性使它在某些地方看起来和 Korn shell 很相似，但它不是 Korn shell 的克隆(请参阅 ksh(1)). 

只有POSIX规范设计的特性, 加上一些伯克利的扩展, 正在合并到这个shell中. 这个帮助页面旨在成为一个教程或者这个shell完整的说明.

### 概述

shell是一个命令, 这个命令从文件或者终端中读取命令行并解释, 一般用来执行其他命令. 这是在用户登入到系统的时候运行的程序(即便用户能够通过chsh命令(1)选择不同的shell). 

shell实现了一种语言, 这种语言具有控制流结构, 一种宏除了数据存储外, 还提供各种功能的宏工具, 这种宏工具具有内置的历史命令和行编辑功能. 

它结合了许多功能来帮助交互使用，并具有以下优点：这种解释性语言对于交互式和非交互式使用(shell脚本)都是通用的. 

也就是说，命令可以直接键入到正在运行的shell中, 也可以放入文件中，文件可以直接被shell执行.

### 调用

如果没有参数, 并且shell的标准输入连接到终端(或者设置了-i标志), -c选项没有设置, 则该shell被视为交互式shell. 交互式shell通常在每个命令之前进行提示, 并以不同的方式处理编程和命令错误(如下所述).第一次启动时, shell检查首个参数, 如果它以破折号"-"开头, 则shell也被视为登录shell. 这通常在用户首次登录时由系统自动完成. 登录shell首先从文件 `/etc/profile` 和 .profile 中读取命令(如果他们存在).如果环境变量ENV在交互式shell的入口上设置, 或者在login shell的.profile中设置. shell接下来就会读取在ENV中指定的文件中的命令. 

因此，用户应在.profile文件中放置仅在登录时执行的命令; 在ENV文件中放置针对每个交互式shell执行的命令.

想要设置ENV变量设置为某个文件, 请在主目录的配置文件 .profile 中写入以下行

```bash
    ENV=$HOME/.shinit; export ENV
```

替换 ".shinit" 为任何你想要的文件名

如果指定了选项之外的命令行参数, 则shell将第一个参数视为从中读取命令的文件名(shell脚本), 其余参数设置为shell的位置参数($1\$2等). 否则，shell将从其标准输入中读取命令.

### 参数列表处理

所有具有相应名称的单字母选项都可以用作-o选项的参数. 在下面的描述中, 在单字母选项旁边提供了 -o 的名称. 

指定破折号 "-" 将启用该选项, 而使用加号 "+" 将禁用该选项. 可以从命令行或使用内置(稍后描述)设置以下选项.

|选项|意义|解释|
|----|----|----|
| -a | allexport | 导出所有已分配变量 |
| -c | - | 从命令字符串而不是从标准输入读取命令. 特殊参数0从命令名称处设置, 位置参数($1，$2等)将从其余参数操作数设置 |
| -C | noclobber |  不使用'>'重写已存在的文件 |
| -e | errexit | 在非交互的情况下, 如果任何非测试的命令执行失败会立即退出. 如果命令用于控制if、elif、while或until; 或者如果命令是 "&&" 或 "||" 运算符的左值, 则认为该命令的退出状态已被明确测试; |
| -f | noglob | 禁用路径名扩展 |
| -n | noexec | 在非交互的情况下, 读取命令单步执行. 这对检查shell脚本的语法是非常有用的 |
| -u | nounset | 当尝试扩展未被设置的变量时, 向标准错误流中写消息, 如果是非交互shell, 立即退出 |
| -v | verbose | shell在读取时向标准错误错误流中写入其输出.在debug的时候有用 |
| -x | xtrace | 在执行每个命令之前, 将其写入标准错误流(前面有一个"+"). Debug时有用 |
| -I | ignoreeof | 在交互式shell中, 从输入中忽略文档结束符EOF |
| -i | interactive | 强制shell表现为交互式 |
| -l | - | 使dash表现为登录 shell 调用的 |
| -m | monitor | 打开作业控制(交互时自动设置) |
| -s | stdin | 从标准输入中读取命令(如果没有文件参数呈现的时候自动设置). 当shell已经运行之后, 这个设置没有效果 |
| -V | vi | 启用内置的vi命令行编辑器(如果-E设置了会取消) |
| -E | emacs | 启用内置的emacs命令行编辑器(如果-V设置了会取消) |
| -b | notify | 启用后台作业完成的异步通知(4.4alpha版本没有实现这个功能) |
| -p | priv | 有效uid与uid不匹配时不尝试重置它. 默认情况下不设置, 因为要避免system(3)和popen(3)的错误使用 |

### 词法结构

shell从文件中按行读取输入, 并从空白(空格和制表符)处和shell特有的特定字符序列("运算符")处分解为单词。

有两种类型的操作符：控制操作符和重定向操作符(稍后讨论).

以下是操作符列表：

控制操作符

```bash
& && ( ) ; ;; | || <newline>
```

重定向操作符

```bash
 < > >| << >> <& >& <<- <>
```

### 引用

引用用于移除shell中某些字符或单词的特殊含义, 如运算符\空格或关键字. 引用有三种类型：匹配的单引号\匹配的双引号和反斜杠。

### 反斜杠

反斜杠保留其后字符的字面含义, 除了⟨newline⟩. 前一个反斜杠⟨newline⟩被视为行的继续.

### 单引号

将字符括在单引号中可以保留所有字符的字面意义(单引号除外, 这使得无法将单引号放在单引号字符串中).

### 双引号

将字符括在双引号内保留除美元符号($)\反引号(`)和反斜杠(\\)之外的所有字符的字面含义. 双引号中的反斜杠在历史上很奇怪，只用于引用以下字符：

```bash
$ ` " \ <newline>
```

否则它仍然是文字.

### 保留字

保留字是对shell有特殊意义的字，在行首和控制操作符之后识别

以下为保留字：

|      |   |    |   | |
|---|---|---|---|---|
| !     |  elif  |  fi    |  while |  case|
| else  |  for   |  then  |  {     |  }|
| do    |  done  |  until |  if    |  esac|

我们将会随后讨论他们的含义.

### 别名

别名是使用alias(1) 内置命令设置的名称和相应值. 每当出现保留字时(见上文), 在检查保留字后, shell会检查该字是否与别名匹配. 如果是, 则在输入流中用其值替换它. 

例如，如果有一个名为"lf"的别名，其值为"ls-F", 如果输入: 

```bash
lf foobar <return>
```

将会变成

```bash
ls -F foobar <return>
```

别名为初级用户提供了一种方便的方法来创建命令的缩写, 而不必学习如何创建带有参数的函数. 它们还可以用于创建词汇含义不明的代码.

不鼓励这样使用

### 命令

shell 根据语言来解释它读取的单词, 该语言的规范不在本手册页的范围内(请参阅POSIX 1003.2文档中的BNF). 但是从本质上讲, 读取一行之后, 如果该行的第一个字(或控制运算符之后)不是保留字, 则 shell 已经识别出一个简单的命令. 否则, 可能识别出复杂的命令或某些其他特殊结构.

### 简单命令

如果已经识别了一个简单的命令, shell会像以下步骤表现

1. 去掉形式为“name=value”的前导词, 并将其分配给简单命令的环境. 重定向运算符及其参数(如下所述)被提取并保存以供处理.

2. 剩余的单词按照“扩展”一节中的描述进行扩展, 剩余的第一个单词被视为命令名, 命令被定位. 其余单词被视为命令的参数. 如果没有生成命令名, 则第1步中识别的“name=value” 变量赋值会影响当前shell.

3. 重定向将按下一节所述执行

### 重定向

重定向用于更改命令读取其输入或发送其输出的位置. 通常, 重定向会打开、关闭或复制对文件的现有引用. 

用于重定向的大概格式为：

`[n] redir-op file`

其中，redir-op 是前面提到的重定向操作符之一. 以下是可能的重定向列表. [n]是介于0和9之间的可选数字, 如“3”(而不是“[3]”), 表示文件描述符.

|形式|解释|
|---|---|
|[n]> file  | 重定向标准输出到文件 |
|[n]>\| file| 同上, 但是重载-C选项 |
|[n]>> file | 添加标准输出流到文件 |
|[n]< file  | 从文件重定向标准输入流 |
|[n1]<&n2   | 复制文件描述符n2作为标准输出 |
|[n]<&-     | 关闭标准输入 |
|[n1]>&n2   | 复制文件描述符n2作为标准输入 |
|[n]>&-     | 关闭标准输出 |
|[n]<> file | 为读写标准输入打开文件 |

以下重定向通常称为“here document”。

```bash
    [n]<< delimiter
          here-doc-text ...
    delimiter
```

连续行中直到定界符的所有文本都会保存下来, 并在标准输入或文件描述符n(如果指定)上提供给命令.

如果引用了初始行中指定的分隔符, 则按字面处理here-doc-text 否则文本将进行参数扩展、命令替换和算术扩展(如“扩展”一节中所述). 如果操作符是“<<-”而不是“<<”, 则此处中here-doc-text 的前导选项卡将被剥离

### 搜索和执行

有三种命令: shell 函数\内置命令和普通程序——命令在搜索的时候也是按上述顺序排列(按照名称). 当 shell 函数执行时, 所有的 shell 位置参数(除了 $0，它保持不变)都被设置为 shell 函数的参数.显式放置在命令环境中的变量(通过把他们放在函数名之前对它们进行赋值)被设为函数的本地变量并设置为给定的值. 然后执行函数定义中给出的命令. 命令执行完成后, 位置参数将恢复为其原始值. 这一切都发生在当前的 shell 中.

Shell 内置函数在 shell 内部执行, 不会产生新进程.

否则, 如果命令名称与函数或内置函数不匹配, 则在文件系统中将命令作为普通程序进行搜索(如下一节所述). 当执行普通程序时, shell 运行程序, 将参数和环境传递给程序. 如果程序不是普通的可执行文件(即, 如果它不以“幻数”开头, “幻数”即ASCII 表示为“#!”, 这时 execve(2) 返回 ENOEXEC) shell 就会在子 shell 中解释程序. 在这种情况下, 子 shell 将重新初始化自己, 因此效果就像调用了一个新的 shell 来处理 ad-hoc shell 脚本, 只是位于父 shell 中的散列的命令的位置将会被子 shell 记住.

请注意, 本文档的先前版本和源代码本身会误导性地偶尔将没有幻数的 shell 脚本称为“shell 过程”.

### 路径搜索

定位命令时, shell 首先查看它是否具有该名称的 shell 函数. 然后它会查找该名称的内置命令. 如果未找到内置命令, 则会发生以下两种情况之一：

1. 包含斜线的命令名称只执行而不执行任何搜索.

2. shell 依次在 PATH 中的每个条目中搜索命令. PATH 变量的值应该是一系列用冒号分隔的条目. 每个条目都包含一个目录名称. 当前目录可以由一个空目录名称隐式指示, 也可以由一个句点显式指示.

### 命令退出状态

每个命令都有一个退出状态, 这个状态可以影响其他 shell 命令的行为. 命令以0表示正常或成功退出, 非0表示失败、错误或错误指示. 每个命令的手册页说明了各种退出代码及其含义. 此外, 内置命令返回退出代码, 执行的 shell 函数也是如此.

如果命令完全由变量赋值组成, 则命令的退出状态是最后一个命令的状态(如果有的话), 否则就是 0.

### 复杂命令

复杂命令是简单命令与控制运算符或保留字的组合, 共同创建一个更大的复杂命令. 更概括地说, 命令是以下之一: 

- 简单命令
- 管道
- 列表或者复合列表
- 复合命令
- 函数定义

除非另有说明, 否则命令的退出状态是该命令执行的最后一个简单命令的退出状态.

### 管道

管道是由控制运算符|分隔的一个或多个命令的序列. 除了最后一个命令之外, 所有命令的标准输出都连接到下一个命令的标准输入. 最后一个命令的标准输出是从 shell 继承的.

管道的格式是 : 

```bash
[!] command1 [| command2 ...]
```

command1 的标准输出连接到 command2 的标准输入. 在作为命令的一部分的重定向运算符指定的任何重定向之前, 一个命令的标准输入、标准输出或两者都被认为是由管道分配的.

如果管道不在后台(稍后讨论), shell 将会等待所有命令完成.

如果保留字 ! 不在管道之前, 退出状态是管道中指定的最后一个命令的退出状态. 否则, 退出状态是最后一个命令的退出状态的逻辑非. 即如果最后一条命令返回0, 则退出状态为1;  如果最后一个命令返回大于零, 则退出状态为零.

因为标准输入或标准输出或两者的管道分配发生在重定向之前, 所以它可以通过重定向来修改. 例如: 

```bash
$ command1 2>&1 | command2
```

将 command1 的标准输出和标准错误发送到 command2 的标准输入.

一个 ; 或 ⟨newline⟩ 终止符导致前面的 AND-OR-list(在下面描述)被顺序执行;

一个 & 异步执行前面的 AND-OR-list

请注意, 与其他一些 shell 不同, 管道中的每个进程都是调用 shell 的子进程(除非它是内置 shell, 在这种情况下它在当前 shell 中执行 —— 但它对环境的任何影响都会被清除).

### 后台命令 -- &

如果命令由控制运算符 & 号 (&) 结束, 则 shell 将异步执行命令. 也就是说, shell 在执行下一个命令之前不会等待命令完成.

在后台运行命令的格式是：

```bash
command1 & [command2 & ...]
```

如果 shell 不是交互式的, 则异步命令的标准输入设置为 /dev/null.

### 列表 -- 概括地说

列表是由换行符、分号或 & 号分隔的零个或多个命令的序列, 并且可选地由这三个字符其中之一终止. 列表中的命令按照它们写的顺序执行. 如果命令后跟一个 & 号, shell 将启动该命令并立即执行下一个命令; 否则, 它会等待命令终止, 然后再继续执行下一个命令.

### 短路列表运算符

“&&”和“||” 是 AND-OR 列表运算符. 

“&&”执行第一个命令, 然后执行第二个命令

当且仅当第一个命令的退出状态为零. “||” 执行第二个命令

当且仅当第一个命令的退出状态为非零时. “&&”和“||” 两者具有相同的优先级.

### 控制流约束 -- if,while,for,case

if 命令的语法是

```bash
    if list
    then list
    [ elif list
    then    list ] ...
    [ else list ]
    fi
```

while 命令的语法是

```bash
    while list
    do   list
    done
```

这两个列表在第一个列表的退出状态为零时重复执行. until 命令类似, 但使用 until 代替 while, 这会导致它重复直到第一个列表的退出状态为零.

for 命令的语法

```bash
    for variable [ in [ word ... ] ]
    do   list
    done
```

后面的单词被展开, 然后列表被重复执行, 变量依次设置为每个单词. 在 word 中省略 ... 相当于在 "$@" 中

break 和 continue 的语法是

```bash
    break [ num ]
    continue [ num ]
```

Break 终止最里面的 num 个 for 或 while 循环. Continue 继续最内层循环的下一次迭代. 这些是作为内置命令实现的.

case 命令的语法是

```bash
    case word in
    [(]pattern) list ;;
    ...
    esac
```

这个模式实际上可以是一个或多个模式(参见后面描述的 Shell 模式), 用“|”分隔字符. 模式前的“(”字符是可选的.

### 将命令组合在一起

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

### 内置的命令或函数

### 命令行编辑

## 退出状态

shell 检测到的错误(例如语法错误)将导致 shell 以非零退出状态退出. 如果 shell 不是交互式 shell, 则 shell 文件的执行将被中止. 否则, shell 将返回最后执行的命令的退出状态, 或者如果 exit 内置函数与数字参数一起使用, 它将返回该参数.

## 环境变量

|环境变量 | 解释 |
|---|---|
|HOME      | Set automatically by login(1) from the user's login directory in the password file (passwd(4)).  This environment variable also functions as the default argument for the cd builtin.|
|PATH      | The default search path for executables.  See the above section Path Search.|
|CDPATH    | The search path used with the cd builtin.|
|MAIL      | The name of a mail file, that will be checked for the arrival of new mail.  Overridden by MAILPATH.|
|MAILCHECK | The frequency in seconds that the shell checks for the arrival of mail in the files specified by the MAILPATH or the MAIL file.  If set to 0, the check will occur at each prompt.|
|MAILPATH  | A colon “:” separated list of file names, for the shell to check for incoming mail.  This environment setting overrides the MAIL setting.  There is a maximum of 10 mailboxes that can be monitored at once.|
|PS1       | The primary prompt string, which defaults to “$ ”, unless you are the superuser, in which case it defaults to “# ”.|
|PS2       | The secondary prompt string, which defaults to “> ”.|
|PS4       | Output before each line when execution trace (set -x) is enabled, defaults to “+ ”.|
|IFS       | Input Field Separators.  This is normally set to ⟨space⟩, ⟨tab⟩, and ⟨newline⟩.  See the White Space Splitting section for more details.|
|TERM      | The default terminal setting for the shell.  This is inherited by children of the shell, and is used in the history editing modes.|
|HISTSIZE  | The number of lines in the history buffer for the shell.|
|PWD       | The logical value of the current working directory.  This is set by the cd command.|
|OLDPWD    | The previous logical value of the current working directory.  This is set by the cd command.|
|PPID      | The process ID of the parent process of the shell.|


## 文件

`$HOME/.profile`

`/etc/profile`

## 引用

csh(1), echo(1), getopt(1), ksh(1), login(1), printf(1), test(1), getopt(3), passwd(5), environ(7), sysctl(8)

## 历史

dash 是 `/bin/sh` 的 POSIX 兼容实现, 旨在尽可能小. dash 是 ash 的 NetBSD 版本(Almquist SHell)的直接后代, 于 1997 年初移植到 Linux. 它在 2002 年更名为 dash.

## BUGS

应尽量避免使用 Setuid shell 脚本, 因为它们存在重大安全风险.

PS1、PS2、PS4在显示前需进行参数扩展.

BSD January 19 2003 BSD