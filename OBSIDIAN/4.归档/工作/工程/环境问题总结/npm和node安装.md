
#node  #NPM 

Node.js是一个[[JavaScript]]运行环境(runtime environment)，不是一个js文件，实质是对Chrome V8引擎进行了封装。[[Node.js]] 是一个让 JavaScript 运行在服务端的开发平台，它让 JavaScript 成为与PHP、[[Python]] 等服务端语言平起平坐的脚本语言。  

[1]Node.js提供替代的API，使得V8在非浏览器环境下运行得更好。V8引擎执行Javascript的速度非常快，性能非常好。  

[2]Node.js是一个基于Chrome JavaScript运行时建立的平台， 用于方便地搭建响应速度快、易于扩展的网络应用。  

chrome浏览器和Node.js在解析javascript都使用了v8引擎：

node内置了npm


## 1 安装

```shell
cd /opt;

wget https://nodejs.org/dist/v16.14.0/node-v16.14.0-linux-x64.tar.xz

tar -xvf node-v16.14.0-linux-x64.tar.xz

ln -s /opt/node-v16.14.0-linux-x64/bin/npm /usr/bin/  
ln -s /opt/node-v16.14.0-linux-x64/bin/node /usr/bin/  
ln -s /opt/node-v16.14.0-linux-x64/bin/npx /usr/bin/
```

![[Pasted image 20220505183225.png]]

## 2 查看config配置并设置全局路径

```shell
npm config ls

npm config set prefix '/home/data/nodejs/node_global'  
npm config set cache '/home/data/nodejs/node_cache'
```

## 3 修改镜像

```shell
# 升级

npm install -g npm@8.5.4

# npm 修改为国内镜像地址

npm config set registry https://registry.npm.taobao.org/

```

## 4 配置后可通过下面方式来验证是否成功

```bash
npm config get registry  
或者  
npm info express
```


## 5 环境变量ENV

```bash
/home/data/nodejs/node_global/bin

export NODE_GLOBAL=/home/data/nodejs/node_global
export PATH=${NODE_GLOBAL}/bin:${PATH}  

source /etc/profile
```

