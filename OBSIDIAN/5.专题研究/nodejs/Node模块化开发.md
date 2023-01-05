
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

