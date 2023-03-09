```ad-note
虽然现在大部分公司使用的状态管理工具还是vuex4，但是pinia必然是大势所趋，pinia相当于vuex5

vuex官方文档：https://vuex.vuejs.org/zh/guide/
```

## 基本使用

### 介绍

管理的什么？服务器返回的数据、缓存数据、用户操作产生的数据等，也包括一些UI的状态，比如某些元素是否被选中，是否显示加载动效，当前分页；

对于一些简单的状态，确实可以通过props的传递或者Provide的方式来共享状态，但是对于复杂的状态管理来说，显然单纯通过传递和共享的方式是不足以解决问题，这时候就要使用状态管理工具进行管理。

基本思想：
- 我们的组件树构成了一个巨大的 “试图View”；
- 不管在树的哪个位置，任何组件都能获取状态或者触发行为；
- 通过定义和隔离状态管理中的各个概念，并通过强制性的规则来维护视图和状态间的独立性，我们的代码边会变得更加结构化和易于维护、跟踪；

![[assets/Pasted image 20230308160016.png]]

![[assets/Pasted image 20230308160022.png]]

```ad-note
title:Vuex和单纯的全局对象有什么区别呢？

第一：Vuex的状态存储是响应式的
- 当Vue组件从store中读取状态的时候，若store中的状态发生变化，那么相应的组件也会被更新；

第二：你不能直接改变store中的状态
- 改变store中的状态的唯一途径就显示提交 (commit) mutation；
- 这样使得我们可以方便的跟踪每一个状态的变化，从而让我们能够通过一些工具帮助我们更好的管理应用的状态；
```

### 基本使用

安装

```bash
npm install vuex
```

在文件夹`src`中创建`store/index.js`

src/store/index.js

```js
import { createStore } from 'vuex'

const store = createStore({
	state: () => ({
		counter: 0
	})
})
```

==导入store==

main.js

```js
import store from './store'

app.use(store)
```

==使用==

template中使用

```html
<div>{{ $store.state.counter }}</div>
```

在计算属性中使用

```js
  export default {
    computed: {
      storeCounter() {
        return this.$store.state.counter
      }
    }
  }
```

Composition API 的 setup 函数中使用

```js
import {useStore} from 'vuex'

const store = useStore()

function increment(){
	console.log(store.state.counter)
	store.commit("increment")
}

// 以上这种方法默认不是响应式的，想要把这个值看成响应式的，应该做如下操作：
import { toRefs } from 'vue'
const { counter } = toRefs(store.state)  
```

## State
 
### mutation

修改store中的数据需要手动提交mutations，而不是直接修改变量。（这个步骤在pinia中已经被废弃了）

store/index.js

```js
import { createStore } from 'vuex'

const store = createStore({
	state: () => ({
		counter: 0
	}),
	mutations: {
		// 增加方法
		increment(state){
			state.counter++
		}
	}
})
```




## Getters


## Mutations


## Actions


## Modules