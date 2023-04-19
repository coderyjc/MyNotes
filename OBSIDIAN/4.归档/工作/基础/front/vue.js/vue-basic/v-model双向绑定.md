---
desc: 双相绑定
complete: true
---

## v-model双向绑定

v-model指令可以在表单 input、textarea以及select元素上创建双向数据绑定；

它会根据控件类型自动选取正确的方法来更新元素，v-model 本质是语法糖，它负责监听用户的输入事件来更新数据，并在某种极端场景下进行一些特殊处理。

### v-model绑定


略


### v-model修饰符

==lazy==

默认情况下，v-model在进行双向绑定时，绑定的是input事件，那么会在每次**内容输入**后就将最新的值和绑定的属性进行同步

如果我们在v-model后跟上lazy修饰符，那么会将绑定的事件切换为 change 事件，只有**在提交时**（比如回车）才会触发

```js
<!-- 1.lazy: 绑定change事件  -->
<input type="text" v-model.lazy="message">
<h2>message: {{message}}</h2>
```

==number==

v-model绑定的值总是string类型的，即使我们设置type为number类型（我们在进行逻辑判断的时候，如果是一个string类型，会进行隐式转换）。

如果我们希望转换为数字类型，那么可以使用 .number 修饰符

```html
<!-- 2.number: 自动将内容转换成数字 -->
<input type="text" v-model.number="counter">
```


==去除首尾空格==

```html
<input type="text" v-model.trim="content">
```


==使用多个修饰符==

```html
<input type="text" v-model.lazy.trim="content">
```

