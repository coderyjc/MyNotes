# Operating System

> 这是 [bilibili-[完结] 2020 南京大学 “操作系统：设计与实现” (蒋炎岩)](https://www.bilibili.com/video/BV1N741177F5) 的课程笔记



## 【C1】应用眼中的操作系统；系统调用




```
本节内容概要：
- 一个最小的不依赖任何库函数的程序
	- 经过编译、链接，被操作系统加载
	- 调用操作系统API（系统调用）
- 粗浅地讲解了应用程序使用何种API实现
	- 编译器、图形界面程序等
```

> 什么是程序？

可执行文件（程序的二进制代码和数据）和其他数据文件

Linux支持多重可执行文件格式，**ELF**二进制文件是其中最常用的

`file 命令查看文件信息`

```bash
❯ vim a.c
❯ gcc -c a.c
❯ ls
a.c  a.o
❯ file a.c
a.c: C source, ASCII text
❯ file a.o
a.o: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped
❯ gcc a.o
❯ file a.out
a.out: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e4a5d3ec4e9319f61211fa13d0e1c32a7db7374d, for GNU/Linux 3.2.0, not stripped
```

运行中的程序成为进（正在运行的）程（程序）

- 操作系统中会有很多进程对象 `ps命令查看进程`
- 在运行时，进程会
  - 在CPU上执行，进行计算
  - 使用操作系统的API访问操作系统中的其他对象

### ELF二进制文件

可执行文件也是普通的文件

- 操作系统的一个对象

- 一个存储在文件系统上的字节序列

  - 和文本文件没有本质区别

  - 操作系统提供API打开、读取、改写（都需要相应的权限）

  - 因此我们可以用xxd、 vim 、 cat 等命令查看可执行文件

    - 在vim中打开，二进制部分显示异常，但可以看到字符串常量（vim /bin/ls）
    - 使用xxd（命令分析工具）可以看到文件以 “\x7f” “ELF”开头

    ```bash
    ❯ xxd /bin/ls | less
    00000000: 7f45 4c46 0201 0100 0000 0000 0000 0000  .ELF............
    00000010: 0300 3e00 0100 0000 1068 0000 0000 0000  ..>......h......
    00000020: 4000 0000 0000 0000 1834 0200 0000 0000  @........4......
    ...
    ```

    

**解析ELF文件**

readelf 是专门解析ELF可执行文件工具；我们主要关注：

- header（元数据）
  - 文件内容分布
  - 指令集体系结构
  - 入口地址
- ELF的program headers 决定了ELD如何被加载

```bash
❯ readelf -h /bin/ls
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x6810 # 第一条指令的位置
  Start of program headers:          64 (bytes into file)
  Start of section headers:          144408 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         13
  Size of section headers:           64 (bytes)
  Number of section headers:         31
  Section header string table index: 30
```

`/usr/include/elf.h` 提供了必要的定义


### 应用程序如何调用操作系统？

#### 失败的尝试#1

假设我们要写一个最小的程序，只输出一句话

```c
#include<stdio.h>
int main(){
        printf("hello world!\n");
}
```

```bash
❯ gcc -c hello.c
❯ ld hello.o
ld: warning: cannot find entry symbol _start; defaulting to 0000000000401000
ld: hello.o: in function `main':
hello.c:(.text+0x10): undefined reference to `puts'
# 我们已经引入了相关的库了，为什么还报错？而且为什么是 puts 不是 printf ？
```

为什么是puts？

- gcc 在 -00 选项下依然会进行一定程度的编译优化
- 这是导致一些编译器bug 的源头

undefined reference to `puts'

- puts是库函数
- 把库函数也链接进来就不是我们要写的最小的程序了
- 放弃这个写法

cannot find entry symbol _start

- _start是连接器默认的入口
- 可以用 -e 指定 比如 -e main

#### 失败的尝试#2

我们连这一句话也不输出了

```c
int main(){
}
```

这样总行了吧？

```bash
❯ vim hello.c
❯ gcc -c hello.c
❯ objdump -d hello.o

hello.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <main>:
   0:	f3 0f 1e fa          	endbr64 
   4:	55                   	push   %rbp
   5:	48 89 e5             	mov    %rsp,%rbp
   8:	b8 00 00 00 00       	mov    $0x0,%eax
   d:	5d                   	pop    %rbp
   e:	c3                   	retq   
❯ ld -e main hello.o
❯ ./a.out
[1]    15746 segmentation fault (core dumped)  ./a.out
```

我们只保留了main函数，编译的时候指定了入口函数，我们查看了汇编代码发现并没有调用任何函数，这已经是最简形式了。

**为什么还错误？**

#### 为什么？？？？

一个工具帮助我们观察程序的执行

GDB！！！！

- starti 可以帮助我们从第一条指令开始执行程序
- layout asm 可以方便地查看汇编（将视图转换为汇编视图）
- info register 可以查看寄存器

通过调试，我们发现前几步都没有问题。

问题出在最后的return上。

```bash
lqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqk
x   0x401000 <main>         endbr64                                                      x
x   0x401004 <main+4>       push   %rbp                                                  x
x   0x401005 <main+5>       mov    %rsp,%rbp                                             x
x   0x401008 <main+8>       mov    $0x0,%eax                                             x
x   0x40100d <main+13>      pop    %rbp                                                  x
x  >0x40100e <main+14>      retq                                                         x
x   0x40100f                    add    %al,(%rax)                                        x
x   0x401011                    add    %al,(%rax)                                        x
x   0x401013                    add    %al,(%rax)                                        x
mqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqj
native process 16992 In:                                                    L??   PC: 0x1 
(gdb) si
0x0000000000401004 in main ()
0x0000000000401005 in main ()
0x0000000000401008 in main ()
0x000000000040100d in main ()
0x000000000040100e in main ()
0x0000000000000001 in ?? ()
Cannot access memory at address 0x1
```

如果执行return指令的话会产生非法的内存访问，因为栈上还有一些其他的数值。然后就崩掉了。

操作系统做了什么？

- 加载程序并初始化运行环境（寄存器、代码、数据、堆栈）
- 从 _start 开始执行 （初试的 %rip PC）

#### 成功的尝试：汇编

main的确运行了，只是在返回的时候crash 了

我们只要写出正确的指令序列，就可以在操作系统上正常运行了

例子：

- 执行100%我们自己的代码
- 调用API打印Helloworld
- 调用API退出

```assembly
.globl foo
foo:
  movl $1,      %eax
  movl $1,      %edi
  movq $s,      %rsi
  movl $(e-s),  %edx
  syscall

  movl $60,     %eax
  movl $1,      %edi
  syscall

s:
  .ascii "\033[01;31mHello World\033[0m\n"
e:
```

```bash
❯ gcc -c minimal.S
❯ ld -e foo minimal.o
❯ ./a.out
Hello World
```

或者写成以下的C代码：

```c
#include<unistd.h>
#include<sys/syscall.h>

#define LENGTH(arr) (sizeof(arr) / sizeof(arr[0]))

const char hello[] = "\033[01;31mHello World\033[0m\n";

int main(){
	syscall(SYS_write, 1, hello, LENGTH(hello));
	syscall(SYS_exit, 1);
}
```

```bash
❯ gcc syscall-demo.c
❯ ./a.out
Hello World
```

成功执行。

应用程序通过设置参数和syscall指令调用操作系统

#### syscall 的代码在哪里？

介绍工具：`objdump`

查看目标文件二进制信息的工具

```bash
❯ gcc  -g syscall-demo.c #把源代码信息一起包装到二进制文件重
❯ objdump -S a.out| less # 查看文件的汇编信息

...

const char hello[] = "\033[01;31mHello World\033[0m\n";

int main(){
    1149:       f3 0f 1e fa             endbr64 
    114d:       55                      push   %rbp
    114e:       48 89 e5                mov    %rsp,%rbp
        syscall(SYS_write, 1, hello, LENGTH(hello));
    1151:       b9 19 00 00 00          mov    $0x19,%ecx
    1156:       48 8d 15 b3 0e 00 00    lea    0xeb3(%rip),%rdx        # 2010 <hello>
    115d:       be 01 00 00 00          mov    $0x1,%esi
    1162:       bf 01 00 00 00          mov    $0x1,%edi
    1167:       b8 00 00 00 00          mov    $0x0,%eax
    116c:       e8 df fe ff ff          callq  1050 <syscall@plt>
        syscall(SYS_exit, 1);
    1171:       be 01 00 00 00          mov    $0x1,%esi
    1176:       bf 3c 00 00 00          mov    $0x3c,%edi
    117b:       b8 00 00 00 00          mov    $0x0,%eax
    1180:       e8 cb fe ff ff          callq  1050 <syscall@plt>
    1185:       b8 00 00 00 00          mov    $0x0,%eax
}

```

在执行syscall之前有 `    116c:       e8 df fe ff ff          callq  1050 <syscall@plt>` 其中 plt 表示这是一个动态链接的函数，并没有在二进制文件里。

也就是说，main函数执行的时候，在syscall之前一定有一些代码把库函数包含在了程序的地址空间里了。

> 面试题：main() 之前发生了什么？ 也就是说，当你写了一个程序的时候这个程序执行的第一条指令在哪里？
>
> 在 /lib64/ld-linux-x86-64.so.2下的 _start() 系统内置的一个加载器

#### main之前发生了什么？

看一个栗子：

```c
#include<stdio.h>

__attribute__((constructor)) void hello() {
	printf("Hello, OS\n");
}

__attribute__((destructor)) void goodbye() {
	printf("Goodbye, OS\n");
}

int main(){
}
```

```bash
❯ gcc hello-goodbye.c
❯ ./a.out
Hello, OS
Goodbye, OS
```

虽然main是空的，但是依然打印出了 hello 和 goodbye。

这就说明main的开始并不是整个程序的开始。

**main之前发生了哪些操作系统API的调用？**

工具： strace

打印一个进程的系统调用事件

`strace ./a.out`

```c
execve("./a.out", ["./a.out"], 0x7ffd7edb1320 /* 65 vars */) = 0
brk(NULL)                               = 0x557f8f045000
arch_prctl(0x3001 /* ARCH_??? */, 0x7fff064eb4f0) = -1 EINVAL (Invalid argument)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=64302, ...}) = 0
mmap(NULL, 64302, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f31c1d43000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\360\215\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
pread64(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0", 32, 848) = 32
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0~\303\347M\250B\312<j\233\242\v!0<\341"..., 68, 880) = 68
fstat(3, {st_mode=S_IFREG|0755, st_size=1995896, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f31c1d41000
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
mmap(NULL, 2004064, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f31c1b57000
mprotect(0x7f31c1b7d000, 1810432, PROT_NONE) = 0
mmap(0x7f31c1b7d000, 1495040, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x26000) = 0x7f31c1b7d000
mmap(0x7f31c1cea000, 311296, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x193000) = 0x7f31c1cea000
mmap(0x7f31c1d37000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1df000) = 0x7f31c1d37000
mmap(0x7f31c1d3d000, 13408, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f31c1d3d000
close(3)                                = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f31c1b55000
arch_prctl(ARCH_SET_FS, 0x7f31c1d42540) = 0
mprotect(0x7f31c1d37000, 12288, PROT_READ) = 0
mprotect(0x557f8daaa000, 4096, PROT_READ) = 0
mprotect(0x7f31c1d81000, 4096, PROT_READ) = 0
munmap(0x7f31c1d43000, 64302)           = 0
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0), ...}) = 0
brk(NULL)                               = 0x557f8f045000
brk(0x557f8f066000)                     = 0x557f8f066000
write(1, "Hello, OS\n", 10Hello, OS
)             = 10
write(1, "Goodbye, OS\n", 12Goodbye, OS
)           = 12
exit_group(0)                           = ?
+++ exited with 0 +++
```

当把输出重定向到 /dev/null 中的时候会有如下差异：

```c
...

write(1, "Hello, OS\nGoodbye, OS\n", 22) = 22

...
```



### 应用眼中的操作系统

本质上所有程序和Hello World类似

- 被操作系统加载
  - 通过父进程的 execve
- 不断执行系统调用
  - 进程管理：fork\execve\exit
  - 文件/设备管理：open\close\read\write
  - 存储管理：mmap\brk
- 直到_exit(exit_group)退出



编译器（gcc）

- strace -f gcc a.c
- 执行程序
  - cc1 - 编译器
  - as - 汇编器
  - collect2 - 收集器
  - ld - 链接



图形界面程序本质上和其他程序是类似的。



各种各样的应用程序都是在非常精简的操作系统api上运行的

- 窗口管理器：管理设备和屏幕（read/write/mmap）；进程通信（send/recv）
- 任务管理器：访问操作系统提供的进程对象(readdir/read)
- 杀毒软件：文件静态扫描（read）扫描危险代码; 动态防御(ptrace)
  - 拦截系统调用















