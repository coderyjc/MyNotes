# STL排序算法

#Cpp/STL/排序算法 

### sort

对容器内元素进行排序

```c
sort(iterator beg, iterator end, _Pred);
sort(开始迭代器, 结束迭代器, 谓词);
//按值查找元素, 找到返回指定位置迭代器, 找不到返回结束迭代器位置
//默认为升序排列

//内置数据类型
//降序排列
class Great3
{
public:
    bool operator()(int v1, int v2)
    {
        return v1 > v2;
    }
};

void test()
{
    vector<int>v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    sort(v.begin(), v.end(), Great3());

    for (auto i : v)
        cout << i << endl;
}


//自定义数据类型

class Person
{
public:
    Person(string name, int age) : m_Age(age), m_Name(name) {}

    string m_Name;
    int m_Age;
};

// 降序排列
class Greater20
{
public:
    bool operator()(const Person& p1, const Person& p2)
    {
        return p1.m_Age > p2.m_Age;
    }
};

void test()
{
    vector<Person>v;
    Person p1("aa", 10);
    Person p2("bb", 20);
    Person p3("cc", 20);
    Person p4("dd", 40);
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);

    sort(v.begin(), v.end(), Greater20());

    for (auto i : v)
    {
        cout << i.m_Age
            << i.m_Name << endl;
    }

}


```



### random_shuffle

指定范围内的元素随机调整次序

```c
random_shuffle(iterator beg, iterator end);
random_shuffle(开始迭代器, 结束迭代器);

//伪随机

void test()
{
    vector<int>v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);

    random_shuffle(v.begin(), v.end());

    for (auto i : v)
        cout << i << endl;
}

//真随机(#include<time.h>)

void test()
{
    srand((unsigned int)time(NULL));  // 按系统时间进行随机
    vector<int>v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);
    random_shuffle(v.begin(), v.end());
    for (auto i : v)
        cout << i << endl;
}
```

### merge

两个容器元素合并, 并存储到另一容器中

```c
//注意：两个容器必须是有序的 , 而且在合并以后依然是有序的
//注意: 一定要在合并之后存放的容器中开辟空间
merge(iterator beg1, iterator end1, 
      iterator beg2, iterator end2, 
      iterator dest);
merge(容器1开始迭代器, 容器1结束迭代器, 
      容器2开始迭代器, 容器2结束迭代器, 
      目标容器开始迭代器);

void test()
{
    vector<int>v;
    vector<int>v1;
    vector<int>vt;
    for (int i = 0; i < 5; i++)
        v.push_back(i);
    for (int i = 5; i < 10; i++)
        v1.push_back(i);

    vt.resize(v.size() + v1.size());

    merge(v.begin(), v.end(), 
    		v1.begin(), v1.end(), vt.begin());

    for (auto i : vt)
        cout << i << " ";
}

```

### reverse

将容器内元素进行反转

```c
reverse(iterator beg, iterator end);
reverse(开始迭代器, 结束迭代器);

void test()
{
    vector<int>vt;
    for (int i = 0; i < 5; i++)
        vt.push_back(i);
    reverse(vt.begin(), vt.end());
    for (auto i : vt)
        cout << i << " ";
}
```

