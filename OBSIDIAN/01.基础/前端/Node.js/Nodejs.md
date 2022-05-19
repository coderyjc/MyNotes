# Node.js

## 简介

Node.js简介Node.js是一个能够在服务器端运行JavaScript的开放源代码、跨平台JavaScript运行环境。

Node采用Google开发的V8引擎运行js代码，使用**事件驱动**、**非阻塞**和**异步IO模型**等技术来提高性能，可优化应用程序的传输量和规模。

Node大部分基本模块都用JavaScript编写。在Node出现之前，JS通常作为客户端程序设计语言使用，以JS写出的程序常在用户的浏览器上运行。

目前，Node已被IBM、Microsoft、Yahoo！、Walmart、Groupon、SAP、LinkedIn、Rakuten、PayPal、Voxer GoDaddy等企业采用。

直接操作系统、将Js的战场扩大到了后端服务器，可以不再依赖浏览器！！！

Node是单线程的，不会有IO阻塞（其他语言C、C++、Java等都做不到）。

web.js -> node.js

### 用途：

- Web服务API,比如REST 
- 实时多人游戏
- 后端的Web服务，例如跨域、服务器端的请求
- 基于Web的应用
- 多客户端的通信，如即时通信
- 
![[image-20211126205558677.png]]


- Node是对ES标准一个实现，Node也是一个8引擎
- 通过Node可以使js代码在服务器端执行
- Node仅仅对Es标准进行了实现，所以在Node中不包含DOM和BOM 
- Node中可以使用所有的内建对象string Number Boolean Math Date RegExp Function object Array 而BoM和DoM都不能使用
  - 但是可以使用console
  - 也可以使用定时器（setrimeout（）setInterval())
- Node可以在后台来编写服务器 Node编写服务器都是单线程的服务器
  - 进程就是一个一个的工作计划（工厂中的车间）
  - 线程是计算机最小的运算单位（工厂中的工人）线程是干活的

传统的服务器都是多线程的，每进来一个请求，就创建一个线程去处理请求

Node处理请求时是单线程，但是在后台拥有一个I/O线程池

优点：可以做成分布式的。

### node执行js

进入目录，然后`node hello.js`

## 模块化



**ECMAScript标准的缺陷**

- 没有模块系统
- 标准库较少
- 没有标准接口
- 缺乏管理系统



 **模块化**

- 如果程序设计的规模达到了一定程度，则必须对其进行模块化。
- 模块化可以有多种形式，但至少应该提供能够将代码分割为多个源文件的机制。
- CommonJS的模块功能可以帮我们解决该问题。



**CommonJS规范**

- CommonJS规范的提出,主要是为了弥补当前JavaScript没有标准的缺陷。
- CommonJS规范为JS指定了一个美好的愿景,希望JS能够在在何地方运行。
- CommonJS对模块的定义十分简单:
  - 模块引用
  - 模块定义
  - 模块标识



在node中，一个Js文件就是一个模块

在node中，通过require()函数引入外部模块，require()可以传递一个文件的路径作为参数，node将会自动根据该路径引入外部模块，这里的路径，如果使用相对路径，必须以`.` 或者 `..` 开头

```js
// 0.hello.js
console.log('Hello World');

// module.js
require('./0.hello.js')
```



使用require引入模块后，函数会返回一个对象，这个对象是引入的模块。

在Node中，一个js文件就是一个模块

在Node中，每一个js文件中的 js 代码都是独立运行在一个函数中，而不是全局作用域，所以一个模块中的变量和函数无法在其他模块中无法访问，因此我们应该向外部暴露属性或者方法

我们可以通过exports来向外部暴露变量和方法

只需要将需要暴露给外部的变量或方法设置为exports的屬性即可

```js
// 0.hello.js
exports.x = 123
exports.fn = function () {
    console.log('hello world')
}	

// module.js
req = require('./0.hello') // 可以不加 js 后缀
console.log(req.x)
req.fn()
// 输出 123 和 hello world
```



模块分成两大类

- 由node引擎提供的模块
- 核心模块的标识就是，模块的名字

文件模块

- 由用户自己创建的模块
- 文件模块的标识就是文件的路径（绝对路径，相对路径）相对路径使用`.`或`..`开头

核心模块不用自己写名字，直接引入就可以了 `var fs = require('fs')`



**引入的模块实际上是运行在一个函数中的，如何证明？**

在node中有一个全局对象global， 它的作用和网页中window类似

- 在全局中创建的变量都会作为global的属性保存

- 在全局中创建的函数都会作为global的方法保存

第一种方法：打印出global中的对象，如果可以找到，就运行在全局中的，找不到就是运行在函数中的

进一步证明：函数中独有的变量`arguments` 打印之后有内容，因此是局部变量

再进一步证明：`arguments.callee `保存当前执行的函数对象，只要打印出这个值即可

![image-20211126220553523](image-20211126220553523.png)



这时候发现本教程版本过低，弃坑了。