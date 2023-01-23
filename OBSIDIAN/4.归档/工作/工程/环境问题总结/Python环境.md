
### pip 使用清华源安装

临时

```bash
pip install ** -i <https://pypi.yuna.tsinghua.edu.en/simple>
```

永久

```bash
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 软件包下载问题

如果直接pip下载慢的话，直接登录所在的软件包管理网站，在目录中查找想要的whl文件，然后使用迅雷新建下载任务，然后下载。