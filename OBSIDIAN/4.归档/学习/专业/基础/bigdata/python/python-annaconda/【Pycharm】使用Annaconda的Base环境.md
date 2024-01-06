
## 基于Virtualenv Envrionment

1. 添加解释器

![[assets/Pasted image 20230106112955.png]]

2. 添加本地解释器

![[assets/Pasted image 20230106113135.png]]

3. 如果是现有的环境，就直接选择Annaconda安装目录下面的python.exe

![[assets/Pasted image 20230106113215.png]]

直接点击OK即可

![[assets/Pasted image 20230106113317.png]]

点击确定。

可以在设置中看到这里已经集成了Annaconda的所有的包

![[assets/Pasted image 20230106113456.png]]


## 基于Conda Environment


1. 添加解释器

![[assets/Pasted image 20230106112955.png]]

2. 添加本地解释器

![[assets/Pasted image 20230106113135.png]]


3. 这里一定要注意，选择的**不是**`_conda.exe` 而是 `conda.exe`，这个exe在`{Annaconda根目录}/Scripts/conda.exe`，实际命令行执行 conda 命令时，执行的是 conda.bat 的脚本。


![[assets/Pasted image 20230106114112.png]]

4. 然后Load Environment

![[assets/Pasted image 20230106114247.png]]

5. 然后OK

![[assets/Pasted image 20230106114307.png]]

创建即可


在项目的设置中可以看到这个项目也集成了Annaconda的库

![[assets/Pasted image 20230106114432.png]]


---

本文是从新建项目开始的，也可以在设置中添加Python解释器

![[assets/Pasted image 20230106114503.png]]