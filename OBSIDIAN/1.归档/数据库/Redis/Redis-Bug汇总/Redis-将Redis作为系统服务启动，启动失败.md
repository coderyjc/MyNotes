---
type: DeBug
skill: Redis
create_date: 2022-01-31
---

#Database #Database/Redis #Database/NoSQL

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

