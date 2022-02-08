---
type: DeBug
skill: Vue.js
create_date: 2022-01-31
---

#前端框架 #前端 

# Vue.js


>数据中带有HTML标签的数据绑定到视图之后不进行渲染，而是直接显示了标签文字

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