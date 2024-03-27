### 1. 安装与启动

采用Anaconda创建名为label_sudio的虚拟环境

```bash
conda create -n label_studio python=3.9
```

 激活该虚拟环境

```bash
conda activate label_studio
```

 安装Label Studio

```bash
pip install label-studio
```

启动Label Studio

```bash
label-studio start
```


### 2.注册与登录

先注册账号，然后登录之后是这个样子

![[assets/Pasted image 20240326204812.png]]


### 3.创建项目与标注
直接点击创建项目即可

（1）填写项目信息

![[assets/Pasted image 20240326204951.png]]

（2）导入数据

![[assets/Pasted image 20240326205341.png]]

（3）选择类型

![[assets/Pasted image 20240326205419.png]]

（4）配置标签名称

![[assets/Pasted image 20240326205850.png]]

然后点击保存

就可以开始标注了


### 4.导出文件

直接点右上角的导出即可

![[assets/Pasted image 20240326211543.png]]

```bash
.
│ classes.txt
│ notes.json
│
├─images
│   ...
│
└─labels
    ...

```


这样就可以用了