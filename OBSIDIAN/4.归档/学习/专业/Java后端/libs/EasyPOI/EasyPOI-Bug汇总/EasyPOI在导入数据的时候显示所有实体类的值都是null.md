问题描述

![[assets/Pasted image 20230408150055.png]]

原因：

设置表头和列标题的时候，那个参数是数量，而不是下标。

```java
// 表头设置为首行  
params.setHeadRows(1);  
params.setTitleRows(0);
```

![[assets/Pasted image 20230408150302.png]]
