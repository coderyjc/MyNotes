---
cssClasses: cards cards-align-bottom cards-2-3 table-100
---

```dataviewjs
dv.table(["封面","书名", "作者", "类型", "评分"], dv.pages("#读书")
    .map(b => [("![](" + b.cover + ")")