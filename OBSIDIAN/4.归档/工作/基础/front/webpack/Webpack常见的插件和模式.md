## Webpack常见的插件和模式

Webpack两大核心：Loader和Plugin

### 认识插件Plugin

- Loader是用于特定的模块类型进行转换；
- Plugin可以用于执行更加广泛的任务，比如打包优化、资源管理、环境变量注入等；

### CleanWebpackPlugin

前面我们演示的过程中，每次修改了一些配置，重新打包时，都需要手动删除dist文件夹，我们还可以借助插件来完成这个过程

安装

```bash
npm install clean-webpack-plugin -D
```

注册

```js
const { CleanWebpackPlugin } = require('clean-webpack-plugin')

moldule.exports = {
	//...
	plugins:[
		new CleanWebpackPlugin()
	]
}

```

测试，在build文件夹中创建文件

![[assets/Pasted image 20230228180329.png]]

重新构建

![[assets/Pasted image 20230228180355.png]]

文件被删除了。

### HtmlWebpackPlugin

我们的HTML文件是编写在根目录下的，而最终打包的dist文件夹中是没有index.html文件的，在进行项目部署的时，必然也是需要有对应的入口文件index.html，所以我们也需要对index.html进行打包处理，对HTML进行打包处理我们可以使用另外一个插件：HtmlWebpackPlugin

安装

```bash
npm install html-webpack-plugin -D
```

基本配置

```js
const HtmlWebpackPlugin = require('html-webpack-plugin')
module.exports = {
// ...
  plugins: [
    new HtmlWebpackPlugin({
      title: "演示"
    }),
  ]
}
```

![[assets/Pasted image 20230228180726.png]]

生成了对应的文件

==如何自定义HTML生成模版？==

这个模板在 `node_moldules/html-webpack-plugin/default_index.ejs`中

![[assets/Pasted image 20230228180945.png]]

我们可以使用template字段指定填充HTML所需要的模版。

创建文件`public/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="<%= BASE_URL %>favicon.ico">
  <title><%= htmlWebpackPlugin.options.title %></title>
</head>
<body>
  <noscript>
    Please enable your JavaScript.
  </noscript>
  <div id="app"></div>
</body>
</html>
```

并在webpack的config中指定模板

```js
    new HtmlWebpackPlugin({
      title: "演示",
      template: "./public/index.html"
    }),
```

重新构建

报错：没有指定BASE_URL

![[assets/Pasted image 20230228182226.png]]

这个时候我们可以使用DefinePlugin插件

### DefinePlugin

 DefinePlugin允许在编译时创建配置的全局常量，是一个webpack内置的插件（不需要单独安装）：

```js
const {DefinePlugin} = require('webpack')
// ......
    new DefinePlugin({
      BASE_URL: '"./"'
    })
```

重新构建

![[assets/Pasted image 20230228182452.png]]

成功

### mode模式配置

Mode配置选项，可以告知webpack使用相应模式的内置优化：
- 默认值是production（什么都不设置的情况下）；
- 可选值有：'none' | 'development' | 'production'；

![[assets/Pasted image 20230228182600.png]]

以下可以了解

![[assets/Pasted image 20230228182653.png]]