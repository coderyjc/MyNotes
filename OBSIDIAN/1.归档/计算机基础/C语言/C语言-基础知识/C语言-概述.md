## C语言-概述

### C语言

一提到语言这个词语，自然会想到的是像英语、汉语等这样的自然语言，因为它是人和人交换信息不可缺少的工具。

而今天计算机遍布了我们生活的每一个角落，除了人和人的相互交流之外，我们必须和计算机角落。

用什么的什么样的方式和计算机做最直接的交流呢？人们自然想到的是最古老也最方便的方式——语言，而C语言就是人和计算机交流的一种语言。

语言是用来交流沟通的。有一方说，有另一方听，必须有两方参与，这是语言最重要的功能：

>  说的一方传递信息，听的一方接收信息；

> 说的一方下达指令，听的一方遵循命令做事情。

<font color="red">语言是人和人交流，C语言是人和机器交流</font>。只是，人可以不听另外一个人，但是，计算机是无条件服从。

语言有独特的语法规则和定义，双方必须遵循这些规则和定义才能实现真正的交流。

### 为什么学C语言

#### C语言特点

- 优点
  - 代码量小
  - 执行速度快
  - 功能强大
  - 编程自由
- 缺点
  - 写代码实现周期长
  - 可移植性较差
  - 过于自由，经验不足易出错
  - 对平台库依赖较多 

#### C语言应用领域

C语言的应用极其广泛，从网站后台，到底层操作系统，从多媒体应用到大型网络游戏，均可使用C语言来开发：

- 写网站后台程序

- 专门针对某个主题写出功能强大的程序库

- 写出大型游戏的引擎

- 写出另一个语言来

- 写操作系统和驱动程序，并且只能用C语言编写

- 任何设备只要配置了微处理器，就都支持C语言。从微波炉到手机，都是由C语言技术来推动的

![[img/clip_image002.png]]

#### C语言关键字

> C语言仅有32个关键字，9种控制语句，34种运算符，却能完成无数的功能：

![[img/clip_image002-1600476849331.jpg]]

![[img/clip_image002-1600476855287.jpg]]

![[img/clip_image002-1600476859772.jpg]]

### 第一个C语言程序：HelloWorld

#### 编写C语言代码：hello.c

```c
#include <stdio.h>

int main(){
	// 第一个C语言程序
	printf("hello world\n");
	return 0;
}
```

> C语言的源代码文件是一个普通的文本文件，<font color="red">但扩展名必须是.c</font>

![[img/image-20200919090134713.png]]

#### 通过gcc编译C代码

1. **gcc编译器介绍**

编辑器(如vi、记事本)是指我用它来写程序的（编辑代码），而我们写的代码语句，电脑是不懂的，我们需要把它转成电脑能懂的语句，编译器就是这样的转化工具。就是说，<font color="red">我们用编辑器编写程序，由编译器编译后才可以运行！</font>

编译器是将易于编写、阅读和维护的高级计算机语言翻译为计算机能解读、运行的低级机器语言的程序

gcc（GNU Compiler Collection，GNU 编译器套件），是由 GNU 开发的编程语言编译器。gcc原本作为GNU操作系统的官方编译器，现已被大多数类Unix操作系统（如Linux、BSD、Mac OS X等）采纳为标准的编译器，gcc同样适用于微软的Windows

gcc最初用于编译C语言，随着项目的发展gcc已经成为了能够编译C、C++、Java、Ada、fortran、Object C、Object C++、Go语言的编译器大家族

编译命令格式：

```cmd
gcc [-option1] ... <filename>
g++ [-option1] ... <filename>
```

- 命令、选项和源文件之间使用空格分隔

- 一行命令中可以有零个、一个或多个选项

- 文件名可以包含文件的绝对路径，也可以使用相对路径

- 如果命令中不包含输出可执行文件的文件名，可执行文件的文件名会自动生成一个默认名，Linux平台为`a.out`，Windows平台为`a.exe`

gcc、g++编译常用选项说明：

| **选项** | **含义**                   |
| -------- | -------------------------- |
| -o file  | 指定生成的输出文件名为file |
| -E       | 只进行预处理               |
| -S(大写) | 只进行预处理和编译         |
| -c(小写) | 只进行预处理、编译和汇编   |

2. **Windows平台下gcc环境配置**

> windows命令行界面下，默认是没有gcc编译器，我们需要配置一下环境

> `MinGW`, 安装使用教程参看：[MinGW安装教程](https://blog.csdn.net/wxh0000mm/article/details/100666329)

3. **linux平台下gcc环境配置**

> 参考教程：[详解Linux安装GCC方法](https://blog.csdn.net/lydong_/article/details/79812402)

#### 代码分析

```php
#include <stdio.h>

/*
#include的意思是头文件包含,
#include <stdio.h>代表包含stdio.h这个头文件

使用C语言库函数需要提前包含库函数对应的头文件，如这里使用了printf()函数，需要包含stdio.h头文件
*/

int main(){
	// 第一个C语言程序
	printf("hello world\n"); // 可以通过man 3 printf查看printf所需的头文件
	return 0;
}
```

1. **include头文件包含**

- `#include< >` 与 `#include ""`的区别：

- `< >` 表示系统<font color="red">直接</font>按系统指定的目录检索

- `" "` 表示系统<font color="red">先</font>在` " " `指定的路径(没写路径代表当前路径)查找头文件，如果找不到，<font color="red">再</font>按系统指定的目录检索

`stdio.h` 在操作系统`/usr/include/`目录下

![[img/image-20200919092034856.png]]

2. **main函数**

- 一个完整的C语言程序，是由一个、<font color="red">且只能有一个</font>`main()`函数(又称主函数，必须有)和若干个其他函数结合而成（可选）
- `main`函数是C语言程序的入口，程序是从main函数开始执行

3. **{} 括号，程序体和代码块**

- `{}`叫代码块，一个代码块内部可以有一条或者多条语句
- C语言每句可执行代码都是"`;`"分号结尾
- 所有的`#`开头的行，都代表预编译指令，预编译指令行结尾是没有分号的
- 所有的可执行语句必须是在代码块里面

4.  **注释**

- `//`叫行注释，注释的内容编译器是忽略的，注释主要的作用是在代码中加一些说明和解释，这样有利于代码的阅读
- `/**/`叫块注释
- 块注释是C语言标准的注释方法
- 行注释是从C++语言借鉴过来的

5. **printf函数**

- `printf`是C语言库函数，功能是向标准输出设备输出一个字符串

- `printf(“hello world\n”);` //`\n`的意思是回车换行

6.  **return语句**

- `return` 代表函数执行完毕，返回return代表函数的终止

- 如果main定义的时候前面是`int`，那么return后面就需要写一个整数；如果main定义的时候前面是`void`，那么return后面什么也不需要写

- 在main函数中`return 0`代表程序执行成功，`return -1`代表程序执行失败

- `int main()`和`void main()`在C语言中是一样的，但C++只接受`int main`这种定义方式

### system函数

#### system函数的使用

```php
#include <stdlib.h>

int system(const char *command);
```

> 功能：在已经运行的程序中执行另外一个外部程序
> 参数：外部可执行程序名字
> 返回值：
> 成功：0
> 失败：任意数字

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
	//system("calc"); //windows平台
	system("ls"); //Linux平台, 需要头文件#include <stdlib.h>

	return 0;
}

```

![[img/image-20200919094712699.png]]

### C语言编译过程

#### C程序编译步骤

> C代码编译成可执行程序经过4步：

1. 预处理：宏定义展开、头文件展开、条件编译等，同时将代码中的注释删除，这里并不会检查语法
2. 编译：检查语法，将预处理后文件编译生成汇编文件
3. 汇编：将汇编文件生成目标文件(二进制文件)
4. 链接：C语言写的程序是需要依赖各种库的，所以编译之后还需要把库链接到最终的可执行程序中去

![[img/clip_image002-1600480373517.png]]

> VS 执行结果一闪而过的解决方法：

1. `system("pause");`

2. `项目->属性->配置属性->链接器->系统->子系统->控制台 增加“/SUBSYSTEM:CONSOLE”链接选项即可`

#### gcc 编译过程

1. **分步编译**

> 预处理：`gcc -E introduce.c -o introduce.i`

> 编 译：`gcc -S introduce.i -o introduce.s`

> 汇 编：`gcc -c introduce.s -o introduce.o`

> 链 接：`gcc  introduce.o -o introduce`

| **选项** | **含义**                    |
| -------- | --------------------------- |
| -E       | 只进行预处理                |
| -S(大写) | 只进行预处理和编译          |
| -c(小写) | 只进行预处理、编译和汇编    |
| -o file  | 指定生成的输出文件名为 file |


| **文件后缀** | **含义**              |
| ------------ | --------------------- |
| .c           | C 语言文件            |
| .i           | 预处理后的 C 语言文件 |
| .s           | 编译后的汇编文件      |
| .o           | 编译后的目标文件      |

编译的时候最后两倒数第二步的时候用了大写`C`

`gcc -C introduce.s -o introduce.o`

`gcc introduce.o -o introduce`

导致了如下问题， 记录一下

```text
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/8/../../../x86_64-linux-gnu/Scrt1.o: in function `_start':
(.text+0x20): undefined reference to `main'
collect2: error: ld returned 1 exit status
```

![[img/image-20200919101105887.png]]

正确的编译过程

```bash
gcc -E introduce.c -o introduce.i
gcc -S introduce.i -o introduce.s
gcc -c introduce.s -o introduce.o
gcc introduce.o -o introduce
./introduce 
```

![[img/image-20200919101944251.png]]

2. **一步编译**

`gcc introduce.c -o introduce1` // 自动完成：预处理、编译、汇编、链接的过程

![[img/image-20200919102259922.png]]

#### 查找程序所依赖的动态库

Windows平台下，需要相应软件(`Depends.exe`)：

> 工具下载地址：http://www.dependencywalker.com/

![[img/image-20200919102850515.png]]

![[img/image-20200919102938934.png]]

### CPU内部结构与寄存器

#### 64位和32位系统区别

- 寄存器是CPU内部最基本的存储单元
- CPU对外是通过总线(地址、控制、数据)来和外部设备交互的，<font color="red">总线的宽度是8位，同时CPU的寄存器也是8位</font>，那么这个CPU就叫8位CPU

- 如果总线是32位，寄存器也是32位的，那么这个CPU就是32位CPU
- 有一种CPU内部的寄存器是32位的，但总线是16位，准32为CPU
- 所有的64位CPU兼容32位的指令，32位要兼容16位的指令，所以在64位的CPU上是可以识别32位的指令
- 在64位的CPU构架上运行了64位的软件操作系统，那么这个系统是64位
- 在64位的CPU构架上，运行了32位的软件操作系统，那么这个系统就是32位
- 64位的软件不能运行在32位的CPU之上

#### 寄存器名字

| **8**位 | **16**位 | **32**位 | **64**位 |
| ------- | -------- | -------- | -------- |
| A       | AX       | EAX      | RAX      |
| B       | BX       | EBX      | RBX      |
| C       | CX       | ECX      | RCX      |
| D       | DX       | EDX      | RDX      |

#### 寄存器、缓存、内存三者关系

按与CPU远近来分，离得最近的是寄存器，然后缓存(CPU缓存)，最后内存。

CPU计算时，先预先把要用的数据从硬盘读到内存，然后再把即将要用的数据读到寄存器。于是 CPU<--->寄存器<--->内存，这就是它们之间的信息交换。

那为什么有缓存呢？因为如果经常操作内存中的同一址地的数据，就会影响速度。于是就在寄存器与内存之间设置一个缓存。

因为从存提取的速度远高于内存。当然缓存的价格肯定远远高于内存，不然的话，机器里就没有内存的存在。

### 汇编语言

#### VS中C语言嵌套汇编代码

```c
#include <stdio.h>

int main()
{
	//定义整型变量a, b, c
	int a;
	int b;
	int c;

	__asm
	{
		mov a, 3	//3的值放在a对应内存的位置
		mov b, 4	//4的值放在b对应内存的位置
		mov eax, a	//把a内存的值放在eax寄存器
		add eax, b	//eax和b相加，结果放在eax
		mov c, eax	//eax的值放在c中
	}
	
	printf("%d\n",  c);//把c的值输出

	return 0;//成功完成
}
```

#### VS反编译

```c
#include <stdio.h>

int main()
{
	//定义整型变量a, b, c
	int a;
	int b;
	int c;

	a = 3;
	b = 4;
	c = a + b;
	
	printf("%d\n",  c);//把c的值输出

	return 0;//成功完成
}
```
