# STL常用算法

> 本文为作者学习[黑马程序员匠心C++教程](https://www.bilibili.com/video/BV1et411b73Z?from=search&seid=7661109126115521926)的学习笔记

> 若无特殊说明，所有的算法都应该包含 algorithem 头文件

## 排序

### sort

对容器内元素进行排序

```c++
sort(iterator beg, iterator end, _Pred);
sort(开始迭代器, 结束迭代器, 谓词);
//按值查找元素, 找到返回指定位置迭代器, 找不到返回结束迭代器位置
//默认为升序排列

//内置数据类型
//降序排列
class Great3
{
public:
    bool operator()(int v1, int v2)
    {
        return v1 > v2;
    }
};

void test()
{
    vector<int>v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    sort(v.begin(), v.end(), Great3());

    for (auto i : v)
        cout << i << endl;
}


//自定义数据类型

class Person
{
public:
    Person(string name, int age) : m_Age(age), m_Name(name) {}

    string m_Name;
    int m_Age;
};

// 降序排列
class Greater20
{
public:
    bool operator()(const Person& p1, const Person& p2)
    {
        return p1.m_Age > p2.m_Age;
    }
};

void test()
{
    vector<Person>v;
    Person p1("aa", 10);
    Person p2("bb", 20);
    Person p3("cc", 20);
    Person p4("dd", 40);
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);

    sort(v.begin(), v.end(), Greater20());

    for (auto i : v)
    {
        cout << i.m_Age
            << i.m_Name << endl;
    }

}


```



### random_shuffle

指定范围内的元素随机调整次序

```c++
random_shuffle(iterator beg, iterator end);
random_shuffle(开始迭代器, 结束迭代器);

//伪随机

void test()
{
    vector<int>v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    random_shuffle(v.begin(), v.end());

    for (auto i : v)
        cout << i << endl;
}

//真随机(#include<time.h>)

void test()
{
    srand((unsigned int)time(NULL));  // 按系统时间进行随机
    vector<int>v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);
    random_shuffle(v.begin(), v.end());
    for (auto i : v)
        cout << i << endl;
}
```



### merge

两个容器元素合并, 并存储到另一容器中



```c++
//注意：两个容器必须是有序的 , 而且在合并以后依然是有序的
//注意: 一定要在合并之后存放的容器中开辟空间
merge(iterator beg1, iterator end1, 
      iterator beg2, iterator end2, 
      iterator dest);
merge(容器1开始迭代器, 容器1结束迭代器, 
      容器2开始迭代器, 容器2结束迭代器, 
      目标容器开始迭代器);

void test()
{
    vector<int>v;
    vector<int>v1;
    vector<int>vt;
    for (int i = 0; i < 5; i++)
        v.push_back(i);
    for (int i = 5; i < 10; i++)
        v1.push_back(i);

    vt.resize(v.size() + v1.size());

    merge(v.begin(), v.end(), v1.begin(), v1.end(), vt.begin());

    for (auto i : vt)
        cout << i << " ";
}

```



### reverse

将容器内元素进行反转

```c++
reverse(iterator beg, iterator end);
reverse(开始迭代器, 结束迭代器);

void test()
{
    vector<int>vt;
    for (int i = 0; i < 5; i++)
        vt.push_back(i);
    reverse(vt.begin(), vt.end());
    for (auto i : vt)
        cout << i << " ";
}
```



## 拷贝和替换

### copy

容器内指定范围的元素拷贝到另一容器中

```c++
copy(iterator eg, iterator end, iterator dest);
copy(开始迭代器, 结束迭代器, 目标起始迭代器);
//目标容器应该先开辟空间

void test()
{
    vector<int>v1;
    vector<int>v2;
    for (int i = 0; i < 5; i++)
        v1.push_back(i);
    v2.resize(v1.size());
    copy(v1.begin(), v1.end(), v2.begin());
    for (auto i : v2)
        cout << i << " ";
}
```

### replace

将容器内指定范围的所有旧元素修改为新元素

```c++
replace(iterator beg, iterator end, oldvalue, newvalue);
replace(开始迭代器, 结束迭代器, 旧元素, 新元素);

void test() {
	vector<int> v;
	v.push_back(1);	
	v.push_back(1);	
	v.push_back(2);
	v.push_back(3);
	replace(v.begin(), v.end(), 1, 10);
	for (auto i : v) {
		cout << i << " ";
	}
}

```



### replace_if

将区间内满足条件的元素, 替换成指定元素

```c++
replace_if(iterator beg, iterator end, _pred, newvalue);
replace_if(开始迭代器,  结束迭代器, 谓词, 替换的新元素);

class Greater2 {
public:
	bool operator()(int x) {
		return x > 2;
	}
};

void test() {

	vector<int> v;
	v.push_back(1);
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	replace_if(v.begin(), v.end(), Greater2(), 0);
	for (auto i : v) {
		cout << i;
	}
}

```

### swap

互换两个容器的元素

```c++
swap(container c1, container c2);
swap(容器1, 容器2);

void test() {

	vector<int> v;
	v.push_back(1);
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	vector<int> v1;
	swap(v, v1);
}
```



## 算数生成和集合

### accumulate

>  使用时包含的头文件为#include < numeric >

返回区间内容器元素累计总和

```c++
accumulate(iterator beg, iterator end, value);
accumulate(开始迭代器, 结束迭代器, 起始值);

void test() {
	vector<int> v(5, 10);
	accumulate(v.begin(), v.end(), 0);
}
```

### fill 

>  使用时包含的头文件为#include < numeric >

向容器中填充指定的元素

```c++
fill(iterator beg, iterator end, vale);
fill(开始迭代器 , 结束迭代器, 填充的值);

void test() {
	vector<int> v(10, 0);
	fill(v.begin(), v.end(), 1);
}
```

### set_intersection

>  使用时包含的头文件为#include < algorithem >

求两个容器的交集

```c++
set_intersection(iterator beg1, iterator end1, 
                 iterator beg2, iterator end2, 
                 iterator dest);
set_intersection(容器1开始迭代器, 容器1结束迭代器, 
                 容器2开始迭代器, 容器2结束迭代器, 
                 目标容器开始迭代器);
//v3使用之前要开辟空间

void test() {
	vector<int> v1;
	vector<int> v2;
	vector<int> v3;
	for (int i = 0; i < 5; i++){
		v1.push_back(i);
		v2.push_back(i + 2);
	}

	v3.resize(v1.size() + v2.size());
	set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), v3.begin());

	for (auto i : v3) {
		cout << i << " ";
	}
	
}
```

### set_union



>  使用时包含的头文件为#include < algorithem >


求两个集合的并集

```c++
set_union(iterator beg1, iterator end1, 
          iterator beg2, iterator end2, 
          iterator dest);

set_union(容器1开始迭代器, 容器1结束迭代器,
		  容器2开始迭代器, 容器2结束迭代器,
		  目标容器开始迭代器);

//两个集合必须是有序序列

//v3使用之前要开辟空间
void test() {
	vector<int> v1;
	vector<int> v2;
	vector<int> v3;
	for (int i = 0; i < 5; i++){
		v1.push_back(i);
		v2.push_back(i + 2);
	}

	v3.resize(v1.size() + v2.size());
	set_union(v1.begin(), v1.end(), v2.begin(), v2.end(), v3.begin());

	for (auto i : v3) {
		cout << i << " ";
	}
	
}
```



### set_difference

>  使用时包含的头文件为#include < algorithem >

```c++
set_difference(iterator beg1, iterator end1, 
      	iterator beg2, iterator end2, 
      	iterator dest);

set_difference(容器1开始迭代器, 容器1结束迭代器,
		  容器2开始迭代器, 容器2结束迭代器,
		  目标容器开始迭代器);

//v3使用之前要开辟空间
void test() {
	vector<int> v1;
	vector<int> v2;
	vector<int> v3;
	for (int i = 0; i < 5; i++){
		v1.push_back(i);
		v2.push_back(i + 2);
	}
	v3.resize(v1.size() + v2.size());
	set_difference(v1.begin(), v1.end(), v2.begin(), v2.end(), v3.begin());
	for (auto i : v3) {
		cout << i << " ";
	}
}
```

