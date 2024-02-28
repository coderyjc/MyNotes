```dataviewjs
var i = [dv.pages().length,
		 dv.pages(`"4.归档"`).length,
		 dv.pages(`"5.专题研究"`).length,
		 dv.pages(`"4.归档/学习/读书/微信读书同步"`).length,
		 dv.pages().file.etags.distinct().length,
		 dv.pages().file.tasks.length]
var diary = dv.pages(`"2.等待处理/Diary"`).length
dv.paragraph(`总共有 **${i[0]}** 篇文档，共计 **829,862** 字，图片 **1454** 张`)
dv.paragraph(`==已归档笔记== **${i[1]}** 篇
			 ==正在进行的笔记== **${i[2]}** 篇
			 ==读书笔记== **${i[3]}** 篇
			 ==日记== **${diary}**篇`)
dv.paragraph(`==已完成任务== **${i[5]}** 个
			 ==标签==  **${i[4]}** 个`)
```


| 文件类型 | 数量 | 大小 |
|----------|-------|------|
| 图片 | 1454 | 194.19 MBytes |
| 插件相关 | 218 | 85.72 MBytes |
| 其他 | 120 | 76.36 MBytes |
| 书籍 | 1 | 5.65 MBytes |
| 笔记 | 1010 | 3.15 MBytes |


```dataview
task 
from "2.等待处理"
where !completed
```

