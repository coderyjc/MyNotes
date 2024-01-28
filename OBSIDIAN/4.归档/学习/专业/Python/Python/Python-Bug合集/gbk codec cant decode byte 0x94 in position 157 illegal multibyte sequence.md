---
type: DeBug
skill: Python
create_date: 2022-03-30
---

#Python 

**报错代码:**

```python
def formatContext():
 source_file = open(SOURCE_FILE, 'r')
 text = source_file.read()
 print(text)
```

**原因:**

编码不支持, open函数无法解析相关的编码

**解决方案:**

1. 如果知道文件的编码格式, 可以指定编码格式

```python  
def formatContext():
 source_file = open(SOURCE_FILE, 'r', encoding='utf-8')
 text = source_file.read()
 print(text)
```

2. 如果不知道文件的编码格式, 可以直接用二进制的方式打开

```python
def formatContext():
 with open(SOURCE_FILE, 'r') as f:
	 text = f.read()
	 print(text)
```