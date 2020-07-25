# C++ vector容器和 deque 容器



## ***#include< vector >***



### 初始化 && 赋值

``` c++
//定义一个int类型的vector并向其中添加0, 1, 2, 3, 4
vector<int> v;
for (int i = 0; i < 5; i++) v.push_back(i);

//赋值
vector<int> v1 = v;

//拷贝构造
vector<int> v2(v);

//用v中的所有元素初始化v3
//迭代器类型
vector<int> v3(v.begin(), v.end());

//初始元素为 50
vector<int> v4(50);

//初始元素为 5个10
vector<int> v5(5, 10);

//用数组初始化容器
int arr[5] = { 0, 1, 2, 3, 4 };
vector<int> v6(arr, arr + sizeof(arr) / sizeof(int));

//用成员函数赋值
vector<int> v6;
v6.assign(v.begin(), v.end());

//交换
vector<int> v7;
v7.swap(v); //交换了v7和v的内容(实质是交换指针)


```
### 访问

```c++
	vector<int> v;
	for (int i = 0; i < 5; i++) v.push_back(i);

	//作为起始端, 返回容器首部元素迭代器
	v.begin();
	
	//返回容器尾部元素迭代器
	v.end();

	//作为起始端, 返回容器尾部元素迭代器
	v.rbegin();

	//返回容器首部元素迭代器
	v.rend();

	//返回容器中第一个数据元素
	v.front();

	//返回容器中最后一个数据元素
	v.back();
```



### 个数/判空/重置/容量/预留

```c++
	vector<int> v;
	for (int i = 0; i < 5; i++) v.push_back(i);
	
	//返回容器中元素的个数
	v.size();

	//判断容器是否为空
	v.empty();

	//重新指定容器的长度为20，
	//若容器变长，则以默认值 0 填充新位置。
	//如果容器变短，则末尾超出容器长度的元素被删除。
	v.resize(20);

	//重新指定容器的长度为20，
	//若容器变长，则以 1 填充新位置。
	//如果容器变短，则末尾超出容器长度的元素被删除。
	v.resize(20, 1);

	//返回容器的容量
	v.capacity();

	//容器预留50个元素长度，预留位置不初始化，元素不可访问
	v.reserve(50);
```



### 存取/插入/删除

```c++
	vector<int> v;
	for (int i = 0; i < 5; i++) v.push_back(i);
	
	//返回索引 4 所指的数据，
	//如果越界，抛出out_of_range异常
	v.at(4);

	//越界时，运行直接报错
	v[4];

	//向迭代器 v.begin() + 3 所指向的位置插入 5 个 0
	v.insert(v.begin() + 1, 5, 0);

	//尾插 0
	v.push_back(0);

	//删除最后一个元素
	v.pop_back();

	//删除迭代器 v.begin() + 3 所指向的元素
	v.erase(v.begin() + 3);

	//删除迭代器 v.begin() + 3 和 v.begin() + 4 之间的元素
	v.erase(v.begin() + 3, v.begin() + 4);
	
	//清空容器中的元素
	v.clear();
```



## ***#include< deque >***

### 初始化

```c++
	deque<int> d;
	for (int i = 0; i < 5; i++) d.push_back(i);
	
	//赋值
	deque<int> d1 = d;

	//拷贝构造
	deque<int> d2(d);

	//用d中的所有元素初始化d3
	//迭代器类型
	deque<int> d3(d.begin(), d.end());

	//初始元素为 50
	deque<int> d4(50);

	//初始元素为 5个10
	deque<int> d5(5, 10);

	//用数组初始化容器
	int arr[5] = { 0, 1, 2, 3, 4 };
	deque<int> d6(arr, arr + sizeof(arr) / sizeof(int));

	//用成员函数赋值
	deque<int> d6;
	d6.assign(d.begin(), d.end());

	//交换
	deque<int> d7;
	d7.swap(d); //交换了v7和v的内容(实质是交换指针)
```



### 访问

```c++
	deque<int> d;
	for (int i = 0; i < 5; i++) d.push_back(i);

	//作为起始端, 返回容器首部元素迭代器
	d.begin();

	//返回容器尾部元素迭代器
	d.end();

	//作为起始端, 返回容器尾部元素迭代器
	d.rbegin();

	//返回容器首部元素迭代器
	d.rend();

	//返回容器中第一个数据元素
	d.front();

	//返回容器中最后一个数据元素
	d.back();
```



### 个数/判空/重置

```c++
	deque<int> d;
	for (int i = 0; i < 5; i++) d.push_back(i);
	
	//返回容器中元素的个数
	d.size();

	//判断容器是否为空
	d.empty();

	//重新指定容器的长度为20，
	//若容器变长，则以默认值 0 填充新位置。
	//如果容器变短，则末尾超出容器长度的元素被删除。
	d.resize(20);

	//重新指定容器的长度为20，
	//若容器变长，则以 1 填充新位置。
	//如果容器变短，则末尾超出容器长度的元素被删除。
	d.resize(20, 1);
```

### 存取/插入/删除

```c++
	deque<int> d;
	for (int i = 0; i < 5; i++) d.push_back(i);
	
	//返回索引 4 所指的数据，
		//如果越界，抛出out_of_range异常
	d.at(4);

	//越界时，运行直接报错
	d[4];

	//向迭代器 d.begin() + 3 所指向的位置插入 5 个 0
	d.insert(d.begin() + 1, 5, 0);

	//头插 0
	d.push_front(0);

	//尾插 0
	d.push_back(0);

	//删除最后一个元素
	d.pop_back();

	//删除首元素
	d.pop_front();

	//删除迭代器 d.begin() + 3 所指向的元素
	d.erase(d.begin() + 3);

	//删除迭代器 d.begin() + 3 和 d.begin() + 4 之间的元素
	d.erase(d.begin() + 3, d.begin() + 4);

	//清空容器中的元素
	d.clear();

```

