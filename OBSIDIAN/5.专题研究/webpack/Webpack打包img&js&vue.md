## WebPack 打包 Img

### 打包图片

加载图片有两种方式：
1. img元素，设置src属性；
2. 其他元素（比如div），设置background-image的css属性；


以前打包图片需要自己安装file-loader，但是现在用不着了，因为已经webpack已经为我们内置了。但是如果我们直接把图片import进来，会导致webpack把他认为是一个js模块，因此我们应该进行相应的配置来告诉webpack。

```js
      {
        test: /\.(png|jpe?g|gif|svg)$/,
        type: "asset"
      }
```

![[assets/Pasted image 20230228125300.png]]

资源模块类型(**asset** module type)，通过添加 4 种新的模块类型，来替换所有这些 loader：
- asset/resource 发送一个单独的文件并导出 URL。之前通过使用 file-loader 实现；
- asset/inline 导出一个资源的 data URI。之前通过使用 url-loader 实现；
- asset/source 导出资源的源代码。之前通过使用 raw-loader 实现；
- asset 在导出一个 data URI 和发送一个单独的文件之间自动选择。之前通过使用 url-loader，并且配置资源体积限制实现；

测试：

拷贝一张图片到img中

add_div.js中新增

错误示范

```js
// 新增图片
const imgEl = document.createElement('img')
imgEl.src = '/src/img/bird.png' //  不能这样写，这样写是直接定死的字符串，而不是资源的引用
document.body.append(imgEl)
```

正确示范

```js
import bird from "../img/bird.png"

// 新增图片
const imgEl = document.createElement('img')
imgEl.src = bird
document.body.append(imgEl)
```


直接构建项目,成功

![[assets/Pasted image 20230228125848.png]]

### 三种解释资源类型的解释

```ad-note
asset/source 在开发中基本不适用，因此不解释了
```


add_div.js

增加一个小图片

```js
// 新增图片2
import dog from "../img/dog.png"
const imgEl1 = document.createElement('img')
imgEl1.src = dog
document.body.append(imgEl1)
```

==asset/resource==

修改资源类型

![[assets/Pasted image 20230228132548.png]]

重新构建

![[assets/Pasted image 20230228133547.png]]

![[assets/Pasted image 20230228133604.png]]

可以看到资源都指向了新生成的图片

因此这个方法是打包两张图片，每张图片都有自己的地址，并把网页中的地址自己的地址（新图片是用哈希算法生成的）

优点：js文件比较小，容易加载
缺点：需要多次发送请求，向服务器请求图片

==asset/inline==

修改资源类型

![[assets/Pasted image 20230228133756.png]]

重新构建

![[assets/Pasted image 20230228133835.png]]

可以看到图片使用base64编码进行内置到了元素里面。

同时js文件变得更大了（存储了图片的编码）

优点：不需要多次发送请求，向服务器请求图片
缺点：js文件比较大，不容易加载

==asset==

修改成asset之后

![[assets/Pasted image 20230228134130.png]]

可以看见对于大图片，构建生成了新的图片并指向链接，而对于小图片，生成了base64编码提高了加载速度，大小图片的区分是有一个临界值的。

这个临界值，当然是可以自定义的：

webpack.config.js

```js
{
	test: /\.(png|jpe?g|gif|svg)$/,
	type: "asset",
	parser: {
	  dataUrlCondition: {
		maxSize: 50 * 1024 // 设置50KB为临界值
	  }
	}
  }
```

![[assets/Pasted image 20230228134439.png]]


### 自定义输出文件的名称和路径

==针对图片路径：==

```js
  {
	test: /\.(png|jpe?g|gif|svg)$/,
	type: "asset",
	generator: {
	  filename: "img/[name].[hash:6].[ext]"
	},
	parser: {
	  dataUrlCondition: {
		maxSize: 50 * 1024 // 设置50KB为临界值
	  }
	}
  }
```


- `[ext]`： 处理文件的扩展名；
- `[name]`：处理文件的名称；
- `[hash]`：文件的内容，使用MD4的散列函数处理，生成的一个128位的hash值（32个十六进制）；

`"img/[name].[hash:6].[ext]"` 表示生成的文件放在img文件夹下面，文件名是原名.6位哈希加上原来的后缀名。

构建之后： 

![[assets/Pasted image 20230228135227.png]]

==针对所有资源路径：==

修改output，添加assetModuleFilename属性；

```js
  output:{
    filename: 'bundle.js',
    // path必须传入一个绝对路径，我们把目标路径和绝对路径拼接
    path: path.resolve(__dirname, "./build"),
    assetModuleFilename: "img/[name].[hash:6].[ext]"
  },
```


![[assets/Pasted image 20230228135154.png]]

## Babel

```ad-attention
我们在开发的时候基本上不适用 autoprefixer，而是使用post-preset-env
```

Babel是一个工具链，主要用于旧浏览器或者环境中将ECMAScript 2015+代码转换为向后兼容版本的JavaScript；包括：语法转换、源代码转换等

默认打包的时候，如果自己写的是es6，那么打包之后的代码也是es6代码，如果想要将es6的代码转化为es5的代码，应该使用babel

### 命令行直接使用


![[assets/Pasted image 20230228140946.png]]


Babel配置方法和PostCSS极其相似。

首先安装babel-loader

@babel/core是babel的核心代码，必须安装；
@babel/cli是命令行使用babel的工具

```bash
npm install @babel/cli @babel/core -D
npm i babel-loader -D
```

### 方法一二：整合配置、抽取文件配置同postcss

平时基本不用，略

![[assets/Pasted image 20230228141005.png]]

### 方法三：使用预设单独配置【推荐】

```bash
npm install @babel/preset-env -D
```

webpack.config.js 中

```js
      {
        test: /\.js$/,
        use: ['babel-loader']
      }
```

![[assets/Pasted image 20230228141619.png]]

另外在根目录创建文件 babel.config.js

```js
module.exports = {
  presets: [
    "@babel/preset-env"
  ]
}
```

进行构建

![[assets/Pasted image 20230228143959.png]]

变成了ES5的语法（const变成了var）

## Vue

在src中创建文件夹`src/vue_demo`，创建文件`App.vue`

```vue
<template>
  <div>
    <h2 class="title">{{ title }}</h2>
    <p class="content">this is content...</p>
  </div>
</template>

<script>
export default {
  data(){
    return {
      title: "Title"
    }
  }
}
</script>

<style>
.title{
  color: red;
  font-weight: 800;
}
.content{
  color: grey;;
}
</style>
```

安装vue框架，因为开发和生产环境都要用到，因此直接安装

```bash
npm install vue
```

安装webpack进行解析的loader并配置

```bash
npm install vue-loader
```

webpack.config.js

vue项目比较特殊，需要引入一个插件：VueLoaderPlugin


```js
const {VueLoaderPlugin} = require('vue-loader/dist/index')

//....
      {
        test: /\.vue$/,
        use: [ "vue-loader"]
      },
//....

plugins: [
    new VueLoaderPlugin()
  ]
```

![[assets/Pasted image 20230228151636.png]]

main.js 中引入vue

```js
import { createApp } from "vue";
import App from "./vue_demo/App.vue"

createApp(App).mount('#app')
```

index.html中创建挂载点

```html
<body>
  <div id="app"></div>
</body>
```

项目构建

```bash
npm run build
```

![[assets/Pasted image 20230228151715.png]]

成功


