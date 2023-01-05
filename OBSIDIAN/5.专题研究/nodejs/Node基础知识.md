## 介绍

官方定义：Node.js是一个基于V8JavaScript引擎的Js运行时环境（V8引擎用来执行JavaScript代码）

V8可以嵌入到任何的C++程序中，无论是Chrome还是Node.js，事实上都是嵌入了V8引擎来执行JavaScript代码。但是在Chrome中，还需要解析渲染HTML、CSS等相关的引擎，另外还需要提供支持浏览器操作的API等
另外在Node.js中我们也需要进行一些额外操作，比如文件系统读写，网络IO，加密，压缩解压文件等操作。

Node是用什么语言编写的？C、C++、和少部分JS

### 浏览器和Node架构的区别

![[assets/Pasted image 20230104185835.png]]

![[assets/Pasted image 20230104190411.png]]


### 应用场景

1. 目前前端开发的库都是以node包的形式进行管理;
2. npm, yarn, pnpm工具成为前端开发使用最多的工具;
3. 越来越多的公司使用Node.js作为web服务器开发、中间件、代理服务器;
4. 大量项目需要借助Node.js完成前后端渲染的同构应用;
5. 资深前端工程师需要为项目编写脚本工具(前端工程师编写脚本通常会使用JavaScript,而不是Python或者shell) ;
6. 很多企业在使用Electon来开发桌面应用程序;

## 安装

### 安装Node.js

[node官网](https://nodejs.org/en/)

LTS版本（Long Term Support）：长期支持，相对稳定，线上使用。真正开发一定要使用LTS版本

Current版本：最新的版本，包含很多新特性

`.msi` microsoft install 微软安装程序

![[assets/Pasted image 20230104193111.png]]

![[assets/Pasted image 20230104193125.png]]

![[assets/Pasted image 20230104193148.png]]

![[assets/Pasted image 20230104193206.png]]

![[assets/Pasted image 20230104193347.png]]

![[assets/Pasted image 20230104193358.png]]

![[assets/Pasted image 20230104193410.png]]

![[assets/Pasted image 20230104193417.png]]

安装成功

![[assets/Pasted image 20230104193535.png]]

### Node多版本工具nvm的安装

本身不支持windows系统。

有大佬在windows系统中复刻了一个nvm，我们在windows上使用的是nvm。

官网：[https://github.com/coreybutler/nvm-windows](https://github.com/coreybutler/nvm-windows)

- 通过 `nvm install latest` 安装最新的node版本
- 通过 `nvm list` 展示目前安装的所有版本
- 通过 `nvm use` 切换版本

![[assets/Pasted image 20230104194510.png]]

![[assets/Pasted image 20230104194529.png]]

![[assets/Pasted image 20230104194615.png]]

点击是即可。


### 版本管理工具 n【Mac】

```bash
npm install -g n

n --version
```

## 输入输出内容

```java
// 给程序输入内容
console.log(process.argv)
```

```bash
R:\code\github\workspace\nodejs>node 输入输出.js num=20
[
  'E:\\Envrionment\\node\\node.exe',
  'R:\\code\\github\\workspace\\nodejs\\输入输出.js',
  'num=20'
]
```

为什么叫做argv？

- argc：argument counter 传递参数的个数
- argv：argument vector 参数响亮

## 常见全局对象

### 特殊全局对象
```js
// 特殊的全局对象

// 表示当前的文件所在的目录
console.log(__dirname)

// 表示当前文件的全路径
console.log(__filename)
```

```bash
R:\code\github\workspace\nodejs>node 输入输出.js
R:\code\github\workspace\nodejs
R:\code\github\workspace\nodejs\输入输出.js
```

### process


很大的一个对象，里面包含了很多东西


### console


### 定时器函数

```js
// 定时器方法

setInterval(() => {

}, 2000)

setTimeout(() => {

}, 2000)

setImmediate(() => {

}, 2000)

process.nextTick(() => {

})
```


### globalThis

在新标准中使用globalThis替代global

