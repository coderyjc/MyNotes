```python
import pandas
```

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


