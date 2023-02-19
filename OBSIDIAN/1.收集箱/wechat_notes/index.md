---
cssClasses: cards cards-align-bottom cards-2-3 table-100
banner: "_plugin/banners/book-banner.gif"
banner_x: 0.5
banner_y: undefined
banner_icon: 📚
---


```dataviewjs
dv.table(["封面","书名", "作者", "类型"], dv.pages("#读书")
    .map(b => [("![](" + b.cover + ")"), b.file.link, b.author, b.category]))
```



