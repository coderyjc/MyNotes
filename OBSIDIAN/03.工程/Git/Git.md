### GIt Push 的时候出现访问不到的错误

> 描述
```bash
Administrator@Jancoyan MINGW64 /r/GITHUB/Learning (master)
$ git push
Connection reset by 20.205.243.166 port 22
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

> 步骤

先查看这个ip能不能ping通，确定不是 git repo 的问题

![[Pasted image 20220516110217.png]]

不能ping通，首先要解决访问的问题

（可以科学上网解决。）

> 解决问题

1. 使用DNS工具查找最近的服务器
![[Pasted image 20220516110554.png]]

2. 