---
type: DeBug
skill: Redis
create_date: 2022-01-31
---

#数据库 #Redis #NoSQL

# Redis

>  将Redis作为系统服务启动，启动失败

现象：

![[assets/Pasted image 20230102143317.png]]

原因：

必须保证所有的进程都已经关闭了才能作为系统进程启动。

以下这两个进程必须都关掉，才能启动成功，使用 `sudo kill -9 {PID}`

![[assets/Pasted image 20230102143119.png]]

关闭进程

![[assets/Pasted image 20230102143227.png]]

启动服务

![[assets/Pasted image 20230102143250.png]]

启动成功

![[assets/Pasted image 20230102143258.png]]



> 远程连接Redis数据库插入数据显示 backup0, backup1...

云数据库没有设置密码。

打开 redis.conf 文件，设置密码重新连接即可。

![[Pasted image 20220131012542.png]]

Redis 远程主机强迫关闭了一个现有的连接

设置配置文件中的这个为 300 → 60

![[Pasted image 20220131012553.png]]

