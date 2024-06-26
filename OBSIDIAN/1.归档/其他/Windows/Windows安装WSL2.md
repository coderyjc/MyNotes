---
tags: Windows/WSL2
---

```ad-cite
Ref: https://zhuanlan.zhihu.com/p/466001838
```

# 安装Ubuntu 20.04到D盘

## 安装

新建想要安装的目标文件夹，进入PowerShell输入命令：

```bash
Invoke-WebRequest -Uri https://wsldownload.azureedge.net/Ubuntu_2004.2020.424.0_x64.appx -OutFile Ubuntu20.04.appx -UseBasicParsing
```

![[assets/Pasted image 20230320153647.png]]

等待写入结束

![[assets/Pasted image 20230320154304.png]]

共计442M

然后执行下面四条命令

```bash
Rename-Item .\Ubuntu20.04.appx Ubuntu.zip

Expand-Archive .\Ubuntu.zip -Verbose

cd .\Ubuntu\

.\ubuntu2004.exe
```

![[assets/Pasted image 20230320154348.png]]

---

<span style="background:#d2cbff">问题与解决</span>

显示我电脑没有开启wsl2

![[assets/Pasted image 20230320154640.png]]

设置中搜索控制面板

![[assets/Pasted image 20230320154653.png]]

打开程序和特性

![[assets/Pasted image 20230320154724.png]]

打开或关闭windows特性

![[assets/Pasted image 20230320154752.png]]

打开WSL

![[assets/Pasted image 20230320154812.png]]

打开之后重启一下电脑。

---

输入初始的用户名和密码即可。

![[assets/Pasted image 20230320155250.png]]


## 换源

```bash
wget https://gitee.com/lin-xi-269/tools/raw/master/os/QHubuntu20.04 && bash QHubuntu20.04
```

## 内存限制

进入`/mnt/c/Users/Administrator$`中，写入文件`.wslconfig` 内容为：

```powershell
[wsl2]
 processors=8
 memory=2GB
 localhostForwarding=true
```