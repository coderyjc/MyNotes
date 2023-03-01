```python
import pandas
```

## Python基础

### 列表推导式和条件赋值

假设我们要生成一个列表

```python
In [8]: def my_func(x):
   ...:     return 2*x
   ...:

In [9]: for i in range(5):
   ...:     L.append(my_func(i))
   ...:

In [10]: L
Out[10]: [0, 2, 4, 6, 8]
```

简单写法

```python
In [11]: [my_func(x) for x in range(5)]
Out[11]: [0, 2, 4, 6, 8]
```

多层嵌套

```python
In [12]: [m+'-'+n for m in ['a', 'c'] for n in ['c','d']]
Out[12]: ['a-c', 'a-d', 'c-c', 'c-d']
```

除此之外，另一个实用的语法糖是带有 if 选择的条件赋值，其形式为 `value = a if condition else b`

```python
In [13]: value = 'cat' if 2 > 1 else 'dog'

In [14]: value
Out[14]: 'cat'
```

举例：截断列表中超过5的元素，即超过5的用5代替，小于5的保留原来的值

```python
In [15]: L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

In [16]: [i if i <= 5 else 5 for i in L]
Out[16]: [1, 2, 3, 4, 5, 5, 5, 5, 5]
```


### 匿名函数与map方法

函数映射关系比较简单的函数，可以使用匿名函数，比如：

```python
In [17]: my_fun = lambda x: 5*x

In [18]: my_fun(8)
Out[18]: 40
```

```python
In [19]: multi_fun = lambda a, b: a * b

In [20]: multi_fun(5, 6)
Out[20]: 30
```

上述只是举例，说是匿名函数，还是给它起了一个名字的，真正使用的时候不会命名的，如下：

```python
# 0-4的平方列表
In [21]: [(lambda x: x*x)(i) for i in range(5)]
Out[21]: [0, 1, 4, 9, 16]
```

对于上述的这种列表推导式的匿名函数映射， Python 中提供了 map 函数来完成，它返回的是一个 map 对象，需要通过 list 转为列表：

```python
In [22]: list(map(lambda x: x*x, range(5)))
Out[22]: [0, 1, 4, 9, 16]
```

对于多个输入值的函数映射，可以通过追加迭代对象实现

```python
In [23]: list(map(lambda a,b:str(a)+'_'+str(b), range(5), list('abcde')))
Out[23]: ['0_a', '1_b', '2_c', '3_d', '4_e']
```

### zip对象和enumerate方法

zip函数能够把多个可迭代对象打包成一个元组构成的可迭代对象，它返回了一个 `zip` 对象，通过 `tuple`, `list` 可以得到相应的打包结果：


```python
In [24]: L1, L2, L3 = list('abc'), list('def'), list('ghi')

In [25]: list(zip(L1, L2, L3))
Out[25]: [('a', 'd', 'g'), ('b', 'e', 'h'), ('c', 'f', 'i')]
```

```python
In [26]: tuple(zip(L1, L2, L3))
Out[26]: (('a', 'd', 'g'), ('b', 'e', 'h'), ('c', 'f', 'i'))
```

```python
# 往往会在循环迭代的时候用到zip函数

In [27]: for i,j,k in zip(L1, L2, L3):
    ...:         print(i, j, k)
    ...:
a d g
b e h
c f i
```

enumerate 是一种特殊的打包，它可以在迭代时绑定迭代元素的遍历序号：

```python
In [28]: L = list('abcdefghij')

In [29]:

In [29]: for index, value in enumerate(L):
    ...:         print(index, value)
    ...:
0 a
1 b
2 c
3 d
4 e
5 f
6 g
7 h
8 i
9 j
```


```python
# zip对象也能简单实现这个功能

In [30]: for index,value in zip(range(len(L)), L):
    ...:         print(index, value)
    ...:
0 a
1 b
2 c
3 d
4 e
5 f
6 g
7 h
8 i
9 j

```

当需要对两个列表建立字典映射，可以使用zip对象

```python
In [31]: L1, L2= list('abc'), list('def')

In [32]: dict(zip(L1, L2))
Out[32]: {'a': 'd', 'b': 'e', 'c': 'f'}
```

也可以使用* 操作符和zip联合使用进行解压

```python
In [33]: L1, L2= list('abc'), list('def')

In [34]: zipped = list(zip(L1, L2))

In [35]: print(zipped)
[('a', 'd'), ('b', 'e'), ('c', 'f')]

In [36]: list(zip(*zipped))
Out[36]: [('a', 'b', 'c'), ('d', 'e', 'f')]
```

## Numpy基础

### np数组的构造

最一般的方法：通过array构造

```python
import numpy as np
```


```python
In [38]: np.array([1, 2, 3, 4, 5])
Out[38]: array([1, 2, 3, 4, 5])
```

【a】等差序列 `np.linspave` `np.arange`

```python
# 起始，终止（包含），样本个数
In [39]: np.linspace(1, 5, 11)
Out[39]: array([1. , 1.4, 1.8, 2.2, 2.6, 3. , 3.4, 3.8, 4.2, 4.6, 5. ])
```

```python
# 起始，终止（不包含），步长
In [40]: np.arange(1, 5, 2)
Out[40]: array([1, 3])
```

【b】特殊矩阵 `zeros`, `eye`, `full`

```python
# 传入元组表示各维度的大小
In [41]: np.zeros( (2,3) )
Out[41]:
array([[0., 0., 0.],
       [0., 0., 0.]])
```

```python
# 单位矩阵
In [42]: np.eye(3)
Out[42]:
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

```python
# 单位矩阵，但是偏移主对角线一个单位
In [43]: np.eye(3, k=1)
Out[43]:
array([[0., 1., 0.],
       [0., 0., 1.],
       [0., 0., 0.]])
```

```python
# 元组传入大小，10表示填充的数值

In [44]: np.full((2,3), 10)
Out[44]:
array([[10, 10, 10],
       [10, 10, 10]])
```

```python
# 每行填入相同的列表
In [45]: np.full((2,3), [3,2,1])
Out[45]:
array([[3, 2, 1],
       [3, 2, 1]])
```


随机矩阵 `np.random`

常用的随机生成函数：

|函数|解释|
|---|---|
|rand| 0-1均匀分布的随机数组 |
|randn| 标准正态的随机数组|
|randint| 随机整数组 |
|choice| 随机列表抽样 |

```python
# 服从a到b上的均匀分布
In [46]: a, b = 5, 15

In [47]: a + (b - a) * np.random.rand(3)
Out[47]: array([11.57051327, 10.44140662, 10.6245656 ])
```

```python
# 一般的，可以选择已有的库函数
In [48]: np.random.uniform(5, 15, 3)
Out[48]: array([13.99944719,  8.2915491 , 13.961735  ])
```

```python
# N(0,1)的标准正态分布
In [2]: np.random.randn(3)
Out[2]: array([-0.10208955, -0.59637412, -0.70934939])

In [3]: np.random.randn(2, 3)
Out[3]:
array([[-0.38054416, -0.76975813,  0.40188118],
       [ 0.17018451, -0.18915139, -0.36936135]])
```


```python

In [2]: np.random.randn(3)
Out[2]: array([-0.10208955, -0.59637412, -0.70934939])

In [3]: np.random.randn(2, 3)
Out[3]:
array([[-0.38054416, -0.76975813,  0.40188118],
       [ 0.17018451, -0.18915139, -0.36936135]])

In [4]: # 对于服从方差为sigma，均值为mu的医院正态分布可以如下生成：

In [5]: sigma, mu = 2.5, 3

In [6]: mu + np.random.randn(3) * sigma
Out[6]: array([5.80186531, 4.1277138 , 3.18129065])

In [7]: # 同样的，也可以选择从已有函数生成

In [8]: np.random.normal(3, 2.5, 3)
Out[8]: array([0.93387648, 0.12258885, 0.35415961])

In [9]: # randint可以指定生成随即证书的最小值和最大值（不包含）和纬度大小

In [10]: low, high, size = 5, 15, (2, 2)

In [11]: # 生成5-14的随机整数

In [12]: np.random.randint(low, high, size)
Out[12]:
array([[ 6, 10],
       [14,  8]])

In [13]: # choice 可以从给定的列表中以一定的概率和方式抽取结果，当不指定概率时为均
    ...: 匀采样，默认抽取方式是有放回抽样

In [14]: my_list = ['a', 'b', 'c', 'd']

In [16]: np.random.choice(my_list, 2, replace=False, p=[0.1, 0.7, 0.1, 0.1])
Out[16]: array(['d', 'a'], dtype='<U1')

In [17]: np.random.choice(my_list, (2, 3))
Out[17]:
array([['a', 'a', 'a'],
       ['b', 'd', 'd']], dtype='<U1')

In [18]: # 当返回的元素个数与原列表相同时，不放回抽样等价于使用permutation函数，也
    ...: 就是打散原列表

In [19]: np.random.permutation(my_list)
Out[19]: array(['d', 'b', 'a', 'c'], dtype='<U1')

In [20]: # 随即种子，能够固定随机数的输出结果

In [21]: np.random.seed(0)

In [22]: np.random.rand()
Out[22]: 0.5488135039273248

In [23]: np.random.seed(0)

In [24]:

In [24]: np.random.rand()
Out[24]: 0.5488135039273248

```

### np数组的变形与合并

