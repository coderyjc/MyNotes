---
create_date: 2024-02-01 11:11
tags:
  - Windows/磁盘清理
  - Windows/C盘
source: https://www.bilibili.com/video/BV16K411v7rc
---

## 系统休眠文件和虚拟内存文件迁移

在`C:`中取消“隐藏受保护的OS文件”，并勾选“显示隐藏的文件xxx”

![[assets/Pasted image 20240201111637.png]]

下述两个文件就是系统休眠文件和虚拟内存文件，这两个文件可以处理以下。

![[assets/Pasted image 20240201112804.png]]

- `hiberfill.sys` cmd输入命令`powercfg.exe -h off`
- `pagefile` 可以移动到其他盘中去

1. 此电脑 - 属性 - 高级系统设置 - 高级 - 性能设置 - 高级 - 更改虚拟内存

![[assets/Pasted image 20240201113413.png]]

2. 取消勾选自动管理xxx，选择C盘，无分页文件

![[assets/Pasted image 20240201113620.png]]

3. 选择自己想要移动到的盘符，选择自定义大小，按照推荐填写即可。

![[assets/Pasted image 20240201113721.png]]

## 清理临时文件等

C盘中这些文件都可以选择性清理。

- Prefetch
- Temp
- Logfiles
- Download

## Windows自动的文件清理功能

1. C盘的文件清理，C盘 - 属性 - 磁盘清理

![[assets/Pasted image 20240201114234.png]]

2. Windows系统自带的存储感知

Win+S搜索存储，打开即可。

![[assets/Pasted image 20240201114524.png]]


## 存储清理软件

Dism++


