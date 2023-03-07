---
desc: watch侦听事件
complete: true
---

## watch侦听

### watch入门

watch是**属性**

开发中我们在data返回的对象中定义了数据，这个数据通过插值语法等方式绑定到template中,当数据变化时，template会自动进行更新来显示最新的数据,但是在某些情况下，我们希望在代码逻辑中监听某个数据的变化，这个时候就需要用侦听器watch来完成了；

侦听器的用法如下：
- 选项：watch
- 类型：`{ [key: string]: string | Function | Object | Array}`

侦听器默认侦听属性的值，对于对象，默认侦听引用的变化，如果要侦听对象内部属性的变化，需要写上`deep`属性，举例如下：

```html
  <div id="app">
    <h2>{{message}}</h2>
    <button @click="changeMessage">修改message</button>
  </div>
```

```js
//...
  data() {
	return {
	  message: "Hello Vue",
	  info: { name: "why", age: 18 }
	}
  },
  methods: {
	changeMessage() {
	  this.message = "你好啊, 李银河!",
	  //this.info.name = "kobe" // 内部属性 变化，watch默认不侦听，除非添加deep属性
	  this.info = { name: "kobe" }
	}
  },
watch: {
	// 1.默认有两个参数: newValue/oldValue
	message(newValue, oldValue) {
	  console.log("message数据发生了变化:", newValue, oldValue)
	},
	info(newValue, oldValue) {
	  // 2.如果是对象类型, 那么拿到的是代理对象
	  // 只有当引用变化的时候才会侦听到
	  // console.log("info数据发生了变化:", newValue, oldValue)
	  // console.log(newValue.name, oldValue.name)
	  console.log(this.info);
	  // 3.获取原生对象
	  // console.log({ ...newValue })
	  // console.log(Vue.toRaw(newValue))
	  // 两种写法是一样的
	}
  }

```

### 侦听相关选项

==深度监听&第一次渲染时执行一次监听器==

默认不会监听对象内部的属性，使用deep属性将会进行深度监听

也可以针对属性进行监听

```js
  watch: {
	// 进行深度监听
	info: {
	  handler(newValue, oldValue) {
		console.log("侦听到info改变:", newValue, oldValue)
		console.log(newValue === oldValue)
	  },
	  // 监听器选项:
	  // info进行深度监听
	  deep: true,
	  // 第一次渲染直接执行一次监听器
	  immediate: true
	},
	"info.name": function(newValue, oldValue) {
	  console.log("name发生改变:", newValue, oldValue)
	}
  }
```

### this.$watch

我们可以在created的生命周期（后续会讲到）中，使用 this.$watchs 来侦听；
- 第一个参数是要侦听的源；
- 第二个参数是侦听的回调函数callback；
- 第三个参数是额外的其他选项，比如deep、immediate；

```js
  // 生命周期回调函数: 当前的组件被创建时自动执行
  // 一般在该函数中, 会进行网络请求
  created() {
	// ajax/fetch/axios
	console.log("created")

	this.$watch("message", (newValue, oldValue) => {
	  console.log("message数据变化:", newValue, oldValue)
	}, { deep: true })
  }
```




