
```dataviewjs
var i = [dv.pages().length,
		 dv.pages(`"4.归档"`).length,
		 dv.pages(`"5.专题研究"`).length,
		 dv.pages(`"1.收集箱/wechat_notes"`).length,
		 dv.pages().file.etags.distinct().length,
		 dv.pages().file.tasks.length]

dv.paragraph(`总共有 **${i[0]}** 篇文档，共计 **1,046,699** 字`)
dv.paragraph(`==已归档笔记== **${i[1]}** 篇，==正在进行的笔记== **${i[2]}** 篇，==读书笔记== **${i[3]}** 篇`)
dv.paragraph(`==任务== **${i[5]}** 个，==标签==  **${i[4]}** 个`)

```

## 待完成的任务：

```dataview
task 
from "2.等待处理"
where !completed
```