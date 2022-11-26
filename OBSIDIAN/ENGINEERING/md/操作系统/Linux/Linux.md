---
type: 工作记录
skill: Linux
create_date: 2022-01-31
---

#Linux #操作系统 

# Linux

## 乱码问题

>cat 查看二进制文件导致的乱码问题

原因是 二进制数据干扰了终端对字符串的解析

使用 reset 命令即可

> 因为字体库字体缺失导致的乱码问题

描述：

出现这种情况，把这些文字复制到文件中，显示的是正常的文字
![[Pasted image 20220208194603.png]]

因此可以确定服务器没有问题，应该是字体的问题。

改变[[shell]]的字体，成功解决这个问题。

![[Pasted image 20220208195130.png]]


## 软件源问题

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

