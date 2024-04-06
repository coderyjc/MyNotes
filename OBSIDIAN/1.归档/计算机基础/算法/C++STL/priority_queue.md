# priority queue 优先级队列

#Cpp/STL/priority_queue 

```cpp
#include<queue>
```

## 操作

```cpp
pq.empty() //如果队列为空返回真

pq.pop() //删除对顶元素

pq.push() //加入一个元素

pq.size() //返回优先队列中拥有的元素个数

pq.top() //返回优先队列对顶元素
```

## 设置优先级

```cpp
struct cmp1{  
    bool operator ()(int &a,int &b){  
        return a>b;//最小值优先  
    }
};

priority_queue<int,vector<int>,cmp1>pq;

// --------------------------------------------------

struct cmp2{  
    bool operator ()(int &a,int &b){  
        return a<b;//最大值优先  
    }  
};

priority_queue<int,vector<int>,cmp2>pq2;

// --------------------------------------------------

struct node  //自定义类型优先级设定
{
    friend bool operator< (node n1, node n2)//重载小于号，，不要重载大于号，可能报错
    {
        return n1.priority < n2.priority;// (priority)大的优先级高
    }
    int priority;
    int value;
};

priority_queue<node> pq4;
```

## 参考

- https://blog.csdn.net/chaiwenjun000/article/details/45457125
- 

