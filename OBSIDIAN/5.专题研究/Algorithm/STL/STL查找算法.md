
# STL查找算法

#Cpp/STL/查找算法

### find

查找制定元素出现位置

```c
find(iterator begin, iterator end, value);
find(开始迭代器, 结束迭代器, 查找的元素)
//找到返回指定位置迭代器, 找不到返回.end()

//查找内置的数据类型

void test()
{
    vector<int>v;
    for (int i = 0; i < 10; i++)
        v.push_back(i);
    vector<int>v1;

    //查找容器中是否有 5  , 返回其第一次出现的位置
    vector<int>::iterator it = find(v.begin(), v.end(), 5);
}



//查找自定义数据类型(需要重载 == 号)
class Person
{
public:
    Person(string name, int age) : m_Age(age), m_Name(name) {}

    //重载==号, 让find知道如何对比 Person 数据类型
    bool operator==(const Person& p) {
        if (this->m_Age == p.m_Age && this->m_Name == p.m_Name)
            return true;
        else
            return false;
    }

    string m_Name;
    int m_Age;
};

void test()
{
    vector<Person> v;
    Person p1("aa", 10);
    Person p2("bb", 20);
    Person p3("cc", 30);
    Person p4("dd", 40);
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);

    //查找容器中是否有 p2 这个元素 , 返回其第一次出现的位置
    vector<Person>::iterator it = find(v.begin(), v.end(), p2);
    if (it == v.end())
        cout << "Not Found" << endl;
    else
        cout << "Name : " << (*it).m_Name << endl;
}

```

### find_if

按条件查找元素

```c
find_if(iterator beg, iterator end, _Pred);
find_if(开始迭代器, 结束迭代器, 函数或者谓词);

//查找内置数据类型

class GreatFive
{
public:
    bool operator()(int i)
    {
        return i > 5;
    }
};

void test()
{
    vector<int>v;
    for (int i = 0; i < 10; i++)
        v.push_back(i);
    //查找容器中是否有 5 这个元素 , 返回其第一次出现的位置, 找不到则返回 v.end()
    vector<int>::iterator it = find_if(v.begin(), v.end(), GreatFive());
    if (it == v.end())
        cout << "Not Found" << endl;
    else
        cout << *it << endl;
}



//查找自定义数据类型

class Person
{
public:
    Person(string name, int age)
    {
        this->m_Age = age;
        this->m_Name = name;
    }

    string m_Name;
    int m_Age;
};

class Greater20
{
public:
    int operator()(const Person& p)
    {
        return p.m_Age > 20;
    }
};

void test()
{
    vector<Person>v;
    Person p1("aa", 10);
    Person p2("bb", 20);
    Person p3("cc", 30);
    Person p4("dd", 40);
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);


//查找容器中是否有 满足条件的元素 , 返回其第一次出现的位置
    vector<Person>::iterator it = find_if(v.begin(), v.end(), Greater20());
    if (it == v.end())
        cout << "Not Found" << endl;
    else
        cout << "Name : " << (*it).m_Name << endl;
}
```

### adjacent_find

查找相邻重复元素

```c
adjacent_find(iterator beg, iterator end);
adjacent_find(开始迭代器, 结束迭代器);
//查找相邻重复元素。返回第一对相邻元素的第一个位置的迭代器, 未找到则返回.end()

void test()
{
    vector<int>v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(2);
    v.push_back(3);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    vector<int>::iterator it = adjacent_find(v.begin(), v.end());
    if (it == v.end())
        cout << "Not Found" << endl;
    else
        cout << *it << endl;
}
```



### binary_search

查找指定元素是否存在

```c
binary_search(iterator beg, iterator end, value);
binary_search(开始迭代器, 结束迭代器, 查找的元素);
//查找指定的元素，查到返回true 否则false
//只查找并表示有或没有, 不会返回有几个和它的位置
//在无序序列中不可用

void test()
{
	vector<int>v;
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	bool it = binary_search(v.begin(), v.end(), 3);
	cout << it << endl;
}
```

### count

统计元素个数

```c
count(iterator beg, iterator end, value); 
count(开始迭代器, 结束迭代器, 统计的元素);

//统计内置数据类型

void test()
{
    vector<int>v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(2);
    v.push_back(3);
    v.push_back(3);
    int it = count(v.begin(), v.end(), 3);
    cout << it << endl;
}

//统计自定义数据类型

class Person
{
public:
    Person(string name, int age) : m_Age(age), m_Name(name) {}
 
//重载==号, 让 编译器 知道如何对比 Person 数据类型
    bool operator==(const Person& p)
    {
        if (this->m_Age == p.m_Age)
            return true;
        else
            return false;
    }

    string m_Name;
    int m_Age;
};

void test()
{
    vector<Person>v;
    Person p1("aa", 10);
    Person p2("bb", 20);
    Person p3("cc", 20);
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);

    Person p("ee", 20);
    int cnt = count(v.begin(), v.end(), p);
    cout << cnt << endl;
}
```



### count_if

按条件统计元素个数

```c
count_if(iterator beg, iterator end, _Pred);
count_if(开始迭代器, 结束迭代器, 谓词);

//内置数据类型

class Great3
{
public:
    bool operator()(int i)
    {
        return i > 3;
    }
};

void test()
{
    vector<int>v;
    v.push_back(1);
    v.push_back(3);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    int it = count_if(v.begin(), v.end(), Great3());
    cout << it << endl;
}

//自定义数据类型

class Person
{
public:
    Person(string name, int age) : m_Age(age), m_Name(name) {}
    string m_Name;
    int m_Age;
};

class Greater20
{
public:
    int operator()(const Person& p)
    {
        return p.m_Age > 20;
    }
};

void test()
{
    vector<Person>v;
    Person p1("aa", 10);
    Person p2("bb", 20);
    Person p3("cc", 20);

    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    
    int cnt = count_if(v.begin(), v.end(), Greater20());
    cout << cnt << endl;
}
```

