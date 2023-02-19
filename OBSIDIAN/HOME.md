---
banner: "_plugin/banners/rainy-day-bird.gif"
banner_icon: 💌
banner_y: 0.24416
banner_x: 0.50168
---

```dataviewjs
let nofold = '!"_plugin"'
let allFile = dv.pages(nofold).file
let totalMd = "共创建 "+
	allFile.length+" 篇文档"
let totalTag = allFile.etags.distinct().length+" 个标签"
let totalTask = allFile.tasks.length+" 个待办 <br><br>"
dv.paragraph(
	totalMd+"、"+totalTag+"、"+totalTask
)
``` 



````ad-flex
<div>

### 最近编辑
```dataview
table WITHOUT ID file.link AS "标题",file.mtime as "时间"
from !"模板" and !"kanban"
sort file.mtime desc
limit 5
```
</div>

<div>

### 三天内创建的笔记
```dataview
table file.ctime as 创建时间
from ""
where date(today) - file.ctime <=dur(3 days)
sort file.ctime desc
limit 5
```
</div>
````


## 数量分布图

```dataviewjs
await dv.view("_plugin/dataview/notes_count_view")
```

