---
tags:
  - Windows/重装系统
  - Windows/EasyU
  - Windows/PE系统
---


> 系统的格式不是iso，而是esd格式

## 制作U盘的PE启动盘

![[assets/image-20221226114515692.png]]

![[assets/image-20221226114554494.png]]

![[assets/image-20221226115255370.png]]

PE系统的U盘就制作完成了

下载镜像并放入U盘中

直接将`.esd`格式的文件复制进去就行

## 插入U盘进入BIOS模式

> **方法一：利用快捷键进入BIOS**
>
>1.开机或重启电脑。
>
>2.当屏幕显示【Lenovo】logo时，快速连续点按【F2】键即可进入BIOS。
>
>**方法二：利用NOVA孔进入BIOS**
>
>1.在电脑关机状态下，使用卡针之类的物品戳下位于机身侧面的【NOVO】孔。
>
>2.电脑启动后，选择【BIOS SETUP】选项即可进入BIOS。
>
>**方法三：利用恢复系统界面进入BIOS**
>
1.打开电脑，点击屏幕左下角的【开始】图标，点击【电源】。
>
>2.按住【shift】键不松，点击【重启】按钮。
>
>3.在进入的界面中，依次点击【疑难解答】-【高级选项】-【UEFI固件设置】即可进入BIOS。

这里使用恢复系统界面进入BIOS

按住Shift点击开始菜单中的重启

重启后进入如下界面，点击“使用设备”

![[assets/Pasted image 20221226224150.png]]

选择第一个，使用EFI USB设备

![[assets/Pasted image 20221226224313.png]]

选择默认的Boot Manager（不用动，会自动进入）

![[assets/Pasted image 20221226224348.png]]

进入之后的界面

![[assets/Pasted image 20221226224411.png]]

可以使用DiskGenius 进行硬盘分区（也可以不分区）

![[assets/Pasted image 20221226224424.png]]

点击系统安装进行安装系统

![[assets/Pasted image 20221226224501.png]]

选择分区类型、镜像名称和磁盘位置进行安装

![[assets/Pasted image 20221226224524.png]]

点击确认执行

![[assets/Pasted image 20221226224553.png]]

等待执行

![[assets/Pasted image 20221226224606.png]]

执行完毕自动重启，安装成功。

![[assets/Pasted image 20221226224617.png]]