

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




### most_common()



### subtract

