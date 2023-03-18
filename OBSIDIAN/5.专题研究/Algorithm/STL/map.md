# map/multimap 映射

#STL/map #STL/multimap #STL/pair

## 创建以string为键的map

map的直接插入不需要判断是否存在

不加这个判断函数也可以，有时候**加上了反而拉低了运行速度**。

```cpp
#include<string.h>

struct StrCmp {
	bool operator()(string l, string r) const { return strcasecmp(l.c_str(), r.c_str()) < 0; }
};
```

## map按照value排序

```cpp
struct CmpByValue {  
  bool operator()(const pair<int, int>& lhs, const pair<int, int>& rhs) {  
    return lhs.second > rhs.second;  
  }  
};

// ....
// 先转换为vector<pair>，再进行排序
vector<pair<int, int>> name_score_vec(name_score_map.begin(), name_score_map.end());
sort(name_score_vec.begin(), name_score_vec.end(), CmpByValue());
```



## pair对组

```c
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

## map操作

map不允许相同的键值的存在但是multimap允许

不允许通过迭代器修改相应的键值

但是可以删了重建

```c
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

