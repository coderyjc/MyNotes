# STL集合算法

#Cpp/STL/STL集合算法

### set_intersection

> 使用时包含的头文件为#include < algorithem >

求两个容器的交集

```c
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



> 使用时包含的头文件为#include < algorithem >

求两个集合的并集

```c
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

> 使用时包含的头文件为#include < algorithem >

```c
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

