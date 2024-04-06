# 本仓库信息

```dataviewjs

// 计算使用天数
var today = new Date(); 
var startDate = new Date('2021-12-22');
var timeDiff = today.getTime() - startDate.getTime(); 
var daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));

// 文档总数
var doc_total = dv.pages().length
// 归档数量
var doc_archieve = dv.pages(`"1.归档"`).length
// 标签总数
var tag_total = dv.pages().file.etags.distinct().length

// 渲染内容
var content = `在你使用Obsidian的**${daysDiff}**天里，
			你一共写下了**${doc_total}**篇文档
			共计 **584,066** 字
			图片 **1266** 张
			打下了**${tag_total}**个标签`

dv.paragraph(content)
```
