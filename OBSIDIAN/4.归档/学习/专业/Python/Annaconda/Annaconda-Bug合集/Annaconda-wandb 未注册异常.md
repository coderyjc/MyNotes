---
type: 知识点总结
skill: Annaconda
create_date: 2022-02-08
---

#python #annaconda

`wandb.errors.UsageError: api_key not configured (no-tty). call wandb.login(key=[your_api_key])`

![[assets/Pasted image 20220131002908.png]]

在Power Shell 输入命令： wandb init 然后出现下图。

![[assets/Pasted image 20220131002923.png]]

在这注册，然后会获得一个key

复制到下面

理论上就可以了，但是又出现了下面这个错误：

wandb.errors.CommError: check_hostname requires server_hostname

![[assets/Pasted image 20220131002946.png]]

这个是因为我科学上网了，科学上网关了之后：

![[assets/Pasted image 20220131002955.png]]

[WinError 1455] 页面文件太小，无法完成操作。

Python没有装在C盘，系统没有分配虚拟内存

高级系统设置：

![[assets/Pasted image 20220131003010.png]]

或者托管到系统

![[assets/Pasted image 20220131003027.png]]