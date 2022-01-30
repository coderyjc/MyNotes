## 最近使用的文件
```dataview
table file.mtime
where date(today) - file.mtime < 3
sort file.mtime desc
limit 10
```
