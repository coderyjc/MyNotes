```ad-note
webpack的官方文档 https://webpack.js.org/
webpack的中文官方文档 https://webpack.docschina.org/
```
## Node的path模块

path模块用于对路径和文件进行处理，提供了很多好用的方法。

我们知道在Mac OS、Linux和window上的路径是不一样的：window上会使用 \或者 \\ 来作为文件路径的分隔符，当然目前也支持 /；在Mac OS、Linux的Unix操作系统上使用 / 来作为文件路径的分隔符；

那么如果我们在window上使用 \ 来作为分隔符开发了一个应用程序，要部署到Linux上面应该怎么办呢，显示路径会出现一些问题，所以为了屏蔽他们之间的差异，在开发中对于路径的操作我们可以使用 path 模块；

==获取路径中的信息==

dirname：获取文件的父文件夹；
basename：获取文件名；
extname：获取文件扩展名

```js
const path = require('path')

const filepath = 'C://dir1/dir2/dir3'

// 从路径中获取信息
console.log(path.extname(filepath))

// 获取文件名
console.log(path.basename(filepath))

// 获取文件夹所在路径
console.log(path.dirname(filepath))
```


==路径的拼接==

如果我们希望将多个路径进行拼接，但是不同的操作系统可能使用的是不同的分隔符；
这个时候我们可以使用path.join函数；

```js
// 将多个路径拼接在一起
const path1 = '/aaa/bbb'
const path2 = '../nodejs'
console.log(path.join(path1, path2))
```

==绝对路径的拼接==

path.resolve() 方法会把一个路径或路径片段的序列解析为一个绝对路径；

给定的路径的序列是从右往左被处理的，后面每个 path 被依次解析，直到构造完成一个绝对路径；如果在处理完所有给定path的段之后，还没有生成绝对路径，则使用当前工作目录；生成的路径被规范化并删除尾部斜杠，零长度path段被忽略；如果没有path传递段，path.resolve()将返回当前工作目录的绝对路径；

```js
const path = require('path')

// 多个路径拼接在一起，最后返回一个绝对路径

// 从后向前查找，直到查找到绝对路径

console.log(path.resolve("./abc/test", "/root/", "/a.txt"))
console.log(path.resolve("./abc/test", "/root/", "a.txt"))
console.log(path.resolve("/abc/test", "root/", "a.txt"))
console.log(path.resolve("./abc/test", "root/", "a.txt"))

```

![[assets/Pasted image 20230228090007.png]]


## 认识Webpack

### 介绍

![[assets/Pasted image 20230228090418.png]]

假设我们现在在做vue项目，那么我们需要加载哪些文件？

JavaScript的打包：
- 将ES6转换成ES5的语法；
- TypeScript的处理，将其转换成JavaScript；

Css的处理：
- CSS文件模块的加载、提取；
- Less、Sass等预处理器的处理；

资源文件img、font：
- 图片img文件的加载；
- 字体font文件的加载；

HTML资源的处理：打包HTML资源文件；
处理vue项目的SFC文件.vue文件；

### 安装

webpack的安装目前分为两个：webpack、webpack-cli

它们的关系：

执行webpack命令，会执行node_modules下的.bin目录下的webpack；webpack在执行时是依赖webpack-cli的，如果没有安装就会报错；而webpack-cli中代码执行时，才是真正利用webpack进行编译和打包的过程；

所以在安装webpack时，我们需要同时安装webpack-cli（第三方的脚手架事实上是没有使用webpack-cli的，而是类似于自己的vue-service-cli的东西）

![[assets/Pasted image 20230228090818.png]]

```bash
npm install webpack webpack-cli –g # 全局安装
npm install webpack webpack-cli –D # 局部安装
```

```ad-info
在实际开发中我们通常使用**局部安装**的webpack
```

安装之后可以直接使用`npx webpack`进行打包，但是这种打包方式有弊端——根目录下必须有一个`src`文件夹.

### 指定配置文件

配置文件可以指定webpack打包的根目录，也可以指定生成的目录等

配置文件的名字是`webpack.config.js`放在项目根目录中，和`node_modules`同级

在这个文件中导出node模块

```js

```