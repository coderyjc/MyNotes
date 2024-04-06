---
type: DeBug
skill: Redis
create_date: 2022-01-31
---

#Database #Database/Redis #Database/NoSQL

> 远程连接Redis数据库插入数据显示 backup0, backup1...

云数据库没有设置密码。

打开 redis.conf 文件，设置密码重新连接即可。

![[assets/Pasted image 20220131012542.png]]

Redis 远程主机强迫关闭了一个现有的连接

设置配置文件中的这个为 300 → 60

![[assets/Pasted image 20220131012553.png]]

