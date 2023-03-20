# 安装Ubuntu 20.04到D盘

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

显示我电脑没有开启wsl2

![[assets/Pasted image 20230320154640.png]]

设置中搜索控制面板

![[assets/Pasted image 20230320154653.png]]

打开程序

![[assets/Pasted image 20230320154724.png]]