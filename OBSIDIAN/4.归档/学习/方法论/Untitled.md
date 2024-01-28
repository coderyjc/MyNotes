---
create_date: 2024-01-28 11:27
tags: 
aliases:
  - 笔记搜索
  - 搜索笔记
source: 【视频】如何在obsidian中找到你要的笔记? https://www.bilibili.com/video/BV19b4y1P7RW
---

## 使用Obsidian内置的Quick Switch快速切换，`Ctrl+O`

可以在front-matter中设置aliases文章别名，从而在搜索的时候使用别名。方便，但只能搜索标题，别名格式：

```yml
# 单个别名：
aliases: 别名

# 多个别名
aliases: 
  - 别名1
  - 别名2
```

## 使用Obsidian内置的搜索功能

1. 直接搜索关键词。 

2. 使用`" "`引号把关键词词组整体括起来

3. 使用搜索语法
	1. 空格，使用空格将关键词区分开表示和。比如，`Obsidian template`搜索的是带有`Obsidian`和`template`的结果。
	2. OR，使用OR将关键词分开表示或。比如`Obsidian OR template`搜索的是带有`Obsidian`或者`template`的结果。
	3. 减号-，使用减号去除部分关键词。比如`Obsidian -template`搜索的是带有`Obsidian`但是不带有`template`的结果。
综合上述搜索语法



4. 使用搜索选项path\file\tag\line\section，略

5. 使用匹配文档属性`[date: ]`