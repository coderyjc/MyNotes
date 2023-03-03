## Vue初探

### MVVM模型

通常情况下，我们也经常称Vue是一个MVVM的框架，Vue官方其实有说明，Vue虽然并没有完全遵守MVVM的模型，但是整个设计是受到它的启发的。

![[vue-basic/assets/Pasted image 20230301163851.png]]

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