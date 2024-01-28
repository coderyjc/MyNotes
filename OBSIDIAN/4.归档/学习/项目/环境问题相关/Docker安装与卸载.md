> 总结: 从官网看文档安装最好 https://docs.docker.com/engine/install/ubuntu/

### 卸载旧版本

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

### 设置仓库

```bash
$ sudo apt-get update

$ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

$ sudo mkdir -p /etc/apt/keyrings
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg


$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

```


![[../前端项目总结/03.50Projects50Days/assets/Pasted image 20220623131117.png]]

### 安装Docker引擎并测试

```bash
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

$ sudo docker run hello-world
```


## 卸载

```bash
$ sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
    
Images, containers, volumes, or customized configuration files on your host are not automatically removed. To delete all images, containers, and volumes:

```bash
$ sudo rm -rf /var/lib/docker
$ sudo rm -rf /var/lib/containerd
```

You must delete any edited configuration files manually.