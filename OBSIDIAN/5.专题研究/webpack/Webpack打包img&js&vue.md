## Webpack打包img&js&vue

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