
```ad-note
https://pintia.cn/problem-sets/15/exam/problems/type/6
```


7-1

7-3 写函数之前一定要先声明
这个题用C++提交成功，但是C语言提交失败

https://www.bilibili.com/video/BV1FJ411k7zd/?spm_id_from=333.337.search-card.all.click&vd_source=69309a650a9cd7253c3121dbac2d898c

### 错误原因

未知的类型名：‘bool’, 因为在C语言标准(C89)没有定义布尔类型，所以会报错。而C99提供了一个头文件`<stdbool.h>`定义了`bool`，`true`代表1，`false`代表0。只要导入`stdbool.h`，就能非常方便的操作布尔类型了。

### 解决方法

```c
#include <stdbool.h>
```

```

a.c:21:1: error: unknown type name ‘bool’
 bool isTongGou(Tree t1, Tree t2);
 ^~~~
a.c:60:1: error: unknown type name ‘bool’
 bool isTongGou(Tree t1, Tree t2){
 ^~~~
a.c: In function ‘isTongGou’:
a.c:62:39: error: ‘true’ undeclared (first use in this function)
   if(t1 == Null && t2 == Null) return true;
                                       ^~~~
a.c:62:39: note: each undeclared identifier is reported only once for each function it appears in
a.c:64:76: error: ‘false’ undeclared (first use in this function)
   else if((t1 == Null && t2 != Null) || (t1 != Null && t2 == Null)) return false;
                                                                            ^~~~~
a.c: In function ‘buildTree’:
a.c:29:3: warning: ignoring return value of ‘scanf’, declared with attribute warn_unused_result [-Wunused-result]
   scanf("%d", &n);
   ^~~~~~~~~~~~~~~
a.c:34:5: warning: ignoring return value of ‘scanf’, declared with attribute warn_unused_result [-Wunused-result]
     scanf("%c", &t[i].element);
     ^~~~~~~~~~~~~~~~~~~~~~~~~~
a.c:36:5: warning: ignoring return value of ‘scanf’, declared with attribute warn_unused_result [-Wunused-result]
     scanf("%c", &cl);
     ^~~~~~~~~~~~~~~~
a.c:38:5: warning: ignoring return value of ‘scanf’, declared with attribute warn_unused_result [-Wunused-result]
     scanf("%c", &cr);
     ^~~~~~~~~~~~~~~~
a.c: In function ‘isTongGou’:
a.c:74:1: warning: control reaches end of non-void function [-Wreturn-type]
 }
 ^
a.c: In function ‘main’:
a.c:86:3: warning: ignoring return value of ‘system’, declared with attribute warn_unused_result [-Wunused-result]
   system("pause");
   ^~~~~~~~~~~~~~~
```


二叉搜索树相关介绍

https://blog.csdn.net/L_T_W_Y/article/details/108407686

