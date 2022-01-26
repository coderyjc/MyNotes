## 最近使用的文件

```dataview
table file.name as 文件名, striptime(file.mtime) as 修改时间
where date(today) - file.mtime < 3
sort file.mtime desc
limit 10
```

