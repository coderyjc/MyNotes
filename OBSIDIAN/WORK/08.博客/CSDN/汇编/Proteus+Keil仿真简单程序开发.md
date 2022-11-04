
[TOC]



# Proteus 创建89c51项目

file -> new project (文件 -> 新项目)

![image-20211015200616298](Proteus+Keil仿真简单程序开发.imgs/image-20211015200616298.png)

如图，选择Default，然后next

![image-20211015200647902](Proteus+Keil仿真简单程序开发.imgs/image-20211015200647902.png)

如图，选择不创建PCB Layout

![image-20211015200713180](Proteus+Keil仿真简单程序开发.imgs/image-20211015200713180.png)

如图，创建Firmware Project

![image-20211015201012745](Proteus+Keil仿真简单程序开发.imgs/image-20211015201012745.png)

点击next，然后Finish即可。

完成之后会自动打开一个asm文件，关掉即可

![image-20211015201106558](Proteus+Keil仿真简单程序开发.imgs/image-20211015201106558.png)

项目创建完成。 

# Proteus 绘制流水灯

## 添加组件

![image-20211015202342243](Proteus+Keil仿真简单程序开发.imgs/image-20211015202342243.png)

![image-20211015202505480](Proteus+Keil仿真简单程序开发.imgs/image-20211015202505480.png)

![image-20211015202632843](Proteus+Keil仿真简单程序开发.imgs/image-20211015202632843.png)

刚才选择的组件就添加进来了。

> 【注意】直接双击搜索结果中的组件也可以直接添加（适合一次性添加多个组件）

![image-20211015202658063](Proteus+Keil仿真简单程序开发.imgs/image-20211015202658063.png)

## 绘制组件

选择组件

![image-20211015203350650](Proteus+Keil仿真简单程序开发.imgs/image-20211015203350650.png)

点击画板，鼠标指针变为组件形状，再次点击可放置组件

![image-20211015203415030](Proteus+Keil仿真简单程序开发.imgs/image-20211015203415030.png)

双击组件可以设置属性。 

![image-20211015203450243](Proteus+Keil仿真简单程序开发.imgs/image-20211015203450243.png)

成品图

![image-20211015204924120](Proteus+Keil仿真简单程序开发.imgs/image-20211015204924120.png)

## 常用组件

LED灯

- LED-BLUE
- LED-YELLO
- LED-GREEN
- LED-RED

电阻

- RES

电源和接地是同一个组件，双击设置一下就好

![image-20211015204859513](Proteus+Keil仿真简单程序开发.imgs/image-20211015204859513.png)

# Keil 创建项目

> > 如果老师给了相关软件，尽量用老师给的，老师给的不会错的。。。。

菜单栏 Project -> new uVision Project

填写项目名称

搜索并选择设备

![image-20211016091321449](Proteus+Keil仿真简单程序开发.imgs/image-20211016091321449.png)

自己手动创建一个main.c文件即可

![image-20211016091409089](Proteus+Keil仿真简单程序开发.imgs/image-20211016091409089.png)



# Keil 生成 hex 文件

点击魔法棒图标，选择生成文件夹，选择创建hex file

点击ok

![image-20211016092621431](Proteus+Keil仿真简单程序开发.imgs/image-20211016092621431.png)

进行编译

![image-20211016092706191](Proteus+Keil仿真简单程序开发.imgs/image-20211016092706191.png)

可以看到文件夹中生成了hex文件

![image-20211016093026168](Proteus+Keil仿真简单程序开发.imgs/image-20211016093026168.png)

# proteus中加载hex文件

双击89c51，选择hex文件

![image-20211016093144639](Proteus+Keil仿真简单程序开发.imgs/image-20211016093144639.png)

点击ok，点击运行

![image-20211016094242714](Proteus+Keil仿真简单程序开发.imgs/image-20211016094242714.png)

可以看出，8个流水灯全亮，然后逐个熄灭。

![image-20211016094304285](Proteus+Keil仿真简单程序开发.imgs/image-20211016094304285.png)

