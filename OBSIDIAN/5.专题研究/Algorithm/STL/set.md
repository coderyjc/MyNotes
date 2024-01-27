# set/multiset 集合

#Cpp/STL/set #Cpp/STL/multiset

set和multiset的区别:set不允许相同的元素而multiset允许

不允许通过迭代器修改元素的值

但是可以删了再加进去

```c
//初始化
	set<int> s;

//拷贝构造
	set<int> s2(s);

//赋值
	s2 = s;

//交换
	s2.swap(s);

//元素的数目
	s.size();

//判空
	s.empty();

//插入
	s.insert(10);

//清除
	s.clear();

//删除
	//删除pos迭代器所指的元素，返回下一个元素的迭代器
	s.erase(pos);

	// 删除区间[beg，end）的所有元素，返回下一个元素的迭代器
	s.erase(beg, end); 

	//删除容器中值为elem的元素
	s.erase(elem);

//查找
	//查找键key是否存在，若存在，返回该键的元素的迭代器；
	//若不存在，返回 s.end()
	s.find(key);

	//返回第一个key>=keyElem元素的迭代器
	s.lower_bound(keyElem);
	
	//返回第一个key > keyElem元素的迭代器
	s.upper_bound(keyElem);

	//返回容器中key与keyElem相等的上下限的两个迭代器
	//返回的是 lower_bound 和 upper_bound 值
	pair<set<int>::iterator, set<int>::iterator> pa = s.equal_range(key);
```

### set更改默认排序

```c
class myCompare {
public:
	bool operator()(int v1, int v2) {
		return v1 > v2;
	}
};

void test01() {
	set<int, myCompare> s;

}

//自定义函数对象同理
```
