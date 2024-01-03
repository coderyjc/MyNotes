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

