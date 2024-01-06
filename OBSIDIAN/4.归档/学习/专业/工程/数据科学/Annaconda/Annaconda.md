---
type: 知识点总结
skill: Annaconda
create_date: 2022-02-08
---

#python #数据科学 #数据分析 #annaconda

# Annaconda

### Conda 命令的使用

添加路径到path，添加后可以使用conda命令了

`C:\\AppData\\Software\\Anaconda3`

`C:\\AppData\\Software\\Anaconda3\\Scripts`

`C:\\AppData\\Software\\Anaconda3\\Library\\bin`

### 配置国内的镜像源

修改 .condarc 文件

```yaml
channels:
  - defaults
show_channel_urls: true
default_channels:
  - <https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main>
  - <https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free>
  - <https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r>
custom_channels:
  conda-forge: <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud>
  msys2: <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud>
  bioconda: <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud>
  menpo: <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud>
  pytorch: <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud>
  simpleitk: <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud>
```

### wandb 未注册异常

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


### 报错回环导入

`ImportError: cannot import name 'svm' from partially initialized module 'sklearn' (most likely due to a circular import) (R:\Code\Pycharm\AI\6.SVM-Regression\[sklearn.py](http://sklearn.py/))`


原因：文件夹或者python文件名字和库的名字一样了。

解决方案：改个文件名