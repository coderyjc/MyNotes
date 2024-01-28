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
比如：
`obsidian plugin OR template` 
搜索的是`obsidian plugin` 或者 `template`，如果不确定搜索的是什么，也可以在搜索设置中打开“说明搜索含义”
`obsidian (plugin OR template)` 搜索的是文本`obsidian`

4. 使用搜索运算符
	1. `path:`文件路径
	2. `file:`文件名
	3. `tag:`标签
	4. `section:`段落，也就是两个标题之间的内容
	5. `[property:]` 文档属性，比如：`[date: 2024-01 OR 2023-1]` 为搜索文档属性date中含有`2024-01`和`2023-1`的文档，也就是2024年1月，2023年10、11、12月的文档。
	6. `content:`文档内容，包含了标签，段落，标题等，就是文档中的所有内容
	7. `block:`块，可以理解为段落，但是段落之间有空行才叫一个block，否则同属于一个block
	8. `task:`todolist任务
		1. `task-todo:` todolist中的未完成的任务
		2. `task-done:`已经完成的任务

## 扩展用法

可以复制搜索结果

可以使用query语法，复制搜索结果作为代码，粘贴在query代码块中，用于聚合搜索结果为一篇文档。
