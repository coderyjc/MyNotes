
## 导入导出方式

### 导出

导出方式1：

```js
const name = 'codryjc'
const age = 20

function sayhello() {
  console.log('hello')
}

export {
  name, 
  age,
  sayhello
}
// 导出的时候直接写 name,age,sayhello
```


导出方式2：

```js
const name = 'codryjc'
const age = 20

function sayhello() {
  console.log('hello')
}

export {
  name as fname, 
  age as fage,
  sayhello as fsayhello
}

// 导出的时候写 fname,fage,fsayhello
```


导出方式3：

```js
export const name = 'codryjc'
export const age = 20

export function sayhello() {
  console.log('hello')
}

```

声明时导出，导入的时候同1

### 导入

1. 直接导入

```js
import {name, age, sayhello} from './util.js'
```


2. 导入时起别名

```js
import {name as fname, age as fname, sayhello} from './util.js'
```

3. 整个模块的别名

```js
import * as util from "./utils.js"
```


## 其他导入导出

如果我们想要把一个文件作为工具文件，则可以这样写

```js
// ./util/utils.js
export function getUserList(){
  console.log("getUserList")
}
// ./util/utils1.js
export function getPostList(){
  console.log("getPostList")
}

// index.js
export { getUserList } from './util/utils.js'
export { getPostList } from './util/utils.js'
```


导入：

```js
import {getUserList, getPostList} from './util'

getUserList()
getPostList()
```

或者

```js
import * from './util'

getUserList()
getPostList()
```

## default的用法

前面我们学习的导出功能都是有名字的导出（named exports）：
- 在导出export时指定了名字；
- 在导入import时需要知道具体的名字；

还有一种导出叫做默认导出（default export）
- 默认导出export时可以不需要指定名字；
- 在导入时不需要使用 {}，并且可以自己来指定名字；
- 它也方便我们和现有的CommonJS等规范相互操作；

注意：在一个模块中，只能有一个默认导出（default export）

默认导出在导入的时候不用写大括号

==方法一==

```js
// utils.js
function getUserList(){
  console.log("getUserList")
}

export default getUserList // 不用写大括号
```

```js
// main.js
import aa from './utils.js'
// 在导入的时候也就不用写大括号，而且可以随便起名字
aa()
```

注意：如果导出的时候有大括号，那么在导入的时候也应该写上大括号

==方法二==

匿名函数导出

```js
// utils.js
export default function(){
  console.log("getUserList")
}
```

```js
// main.js
import aa from './utils.js'

aa()
```

## import函数

通过import加载一个模块，是不可以在其放到逻辑代码中的，比如：

```js
let flag = true
if(flag){
	// 这种情况是绝对不允许的
	import { name, age } from "./util.js"
	console.(name)
}
```

import声明必须写在顶层。

为什么会出现这个情况呢？

这是因为ES Module在被JS引擎解析时，就必须知道它的依赖关系，由于这个时候js代码没有任何的运行，所以无法在进行类似于if判断中根据代码的执行情况，甚至拼接路径的写法也是错误的：因为我们必须到运行时能确定path的值。

但是某些情况下，我们确确实实希望动态的来加载某一个模块：

如果根据不懂的条件，动态来选择加载模块的路径，这个时候我们需要使用 import() 函数来动态加载，import函数返回一个Promise，可以通过then获取结果；

```js
let flag = true

if (flag) {
  const importPromise = import("./utils.js")
  importPromise.then(res => {
    console.log(res.name)
  })
}
```


import中有个meta属性，了解即可。

## ES Module解析流程

https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/

阶段一：构建（Construction），根据地址查找js文件，并且下载，将其解析成模块记录（Module Record）；
阶段二：实例化（Instantiation），对模块记录进行实例化，并且分配内存空间，解析模块的导入和导出语句，把模块指向对应的内存地址。
阶段三：运行（Evaluation），运行代码，计算值，并且将值填充到内存地址中；

![[assets/Pasted image 20230227122453.png]]

![[assets/Pasted image 20230227122504.png]]

![[assets/Pasted image 20230227122511.png]]