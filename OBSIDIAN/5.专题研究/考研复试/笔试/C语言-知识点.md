
实参和与其对应的形参各占用独立的存储单元

在C语言中，能代表逻辑值“真”的是任何非0的数（整数和浮点数都可以）

`calloc` 是C语言中的一个内存分配函数，其作用是用于动态分配指定数量的连续内存空间，并将分配到的每个字节初始化为零。

空指针是指所指向的空间位置就是地址0的指针

**声明枚举变量三种方法**

1、先声明枚举类型后定义枚举类型变量
```c
enum WeekdayType  
{  
  sun,mou,tue,wed,thu,fri,sat  
};  
enum WeekdayType today,yesterday,tomorrow;
```

2、声明枚举类型的同时定义枚举类型变量
```c
enum WeekdayType  
{  
   sun,mou,tue,wed,thu,fri,sat   
}today,yesterday,tomorrow;
```

3、直接定义枚举类型变量
```c
enum  
{  
   sun,mou,tue,wed,thu,fri,sat  
}today,yesterday,tomorrow;
```

**数据输入输出**

在`scanf`函数中，用于读取`double`类型的格式说明符有两个常用的变体：`%le` 和 `%lf`。

`scanf("%*2s")`其中的星号表示读取并忽略其中的输入。
`printf("%-2c")`表示输出一个字符，并且左对齐并在字段宽度为2的情况下进行格式化。`-` 是用于左对齐的标志，`2` 是字段宽度。如果输出字符的宽度小于2，则在字符的右侧填充空格以满足指定的字段宽度。如果输出字符的宽度大于2，则不进行截断，而是按原样输出。右对齐不用特别指定，因为默认是右对齐的。
`printf("%+2c")`中的正号表示显示输出数字的正号
