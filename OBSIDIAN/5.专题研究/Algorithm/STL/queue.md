# queue 队列

#STL/queue

**不能进行遍历, 不提供迭代器, 不支持随机访问**

```c
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
