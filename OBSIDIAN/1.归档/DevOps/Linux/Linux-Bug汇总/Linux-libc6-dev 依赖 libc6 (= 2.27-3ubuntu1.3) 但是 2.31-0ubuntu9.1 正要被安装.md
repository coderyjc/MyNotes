---
type: 工作记录
skill: Linux
create_date: 2022-01-31
---

#OS/Linux 


### libc6-dev: 依赖: libc6 (= 2.27-3ubuntu1.3) 但是 2.31-0ubuntu9.1 正要被安装

**修改的apt源与ubuntu系统的发行版本不一致导致的！**

```bash
# 修改软件源配置文件
$ sudo vim /etc/apt/sources.list
```

Ubuntu 20.04 

```bash
#阿里源 deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
```


Ubuntu 18.04

```bash

#阿里源 deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
```

更新列表

```bash
$ sudo apt-get update 
$ sudo apt-get upgrade
```