
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

