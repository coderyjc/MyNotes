

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


