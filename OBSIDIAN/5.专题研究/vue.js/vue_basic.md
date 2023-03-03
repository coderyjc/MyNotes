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

保持在元素上直到关联组件实例结束编译

 和 CSS 规则如` [v-cloak] { display: none } `一起用时，这个指令可以隐藏未编译的 Mustache 标签直到组件实例准备完毕

![[assets/Pasted image 20230303212111.png]]

### v-bind

动态绑定元素属性

```html
<img :src="showImgUrl" alt="">
```

动态绑定class

```html

  <div id="app">
    <!-- 1.基本绑定class -->
    <h2 :class="classes">Hello World</h2>

    <!-- 2.动态class可以写对象语法 -->
    <button :class=" isActive ? 'active': '' " @click="btnClick">我是按钮</button>

    <!-- 2.1.对象语法的基本使用(掌握) -->
    <button :class="{ active: isActive }" @click="btnClick">我是按钮</button>

    <!-- 2.2.对象语法的多个键值对 -->
    <button :class="{ active: isActive, why: true, kobe: false }" @click="btnClick">我是按钮</button>
    
    <!-- 2.3.动态绑定的class是可以和普通的class同时的使用 -->
    <button class="abc cba" :class="{ active: isActive, why: true, kobe: false }" @click="btnClick">我是按钮</button>
    
    <!-- 2.4.动态绑定的class是可以和普通的class同时的使用 -->
    <button class="abc cba" :class="getDynamicClasses()" @click="btnClick">我是按钮</button>

    <!-- 3.动态class可以写数组语法(了解) -->
    <h2 :class="['abc', 'cba']">Hello Array</h2>
    <h2 :class="['abc', className]">Hello Array</h2>
    <h2 :class="['abc', className, isActive? 'active': '']">Hello Array</h2>
    <h2 :class="['abc', className, { active: isActive }]">Hello Array</h2>
  </div>
  
  <script src="../lib/vue.js"></script>
  <script>
    // 1.创建app
    const app = Vue.createApp({
      // data: option api
      data: function() {
        return {
          classes: "abc cba nba",
          isActive: false,
          className: "why"
        }
      },

      methods: {
        btnClick: function() {
          this.isActive = !this.isActive
        },

        getDynamicClasses: function() {
          return { active: this.isActive, why: true, kobe: false }
        }
      }
    })

    // 2.挂载app
    app.mount("#app")
  </script>
```

绑定style

```html
  <div id="app">
    <!-- 1.普通的html写法 -->
    <h2 style="color: red; font-size: 30px;">哈哈哈哈</h2>

    <!-- 2.style中的某些值, 来自data中 -->
    <!-- 2.1.动态绑定style, 在后面跟上 对象类型 (重要)-->
    <h2 v-bind:style="{ color: fontColor, fontSize: fontSize + 'px' }">哈哈哈哈</h2>
    <!-- 2.2.动态的绑定属性, 这个属性是一个对象 -->
    <h2 :style="objStyle">呵呵呵呵</h2>

    <!-- 3.style的数组语法 -->
    <h2 :style="[objStyle, { backgroundColor: 'purple' }]">嘿嘿嘿嘿</h2>
  </div>
  
  <script src="../lib/vue.js"></script>
  <script>
    // 1.创建app
    const app = Vue.createApp({
      // data: option api
      data: function() {
        return {
          fontColor: "blue",
          fontSize: 10,
          objStyle: {
            fontSize: '50px',
            color: "green"
          }
        }
      },
    })
    // 2.挂载app
    app.mount("#app")
  </script>

```

绑定属性名

```html
<h2 :[name]="'aaaa'">Hello World</h2>


data: function() {
	return {
	  name: "class"
	}
  },
```

绑定对象

```html
<h2 :name="name" :age="age" :height="height">Hello World</h2>
<!--两种方式效果是一样的。 v-bind绑定对象: 给组件传递参数 -->
<h2 v-bind="infos">Hello Bind</h2>

```

```js
  data: function() {
	return {
	  infos: { name: "why", age: 18, height: 1.88, address: "广州市" },

	  name: "why",
	  age: 18,
	  height: 1.88
	}
  },
```

## 事件绑定

### 基本操作

`v-on`指令用来监听事件

基本写法（直接写v-on的写法不再举例）

```html
<div class="box" @click="divClick"></div>
```

也可以写成一个表达式(不推荐)

```html
<button @click="counter++">+1</button>
```

绑定其他方法

```html
<div class="box" @mousemove="divMousemove"></div>
```

绑定多个事件直接写上就行

```html
<div class="box" @click="divClick" @mousemove="divMousemove"></div>
```

方法：

```js
divClick() {
  console.log("divClick")
},
increment() {
  this.counter++
},
divMousemove() {
  console.log("divMousemove")
}
```

### 参数传递

默认传递event对象
```html
    <button @click="btn1Click">按钮1</button>
```

```js
        btn1Click(event) {
          console.log("btn1Click:", event)
        },
```


自定义参数
```html
    <button @click="btn2Click('why', age)">按钮2</button>
```

```js
        btn2Click(name, age) {
          console.log("btn2Click:", name, age)
        },
```

自定义参数和event对象
```html
    <button @click="btn3Click('why', age, $event)">按钮3</button>
```

```js
        btn3Click(name, age, event) {
          console.log("btn3Click:", name, age, event)
        }
```

### 带有修饰符的事件

支持修饰符
-   `.stop` - 调用 `event.stopPropagation()`。
-   `.prevent` - 调用 `event.preventDefault()`。
-   `.capture` - 在捕获模式添加事件监听器。
-   `.self` - 只有事件从元素本身发出才触发处理函数。
-   `.{keyAlias}` - 只在某些按键下触发处理函数。
-   `.once` - 最多触发一次处理函数。
-   `.left` - 只在鼠标左键事件触发处理函数。
-   `.right` - 只在鼠标右键事件触发处理函数。
-   `.middle` - 只在鼠标中键事件触发处理函数。
-   `.passive` - 通过 `{ passive: true }` 附加一个 DOM 事件。


```js
      <button @click.stop="btnClick">按钮</button>
```


## 条件渲染

### v-if v-else v-if-else

v-if 个人信息存在就显示

```html
    <div class="info" v-if="Object.keys(info).length">
      <h2>个人信息</h2>
      <ul>
        <li>姓名: {{info.name}}</li>
        <li>年龄: {{info.age}}</li>
      </ul>
    </div>
```

v-if 和 v-else 

```html
  <div id="app">
    <!-- v-if="条件" -->
    <div class="info" v-if="Object.keys(info).length">
      <h2>个人信息</h2>
      <ul>
        <li>姓名: {{info.name}}</li>
        <li>年龄: {{info.age}}</li>
      </ul>
    </div>

    <!-- v-else -->
    <div v-else>
      <h2>没有输入个人信息</h2>
      <p>请输入个人信息后, 再进行展示~</p>
    </div>
  </div>
```

合起来用

```html
  <div id="app">
    <h1 v-if="score > 90">优秀</h1>
    <h2 v-else-if="score > 80">良好</h2>
    <h3 v-else-if="score >= 60">及格</h3>
    <h4 v-else>不及格</h4>
  </div>
```

### template的使用

把要写的信息放在template中，根据条件渲染。最终template不会被渲染出来，但是template里面的元素会被渲染出来。

有点类似于小程序中的block

```html
    <!-- v-if="条件" -->
    <template v-if="Object.keys(info).length">
      <h2>个人信息</h2>
      <ul>
        <li>姓名: {{info.name}}</li>
        <li>年龄: {{info.age}}</li>
      </ul>
    </template>

    <!-- v-else -->
    <template v-else>
      <h2>没有输入个人信息</h2>
      <p>请输入个人信息后, 再进行展示~</p>
    </template>
```


### v-show和v-if 的区别

v-show也是隐藏元素的一种方法，用法和v-if完全一样

首先，在用法上的区别：
1. v-show是不支持template；
2. v-show不可以和v-else一起使用；

其次，本质的区别：
1. v-show元素无论是否需要显示到浏览器上，它的DOM实际都是有存在的，只是通过CSS的display属性来进行切换；
2. v-if当条件为false时，其对应的原生压根不会被渲染到DOM中；

开发中如何进行选择？
1. 如果我们的原生需要在显示和隐藏之间频繁的切换，那么使用v-show；
2. 如果不会频繁的发生切换，那么使用v-if；

## 列表渲染

### 基本使用

v-for的基本格式是 "item in 数组"：
1. 数组通常是来自data或者prop，也可以是其他方式；
2. item是我们给每项元素起的一个别名，这个别名可以自定来定义；

电影列表的渲染

```html
<ul>
<li v-for="movie in movies">{{ movie }}</li>
</ul>
```

我们知道，在遍历一个数组的时候会经常需要拿到数组的索引：
1. 如果我们需要索引，可以使用格式： "(item, index) in 数组"；
2. 注意上面的顺序：数组元素项item是在前面的，索引项index是在后面的；

带有索引的渲染

```html
<ul>
  <li v-for="(movie, index) in movies">{{index + 1}} - {{ movie }}</li>
</ul>

```


 v-for也支持遍历对象，并且支持有一二三个参数：
- 一个参数： "value in object";
- 二个参数： "(value, key) in object";
- 三个参数： "(value, key, index) in object";

v-for同时也支持数字的遍历：每一个item都是一个数字；

v-for也可以遍历其他可迭代对象(Iterable)

```html
    <!-- 2.遍历对象 -->
    <ul>
      <li v-for="(value, key, index) in info">{{value}}-{{key}}-{{index}}</li>
    </ul>

    <!-- 3.遍历字符串(iterable) -->
    <ul>
      <li v-for="item in message">{{item}}</li>
    </ul>

    <!-- 4.遍历数字 -->
    <ul>
      <li v-for="item in 100">{{item}}</li>
    </ul>
```

列表渲染中的key有什么用？
官方解释：

- key属性主要用在Vue的虚拟DOM算法，在新旧nodes对比时辨识VNodes；
- 如果不使用key，Vue会使用一种最大限度减少动态元素并且尽可能的尝试就地修改/复用相同类型元素的算法；
- 而使用key时，它会基于key的变化重新排列元素顺序，并且会移除/销毁key不存在的元素

### 使用template

类似于v-if，你可以使用 template 元素来循环渲染一段包含多个元素的内容 -- 我们使用template来对多个元素进行包裹，而不是使用div来完成；

这样使用的前提是div是没有意义的。

```html
    <template v-for="(value, key, index) in infos">
      <span>{{value}}</span>
      <strong>{{key}}</strong>
      <i>{{index}}</i>
    </template>
```

### 数组更新检测

Vue 将被侦听的数组的变更方法进行了包裹，所以它们也将会触发视图更新

这些被包裹过的方法包括：
- push()
- pop()
- shift()
- unshift()
- splice()
- sort()
- reverse()

