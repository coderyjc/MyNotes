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


```ad-summary
title:webpack到底是如何对我们的项目进行打包的呢？
事实上webpack在处理应用程序时，它会根据命令或者配置文件找到入口文件；从入口开始，会生成一个 依赖关系图，这个依赖关系图会包含应用程序中所需的所有模块（比如.js文件、css文件、图片、字体等）；然后遍历图结构，打包一个个模块（根据文件的不同使用不同的loader来解析）；
```



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
const path = require('path')

module.exports = {
  // 打包的入口
  entry: './src/main.js',
  // 输出设置
  output:{
    filename: 'bundle.js',
    // path必须传入一个绝对路径，我们把目标路径和绝对路径拼接
    path: path.resolve(__dirname, "./build")
  }
}
```

如果我们的webpack配置文件是别的名字，可以从脚本里面设置script，指定参数运行webpack

修改配置文件为 `pack.config.js`

package.json文件

```json
{
  "name": "test",
  "version": "1.0.0",
  "description": "test project",
  "scripts": {
    "build": "webpack --config config.js"
  },
  "devDependencies": {
    "webpack": "^5.75.0",
    "webpack-cli": "^5.0.1"
  }
}
```

然后可以直接运行 `npm run build` 直接使用指定文件打包