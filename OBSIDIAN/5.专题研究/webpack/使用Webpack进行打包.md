## 使用Webpack进行打包


### 打包 

依赖图：

![[assets/Pasted image 20230228095220.png]]

```ad-tip
在使用webpack进行打包的时候，在js中只引入文件构建依赖图，而不导入资源，可以直接使用 `import "path"的形式`
```

**main.js**

```js
import "./components/add_div.js"
```


**css/div.css**

```css
.content{
  width: 200px;
  height: 200px;
  background-color: aqua;
}
```


**components/add_div.js**

```js
import "../css/div.css"

const divEl = document.createElement('div')

divEl.textContent = 'Hello World!'
divEl.classList.add('content')
document.body.append(divEl)
```

执行命令 `npm run build`进行打包

![[assets/Pasted image 20230228100004.png]]

上面的错误信息告诉我们需要一个loader来加载这个css文件，但是loader是什么呢？loader 可以用于对模块的源代码进行转换；

我们可以将css文件也看成是一个模块，我们是通过import来加载这个模块的；

在加载这个模块时，webpack其实并不知道如何对其进行加载，我们必须制定对应的loader来完成这个功能；

那么我们需要一个什么样的loader呢？
对于加载css文件来说，我们需要一个可以读取css文件的loader，这个loader最常用的是css-loader；

### css-loader安装

css-loader的安装：

```bash
npm install css-loader -D
```

如何使用css-loader?
1. 内联方式；
2. CLI方式（webpack5中不再使用）；
3. 配置方式；

我们只讲配置方式，其他方式基本已经不再使用。

配置方式表示的意思是在我们的webpack.config.js文件中写明配置信息：
- module.rules中允许我们配置多个loader（因为我们也会继续使用其他的loader，来完成其他文件的加载）；
- 这种方式可以更好的表示loader的配置，也方便后期的维护，同时也让你对各个Loader有一个全局的概览；

module.rules的配置如下：
- rules属性对应的值是一个数组：`[Rule]`
- 数组中存放的是一个个的Rule，Rule是一个对象，对象中可以设置多个属性：
	- test属性：用于对 resource（资源）进行匹配的，通常会设置成**正则表达式**；
	- use属性：对应的值是一个数组：`[UseEntry]`
		- UseEntry是一个对象，可以通过对象的属性来设置一些其他属性
		- loader：必须有一个 loader属性，对应的值是一个字符串；
		- options：可选的属性，值是一个字符串或者对象，值会被传入到loader中；
		- query：目前已经使用options来替代；
		- 传递字符串（如：`use: [ 'style-loader' ]`）是 loader 属性的简写方式（如：`use: [ { loader: 'style-loader'} ]`）；
	- loader属性： `Rule.use: [ { loader } ]` 的简写。

![[assets/Pasted image 20230228101737.png]]

然后 `npm run build`构建项目

![[assets/Pasted image 20230228101836.png]]

构建成功

打开`src/index.html`查看文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
  <body></body>
  <script src="../build/bundle.js"></script>
</html>
```

```ad-warning
注意：这里的script引入应该在body之后，以防引入js的时候，body还没有加载出来导致错误
```

![[assets/Pasted image 20230228102523.png]]

我们已经可以通过css-loader来加载css文件了，但是你会发现这个css在我们的代码中并没有生效（页面没有效果）。

这是为什么呢？

因为css-loader只是负责将.css文件进行解析，并不会将解析之后的css插入到页面中；如果我们希望再完成插入style的操作，那么我们还需要另外一个loader，就是style-loader；

### style-loader安装

安装style-loader：

```bash
npm install style-loader -D
```

配置style-loader

那么我们应该如何使用style-loader：
- 在配置文件中，添加style-loader

注意：因为loader的执行顺序是从右向左（或者说从下到上，或者说从后到前的），所以我们需要将style-loader写到css-loader的前面；

![[assets/Pasted image 20230228102736.png]]

如下，这样就可以了

![[assets/Pasted image 20230228102743.png]]