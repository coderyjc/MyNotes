# deque 双端数组

#STL/deque

## 初始化

```c
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



## 访问

```c
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

## 个数/判空/重置

```c
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

## 存取/插入/删除

```c
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

