# 使用CuteHttpFileServer/chfs搭建局域网文件传输服务

> 官网: http://iscute.cn/chfs
> 下载: 
> 命令行程序: 
> - win-64 http://iscute.cn/tar/chfs/2.0/chfs-windows-x64-2.0.zip
> - linux-arm-64: http://iscute.cn/tar/chfs/2.0/chfs-linux-arm64-2.0.zip
> - linux-amd-64: http://iscute.cn/tar/chfs/2.0/chfs-linux-amd64-2.0.zip
> GUI程序: http://iscute.cn/tar/chfs/2.0/gui-chfs-windows.zip


## 命令行版本

以下是官网的参数说明

![](image-20220712084957.png)

部分示例

> 默认共享程序运行目录, 监听80口

```bash
//都使用默认参数，共享目录为程序运行目录，监听端口号为80
chfs
```

> 设置共享目录和端口号

```bash
//共享一整个R盘，监听端口号为8890
chfs --path="d:/" --port=8890

//共享目录为"C:\\Users\\Administrator\\Pictures\\Wallpaper"和"r:\\repo"，监听端口号为80
chfs --path="C:\\Users\\Administrator\\Pictures\\Wallpaper|r:\\repo"
```

当有人下载的时候就会打印出log并及时保存到文件

![](image-20220712090419.png)

> 设置白名单和黑名单

```bash
//白名单模式，允许192.168.1.2-192.168.1.100以及192.168.1.200进行访问
chfs --allow="192.168.1.2-192.168.1.100,192.168.1.200"

//黑名单模式，禁止192.168.1.2-192.168.1.100以及192.168.1.200进行访问
chfs --allow="not(192.168.1.2-192.168.1.100,192.168.1.200)"
```

> 账户设置(来自官方文档)

```bash
//匿名用户具有只读权限（默认情况下匿名用户具有读写权限）
//账户ceshizu，密码为ceshizu123，对根目录的权限为只读，但对test目录具有读写权限
//账户yanfazu，密码为yanfazu123，对根目录的权限为只读，但对yanfa目录具有读写权限
chfs --rule="::r|ceshizu:ceshizu123:r:test:rw|yanfazu:yanfazu123:r:yanfa:rw"

//匿名用户什么权限都没有（默认情况下匿名用户具有读写权限）
//账户admin，密码为admin123，具有读写权限
//账户zhangsan，密码为zhangsan123，对根目录的权限为不可读写，但对zhangsanfiles目录具有读写权限
chfs --rule="::|admin:admin123:rw|zhangsan:zhangsan123::zhangsanfiles:rw"

//通过配置文件进行配置，该文件可以不存在，待以后需要更改配置时使用
chfs --file="d:\chfs\chfs.ini"
```

## GUI版本

GUI比较适合一些非专业人员或者想偷懒的人(划掉)使用, 界面简洁直观, 通过简单的操作就能进行局域网的文件传输

![](image-20220712094633.png)

GUI版本所见即所得, 进行相关配置之后直接点击左上角运行即可.

## windows系统使用右键弹出菜单快速共享目录

> 官网给的模板
> [ 官方给的模板好像有点问题, 只有第一项能够添加,第二项添加不上去... ]

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\chfs]
@="使用CHFS共享当前目录"

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\chfs\command]
@="\"C:\\windows\\chfs.exe\" --path=\"%v.\""
```

> 我的示例
> 路径换成chfs软件的绝对路径, `C:\Program Files\Utils\chfs.exe`

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\chfs]
@="Share Directory With CHFS"

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\chfs\command]
@="C:\\Program Files\\Utils\\chfs.exe --path=%v. "
```

其中第一个注册表项是点击鼠标右键的时候显示的表项, 如下图所示

![](image-20220712091239.png)

==第二个注册表项是点击之后要执行的命令, 官网中给出的命令字符串转义了双引号, 但是这样可能会出现解析为空字符串的问题, 把转义字符串去掉(就像我给出的示例一样)就可以了==

顺带一提, 这个是可以带有图标的

icon换成你自己的这个软件的位置

```
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\chfs]
icon="C:\\Program Files\\Utils\\chfs.exe"
```

## 个性化配置

个性化配置需要编辑配置文件 `config.ini` 文件名随意

> 网页标题配置为 局域网文件传输

```
html.title=局域网文件传输
```

> 网页的公告栏 "公告板 HELLOWORLD"
> 其中HELLO WORLD是HTML标签

```
html.notice=公告板<span style="color:red">HELLO WORLD</span>
```

> 其他

```
ssl.cert和ssl.key: 用来配置SSL，启用HTTPS

folder.leaf.download: 仅最后一个目录可以打包下载

session.timeout: 会话的时长，单位是分钟
```

> 指定启动参数启动

```
chfs.exe --file="config.ini"
```

![](image-20220712094408.png)

## 后记

作者给我们提供了很多改进的空间, 官网上给出了api的获取方法, 我们可以根据这个程序自己开发一个local webapp.

