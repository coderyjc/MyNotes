

`Counter`实际上是`dict`的一个子类，上面的结果可以看出每个字符出现的次数。

## 构建


```python
counter_str = Counter('hello')
counter_list = Counter(['h', 'e', 'l', 'l', 'o'])
counter_tuple = Counter(('h', 'e', 'l', 'l', 'o'))
counter_dict = Counter({'h':1, 'e':1, 'l':2, 'o':1})

print(counter_str['h'])
print(counter_list['e'])
print(counter_tuple['l'])
print(counter_dict['o'])
```

以上方法得到的结果是一致的

虽然传入的 mapping 类型的数据是一样的，**但是由于字典中的键是唯一的，因此如果多次插入同一个key的value，会保留最后一个**。

## 方法

### 继承自字典的方法

![[assets/v2-2f8fc96149c2e900147b1ac3e4e789b2_720w.webp]]

但是有两个方法和在字典中有区别

![[assets/v2-8718e143bcd4df871f609d7ed4dc8cd4_720w.png]]

### elements()

返回一个==迭代器==，每个元素重复的次数为它的数目，顺序是任意的顺序，如果一个元素的数目少于1，那么elements()就会忽略它

```python
test = "aasdofijclkaoldsjikfalskjxcv"
counter_test = Counter(test)

print("".join(counter_test.elements()))
```

> 'aaaasssddooffiijjjcclllkkkxv'

### most_common()

返回一个==列表==，包含counter中n个最大数目的元素，如果忽略n或者为None，most_common()将会返回counter中的所有元素，元素有着相同数目的将会选择出现早的元素

```python
test = "aasdofijclkaoldsjikfalskjxcv"
counter_test = Counter(test)

print(counter_test.most_common(1))
print(counter_test.most_common(2))
```

>[('a', 4)] 
>[('a', 4), ('s', 3)]

### update

从一个可迭代对象（可迭代对象是一个元素序列，而非(key,value)对构成的序列）中或者另一个映射（或counter）中所有元素**相加**，是数目相加而非替换它们

```python
dic1 = {'a': 3, 'b': 4, 'c': 0, 'd': 1, 'e': 2, 'f': 0}
dic2 = {'a': 1, 'b': 2, 'c': 1, 'd': 0, 'e': -1}

a = Counter(dic1)
print(a)
b = Counter(dic2)
print(b)

a.update(b)
print(a)
```

>Counter({'b': 4, 'a': 3, 'e': 2, 'd': 1, 'c': 0, 'f': 0})
>Counter({'b': 2, 'a': 1, 'c': 1, 'd': 0, 'e': -1}) 
>Counter({'b': 6, 'a': 4, 'c': 1, 'd': 1, 'e': 1, 'f': 0})

### subtract

从一个可迭代对象中或者另一个映射（或counter）中，元素**相减**，是数目相减而不是替换它们

```python
dic1 = {'a': 3, 'b': 4, 'c': 0, 'd': 1, 'e': 2, 'f': 0}
dic2 = {'a': 1, 'b': 2, 'c': 1, 'd': 0, 'e': -1}

a = Counter(dic1)
print(a)
b = Counter(dic2)
print(b)

a.subtract(b)
print(a)
```

>Counter({'b': 4, 'a': 3, 'e': 2, 'd': 1, 'c': 0, 'f': 0})
>Counter({'b': 2, 'a': 1, 'c': 1, 'd': 0, 'e': -1})
>Counter({'e': 3, 'a': 2, 'b': 2, 'd': 1, 'f': 0, 'c': -1})

