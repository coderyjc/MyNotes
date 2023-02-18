
<div style="padding: 1.2em 1em; font-size: 1.8rem; text-align: center; border-radius: 6px; font-weight: 700; background: linear-gradient(105deg, #EF32D9, #89FFFD); color: #111116;">
HOME
</div>

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
## 最近编辑

```dataview
table WITHOUT ID 
	file.link AS "标题",file.mtime as "时间"
sort 
	file.mtime desc
limit 5
```

## 数量分布图
```dataviewjs
await dv.view("_plugin/dataview/notes_count_view")
```




