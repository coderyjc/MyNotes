# Operating System

> 这是 [bilibili-[完结] 2020 南京大学 “操作系统：设计与实现” (蒋炎岩)](https://www.bilibili.com/video/BV1N741177F5) 的课程笔记



## 【Code-1】应用眼中的操作系统；系统调用




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



## 【Con-1】多处理器编程：从入门到放弃



```
本讲概要：
什么是并发、为什么需要并发、并发编程初识
放弃程序的原子性、顺序性、可见性
```

### 并发与并行

假设系统只有一个CPU

操作系统可以同时加载多个程序（进程）

- 每个进程都有独立的地址空间里，不会互相干扰
- 即便有root权限的进程，也不会直接访问操作系统内核的内存
- 每隔一段时间就切换到另一个进程进行

多任务操作系统中的并发：

并发性的来源：进程会调用操作系统的API

- write(fd, bug, 1 TiB)

- write 的实现是操作系统的一部分
  - x86-64 应用程序执行syscall后就进入操作系统执行（应用程序不可见）
  - 类似中断处理程序
  - 运行在处理器的高特权级：能访问硬件设备（否则就不能写数据了）
  - 不能一直霸占着处理器运行（否则系统就卡死了）
- 因此必须允许write到一半的时候，让另一个进程执行
  - 另一个进程调用read(fd, buf, 512 MiB)读取同一个文件
  - 操作系统API需要考虑并发

并发（Concurrency）：多个执行流可以不按照一个特定的顺序执行

并行（Parallelism）：允许多个执行流同时执行（多处理器）

| 处理器数量 | 共享内存   | 典型的并发系统               | 并发并行   |
| ---------- | ---------- | ---------------------------- | ---------- |
| 单处理器   | 共享内存   | OS内核/多线程程序            | 并发不并行 |
| 多处理器   | 共享内存   | OS内核/多线程程序/GPU Kernel | 并发并行   |
| 多处理器   | 不共享内存 | 分布式系统（消息通信）       | 并发并行   |

### 多处理器编程：入门

#### 线程

线程：多个执行流并发/并发执行，并且他们共享内存

- 两个执行流共享代码和所有全局变量（数据、堆区）
- 线程之间的执行顺序是不确定的（non-deterministic）的

```c
int x = 0, y = 0;

void thread_1(){
    x  = 1; // [1]
    printf("y = %d\n",y); // [2]
}

void thread_2(){
    y = 1; // [3]
    printf("x = %d\n",x); // [4]
}
```

1 - 2 - 3 - 4 (y=0,x=1)

1 - 3- 2 - 4 (y=1, x=1)

...

#### 线程：什么该共享、什么不共享？

```c
extern int x;
int foo(){
    int volatile t = x;
    t += 1;
    x = t;
}
```

考虑如果有两个执行流同时调用foo，哪些资源是共享的?

- foo的代码（1140_115f）
  - 这个函数可以被所有线程调用，所以是共享的
- 寄存器：rip\rsp\rax
- 变量：x:0x2eb5
  - 线程之间会共享数据，所以全局变量是共享的

除了代码和全局数据之外，每一个线程的堆栈和寄存器都是他们独享的

#### POSIX Threads

- 使用 pthread_create 创建并运行线程
  - 得到若干个共享了当前地址空间的线程
- 使用pthread_join 等待某个线程结束

可以使用`man 7 pthreads`查看pthreads的帮助文档

> 帮助文件man：
>
>man 1：用户命令（可执行命令和shell程序）
>
>man 2：系统调用（从用户空间调用的内核例程）
>
>man 3：库函数（有程序库提供）
>
>man 4：特殊文件（如设备文件）
>
>man 5：文件格式（用于许多配置文件和结构）
>
>man 6：游戏（过去的有趣程序章节）
>
>man 7：惯例、标准和其他（协议、文件系统）
>
>man 8：系统管理和特权命令（维护任务）
>
>man 9：Linux 内核API（内核调用）

无论系统是单处理器还是多处理器，都得到了若干共享了当前进程地址空间的线程

- 共享代码：所有线程的代码都来自于当前进程的代码
- 共享数据：全局数据/堆区可以自由引用
- 独立堆栈：每个线程有独立的堆栈

#### threads.h: Simplified Thread APIs

create(fn)

- 创建并运行一个线程，该线程立即开始执行函数 fn
- 函数原型 :void fn(int tid){}
- tid从1开始编号

join(fn)

- 当代所有线程执行结束
- 执行函数 fn
- 只能 join 一次

#### threads.h实现

数据结构：

```c
struct thread {
  int id; // 线程号
  pthread_t thread; // pthread 线程api中的线程号
  void (*entry)(int); // 入口地址
  struct thread *next; // 链表
};

struct thread *threads; // 链表头
void (*join_fn)(); // 回调函数
```

线程创建实现：

```c
static inline void *entry_all(void *arg) {
  struct thread *thread = (struct thread *)arg;
  thread->entry(thread->id);
  return NULL;
}

static inline void create(void *fn) {
  struct thread *cur = (struct thread *)malloc(sizeof(struct thread)); // 分配给线程内存
  assert(cur); //假设内存分配成功
  cur->id    = threads ? threads->id + 1 : 1; // 分配线程号
  cur->next  = threads;
  cur->entry = (void (*)(int))fn;
  threads    = cur;
  pthread_create(&cur->thread, NULL, entry_all, cur); // 调用posix的api
}
```

线程join实现

```c
static inline void join(void (*fn)()) {
  join_fn = fn;
}

__attribute__((destructor)) static void join_all() {
  for (struct thread *next; threads; threads = next) {
      // 等待所有线程结束
    pthread_join(threads->thread, NULL);
    next = threads->next;
    free(threads);
  }
  join_fn ? join_fn() : (void)0; // 调用回调函数
}
```

thread.h 

```c
// threads.h

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <pthread.h>

struct thread {
  int id;
  pthread_t thread;
  void (*entry)(int);
  struct thread *next;
};

struct thread *threads;
void (*join_fn)();

// ========== Basics ==========

__attribute__((destructor)) static void join_all() {
  for (struct thread *next; threads; threads = next) {
    pthread_join(threads->thread, NULL);
    next = threads->next;
    free(threads);
  }
  join_fn ? join_fn() : (void)0;
}

static inline void *entry_all(void *arg) {
  struct thread *thread = (struct thread *)arg;
  thread->entry(thread->id);
  return NULL;
}

static inline void create(void *fn) {
  struct thread *cur = (struct thread *)malloc(sizeof(struct thread));
  assert(cur);
  cur->id    = threads ? threads->id + 1 : 1;
  cur->next  = threads;
  cur->entry = (void (*)(int))fn;
  threads    = cur;
  pthread_create(&cur->thread, NULL, entry_all, cur);
}

static inline void join(void (*fn)()) {
  join_fn = fn;
}

// ========== Synchronization ==========

#include <stdint.h>

intptr_t atomic_xchg(volatile intptr_t *addr,
                               intptr_t newval) {
  // swap(*addr, newval);
  intptr_t result;
  asm volatile ("lock xchg %0, %1":
    "+m"(*addr), "=a"(result) : "1"(newval) : "cc");
  return result;
}

intptr_t locked = 0;

static inline void lock() {
  while (1) {
    intptr_t value = atomic_xchg(&locked, 1);
    if (value == 0) {
      break;
    }
  }
}

static inline void unlock() {
  atomic_xchg(&locked, 0);
}

#include <semaphore.h>

#define P sem_wait
#define V sem_post
#define SEM_INIT(sem, val) sem_init(&(sem), 0, val)
```



####  多线程入门：

编写程序，引入thread.h

有两种引用方法：

1. 将 thread.h 和源程序放在同一个文件夹下，`#include"thread.h"`

2. 使用 -I 路径 增加一个include path`gcc -I. a.c`

   ```bash
   ❯ gcc -I. a.c
   /usr/bin/ld: /tmp/ccGTJbHj.o: in function `join_all':
   a.c:(.text+0x22): undefined reference to `pthread_join'
   /usr/bin/ld: /tmp/ccGTJbHj.o: in function `create':
   a.c:(.text+0x150): undefined reference to `pthread_create'
   collect2: error: ld returned 1 exit status
   ```

可以看出修改了路径还是有错误

这是因为我们代码中调用了pthread，但是没有链接pthread这个文件。

用 -l 这个选项把pthread这个库链接进来

```bash
❯ gcc a.c -l pthread
❯ ls
a.c  a.out 
```

编译成功

使用ldd查看 a.out 可以看到需要pthread这个库

```bash
❯ ldd a.out
	linux-vdso.so.1 (0x00007ffc25dcc000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fe681014000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe680e2a000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fe68104d000)
```

执行 a.out 可以看到ab间隔打印。

更多的栗子

1. 如何相信真的启动了多个线程？

```c
// hello-mt.c
#include "threads.h"

void f() {
  static int x = 0;
  printf("Hello from thread #%d\n", x++);
  while (1);
}

int main() {
  for (int i = 0; i < 10; i++) {
    create(f);
  }
  join(NULL);
}
```

创建10和线程，执行函数f，每次创建的时候输出当前的线程号。

```bash
❯ gcc hello-mt.c -l pthread
❯ ./a.out
Hello from thread #1
Hello from thread #2
Hello from thread #3
Hello from thread #6
Hello from thread #0
Hello from thread #4
Hello from thread #7
Hello from thread #8
Hello from thread #5
Hello from thread #9
^C
```

我们可以发现有10个线程被创建了，这证明了所有的线程是共享内存的，共享了变量 x

但是并不是按照顺序创建的，关于这个问题，我们会在以后的课程中讲解

2. 知道每一个线程的堆栈范围大小

```c
// stack-probe.c
#include "threads.h"

__thread char *base, *now; // 每一个线程独享的变量
__thread int id;
/*
base 是线程的大概的基地址
now 是线程栈当前的地址
id 是线程号
*/

// objdump to see how thread local variables are implemented
void set_base(char *ptr) { base = ptr; }
void set_now(char *ptr)  { now = ptr; }
void set_base(char *ptr) { base = ptr; }
void set_now(char *ptr)  { now = ptr; }
void *get_base()         { return &base; }
void *get_now()          { return &now; }

void stackoverflow(int n) {
  // 无穷递归
  char x;
  if (n == 0) set_base(&x);
  set_now(&x);
  if (n % 1024 == 0) {
  // 每循环 1024 次，就打印 线程ID，递归次数，基地址和地址差值
    printf("[T%d] Stack size @ n = %d: %p +%ld KiB\n",
      id, n, base, (base - now) / 1024);
  }
  stackoverflow(n + 1); 
}

void probe(int tid) {
  id = tid;
  printf("[%d] thread local address %p\n", id, &base);
  stackoverflow(0);
}

int main() {
  setbuf(stdout, NULL);
  for (int i = 0; i < 4; i++) { // 创建4个线程，每一个线程都执行probe
    create(probe);
  }
  join(NULL);
}
```

```bash
❯ gcc stack-probe.c -l pthread
❯ ./a.out
[1] thread local address 0x7f52bb69d628
[T1] Stack size @ n = 0: 0x7f52bb69cdf7 +0 KiB
[2] thread local address 0x7f52bae9c628
[T1] Stack size @ n = 1024: 0x7f52bb69cdf7 +48 KiB
[T2] Stack size @ n = 0: 0x7f52bae9bdf7 +0 KiB
[T1] Stack size @ n = 2048: 0x7f52bb69cdf7 +96 KiB
[4] thread local address 0x7f52b9e9a628
[T4] Stack size @ n = 0: 0x7f52b9e99df7 +0 KiB
[T2] Stack size @ n = 1024: 0x7f52bae9bdf7 +48 KiB
[T1] Stack size @ n = 3072: 0x7f52bb69cdf7 +144 KiB
[T4] Stack size @ n = 1024: 0x7f52b9e99df7 +48 KiB
[T2] Stack size @ n = 2048: 0x7f52bae9bdf7 +96 KiB
...
...
...
[T2] Stack size @ n = 151552: 0x7f52bae9bdf7 +7104 KiB
[T1] Stack size @ n = 173056: 0x7f52bb69cdf7 +8112 KiB
[T3] Stack size @ n = 148480: 0x7f52ba69adf7 +6960 KiB
[T4] Stack size @ n = 174080: 0x7f52b9e99df7 +8160 KiB
[T1] Stack size @ n = 174080: 0x7f52bb69cdf7 +8160 KiB
[T2] Stack size @ n = 152576: 0x7f52bae9bdf7 +7152 KiB
[1]    37437 segmentation fault (core dumped)  ./a.out
```

栈帧大小到了 8M左右就发生了段错误，线程的内存不够了。

使用pmap可以查看到8192KiB内存映射区域和4KiB（一页）的guard

> 命令 free
>
> - -b 　以Byte为单位显示内存使用情况。
> - -k 　以KB为单位显示内存使用情况。
> - -m 　以MB为单位显示内存使用情况。
> - -h 　以合适的单位显示内存使用情况，最大为三位数，自动计算对应的单位值。单位有：
> - -o 　不显示缓冲区调节列。
> - -s<间隔秒数> 　持续观察内存使用状况。
> - -t 　显示内存总和列。
> - -V 　显示版本信息。

```bash
❯ free -h
              total        used        free      shared  buff/cache   available
Mem:          7.6Gi       2.3Gi       2.6Gi       452Mi       2.8Gi       4.6Gi
Swap:         9.8Gi          0B       9.8Gi
```

我的内存一共不到 8G，**每一个线程要分配8MiB内存，那么为什么1000个线程没有耗尽内存？**

申请一块内存，操作系统不是马上给你一块实际内存，而只是给你一个逻辑地址，当你真的访问这段地址时，操作系统才会进行逻辑地址到物理地址的映射。

修改hello-mt.c，变为3个线程，后台运行，用pmap观察其内存映射关系

```c
#include "threads.h"

void f() {
  static int x = 0;
  printf("Hello from thread #%d\n", x++);
  while (1); // to make sure we're not calling f() for ten times
}

int main() {
  for (int i = 0; i < 3; i++) {
    create(f);
  }
  join(NULL);
}
```

```bash
❯ gcc hello-mt.c -l pthread
❯ ./a.out &
[1] 38856
Hello from thread #0                                                                 
Hello from thread #1
Hello from thread #2
❯ pmap 38856
38856:   ./a.out
0000558e10c44000      4K r---- a.out
0000558e10c45000      4K r-x-- a.out
0000558e10c46000      4K r---- a.out
0000558e10c47000      4K r---- a.out
0000558e10c48000      4K rw--- a.out
0000558e1287c000    132K rw---   [ anon ]
00007fd1a8000000    132K rw---   [ anon ]
00007fd1a8021000  65404K -----   [ anon ]
00007fd1ae049000      4K -----   [ anon ]
00007fd1ae04a000   8192K rw---   [ anon ]
00007fd1ae84a000      4K -----   [ anon ]
00007fd1ae84b000   8192K rw---   [ anon ]
00007fd1af04b000      4K -----   [ anon ]
00007fd1af04c000   8204K rw---   [ anon ]
00007fd1af84f000    152K r---- libc-2.32.so
00007fd1af875000   1460K r-x-- libc-2.32.so
...
```

可以看出在每一个8192k的栈上下都有一个 4k 大小的不可读写的区域，当栈上溢出或者下溢出的时候都会报错。

> 命令 pmap
>
> **Linux pmap命令**用于报告进程的内存映射关系，是Linux调试及运维一个很好的工具。
>
> -x：显示扩展格式
> -d：显示设备格式
> -q：不显示头尾行
> -V：显示指定版本。

### 多处理器编程：放弃

####  原子性

随着线程数量的增加，并发控制的难度越来越大

**案例1：转账**

```c
int pay(int money){
    if (deposit > money){
        deposit -= money;
        return SUCCESS;
    } else {
        return FAIL;
    }
}
```

其中的 deposit 在硬件上的实现是：

```c
int tmp = deposit;
//可能与其他处理器并发
tmp -= money;
//可能与其他处理器并发
deposit = tmp;
```

例如：

线程1：

[1]if(deposit>money)

[3] deposit -= money;

线程2：

[2]if(deposit>money)

[4] deposit -= money;

如果deposit == 100,money==100 那么在1、2两个步骤都会判定为成功，那么经过3.4 , deposit 会变成 -100。显然是不合理的。

**案例2：多线程求和**

分两个线程计算 2n个 1

```c
#include"threads.h"

#define n 10000000
long sum = 0;

void do_sum(){ for(int i = 0; i < n; i++) sum++; }
void print() {printf("sum = %ld\n", sum);}

int main(){
	create(do_sum);
	create(do_sum);
	join(print);
}
```

```bash
❯ gcc sum.c -l pthread
❯ ./a.out
sum = 10261926
```

答案应该是 20000000，可是结果出乎意料。

一种情况：sum++ 被编译成了：`t=sum;t++;sum=t`

这种情况下：

线程1：`[1]t=sum; [5]t++; [6]sum=t`

线程2：`[2]t=sum; [3]t++; [4]sum=t`

t是寄存器，寄存器是每个线程独享的。

sum=0；经过1、2、3、4、5、6步骤之后，sum循环了两次，但是只加了一次，sum=1。

不只是多处理器的时候会这样，在单处理器中，由于程序会发生中断，也会导致类似的情况发生。

即使是最简单的x++也不能保证原子性。


#### 顺序性

让我们以不同的编译优化等级编译这个求 2n 的文件

```bash
❯ gcc -O0 sum.c -o sum-0.out -l pthread
❯ gcc -O1 sum.c -o sum-1.out -l pthread
❯ gcc -O2 sum.c -o sum-2.out -l pthread
❯ ./sum-0.out
sum = 10129839
❯ ./sum-1.out
sum = 10000000
❯ ./sum-2.out
sum = 20000000
```

三种编译优化等级得到的输出结果不同，为什么？

查看三种文件分别被编译成了什么代码 `objdump -d sum-0.out | less `

```assembly
# 优化等级 - 0
0000000000001380 <do_sum>:
    1380:       f3 0f 1e fa             endbr64 
    1384:       55                      push   %rbp
    1385:       48 89 e5                mov    %rsp,%rbp
    1388:       c7 45 fc 00 00 00 00    movl   $0x0,-0x4(%rbp)
    138f:       eb 16                   jmp    13a7 <do_sum+0x27>
    1391:       48 8b 05 98 2c 00 00    mov    0x2c98(%rip),%rax        # 4030 <sum>
    1398:       48 83 c0 01             add    $0x1,%rax
    139c:       48 89 05 8d 2c 00 00    mov    %rax,0x2c8d(%rip)        # 4030 <sum>
    13a3:       83 45 fc 01             addl   $0x1,-0x4(%rbp)
    13a7:       81 7d fc 7f 96 98 00    cmpl   $0x98967f,-0x4(%rbp)
    13ae:       7e e1                   jle    1391 <do_sum+0x11>
    13b0:       90                      nop
    13b1:       90                      nop
    13b2:       5d                      pop    %rbp
    13b3:       c3                      retq   


# 优化等级 1
0000000000001203 <do_sum>:
    1203:       f3 0f 1e fa             endbr64 
    1207:       48 8b 15 0a 2e 00 00    mov    0x2e0a(%rip),%rdx        # 4018 <sum>
    120e:       48 8d 42 01             lea    0x1(%rdx),%rax
    1212:       48 81 c2 81 96 98 00    add    $0x989681,%rdx
    1219:       48 89 c1                mov    %rax,%rcx
    121c:       48 83 c0 01             add    $0x1,%rax
    1220:       48 39 d0                cmp    %rdx,%rax
    1223:       75 f4                   jne    1219 <do_sum+0x16>
    1225:       48 89 0d ec 2d 00 00    mov    %rcx,0x2dec(%rip)        # 4018 <sum>
    122c:       c3                      retq 

# 优化等级 2
00000000000012a0 <do_sum>:
    12a0:       f3 0f 1e fa             endbr64 
    12a4:       48 81 05 69 2d 00 00    addq   $0x989680,0x2d69(%rip)        # 4018 <sum>
    12ab:       80 96 98 00 
    12af:       c3                      retq 
```

编译器会对我们编写的程序做出一定的修改，这些修改在顺序执行的时候是没有问题的，但是在并发执行的时候就会产生不好的结果。

#### 可见性

之前的一小段代码：

```c
int x = 0, y = 0;

void thread_1(){
    x  = 1; // [1]
    printf("y = %d\n",y); // [2]
}

void thread_2(){
    y = 1; // [3]
    printf("x = %d\n",x); // [4]
}
```

放弃可见性。

理由：

为了使CPU运行更快，CPU可以不按照顺序执行命令

```assembly
movl	$1, (x)    # x = 1, cache miss
				   # 如果等这条指令执行完，会浪费大量时间
movl	(y), %eax  # 因此只要xy不是同一个变量，CPU会立即执行这条命令
				   # 此时 y = 0
```

现代处理器：

- 如果两条指令没有数据依赖关系，就让他们并行执行
- 乱序执行
  - 多个处理器上执行的结果可以不等价于指令按照某个顺序执行的结果



#### 代码的执行比我们想象的复杂

在现代计算机系统中，即便是一个简单的 x = 1 也会经历：

- C代码
  - 编译器优化 -> 顺序性的丧失
- 二进制文件
- 处理器执行
  - 终端/执行 -> 原子性的丧失
  - 乱序执行 -> 可见性的丧失

共享内存并发变成真正需要面对的难题：

- 内存访问并不保证按照代码书写的顺序发生
- 代码的原子性随时被破坏
- 执行过的指令可能在多处理器间不可见

**保证顺序：**

使用 volatile 关键字

```c
void delay(){
    for (volatile int i = 0; i < DELAY_COUNT; i++);
}
```

保证内存访问的顺序

```c
extern int x;

#define barrier() asm volatile("" ::: "memory")

void foo(){
    x++;
    barrier(); // 组织x的访问被合并
    x++; // y的访问不能移到barrier之前
    y++;
}
```

**保证原子性**

stop_the_world() 函数，执行之后整个系统的其他所有线程都暂停

resume_the_world() 函数，执行之后其他线程恢复

## 【Con-2】理解并发程序的执行

```
本讲内容：
- 串行程序的状态机模型
- 状态机模型的应用
- 并发程序的状态机模型
- 理解并发程序的执行
```

### 串行程序的状态机模型

#### 有限状态机（Finite State Machine）

有向图G（V, E）

- 节点->状态

- 边->状态转换

- 边上的label代表执行某个状态

操作系统上的程序执行时，状态是有限的，

- 寄存器
- 内存：代码、数据、堆栈（暂时假设内存静态分配）

构造有限状态机

- 每个不同的 configuration 都是状态机的节点
  - s=(M,R) 属于 V，代表某个时刻程序内存/寄存器的快照
  - 16m的内存就有2的24m次方种不同的状态
- s=(M,R)的下一个状态是执行 M[R[%rip]] 处的指令得到 s_1 = (M_1, R_1)
  - 取出PC指针处的指令、译码、执行、写回数据
  - (s, s_1) 属于 E

大部分状态有唯一的后续状态(deterministic)

我们学习的大部分算法都是 deterministic 的

程序 = 有限状态机

不确定的指令可能有多个状态(non-deterministic)的指令可能有多个后续状态

- (时间)rdtsc/rdtscp

  - 获取处理器的时间戳用于精确定时

- 机器状态 rdrand

  - 处理器自身提供的随机数指令
  - 读取处理器上的白噪声生成随机数

  ```c
  // rdrand.c
  #include <stdio.h>
  #include <stdint.h>
  
  int main() {
    uint64_t val;
    asm volatile ("rdrand %0": "=r"(val));
    printf("rdrand returns %016lx\n", val);
  }
  ```

  ```bash
  ❯ vim rdrand.c
  ❯ gcc rdrand.c
  ❯ ./a.out
  rdrand returns da53e8a19ebdb3d1
  ❯ ./a.out
  rdrand returns cb075a76ba90effd
  ❯ ./a.out
  rdrand returns fde2ddfb5c7a2bf3
  ❯ ./a.out
  rdrand returns 10d0889b7c044cdc
  ```

- 系统调用 syscall

  - 一般应用唯一不确定的来源
  - read(fd, buf, size) 返回值不确定、buf中的数据不确定，比如从键盘输入

#### x86-64的栗子

运行在 ring3（低特权级）的应用程序

- 通用寄存器 16 个
  - rax\rbx\rcx\rdx\rsi\rbp\rsp
  - r8 ~ r15
- PC 指针/机器状态
  - rip\rflags\cs\ds\es\fs\gs
- 内存
  - 操作系统分配；通过procfs查看

---

这些状态都能被gdb观察到

- `info registers ` 列出所有寄存器
- `/proc/[pid]/maps` 有内存映射信息

```assembly
// minimal.S
.globl foo
foo:
  movl $1,	%eax
  movl $1,	%edi
  movq $s,	%rsi
  movl $(e-s),	%edx
  syscall

  movl $60,	%eax
  movl $1,	%edi
  syscall

s:
  .ascii "\033[01;31mHello World\033[0m\n"
e:

// code
.fill 1 << 20, 1, 0xcc

// data
.section .data
.fill 2 << 20, 1, 0xff

//bss
.section .bss
.fill 3 << 20
```

```bash
❯ gcc -c minimal.S
❯ ld minimal.o
ld: warning: cannot find entry symbol _start; defaulting to 0000000000401000
❯ ./a.out
Hello World
```

程序可以执行，我们用gdb调试这个程序

```bash
❯ gdb a.out
(gdb) starti
Starting program: /tmp/tmp/a.out 

Program stopped.
0x0000000000401000 in foo ()
(gdb) info registers  # 查看寄存器状态 
rax            0x0                 0
rbx            0x0                 0
rcx            0x0                 0
rdx            0x0                 0
rsi            0x0                 0
rdi            0x0                 0
rbp            0x0                 0x0
rsp            0x7fffffffdf00      0x7fffffffdf00
...
...
rip            0x401000            0x401000 <foo>
eflags         0x200               [ IF ]
cs             0x33                51
ss             0x2b                43
ds             0x0                 0
es             0x0                 0
fs             0x0                 0
gs             0x0                 0

(gdb) info inferiors # 查看程序的进程信息
  Num  Description       Executable        
* 1    process 14178     /tmp/tmp/a.out    
(gdb) !cat /proc/14178/maps # 查看进程内存中信息
00400000-00401000 r--p 00000000 103:07 538911                            /tmp/tmp/a.out
00401000-00502000 r-xp 00001000 103:07 538911                            /tmp/tmp/a.out
00502000-00702000 rw-p 00102000 103:07 538911                            /tmp/tmp/a.out
00702000-00a02000 rw-p 00000000 00:00 0                                  [heap]
7ffff7ff9000-7ffff7ffd000 r--p 00000000 00:00 0                          [vvar]
7ffff7ffd000-7ffff7fff000 r-xp 00000000 00:00 0                          [vdso]
7ffffffde000-7ffffffff000 rw-p 00000000 00:00 0                          [stack]
ffffffffff600000-ffffffffff601000 --xp 00000000 00:00 0                  [vsyscall]
(gdb) 
```

### 状态机模型：应用

在计算机硬件上的应用：高性能处理器实现

- 超标量处理器
  - insight ：允许在状态机上跳跃
- 在计算机系统上的应用：程序分析技术
  - 静态分析：根据程序代码推导出状态机的性质
  - 动态分析：检查运行时观测到状态机的执行

#### 应用(1):Time-Travel Debugging

GDB的隐藏功能

- target record-full 开始记录（需要程序开始执行）
- record stop 结束记录
- reverse-step/reverse-stepi 时间旅行调试

对syscall指令不适用，因为side-effect难以准确定义

#### 应用(2):Record & Repaly

在程序执行时记录信息，结束后重现程序的行为

- 确定的程序不必记录
- 假设s0执行1000000条确定的指令之后得到 s1
  - 那么只需要记录 s0 和 1000000
  - 就能通过“再执行一次”推导出 s1

Record&Repaly: 只需要记录 non-deterministic 的指令的效果（side-effect）

- (单线程)应用程序
  - syscall\rdrand\rdtsc
- (单处理器)操作系统
  - mmio\in\out\rdrand\rdtsc\中断
  - QEMU内置了 record/repaly

### 并发程序的状态机模型

系统中有n个线程，则并发程序的状态：

- s= (M,R1,R2,…,Rn) 
- 并发程序执行的每一步都是不确定的

多线程程序可以看成是若干个单线程程序。在任意时刻，状态的转换就是 “选择一个线程执行一条指令”：

- 选择线程 1 执行：(M,R1)→(M1′,R1′)，得到状态 (M1′,R1′,R2,…,Rn)；
- 选择线程 2 执行：(M,R2)→(M2′,R2′)，得到状态 (M2′,R1,R2′,…,Rn)；
- …
- 选择线程 n 执行：(M,Rn)→(Mn′,Rn′)，得到状态 (Mn′,R1,R2,…,Rn′)；

![img](http://jyywiki.cn/pages/OS/2021/notes/img/state-space.png)



n 个线程的并发程序，若每个线程执行 m 条指令，就算所有指令都是确定的，不同的执行顺序也多达 n^O(mn)，这个状态机太大了。

就算是合并确定的状态，只要有共享内存，状态空间就很难画出了

- 而且还不考虑编译优化、多处理器之间的可见性等问题

刚才介绍了各种状态机的应用，都需要为多线程重新设计

- 共享内存是 non-determinism 的重要来源
- time-travel debugging/record & replay 需要记录内存访问的数据
- 自动测试要考虑如何探索线程调度
- ... ...



### :star:理解并发程序的执行

程序

- 指令序列的静态描述
  - 是非常概括、精简的
  - 所以行为有时候难以理解——循环、递归、分支的组合和不确定的共享内存

状态机

- 所有动态行为的集合
  - 静态时的分支、循环全部被展开成了顺序结构
  - 大量的冗余和重复(verbose)
  - **行为明确、容易理解**

#### 栗子：实现互斥

希望实现 lock/unlock 保证：

- （顺序）编译优化不能越过 lock/unlock 
- （原子）lock 返回后，unlock之前，其他线程的lock不能返回
- （可见）unlock 之前执行的写操作，在unlock之后对其他线程可见


```c
void do_sum(){
    for(int i = 0; i < n; i++){
        lock(); // 保证顺序、原子性、可见性
        // critical section；临界区
        sum++;
        // lock和unlock之间的代码被保护起来了
        unlock();
    }
}
```

Peterson 算法: 代码


```c
int turn, x = 0, y = 0;

void thread1() {
  [1] x = 1;
  [2] turn = T2;
  [3] while (y && turn == T2) ;
  [4] // critical section
  [5] x = 0;
}

void thread2() {
  [1] y = 1;
  [2] turn = T1;
  [3] while (x && turn == T1) ;
  [4] // critical section
  [5] y = 0;
}
```

假设：机器每次原子地执行一行代码，内存访问立即可见。

证明：

Safety: 坏事永远不会发生。

- 不存在一条从初始节点到错误状态的路径。

Liveness: 好事永远会发生。

- 不存在无穷长的路径。























