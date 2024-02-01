---
create_date: 2024-02-01 11:11
tags:
  - Windows/磁盘清理
  - Windows/C盘
---

## 系统休眠文件和虚拟内存文件迁移

在`C:`中取消“隐藏受保护的OS文件”，并勾选“显示隐藏的文件xxx”

![[assets/Pasted image 20240201111637.png]]

下述两个文件就是系统休眠文件和虚拟内存文件，这两个文件可以处理以下。

![[assets/Pasted image 20240201112804.png]]

- `hiberfill.sys` cmd输入命令`powercfg.exe -h off`
- 
