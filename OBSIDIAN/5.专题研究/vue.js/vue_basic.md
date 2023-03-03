## Vue初探

### MVVM模型

通常情况下，我们也经常称Vue是一个MVVM的框架，Vue官方其实有说明，Vue虽然并没有完全遵守MVVM的模型，但是整个设计是受到它的启发的。

![[assets/Pasted image 20230301163851.png]]

### 引入方法

方法一：CDN引入

```html
  <div id="app"></div>
  
  <!-- CDN地址 -->
  <script src="https://unpkg.com/vue@next"></script>
  <script>
    // 使用Vue
    const app = Vue.createApp({
      template: `<h2>Hello World</h2><span>呵呵呵</span>`
    })
    // 挂载
    app.mount("#app")

  </script>
```

方法二：

```html
  <script src="./lib/vue.js"></script>
  <script>
    
    // 1.创建app
    const app = Vue.createApp({
      template: `<h1>Hello Vue</h1>`
    })

    // 2.挂载app
    app.mount("#app")

  </script>

```


### data属性

data是一个`函数`

data属性是传入一个函数，并且该函数需要返回一个对象。在Vue3.x的时候，必须传入一个函数（vue2可以传入对象），否则就会直接在浏览器中报错；

data中返回的对象会被Vue的响应式系统劫持，之后对该对象的修改或者访问都会在劫持中被处理：所以我们在template或者app中通过 {{counter}} 访问counter，可以从对象中获取到数据；所以我们修改counter的值时，app中的 {{counter}}也会发生改变；

### method属性

methods属性是一个`对象`，通常我们会在这个对象中定义很多的方法：
- 这些方法可以被绑定到 模板中；
- 在该方法中，我们可以使用this关键字来直接访问到data中返回的对象的属性；

```ad-question
title: 为什么不能使用箭头函数？
我们在methods中要使用data返回对象中的数据，这个this是必须有值的，并且应该可以通过this获取到data返回对象中的数据。
那么我们这个this能不能是window呢？不可以是window，因为window中我们无法获取到data返回对象中的数据；但是如果我们使用箭头函数，那么这个this就会是window了；为什么是window呢？这里涉及到箭头函数使用this的查找规则，它会在自己的上层作用于中来查找this；最终刚好找到的是script作用于中的this，所以就是window；
```

```ad-question
title: this到底指向什么？
Vue的源码当中就是对methods中的所有函数进行了遍历，并且通过bind绑定了this：
![[assets/Pasted image 20230301164255.png]]
```

## 模板语法

### mustache 插值语法

```html
<!-- 1.基本使用 -->
<h2>{{ message }}</h2>
<h2>当前计数: {{ counter }} </h2>

<!-- 2.表达式 -->
<h2>计数双倍: {{ counter * 2 }}</h2>
<h2>展示的信息: {{ info.split(" ") }}</h2>

<!-- 3.三元运算符 -->
<h2>{{ age >= 18? "成年人": "未成年人" }}</h2>

<!-- 4.调用methods中函数 -->
<h2>{{ formatDate(time) }}</h2>

<!-- 5.注意: 这里不能定义语句 -->
<!-- <h2>{{ const name = "why" }}</h2> -->
```

### v-once

v-once用于指定元素或者组件只渲染一次, 当数据发生变化时，元素或者组件以及其所有的子元素将视为静态内容并且跳过，该指令可以用于性能优化。

如果是子节点，也是只会渲染一次。

```html
<h2 v-once>
  {{ message }}
  <span>数字: {{counter}}</span>
</h2>
```

### v-text

用于更新元素的`textContent`

```html
<span v-text="msg"></span>

<span>{{ msg }}</span>
```

### v-html

默认情况下，如果我们展示的内容本身是 html 的，那么vue并不会对其进行特殊的解析,如果我们希望这个内容被Vue可以解析出来，那么可以使用 v-html 来展示

```html
  <div id="app">
    <h2>{{ content }}</h2>
    <h2 v-html="content"></h2>
  </div>
  
  <script src="../lib/vue.js"></script>
  <script>
    // 1.创建app
    const app = Vue.createApp({
      // data: option api
      data: function() {
        return {
          content: `<span style="color: red; font-size: 30px;">哈哈哈</span>`
        }
      },
    })

    // 2.挂载app
    app.mount("#app")
  </script>
```

### v-pre

 v-pre用于跳过元素和它的子元素的编译过程，显示原始的Mustache标签，跳过不需要编译的节点，加快编译的速度

```html
    <div v-pre>
      <h2>{{ message }}</h2>
    </div>
```

### v-cloak




### v-memo



### v-bind







## Options API



## v-model表单



## 其他


