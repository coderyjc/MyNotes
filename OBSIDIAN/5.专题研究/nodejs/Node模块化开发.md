
是什么？

- 将程序划分为一个个的小结构
- 这个结构中编写属于自己的代码， 有自己的作用域，定义变量的时候不会影响到其他的结构
- 这个结构可以将自己希望暴露的变量、函数、对象等**导出**给其结构使用
- 也可以通过某种方式**导入**另外结构中的变量、函数、对象等

上面说提到的结构，就是模块；按照这种结构划分开发程序的过程，就是模块化开发的过程；

无论你多么喜欢JavaScript，以及它现在发展的有多好，它都有很多的缺陷：

- 比如var定义的变量作用域问题；
- 比如JavaScript的面向对象并不能像常规面向对象语言一样使用class；
- 比如JavaScript没有模块化的问题；

在网页开发的早期，Brendan Eich开发JavaScript仅仅作为一种脚本语言，做一些简单的表单验证或动画实现等，那个时候代码还是很少的，这个时候我们只需要讲JavaScript代码写到`<script>`标签中即可，并没有必要放到多个文件中来编写；甚至流行：通常来说 JavaScript 程序的长度只有一行。

但是随着前端和JavaScript的快速发展，JavaScript代码变得越来越复杂了：

- ajax的出现，前后端开发分离，意味着后端返回数据后，我们需要通过JavaScript进行前端页面的渲染；
- SPA的出现，前端页面变得更加复杂：包括前端路由、状态管理等等一系列复杂的需求需要通过JavaScript来实现；
- 包括Node的实现，JavaScript编写复杂的后端程序，没有模块化是致命的硬伤；

所以，模块化已经是JavaScript一个非常迫切的需求：

但是JavaScript本身，直到ES6（2015）才推出了自己的模块化方案；在此之前，为了让JavaScript支持模块化，涌现出了很多不同的模块化规范：AMD、CMD、CommonJS等；


早期没有模块化带来了很多的问题：比如命名冲突的问题

当然，我们有办法可以解决上面的问题：立即函数调用表达式（IIFE） IIFE (Immediately Invoked Function Expression)

但是，我们其实带来了新的问题：

- 第一，我必须记得每一个模块中返回对象的命名，才能在其他模块使用过程中正确的使用；
- 第二，代码写起来混乱不堪，每个文件中的代码都需要包裹在一个匿名函数中来编写；
- 第三，在没有合适的规范情况下，每个人、每个公司都可能会任意命名、甚至出现模块名称相同的情况；

所以，我们会发现，虽然实现了模块化，但是我们的实现过于简单，并且是没有规范的。

我们需要制定一定的规范来约束每个人都按照这个规范去编写模块化的代码；

这个规范中应该包括核心功能：模块本身可以导出暴露的属性，模块又可以导入自己需要的属性；

JavaScript社区为了解决上面的问题，涌现出一系列好用的规范，接下来我们就学习具有代表性的一些规范。


## CommonJS规范

CommonJS是一个规范，最初提出来是在浏览器以外的地方使用，并且当时被命名为ServerJS，后来为了体现它的广泛性，修改为CommonJS，平时我们也会简称为CJS。

- Node是CommonJS在服务器端一个具有代表性的实现；
- Browserify是CommonJS在浏览器中的一种实现；
- webpack打包工具具备对CommonJS的支持和转换；

浏览器中默认不支持CommonJS

所以，Node中对CommonJS进行了支持和实现，让我们在开发node的过程中可以方便的进行模块化开发：

- 在Node中每一个js文件都是一个单独的模块；
- 这个模块中包括CommonJS规范的核心变量：exports、module.exports、require；
- 我们可以使用这些变量来方便的进行模块化开发；

前面我们提到过模块化的核心是导出和导入，Node中对其进行了实现：

- exports和module.exports可以负责对模块中的内容进行导出；
- require函数可以帮助我们导入其他模块（自定义模块、系统模块、第三方库模块）中的内容；

### 基本用法

utils.js
```js
FILE_NAME = "utils.js"

function hello(){
  console.log("hello");
}

// 导出模块中的内容
exports.FILE_NAME = FILE_NAME
exports.hello = hello

```

main.js
```js
// 导入时解构
const {FILE_NAME, hello} = require('./utils.js')

console.log(FILE_NAME)

hello()
```

### 实质

实际上，exports是一个对象，向其中添加的属性将会被导出。

在另一个文件中使用require实际上是拿到了这个exports对象，也就是require通过各种查找的方式，最终找到了export对象，并且把这个exports对象赋值给了另一个文件中的变量，这个变量就是exports对象了。

exports的本质就是一种引用赋值，在被引用的文件中修改导出值的时候，在引用的文件中也会变化。

utils.js

```js
let name = "bar"

exports.name = name

// 2s之后修改
setTimeout(() => {
  exports.name = "why"
  console.log('已修改');
}, 2000)

```

main.js

```js
// 探讨require的本质
const bar = require("./utils")
console.log(bar.name) // bar

// 4s之后重新获取name
setTimeout(() => {
  console.log(bar.name)
}, 4000)
```

![[assets/Pasted image 20230105142438.png]]


## module.exports

开发中的常见写法：

utils.js

```js
user_name = 'jack'
user_age = 18

user_quote = function(user_name) {
  console.log('hello, i am ' + user_name);
}

// 常用写法
module.exports = {
  user_name, 
  user_age,
  user_quote
}
```

main.js

```js
user = require('./utils')

console.log(user.user_name)
console.log(user.user_age)
user.user_quote(123)
```

但是Node中我们经常导出东西的时候，又是通过module.exports导出的：module.exports和exports有什么关系或者区别呢？

我们追根溯源，通过维基百科中对CommonJS规范的解析：

- CommonJS中是没有module.exports的概念的；

但是为了实现模块的导出，Node中使用的是Module的类，每一个模块都是Module的一个实例，也就是module；所以在Node中真正用于导出的其实根本不是exports，而是module.exports；因为module才是导出的真正实现者；

但是，为什么exports也可以导出呢？

- 这是因为module对象的exports属性是exports对象的一个引用；也就是说 module.exports = exports = main中的bar；


## require查找规则


**情况一. X是一个Node核心模块，比如path、http**

- 直接返回核心模块，并且停止查找

**情况二：X是以 ./ 或 ../ 或 /（根目录）开头的**

第一步：将X当做一个文件在对应的目录下查找；

1. 如果有后缀名，按照后缀名的格式查找对应的文件
2. 如果没有后缀名，会按照如下顺序：
	1. 直接查找文件X
	2. 查找X.js文件
	3. 查找X.json文件
	4. 查找X.node文件

第二步：没有找到对应的文件，将X作为一个目录，查找目录下面的index文件

1. 查找X/index.js文件
2. 查找X/index.json文件
3. 查找X/index.node文件

如果没有找到，那么报错：not found

**情况三：直接是一个X（没有路径），并且X不是一个核心模块**

/Users/coderwhy/Desktop/Node/TestCode/04_learn_node/05_javascript-module/02_commonjs/main.js中编写 require('why’)

![[assets/Pasted image 20230105145832.png]]

如果上面的路径中都没有找到，那么报错：not found


## 模块加载过程

**结论一：模块在被第一次引入时，模块中的js代码会被运行一次**


**结论二：模块被多次引入时，会缓存，最终只加载（运行）一次**

为什么只会加载运行一次呢？

这是因为每个模块对象module都有一个属性：loaded。

为false表示还没有加载，为true表示已经加载；

**结论三：如果有循环引入，那么加载顺序是深度优先算法**

如果出现右图模块的引用关系，那么加载顺序是什么呢？

![[assets/Pasted image 20230105151203.png]]

Node采用的是深度优先算法：main -> aaa -> ccc -> ddd -> eee ->bbb

## CommonJS加载模式的缺点

CommonJS加载模块是同步的：

同步的意味着只有等到对应的模块加载完毕，当前模块中的内容才能被运行；这个在服务器不会有什么问题，因为服务器加载的js文件都是本地文件，加载速度非常快；

如果将它应用于浏览器呢？

浏览器加载js文件需要先从服务器将文件下载下来，之后再加载运行；那么**采用同步的就意味着后续的js代码都无法正常运行**，即使是一些简单的DOM操作；

所以在浏览器中，我们通常**不使用CommonJS规范**：

当然在webpack中使用CommonJS是另外一回事；因为它会将我们的代码转成浏览器可以直接执行的代码；

在早期为了可以在浏览器中使用模块化，通常会采用AMD或CMD：但是目前一方面现代的**浏览器已经支持ES Modules**，另一方面借助于webpack等工具可以**实现对CommonJS或者ES Module代码的转换**；AMD和CMD已经使用非常少了；


## AMD和CMD规范【了解即可】

AMD主要是应用于浏览器的一种模块化规范：

AMD是Asynchronous Module Definition（异步模块定义）的缩写，它采用的是异步加载模块。

事实上AMD的规范还要早于CommonJS，但是CommonJS目前依然在被使用，而AMD使用的较少了。我们提到过，规范只是定义代码的应该如何去编写，只有有了具体的实现才能被应用。

AMD实现的比较常用的库是require.js和curl.js；

![[assets/Pasted image 20230105151548.png]]

----

CMD规范也是应用于浏览器的一种模块化规范：

CMD 是Common Module Definition（通用模块定义）的缩写；

它也采用的也是异步加载模块，但是它将CommonJS的优点吸收了过来；

但是目前CMD使用也非常少了；

CMD也有自己比较优秀的实现方案：SeaJS

![[assets/Pasted image 20230105151556.png]]
