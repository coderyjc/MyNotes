---
type: DeBug
skill: Python
create_date: 2022-03-30
---

#Python 

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