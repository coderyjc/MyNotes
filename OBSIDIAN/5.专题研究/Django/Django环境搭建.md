
```ad-note
默认认为已经安装了Python环境和pip环境
如果没有安装，参考这里
- [[../../4.归档/工作/基础/bigdata/python/python-annaconda/【安装】Annaconda安装以及镜像源配置|Annaconda环境配置]]
- [[../../4.归档/工作/工程/环境问题相关/Python第三方库安装相关|pip环境配置]]
```


先检查一下Python环境是否正确安装。

cmd输入`python --version`

```bash
C:\Users\Administrator>python --version
Python 3.9.13
```

就可以开始了。

## 安装virtualenv虚拟环境

安装虚拟环境

```bash
pip3 install virtualenv
```

![[assets/Pasted image 20230226084152.png]]

创建文件夹`backend`

输入以下命令安装虚拟环境

```bash
virtualenv venv -p python3
```

![[assets/Pasted image 20230226084238.png]]

激活虚拟环境

激活之后命令行前面出现（venv）即为成功

```bash
venv\Scripts\activate.bat

(venv) D:\code\github\certificate_analysis\certificate_analysis\backend>
```

![[assets/Pasted image 20230226084533.png]]

在上一步中，我们创建了一个名为**venv**的特殊文件夹。该文件夹内包含了一个python的副本。在我们激活了**venv**环境之后，当我们运行`Python`命令时，它将使用我们存储在venv里面的本地副本，而不是我们之前在操作系统中安装的那个。

另一个重要的事情是，**pip**程序也已经安装好了，当我们使用它来安装Python的软件包（比如Django）时，它将被安装在**venv**环境中。

顺便说一句，要想退出**venv**环境，运行下面的命令：

```bash
deactivate
```

现在先保持激活状态来进行下一步。

## 安装Django

```bash
pip install django
```

![[assets/Pasted image 20230226084722.png]]

