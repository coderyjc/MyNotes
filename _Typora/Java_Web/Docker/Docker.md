# Docker

> 来源：[bilibili-狂神说java - Docker最新超详细版教程通俗易懂](https://www.bilibili.com/video/BV1og4y1q7M4)

## 概述

**Docker为什么出现？**


Docker的思想来自于集装箱；

JRE – 多个应用（端口冲突）-- 原来都是交叉的！

隔离 ： Docker核心思想，打包装箱，每个箱子是互相隔离的。

Docker通过隔离机制，可以将服务器利用到极致！

**Docker的历史**

Docker 是 PaaS 提供商 dotCloud 开源的一个基于 LXC 的高级容器引擎，源代码托管在 Github 上, 基于go语言并遵从Apache2.0协议开源。

**Docker能做什么？**

> 之前的虚拟机技术

<img src=".\Untitled.imgs\image-20210625092430285.png" alt="image-20210625092430285" style="zoom: 50%;" />

虚拟机技术的缺点：

1. 资源占用十分多
2. 冗余步骤多
3. 启动很慢

> 容器化技术

容器化技术不是模拟一个完整的操作系统

<img src=".\Untitled.imgs\image-20210625092546738.png" alt="image-20210625092546738" style="zoom: 67%;" />



比较Docker和虚拟机技术的不同：

- 传统虚拟机，虚拟出一套硬件，运行一个完整的操作系统，然后在这个系统上安装和运行软件

- Docker容器内的应用直接运行在宿主机的内核，容器没有自己的内核，也没有虚拟我们的硬件，所以就轻便了

- 每个容器间是相互隔离，每个容器都有一个属于自己的文件系统，互不影响

> DevOps（开发、运维）

**应用更快速的交付和部署**

传统：一堆帮助文档，安装程序

Docker : 打包镜像发布测试，一键运行

**更快捷的升级和扩容**

使用了Docker之后，我们部署应用就和搭积木一样！

项目打包为一个镜像

**更简单的系统运维**

在容器化之后，我们的开发，测试环境都是高度一致的

**更高效的计算资源利用**

Docker是内核级别的虚拟化，可以在一个物理机上运行很多的容器实例，服务器的性能可以被压榨到极致。

## Docker安装

### Docker基本组成

<img src=".\Untitled.imgs\image-20210625092821052.png" alt="image-20210625092821052" style="zoom:67%;" />

**镜像（image）**

docker镜像就好比是一个模板，可以通过这个模板来创建容器服务。

tomcat镜像 ==> run ==> tomcat容器（提供服务）

通过这个镜像可以创建多个容器（最终运行或者项目运行都是在容器中的）。

**容器（container）**

Docker利用容器技术，独立运行一个或者一组应用，是通过镜像来创建的。

有启动，停止，删除等Linux基本指令！

目前就可以把这个容器理解为一个简易的Linux系统

**仓库（repository）**

仓库就是存放镜像的地方，分为私有仓库和公有仓库；

Docker Hub（默认是国外的）

阿里云都有容器服务器（配置镜像加速！）


### 安装

查看服务器环境，系统环境是 3.10 以上的。

![image-20210625190020465](.\Docker.imgs\image-20210625190020465.png)

查看系统信息

![image-20210625190119128](.\Docker.imgs\image-20210625190119128.png)

**开始安装**

帮助文档：https://docs.docker.com/engine/install/centos/

1. 卸载旧版本

   ```bash
   yum remove docker \
                     docker-client \
                     docker-client-latest \
                     docker-common \
                     docker-latest \
                     docker-latest-logrotate \
                     docker-logrotate \
                     docker-engine
   ```

2. 安装相关的安装包

   ```bash
   yum install -y yum-utils
   ```

3. 设置镜像仓库, 最好用阿里云的

   ```bash
   yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
   ```
   
4. 更新yum的索引

   ```bash
   yum makecache fast
   ```


5. 安装最新版的docker引擎

   ```bash
   yum install docker-ce docker-ce-cli containerd.io
   ```

6. 启动docker

   ```bash
   systemctl start docker
   ```

7. 查看版本信息

   ```bash
   docker version
   ```

   ![image-20210625191005181](.\Docker.imgs\image-20210625191005181.png)

8. 测试hallo world

   ![image-20210625191347316](.\Docker.imgs\image-20210625191347316.png)

9. 查看本地镜像 `docker images` 我们最终的服务都要打包成镜像运行

   ![image-20210625191452451](.\Docker.imgs\image-20210625191452451.png)



了解 ： 卸载docker

```bash
# 1、依赖卸载
yum remove docker-ce docker-ce-cli containerd.io

# 2、删除资源
rm -rf /var/lib/docker

# /var/lib/docker docker的默认工作路径
```

### 阿里云镜像加速服务

![image-20210625192048000](.\Docker.imgs\image-20210625192048000.png)

![image-20210625192115542](.\Docker.imgs\image-20210625192115542.png)

### 回顾HelloWorld流程

![image-20210625192722979](.\Docker.imgs\image-20210625192722979.png)

### 底层原理

**Docker是怎么工作的？**

Docker是一个Client-Server结构的系统，Docker的守护进程运行在主机上，通过Socket从客户端访问！

DockerServer接收到Docker-Client的指令，就会执行这个命令！

![image-20210625193108916](R:\GITHUB\MyNotes\_Typora\Java_Web\Docker\Docker.imgs\image-20210625193108916.png)

**Docker为什么比VM快？**

1. Docker有着比虚拟机更少的抽象层
2. Docker利用的是宿主机的内核，VM需要的是Guest OS

<img src="R:\GITHUB\MyNotes\_Typora\Java_Web\Docker\Docker.imgs\image-20210625193259429.png" alt="image-20210625193259429" style="zoom:67%;" />

所以说，新建一个容器的时候，docker不需要像虚拟机一样重新加载一个操作系统内核，避免引导。虚拟机是加载Guset OS , 分钟级别的，而docker是利用宿主机的操作系统，省略了这个复杂的过程，秒级。

<img src="R:\GITHUB\MyNotes\_Typora\Java_Web\Docker\Docker.imgs\image-20210625193639364.png" alt="image-20210625193639364" style="zoom:67%;" />

## Docker常用命令

### 帮助命令

```bash
docker version      # 显示docker的版本信息
docker info         # 显示docker的系统信息，包括镜像和容器的数量
docker 命令 --help   # 帮助命令
```

帮助文档的地址：https://docs.docker.com/reference/

### 镜像命令

> docker images 查看所有本地主机上的镜像

```bash
[root@iz2ze1rhvd25ba6iiq2dvwz ~]# docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    d1165f221234   3 months ago   13.3kB


# 解释
REPOSITORY  镜像的仓库源
TAG         镜像的标签
IMAGE ID    镜像的id
CREATED     镜像的创建时间

# 可选项
	-a, --all      # 列出所有的镜像
	-q, --quiet    # 只显示镜像的id
```

> docker serch 在dockhub中搜索镜像

```bash
[root@iz2ze1rhvd25ba6iiq2dvwz ~]# docker search mysql
NAME                              DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
mysql                             MySQL is a widely used, open-source relation…   11038     [OK]       

# 可选项
--filter , -f		Filter output based on conditions provided

docker search mysql -f=stars=5000
```



> docker pull 下载镜像

```bash

```





> docker rmi 删除镜像

```bash

```





### 容器命令





