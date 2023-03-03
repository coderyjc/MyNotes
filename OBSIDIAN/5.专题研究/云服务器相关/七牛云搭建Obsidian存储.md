
## 账号注册与薅羊毛

账号注册步骤省略，先注册账号，再进行用户实名认证，认证完成之后才能每个月领取10G的存储额度。

注册七牛云账号，新用户可以每个月免费领10G的云存储，在这个页面 https://marketing.qiniu.com/activity/act-free

![[assets/Pasted image 20230303192332.png]]

从这里领取。

## 新建bucket（存储空间）

从这进去

![[assets/Pasted image 20230303192522.png]]

点击空间管理，进入管理空间

点击新建空间

![[assets/Pasted image 20230303192626.png]]

填写存储空间名称（bucket name），选择一个比较近的存储区域，访问控制为公开。

```ad-warning
title:注意
记住存储空间名称和存储区域，一会要用。
```

![[assets/Pasted image 20230303193057.png]]

创建成功后会有提示：

文件上传需要绑定自定义域名，最好绑定一个自己的域名，但是一开始官方免费提供试用一个月的，这就意味着如果直接用官方给定的， 一个月到了之后就不能用了，所以还要绑定自己的域名。

![[assets/Pasted image 20230303193116.png]]

可以先点击“好的，我知道了”进行后续的配置


## 配置Obsidian

### 安装插件

下载插件 remotely-save ，地址：https://gitee.com/whghcyx/obsidian-plugin/raw/master/plugin/remotely-save.zip

添加到obsidian，启用插件

![[assets/Pasted image 20230303193920.png]]

进入插件配置页面

### 服务类型

远程服务选择S3或者兼容S3的服务

![[assets/Pasted image 20230303194010.png]]

剩下的主要配置下列五项

![[assets/Pasted image 20230303194101.png]]

### 配置服务地址 Endpoint

进入七牛云空间管理

![[assets/Pasted image 20230303193404.png]]

点击查看S3域名

![[assets/Pasted image 20230303194348.png]]

这个结点名称，填写到①处，服务地址

![[assets/Pasted image 20230303194500.png]]

### 配置区域 Region

七牛云存储区域上传地址 https://developer.qiniu.com/kodo/1671/region-endpoint-fq

这个地址是你创建存储空间（Bucket）的时候选择的地址，也就是在[[七牛云搭建Obsidian存储#新建bucket（存储空间）]] 中选择的地址，我的存储空间在河北。

![[assets/Pasted image 20230303192221.png]]

查上表可得，河北区的地址为`z1`

因此我的第②项填`z1`

### 填写Access Key和 Secert Access Key

在自己的七牛云空间的个人空间，选择密钥管理

![[assets/Pasted image 20230303194713.png]]

上图中的AK和SK就是要填写的③和④

![[assets/Pasted image 20230303194749.png]]

### 填写存储桶名字

存储桶名字，就是存储空间名字，就是[[七牛云搭建Obsidian存储#新建bucket（存储空间）]] 中填写的名字。


### 测试链接情况

配置完之后是这样的：

![[assets/Pasted image 20230303195110.png]]

点击检查，成功即可。

![[assets/Pasted image 20230303195131.png]]


## 开始同步

点击这个按钮，开始同步

![[assets/Pasted image 20230303195240.png]]

显示已完成同步

![[assets/Pasted image 20230303195306.png]]

去七牛云的服务器上查看：

