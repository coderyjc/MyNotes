
#Python/Jupyter

## 运行

这是一个基于web的交互式Python编辑器

安装完Annaconda之后就可以直接运行Jupyter Notebook了

在cmd命令行界面直接输入命令`jupyter notebook`可以直接打开notebook

![[assets/Pasted image 20230106125604.png]]

直接打开的默认路径是操作系统的用户目录

这个目录可以改

![[assets/Pasted image 20230106125613.png]]

## 配置文件配置

cmd输入 `jupyter notebook --generate-config`

生成配置文件，执行命令之后会显示配置文件的路径`Writing default config to: C:\Users\Administrator\.jupyter\jupyter_notebook_config.py`

打开这个文件可以进行一些基本属性的配置

### 默认打开的目录

【393行】配置项 `c.NotebookApp.notebook_dir` 

设置为自己的目录，这里我设置为了

```
c.NotebookApp.notebook_dir = 'R:\code\github\workspace\jupyter'
```

### 应用密码

【412，421行】`c.NotebookApp.password`  `c.NotebookApp.password_required`

