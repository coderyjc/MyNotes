---
wordCount: 0
---


```dataview
table wordCount
from "5.专题研究/【本科毕设】教师资格证数据分析系统/毕业论文"
```


```dataviewjs
let sum = 0
dv.pages(`"5.专题研究/【本科毕设】教师资格证数据分析系统/毕业论文"`).filter(p => sum += p.wordCount)
dv.paragraph(`sum: ==${sum}==`)
```


[[摘要]]

[[第1章 绪论]]

[[第2章 系统关键技术]]

[[第3章 系统需求分析]]

[[第4章 系统设计]]

[[第5章 系统的实现]]

[[第6章 系统测试]]

[[第7章 总结与展望]]

[[参考文献、致谢]]
