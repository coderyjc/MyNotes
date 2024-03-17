# HOME

```dataviewjs

// 计算使用天数
var today = new Date(); 
var startDate = new Date('2021-12-22');
var timeDiff = today.getTime() - startDate.getTime(); 
var daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));

// 文档总数
var doc_total = dv.pages().length
// 归档数量
var doc_archieve = dv.pages(`"4.归档"`).length
// 读书笔记
var doc_reading = dv.pages(`"4.归档/学习/读书/微信读书同步"`).length
// 标签总数
var tag_total = dv.pages().file.etags.distinct().length
// 任务总数
var task_total = dv.pages().file.tasks.length

// 渲染内容
var content = `在你使用Obsidian的**${daysDiff}**天里，
			你一共写下了**${doc_total}**篇文档
			共计 **936,177** 字
			图片 **1855** 张
			读了**${doc_reading}**本书
			完成了**${task_total}**个任务
			打下了**${tag_total}**个标签`

dv.paragraph(content)
```

## 未完成任务

```dataview
task
from "2.等待处理"
where !completed
```

