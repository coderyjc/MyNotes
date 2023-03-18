
# STL拷贝和替换算法

#STL/拷贝替换算法

### copy

容器内指定范围的元素拷贝到另一容器中

```c
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

```c
replace(iterator beg, iterator end, 
				oldvalue, newvalue);
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

```c
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

```c
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


