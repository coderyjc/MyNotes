# STL填充算法
#Cpp/STL/STL填充算法

### accumulate

> 使用时包含的头文件为#include < numeric >

返回区间内容器元素累计总和

```c
accumulate(iterator beg, iterator end, value);
accumulate(开始迭代器, 结束迭代器, 起始值);

void test() {
	vector<int> v(5, 10);
	accumulate(v.begin(), v.end(), 0);
}
```

### fill 

> 使用时包含的头文件为#include < numeric >

向容器中填充指定的元素

```c
fill(iterator beg, iterator end, vale);
fill(开始迭代器 , 结束迭代器, 填充的值);

void test() {
	vector<int> v(10, 0);
	fill(v.begin(), v.end(), 1);
}
```
