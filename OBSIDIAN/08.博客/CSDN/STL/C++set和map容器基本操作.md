# C++set/multiset/pair/map/multimap容器基本操作

## set/multiset|#include< set >

set和multiset的区别:set不允许相同的元素而multiset允许

不允许通过迭代器修改元素的值

但是可以删了再加进去

```c++
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

```c++
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

## pair对组

```c++
//初始化
	pair<int, string> p = make_pair(1, "No.1");
	pair<int, string> p1(1, "No.1");
//访问

//返回第一个元素
	p1.first;

//返回第二个元素
	p1.second;

//赋值
	pair<int, string> p2 = p1;
```

## map/multimap|#include< map >

map不允许相同的兼职的存在但是multimap允许

不允许通过迭代器修改相应的键值

但是可以删了重建

```c++

//初始化
	map<int, int> m;

//拷贝构造
	map<int, int> m1(m);

//赋值
	m1 = m;

//交换
	m.swap(m1);

//元素数目
	m.size();

//判空
	m.empty();

//插入
	//插入之后是有返回值的, 返回值为一个迭代器和bool类型组成的对组
	//迭代器指向刚刚插入的位置
	//bool 返回是否插入成功

	//匿名对象
	m.insert(pair<int, int>(10, 10));
	
	//函数
	m.insert(make_pair(10, 10));
	
	//valueType
	m.insert(map<int, int>::value_type(10, 10));
	
	//类似python字典
	//这种方式的话, 如果key存在就会修改, 不存在就会创建一个
	m[10] = 10;


//访问
	//迭代器取出的是一个pair
	map<int, int>::iterator it = m.begin();
	(*it).first;
	(*it).second;

	map<int, int> s;
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
	pair<map<int, int>::iterator, map<int, int>::iterator> res = s.equal_range(key);

```

