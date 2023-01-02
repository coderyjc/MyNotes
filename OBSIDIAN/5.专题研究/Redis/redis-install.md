## 单机安装Redis


> Redis下载地址 https://redis.io/download/

安装之前首先要保证环境中有安装Redis所需要的gcc依赖

1. 上传安装包并解压

这里使用宝塔Linux面板进行上传

![[assets/Pasted image 20230102101106.png]]

```bash
redis sudo tar -xzvf redis-6.2.6.tar.gz
```

![[assets/Pasted image 20230102101010.png]]

2. 进入目录并编译

```bash
cd redis-6.2.6

sudo make && make install
```
默认的安装路径是在 `/usr/local/bin`目录下：

![[assets/Pasted image 20230102101653.png]]

该目录以及默认配置到环境变量，因此可以在任意目录下运行这些命令。其中：
-   redis-cli：是redis提供的命令行客户端    
-   redis-server：是redis的服务端启动脚本
-   redis-sentinel：是redis的哨兵启动脚本


## 启动

redis的启动方式有很多种，例如：

-   默认启动
-   指定配置启动
-   开机自启

### 默认启动

任意位置输入命令

```bash
redis-server
```

![[assets/Pasted image 20230102101813.png]]

这种启动属于`前台启动`，会阻塞整个会话窗口，窗口关闭或者按下`CTRL + C`则Redis停止。不推荐使用。

### 指定配置启动

如果要让Redis以`后台`方式启动，则必须修改Redis配置文件，就在我们之前解压的redis安装包下（`/usr/local/src/redis-6.2.6`），名字叫redis.conf：

![[assets/Pasted image 20230102101901.png]]

我们先将这个配置文件备份一份：

```bash
sudo cp redis.conf redis.conf.bak
```

![[assets/Pasted image 20230102101946.png]]

然后修改redis.conf文件中的一些配置：

```
# 允许访问的地址，默认是127.0.0.1，会导致只能在本地访问。修改为0.0.0.0则可以在任意IP访问，生产环境不要设置为0.0.0.0

# 在文件的第75行
bind 0.0.0.0

# 守护进程，修改为yes后即可后台运行
# 在文件的第257行
daemonize yes 

# 密码，设置后访问Redis必须输入密码
# 在文件的第901行
requirepass 333
```

Redis的其它常见配置：

```
# 监听的端口
port 6379

# 工作目录，默认是当前目录，也就是运行redis-server时的命令，日志、持久化等文件会保存在这个目录
dir .

# 数据库数量，设置为1，代表只使用1个库，默认有16个库，编号0~15
databases 1

# 设置redis能够使用的最大内存
maxmemory 512mb

# 日志文件，默认为空，不记录日志，可以指定日志文件名
logfile "redis.log"
```

启动Redis：

```
# 进入redis安装目录 
cd /usr/local/src/redis-6.2.6

# 启动
redis-server redis.conf
```

![[assets/Pasted image 20230102102937.png]]

停止服务

找到进程直接kill即可。

### 设置开机自启

1. 新建一个系统服务文件

```bash
sudo vim /etc/systemd/system/redis.service
```

内容如下：

```
[Unit]
Description=redis-server
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/bin/redis-server /usr/local/src/redis-6.2.6/redis.conf
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

![[assets/Pasted image 20230102115530.png]]


2.  重载系统服务

```bash
sudo systemctl daemon-reload
```

3. 使用以下命令操作redis

```bash
# 启动
systemctl start redis
# 停止
systemctl stop redis
# 重启
systemctl restart redis
# 查看状态
systemctl status redis
```

执行下面的命令，可以让redis开机自启：

```bash
systemctl enable redis
```

## Redis客户端

安装完成Redis，我们就可以操作Redis，实现数据的CRUD了。这需要用到Redis客户端，包括：

-   命令行客户端    
-   图形化桌面客户端
-   编程客户端

### 命令行客户端

Redis安装完成后就自带了命令行客户端：redis-cli，使用方式如下

```bash
redis-cli [options] [commonds]
```

其中常见的options有：

-   `-h 127.0.0.1`：指定要连接的redis节点的IP地址，默认是127.0.0.1
-   `-p 6379`：指定要连接的redis节点的端口，默认是6379
-   `-a 333：指定redis的访问密码

其中的commonds就是Redis的操作命令，例如：

-   `ping`：与redis服务端做心跳测试，服务端正常会返回`pong`

不指定commond时，会进入`redis-cli`的交互控制台：

![[assets/Pasted image 20230102115916.png]]

###  图形化桌面客户端RDM




## Docker安装Redis



