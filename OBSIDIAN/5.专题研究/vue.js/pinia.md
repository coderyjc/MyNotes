## 介绍

### Pinia对比Vuex

和Vuex相比，Pinia有很多的优势：
- 比如mutations 不再存在：
	- 他们经常被认为是 非常 冗长；
	- 他们最初带来了 devtools 集成，但这不再是问题；
- 更友好的TypeScript支持，Vuex之前对TS的支持很不友好；
- 不再有modules的嵌套结构：
	- 你可以灵活使用每一个store，它们是通过扁平化的方式来相互使用的；
- 也不再有命名空间的概念，不需要记住它们的复杂关系；

![[assets/Pasted image 20230309151333.png]]

### 安装和基本使用

安装

```bash
npm install pinia
```

创建pinia

store/index.js

```js
import { createPinia } from 'pinia'

const pinia = createPinia()

export default pinia

```

使用pinia

src/main.js

```js
import pinia from './stores'

app.use(pinia)
```

## Store

### 是什么？

什么是Store？
- 一个 Store （如 Pinia）是一个实体，它会持有为绑定到你组件树的状态和业务逻辑，也就是保存了全局的状态；
- 它有点像始终存在，并且每个人都可以读取和写入的组件；
- 你可以在你的应用程序中定义任意数量的Store来管理你的状态；

Store有三个核心概念：
- state、getters、actions；
- 等同于组件的data、computed、methods；
- 一旦 store 被实例化，你就可以直接在 store 上访问 state、getters 和 actions 中定义的任何属性；

### 使用

使用`defineStore()`定义store，并且它需要一个**唯一**名称，作为**第一个**参数传递。

这个 name，也称为 id，是必要的，Pinia 使用它来将 store 连接到 devtools。返回的函数统一使用useX作为命名方案，这是约定的规范；

store

```js
// 定义关于counter的store
import { defineStore } from 'pinia'

const useCounter = defineStore("counter",  {
	state(){
		return {
			counter: 0
		}
	}
})

export default useCounter
```





## State


## Getters


## Actions

