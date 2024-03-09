# STL-遍历算法

#Cpp/STL/遍历算法

### for_each

用函数遍历元素

```c
for_each(iterator begin, iterator end, _func);
for_each(开始迭代器, 结束迭代器, _func函数或者函数对象);

//普通函数
void print(int i)
{
    cout << i << endl;
}

//仿函数
class Print
{
public:
    void operator()(int i)
    {
        cout << i << endl;
    }
};

void test()
{
    vector<int>v;
    for (int i = 0; i < 10; i++) v.push_back(i);

//普通函数对象
    for_each(v.begin(), v.end(), print); 

//重载了 () 的匿名函数对象
    for_each(v.begin(), v.end(), Print()); 
}
```



### transform

将一个容器中的元素搬运容器到另一个容器中, 前提是目标容器需要提前开辟空间

```c
transform(iterator begin1, iterator end1, iterator begin2, _func);
transform(原容器开始迭代器, 原容器结束迭代器, 目标容器开始迭代器,函数或者函数对象(回调函数));


class Transform
{
    // 在搬运的过程中可以进行一些操作
public:
    int operator()(int i)
    {
        return i;
    }
};

void test()
{
    vector<int> v;
    for (int i = 0; i < 10; i++)
        v.push_back(i);
    vector<int> v1;
    v1.resize(v.size()); //提前开辟空间
    transform(v.begin(), v.end(), v1.begin(), Transform()); //搬运
}
```

