

```python
type_1_labels = type_1_labels[:TYPE_1_COUNT]

type_1_labels.append('其他') # 添加了这个标签

temp = 500 - np.sum(type_1_count[TYPE_1_COUNT:])

type_1_count = type_1_count[:TYPE_1_COUNT]

type_1_count.append(temp) # 添加了这个数据
```


![[assets/Pasted image 20220521211402.png]]

原因：pyecharts 中的数据源的整形数据类型必须是int类型，而不是numpy的类型，我在上面用了numpy的sum

```python
type_1_labels = type_1_labels[:TYPE_1_COUNT]

type_1_labels.append('其他')

temp = int(500 - np.sum(type_1_count[TYPE_1_COUNT:])) # 转换成int即可

type_1_count = type_1_count[:TYPE_1_COUNT]

type_1_count.append(temp)
```

