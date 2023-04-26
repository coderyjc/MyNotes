---
wordCount: 0
charCount: 0
---

---

```dataviewjs
let sum = 0, sumChar = 0
dv.pages(`"5.专题研究/【本科毕设】教师资格证数据分析系统/毕业论文"`).filter(p => {
sum += p.wordCount
sumChar += p.charCount
})
dv.paragraph(`总字数: ==${sum}==`)
dv.paragraph(`字符数: ==${sumChar}==`)
```

---


```dataview
table wordCount as 字数, charCount as 字符数
from "5.专题研究/【本科毕设】教师资格证数据分析系统/毕业论文"
```

---

[[摘要]]

[[第1章 绪论]]

[[第2章 系统关键技术]]

[[第3章 系统需求分析]]

[[第4章 系统设计]]

[[第5章 系统的实现]]

[[第6章 系统测试]]

[[第7章 总结与展望]]

[[参考文献、致谢]]
