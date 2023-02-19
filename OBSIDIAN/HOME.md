---
banner: "_plugin/banners/rainy-day-bird.gif"
banner_icon: 💌
banner_y: 0.304
banner_x: 0.50094
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

```dataview
table WITHOUT ID 
	file.link AS "最近编辑",file.mtime as "时间"
sort 
	file.mtime desc
limit 5
```

## 数量分布图
```dataviewjs
await dv.view("_plugin/dataview/notes_count_view")
```




