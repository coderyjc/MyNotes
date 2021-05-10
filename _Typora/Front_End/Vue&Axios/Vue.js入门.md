# Vue.js入门

## 概述

**渐进式**

      1. 易用  html css javascript
      2. 高效  开发前端页面 非常高效 
      3. 灵活  开发灵活 多样性

**总结** Vue 是一个javascript 框架

**后端服务端开发人员:** 

Vue 渐进式javascript框架: 让我们通过操作很少的DOM,甚至不需要操作页面中任何DOM元素,就很容易的完成数据和视图绑定  双向绑定 MVVM  

注意: 日后在使用Vue过程中页面中不要在引入Jquery框架

htmlcss--->javascript ----->jquery---->angularjs -----> Vue

把js标签写在书写临近的js代码的位置

## Start up

### 入门应用

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>第一个Vue入门案例</title>
		<script type="text/javascript" src="../static/vue.js"></script>
	</head>
	<body>
		<!-- 
			注意代码书写的顺序，
			vue实例的代码应该放在里面作用域元素的后面
		 -->
		<div id="hello">
			<h1>{{ msg }}</h1>
			{{ msg }}
		</div>
		<script type="text/javascript">
			const vue = new Vue({
				// 用来给Vue实例定义一个作用范围
				// el表示element，表示作用于哪一个元素，一般不设置<body>，而是一个div
				// 同时也能作用到指定元素的子元素
				el: "#hello",
				data: { // 定义一种相关的数据
					msg: "Hello World"
				}
			});
		</script>
	</body>
</html>
```

> el表示元素，表示这个vue实例的作用范围，里面可以书写任意css或者jquery选择器，但是在使用vue开发时**推荐使用id选择器**（确保实例唯一性）
>
> data表示数据，可以在里面定义数据进行绑定，绑定的数据可以通过双大括号的形式在Vue的作用域内进行取出
>
> 使用双大括号的时候，可以在双大括号中书写表达式，也可以进行运算

> 对应 /Learning/Vue.js/[01* - 03*]	

### v-text和v-html

类似于js中的innertext和innerhtml

v-text 是一个指令，可以直接取出vue实例中指定的数据渲染到标签中

```html
		<div id="app">
			<!-- v-text 是一个指令，可以直接取出vue实例中指定的数据渲染到标签中 -->
			<span v-text="msg"></span>
		</div>
		<script type="text/javascript">
			const vue = new Vue({
				el: "#app",
				data: {
					msg: "Hello World!"
				}
			});
		</script>
```

v-text和插值表达式的区别：

1. 使用v-text取值会将原有数据覆盖，插值表达式不会。
2. 使用v-text可以避免页面加载时由于网络比较差时出现插值闪烁的问题
   1. 插值闪烁：vue在插值的时候会先显示原有的插值表达式原型，再进行插值
   2. 网络比较快的时候不会出现这种问题

v-html会将内容先解析再输出，类似于js的innerhtml

v-html也会覆盖原有的内容

### 事件的绑定和使用

v-on

1. 在vue中携定事件是通过v-on指令来完成的 v-on：事件名，如 v-on:click

2. 在v-on：事件名的赋值语句中是当期时间触发调用的函数名

3. 在vue中事件的统一定义在vue实例的属性中
4. 在vue定义的事件中this指的就是当前的Vue实例，日后可以在事件中通过使用this调用vue实例中的相关属性

简化写法(Vue2.0 +)：

