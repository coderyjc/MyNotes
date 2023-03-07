## np数组的构造

### 通过array构造

最一般的方法：通过array构造

```python
import numpy as np
```


```python
In [38]: np.array([1, 2, 3, 4, 5])
Out[38]: array([1, 2, 3, 4, 5])
```

### 【a】等差序列 `np.linspave` `np.arange`

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

### 【b】特殊矩阵 `zeros`, `eye`, `full`

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


### 随机矩阵 `np.random`

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

In [20]: # 随机种子，能够固定随机数的输出结果

In [21]: np.random.seed(0)

In [22]: np.random.rand()
Out[22]: 0.5488135039273248

In [23]: np.random.seed(0)

In [24]:

In [24]: np.random.rand()
Out[24]: 0.5488135039273248

```

## np数组的变形与合并

```python
In [1]: import numpy as np
```



```python


In [2]: np.zeros( (2,3) ).T
Out[2]:
array([[0., 0.],
       [0., 0.],
       [0., 0.]])

In [4]: np.r_[np.zeros((2,3)), np.zeros((2,3))]
Out[4]:
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])

In [5]: np.c_[np.zeros((2,3)), np.zeros((2,3))]
Out[5]:
array([[0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.]])

In [6]: # 一维数组和二维数组进行合并时，应当把其视作列向量，在长度匹配的情况下只能
   ...: 够使用左右合并的 c_ 操作：

In [7]: try:
   ...:     np.r_[np.array([0,0]), np.zeros((2,1))]
   ...: except Exception as e:
   ...:     msg = e
   ...:

In [8]: msg
Out[8]: ValueError('all the input arrays must have same number of dimensions, but the array at index 0 has 1 dimension(s) and the array at index 1 has 2 dimension(s)')

In [9]: np.r_[np.array([0,0]), np.zeros(2)]
Out[9]: array([0., 0., 0., 0.])

In [10]: np.r_[np.array([1,2]), np.zeros(2)]
Out[10]: array([1., 2., 0., 0.])

In [12]: np.c_[np.array([1,2]), np.zeros((2,3))]
Out[12]:
array([[1., 0., 0., 0.],
       [2., 0., 0., 0.]])

In [13]: # reshape 能够帮助用户把原数组按照新的维度重新排列。在使用时有两种模式，分别为 C 模式和 F 模式，分别以逐行和逐列的顺序进行填充读取。

In [14]: target = np.arange(8).reshape(2,4)

In [15]: target
Out[15]:
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])

In [16]: target = np.arange(8).reshape((2,4), order='C')

In [17]: target
Out[17]:
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])

In [20]: target = np.arange(8).reshape((4,2), order='F')

In [21]: target
Out[21]:
array([[0, 4],
       [1, 5],
       [2, 6],
       [3, 7]])

In [22]: # 特别地，由于被调用数组的大小是确定的， reshape 允许有一个维度存在空缺，
    ...: 此时只需填充-1即可

In [23]: target.reshape((4, -1))
Out[23]:
array([[0, 4],
       [1, 5],
       [2, 6],
       [3, 7]])

In [24]: #  下面将n*1大小的数组转换为1维数组

In [25]: target = np.ones((3,1))

In [26]: target
Out[26]:
array([[1.],
       [1.],
       [1.]])

In [27]: target.reshape(-1)
Out[27]: array([1., 1., 1.])

In [28]: #-------------------------------

In [29]: # 数组的切片模式支持使用slice类型的start:end:step切片，还可以直接传入列表
    ...: 指定某个维度的索引进行切片

In [30]: target = np.arange(9).reshape(3,3)

In [31]: target
Out[31]:
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])

In [33]: target[: -1, [0, 2]]
Out[33]:
array([[0, 2],
       [3, 5]])

In [34]: # 此外，还可以利用 np.ix_ 在对应的维度上使用布尔索引，但此时不能使用 slice 切片

In [35]: target[np.ix_([True, False, True], [True, False, True])]
Out[35]:
array([[0, 2],
       [6, 8]])

In [36]: target[np.ix_([1,2], [True, False, True])]
Out[36]:
array([[3, 5],
       [6, 8]])

In [37]: # 当数组维度为1维时，可以直接进行布尔索引，而无需 np.ix_

In [38]: new = target.reshape(-1)

In [39]: new[new % 2 == 0]
Out[39]: array([0, 2, 4, 6, 8])

```

## 常用函数

### where

```python
In [1]: # where

In [4]: a = np.array([-1, 1, -1, 0])

In [5]: np.where(a>0, a, 5)
Out[5]: array([5, 1, 5, 5])

```


### nonzero, argmax, argmin

```python
In [7]: # 返回索引，nonzero返回非零索引，另外两个分别返回最大和最小数的索引

In [8]: a = np.array([-2, -5, 0, 1, 3, -1])

In [9]: np.nonzero(1)
Out[9]: (array([0], dtype=int64),)

In [10]: np.nonzero(a)
Out[10]: (array([0, 1, 3, 4, 5], dtype=int64),)

In [11]: a.argmax()
Out[11]: 4

In [12]: a.argmin()
Out[12]: 1

In [13]: # any, all

In [14]: a = np.array([0, 1])

In [15]: a.any()
Out[15]: True

In [16]: a.all()
Out[16]: False

```

### cumprod, cumsum, diff

```python
In [18]: a = np.array([1,2,3])

In [19]: a.cumprod()
Out[19]: array([1, 2, 6], dtype=int32)

In [20]: a.cumsum()
Out[20]: array([1, 3, 6], dtype=int32)

In [21]: np.diff(a)
Out[21]: array([1, 1])

In [22]: # 统计函数

In [23]: target = np.arange(5)

In [24]: target
Out[24]: array([0, 1, 2, 3, 4])

In [25]: target.max()
Out[25]: 4

In [26]: target.min()
Out[26]: 0

In [27]: np.quantile(target, 0.5)
Out[27]: 2.0


```

但是对于含有缺失值的数组，它们返回的结果也是缺失值，如果需要略过缺失值必须使用 nan* 类型的函数，上述的几个统计函数都有对应的 nan* 函数。也就是函数的名称必须以`nan`开头

```python
In [3]: target = np.array([1, 2, np.nan])

In [4]: target
Out[4]: array([ 1.,  2., nan])

In [5]: target.max()
Out[5]: nan

In [6]: np.nanmax(target)
Out[6]: 2.0

In [7]: np.nanquantile(target, 0.5)
Out[7]: 1.5

```

对于协方差和相关系数分别可以利用 `cov, corrcoef` 如下计算：

```python
In [8]: target1 = np.array([1, 3, 5, 9])

In [9]: target2 = np.array([1, 5, 3, -9])

In [10]: np.cov(target1, target2)
Out[10]:
array([[ 11.66666667, -16.66666667],
       [-16.66666667,  38.66666667]])

In [11]: np.corrcoef(target1, target2)
Out[11]:
array([[ 1.        , -0.78470603],
       [-0.78470603,  1.        ]])
```

最后，需要说明二维 `Numpy` 数组中统计函数的 `axis` 参数，它能够进行某一个维度下的统计特征计算，当 `axis=0` 时结果为列的统计指标，当 `axis=1` 时结果为行的统计指标：

```python
In [12]: target = np.arange(1, 10).reshape(3, -1)

In [13]: target
Out[13]:
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

In [14]: target.sum(0)
Out[14]: array([12, 15, 18])

In [15]: target.sum(1)
Out[15]: array([ 6, 15, 24])
```


