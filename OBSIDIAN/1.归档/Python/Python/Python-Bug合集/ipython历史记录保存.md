1. 利用hist保存当前session历史记录到文件

```python
# 在ipython中输入以下命令，保存的python代码不包含输出
%hist -f log.txt
```

2. 利用logstart保存当前session历史记录到文件

```python
# 在ipython中输入以下命令，保存的python代码包含输出
# -o: 保存输出
# -r: 保存原始输入
# -t: 保存每一行输入的时间
# 历史记录/history.py: 保存的路径，也可以保存为其他格式，比如.md, .txt
%logstart -o -r -t log.txt
import pandas as pd
# 一连串操作后
%logstop
```

