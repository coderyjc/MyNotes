# C++ stack 容器/ queue 容器 和 list 容器

## #include< stack >

**栈不能遍历，不支持随机存取，只能通过top从栈顶获取和删除元素。**

```c++
	stack<int> s;

	//拷贝构造函数
	stack<int> s1(s);

	//入栈, 向栈中压元素 10
	s.push(10);
	
	//出栈, 弹出栈顶元素
	s.pop();

	//返回栈顶元素值
	s.top();

	//返回栈是否为空 空为1, 非空为0
	s.empty();

	//返回栈中元素的个数
	s.size();
```

## #include< queue >

**不能进行遍历, 不提供迭代器, 不支持随机访问**

```c++
	queue<int> q;

	//拷贝构造函数
	queue<int> q1(q);

	//入队
	q.push(10);

	//出队
	q.pop();

	//返回队首元素
	q.front();
	
	//返回队尾元素
	q.back();

	//返回栈是否为空 空为1, 非空为0
	q.empty();

	//返回栈中元素的个数
	q.size();
```



## #include< list >

### 初始化

```c++
	list<int> l1;

	//使用l1中元素的迭代器来初始化l2
	list<int> l2(l1.begin(), l1.end());
	
	//l3中的元素为 3 个 5
	list<int> l3(3, 5);
	
	//拷贝构造
	list<int> l4(l1);
```

### 数据的存取/删除/清空

```c++

	list<int> lis;

	//返回第一个元素
	lis.front();

	//返回最后一个元素
	lis.back();

	//尾插元素 6
	lis.push_back(6);

	//头插元素 1
	lis.push_front(1);

	//删除尾部元素
	lis.pop_back();

	//删除头部元素
	lis.pop_front();

	//向迭代器指向的位置插入元素 5
	lis.insert(lis.begin(), 5);
	/*
		注意 : list 不支持随机访问, 所以如果想要向某一位置插元素
		只能用循环把迭代器 ++ 上去. 下同
	*/
	//向迭代器指向的位置插入5 个元素 5
	lis.insert(lis.begin(), 5, 5);

	//移除所有数据
	lis.clear();

	//删除begin到end区间内的数据, 返回下一数据的位置
	lis.erase(lis.begin(), lis.end());

	//删除pos位置的数据, 返回下一数据的位置
	lis.erase(lis.begin());

	//删除容器中所有的 10
	lis.remove(10);
```

### 容器中元素的个数/判空/容量重设/反转

```c++
	//返回容器中元素的个数
	lis.size();

	//判断容器是否为空
	lis.empty();

	//重新指定容器的长度为20，
	//若容器变长，则以默认值填充新位置
	lis.resize(20);

	//重新指定容器的长度为20，
	//若容器变长，则以 1 填充新位置
	lis.resize(20, 1);

	//如果容器变短，则末尾超出容器长度的元素被删除

	//反转链表
	lis.reverse();
```

### 内置排序

```c++
//默认升序
lis.sort();

//降序写仿函数
bool myCompare(int v1, int v2) {
	return v1 > v2;
}

lis.sort(myCompare);

//同理, 内置数据类型也要写仿函数
```

