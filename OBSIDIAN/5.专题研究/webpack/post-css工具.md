## post-css工具

```ad-attention
我们在开发的时候基本上不适用 autoprefixer，而是使用post-preset-env
```

假设我们要设置css属性： `user-select: none`，该属性的作用是，用户鼠标悬浮在元素上的时候不显示任何交互动作（文字不能被选中和复制），但是这个属性在不同的浏览器中的设置是不一样的，比如 `-ms-user-select:none`，`--webkit-user-select:none`

我们需要一个工具，当我们设置了这个元素之后，自动帮我们添加上在不同浏览器上的属性，这个工具就是`postcss`（的autoprefixer插件）

安装post-css

```bash
npm install postcss-loader -D
```

安装autoprefixer插件

```bash
npm install autoprefixer -D
```

### 整合配置的post-css

**webpack.config.js** 

```js
use: [
  'style-loader', 
  'css-loader',
  {
	loader: 'postcss-loader',
	options: {
	  postcssOptions: {
		plugins: [
		  require('autoprefixer')
		]
	  }
	}
  }
]
```

![[assets/Pasted image 20230228122716.png]]

**div.css**

```css
.content{
  width: 200px;
  height: 200px;
  background-color: aqua;
  user-select: none;
}
```

css中只写了一个user-select，但是构建完成的网站中显示如下：

![[assets/Pasted image 20230228122908.png]]

### 单独配置的post-css文件

webpack.config.js 中

![[assets/Pasted image 20230228123111.png]]

另外在根目录创建文件 postcss.config.js

```js
module.exports = {
  plugins: [
    require('autoprefixer')
  ]
}
```

同理

![[assets/Pasted image 20230228123304.png]]


### postcss-preset-env

事实上，在配置postcss-loader时，我们配置插件并不需要使用autoprefixer。我们可以使用另外一个插件：postcss-preset-env

postcss-preset-env也是一个postcss的插件，它可以帮助我们将一些现代的CSS特性，转成大多数浏览器认识的CSS，并且会根据目标浏览器或者运行时环境添加所需的polyfill；也包括会自动帮助我们添加autoprefixer（所以相当于已经内置了autoprefixer）；

首先，我们需要安装postcss-preset-env：

```bash
npm install postcss-preset-env -D
```

直接在postcss.config.js 中引入插件

```js
module.exports = {
  plugins: [
    require('postcss-preset-env')
  ]
}
```

效果是一样的

![[assets/Pasted image 20230228123635.png]]