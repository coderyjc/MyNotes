---
alias: Miniconda安装与配置
tags: 
- Python/Annaconda
---


## 安装Annaconda本体

1. 直接点击next

![[assets/Pasted image 20230106104437.png]]

2. 接受协议

![[assets/Pasted image 20230106104455.png]]

3. 一般我们的电脑只有我们一个用户使用，这里选择为所有用户安装即可

![[assets/Pasted image 20230106104518.png]]

4. 选择安装文件夹

![[assets/Pasted image 20230106104611.png]]

5. 如果能添加到PATH环境变量，最好还是添加上，这里他不让添加了，可能是因为我选择安装的目录不是C盘，一会手动添加即可。

![[assets/Pasted image 20230106104634.png]]

6. 等待安装

![[assets/Pasted image 20230106104741.png]]

7. 成功后点击next

![[assets/Pasted image 20230106105838.png]]

8. 继续点击next

![[assets/Pasted image 20230106105900.png]]

9. 第一个是查看发布指南，第二个是快速开始，这里都不用点，直接Finish

![[assets/Pasted image 20230106105923.png]]

10. 成功

## 配置Annaconda环境变量

右键`此电脑` -> `属性` -> `高级系统设置` -> `环境变量` -> `path`

将以下路径添加进PATH

```
{Annaconda根目录}
{Annaconda根目录}\Scripts  
{Annaconda根目录}\Library\bin  
{Annaconda根目录}\Library\mingw-w64\bin
```

比如我的环境变量为

```
E:\IDE\Annaconda
E:\IDE\Annaconda\Scripts
E:\IDE\Annaconda\Library\bin
E:\IDE\Annaconda\Library\mingw-w64\bin
```

![[assets/Pasted image 20230106110433.png]]

然后点击三次`确定`

**测试环境变量**

cmd环境下输入 `conda info`出现如下信息

![[assets/Pasted image 20230106110549.png]]

输入`python`出现python命令行

![[assets/Pasted image 20230106110622.png]]

不显示找不到命令等字眼即可。

## 配置conda镜像源

### 方法一 命令行添加

cmd输入以下内容

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
```

![[assets/Pasted image 20230106110935.png]]


### 方法二 配置文件添加

创建或者修改文件 `C:\Users\Administrator\.condarc`

文件实时更新，建议查看官网镜像源： https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

将内容替换为以下内容

```text
channels:
  - defaults
show_channel_urls: true
channel_alias: https://mirrors.tuna.tsinghua.edu.cn/anaconda
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

保存退出

然后CMD输入 `conda clean -i` 

![[assets/Pasted image 20230106111248.png]]

完成。

以后安装python包就用conda即可，可以不用pip了