```python
import pandas
```

# 预备知识

## Python基础

### 列表推导式和条件赋值

假设我们要生成一个列表


```python
L = []

def my_func(x):
    return 2*x

# 复杂写法
for i in range(5):
    L.append(my_func(i))

print(L)
```

    [0, 2, 4, 6, 8]
    


```python
# 简单写法
[my_func(x) for x in range(5)]
```




    [0, 2, 4, 6, 8]




```python
# 多层嵌套
[m+'-'+n for m in ['a', 'c'] for n in ['c','d']]
```




    ['a-c', 'a-d', 'c-c', 'c-d']



除此之外，另一个实用的语法糖是带有 if 选择的条件赋值，其形式为 `value = a if condition else b`


```python
value = 'cat' if 2 > 1 else 'dog'
value
```




    'cat'



举例：截断列表中超过5的元素，即超过5的用5代替，小于5的保留原来的值


```python
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
[i if i <= 5 else 5 for i in L]
```




    [1, 2, 3, 4, 5, 5, 5, 5, 5]



### 匿名函数与map方法

函数映射关系比较简单的函数，可以使用匿名函数，比如：


```python
my_fun = lambda x: 5*x

my_fun(8)
```




    40




```python
multi_fun = lambda a, b: a * b

multi_fun(5, 6)
```




    30



上述只是举例，说是匿名函数，还是给它起了一个名字的，真正使用的时候不会命名的，如下：


```python
# 0-4的平方列表
[(lambda x: x*x)(i) for i in range(5)]
```




    [0, 1, 4, 9, 16]



对于上述的这种列表推导式的匿名函数映射， Python 中提供了 map 函数来完成，它返回的是一个 map 对象，需要通过 list 转为列表：


```python
list(map(lambda x: x*x, range(5)))
```




    [0, 1, 4, 9, 16]



对于多个输入值的函数映射，可以通过追加迭代对象实现


```python
list(map(lambda a,b:str(a)+'_'+str(b), range(5), list('abcde')))
```




    ['0_a', '1_b', '2_c', '3_d', '4_e']



### zip对象和enumerate方法

zip函数能够把多个可迭代对象打包成一个元组构成的可迭代对象，它返回了一个 `zip` 对象，通过 `tuple`, `list` 可以得到相应的打包结果：


```python
L1, L2, L3 = list('abc'), list('def'), list('ghi')
list(zip(L1, L2, L3))
```




    [('a', 'd', 'g'), ('b', 'e', 'h'), ('c', 'f', 'i')]




```python
tuple(zip(L1, L2, L3))
```




    (('a', 'd', 'g'), ('b', 'e', 'h'), ('c', 'f', 'i'))




```python
# 往往会在循环迭代的时候用到zip函数

for i,j,k in zip(L1, L2, L3):
    print(i, j, k)
```

    a d g
    b e h
    c f i
    

enumerate 是一种特殊的打包，它可以在迭代时绑定迭代元素的遍历序号：


```python
L = list('abcdefghij')

for index, value in enumerate(L):
    print(index, value)
```

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
    


```python
# zip对象也能简单实现这个功能

for index,value in zip(range(len(L)), L):
    print(index, value)
```

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
    

当需要对两个列表建立字典映射，可以使用zip对象


```python
L1, L2= list('abc'), list('def')
dict(zip(L1, L2))
```




    {'a': 'd', 'b': 'e', 'c': 'f'}



也可以使用*操作符和zip联合使用进行解压


```python
L1, L2= list('abc'), list('def')

zipped = list(zip(L1, L2))
print(zipped)

list(zip(*zipped))
```

    [('a', 'd'), ('b', 'e'), ('c', 'f')]
    




    [('a', 'b', 'c'), ('d', 'e', 'f')]



## Numpy基础

### np数组的构造

最一般的方法：通过array构造


```python
import numpy as np
```


```python
np.array([1, 2, 3, 4, 5])
```




    array([1, 2, 3, 4, 5])



【a】等差序列 `np.linspave` `np.arange`


```python
np.linspace(1, 5, 11) # 起始，终止（包含），样本个数
```




    array([1. , 1.4, 1.8, 2.2, 2.6, 3. , 3.4, 3.8, 4.2, 4.6, 5. ])




```python
np.arange(1, 5, 2) # 起始，终止（不包含），步长
```




    array([1, 3])



【b】特殊矩阵 `zeros`, `eye`, `full`


```python
# 传入元组表示各维度的大小
np.zeros( (2,3) )
```




    array([[0., 0., 0.],
           [0., 0., 0.]])




```python
# 单位矩阵
np.eye(3)
```




    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])




```python
# 单位矩阵，但是偏移主对角线一个单位
np.eye(3, k=1)
```




    array([[0., 1., 0.],
           [0., 0., 1.],
           [0., 0., 0.]])




```python
# 元组传入大小，10表示填充的数值
np.full((2,3), 10)
```




    array([[10, 10, 10],
           [10, 10, 10]])




```python
# 每行填入相同的列表
np.full((2,3), [3,2,1])
```




    array([[3, 2, 1],
           [3, 2, 1]])



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

a, b = 5, 15
a + (b - a) * np.random.rand(3)
```




    array([ 5.16236651,  9.86165185, 10.97996388])




```python
# 一般的，可以选择已有的库函数
np.random.uniform(5, 15, 3)
```




    array([ 8.22124052, 14.71862829,  9.30833058])




```python
# N(0,1)的标准正态分布


```


```python

```


```python

```


```python

```


```python

```
