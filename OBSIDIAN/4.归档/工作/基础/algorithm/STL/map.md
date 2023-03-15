## 创建以string为键的map

不加这个判断函数也可以，有时候**加上了反而拉低了运行速度**。

```cpp
#include<string.h>

struct StrCmp {
	bool operator()(string l, string r) const { return strcasecmp(l.c_str(), r.c_str()) < 0; }
};
```


## map的直接插入不需要判断是否存在

