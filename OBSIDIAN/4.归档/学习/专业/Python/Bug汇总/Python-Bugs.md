---
type: DeBug
skill: Python
create_date: 2022-03-30
---

#Python 

### 'gbk' codec can't decode byte 0x94 in position 157: illegal multibyte sequence

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

### Pandas读取xls文件时报错

错误1：

```python
import pandas as pd

pd.read_excel(io=r'./data/xxx.xls', engine='openpyxl')
```

> 使用pandas读取xls文件的时候报错：
> **ValueError**: Excel file format cannot be determined, you must specify an engine manually.

错误2：

> 使用xlrd读取xls文件的时候报错：
> **XLRDError**: Unsupported format, or corrupt file: Expected BOF record; found b'<table c'

```python
import xlrd

data = xlrd.open_workbook('./data/xxx.xls')
```

解决：以上错误都是因为xls文件版本太老了，转换成xlsx再读取就行了。
