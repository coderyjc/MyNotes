---
type: DeBug
skill: Vue.js
create_date: 2022-01-31
---

#前端框架 #前端 


### 数据中带有HTML标签的数据绑定到视图之后不进行渲染，而是直接显示了标签文字

需要进行HTML渲染的数据标签需要加上 v-html 指令，让其值等于需要渲染的字符串

```jsx
<div v-html="articleContent">
    {{ articleContent }}
</div>

<script>
	var App = new Vue({
		el:...,
		data: {
			articleContent: "<p>Hello World</p>"
		},
		methods:{}
	})
</script>
```

### 使用vue3, 导入router之后, 在app.vue 中显示  Cannot use JSX unless the '--jsx' flag is provided.ts(17004)

在项目根目录的jsconfig.json 中添加这一行

```js
    "jsx": "preserve"
```

![[assets/Pasted image 20220623201636.png]]


### 使用echarts的时候报错TypeError: error loading dynamically imported module


![[assets/Pasted image 20230310084246.png]]

代码中的option应该提前声明

错误代码：

```js
option =  {
// .....
}
```

正确代码：

```js
const option = {
// .....
}
```


### 使用echarts连续引入两个相同的echarts封装成的组件导致只渲染一个，另一个不显示

封装echarts图标到组件中时指定了固定的id，在父组件中引入的时候相当于在一个页面中引入了两个id相同的echarts组件，因此会只显示一个。

解决方案：手动传入组件id，将id改为组件的一个prop




