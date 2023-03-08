# vue_router

## 介绍

### 后段路由阶段

早期的网站开发整个HTML页面是由服务器来渲染的. 服务器直接生产渲染好对应的HTML页面, 返回给客户端进行展示.

但是, 一个网站, 这么多页面服务器如何处理呢?
- 一个页面有自己对应的网址, 也就是URL；
- URL会发送到服务器, 服务器会通过正则对该URL进行匹配, 并且最后交给一个Controller进行处理；
- Controller进行各种处理, 最终生成HTML或者数据, 返回给前端.

上面的这种操作, 就是后端路由：

- 当我们页面中需要请求不同的路径内容时, 交给服务器来进行处理, 服务器渲染好整个页面, 并且将页面返回给客户端.
- 这种情况下渲染好的页面, 不需要单独加载任何的js和css, 可以直接交给浏览器展示, 这样也有利于SEO的优化.

后端路由的缺点:
- 一种情况是整个页面的模块由后端人员来编写和维护的；
- 另一种情况是前端开发人员如果要开发页面, 需要通过PHP和Java等语言来编写页面代码；
- 而且通常情况下HTML代码和数据以及对应的逻辑会混在一起, 编写和维护都是非常糟糕的事情；

### 前后端分离阶段

前端渲染的理解：
- 每次请求涉及到的静态资源都会从静态资源服务器获取，这些资源包括HTML+CSS+JS，然后在前端对这些请求回来的资源进行渲染；
- 需要注意的是，客户端的每一次请求，都会从静态资源服务器请求文件；
- 同时可以看到，和之前的后端路由不同，这时后端只是负责提供API了；

前后端分离阶段：
- 随着Ajax的出现, 有了前后端分离的开发模式；
- 后端只提供API来返回数据，前端通过Ajax获取数据，并且可以通过JavaScript将数据渲染到页面中；
- 这样做最大的优点就是前后端责任的清晰，后端专注于数据上，前端专注于交互和可视化上；
- 并且当移动端(iOS/Android)出现后，后端不需要进行任何处理，依然使用之前的一套API即可；
- 目前比较少的网站采用这种模式开发；

单页面富应用阶段:
- 其实SPA最主要的特点就是在前后端分离的基础上加了一层前端路由.
- 也就是前端来维护一套路由规则.

前端路由的核心是什么呢？改变URL，但是页面不进行整体的刷新。

前端路由是如何做到URL和内容进行映射呢？监听URL的改变。

### 两种路由模式

URL的hash也就是锚点(#), 本质上是改变window.location的href属性， 我们可以通过直接赋值location.hash来改变href, 但是页面不发生刷新；

hash的优势就是兼容性更好，在老版IE中都可以运行，但是**缺陷是有一个#**，显得不像一个真实的路径。

![[assets/Pasted image 20230308132326.png]]

history接口是HTML5新增的, 它有六种模式改变URL而不刷新页面：
- replaceState：替换原来的路径；
- pushState：使用新的路径；
- popState：路径的回退；
- go：向前或向后改变路径；
- forward：向前改变路径；
- back：向后改变路径

history模式不显示路径

![[assets/Pasted image 20230308134752.png]]

### 认识vue-router

目前前端流行的三大框架, 都有自己的路由实现:
- Angular的ngRouter
- React的ReactRouter
- Vue的vue-router

Vue Router 是 Vue.js 的官方路由：
- 它与 Vue.js 核心深度集成，让用 Vue.js 构建单页应用（SPA）变得非常容易；
- 目前Vue路由最新的版本是4.x版本，我们上课会基于最新的版本讲解；

vue-router是基于路由和组件的
- 路由用于设定访问路径, 将路径和组件映射起来；
- 在vue-router的单页面应用中, 页面的路径的改变就是组件的切换；

安装vue-router

```bash
npm install vue-router
```

## 基本使用

### 使用步骤

1. 安装vue-router `npm install vue-router`
2. 创建路由需要映射的组件（打算显示的页面）
3. 通过createRouter创建路由对象，并且传入routes和history模式
	-  配置路由映射: 组件和路径映射关系的routes数组
	-  创建基于hash或者history的模式
4. 使用app注册路由对象（use方法）
5. 路由使用: 通过`<router-link>`和`<router-view>`

在`src/router/index.js`中维护映射关系

index.js

```js
import { createRouter, createWebHashHistory } from 'vue-router'

import Home from '../Views/Home.vue'
import About from '../Views/About.vue'

// 创建映射关系
const routes = [
    { path: "/home", component: Home },
    { path: "/about", component: About },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

// 导出模块
export default router
```

main.js 注册

```js
import router from './router'

app.use(router)
```

app.vue 使用router-view

```vue
<template>
  <div class="app">
    <h2>App Content</h2>
    <router-view></router-view>
  </div>
</template>
```


## router-link

### 默认路径

默认情况下, 进入网站的首页, 我们希望`<router-view>`渲染首页的内容，但是我们的实现中, 默认没有显示首页组件, 必须让用户点击才可以

如何可以让路径默认跳到到首页, 并且`<router-view>`渲染首页组件呢?

![[assets/Pasted image 20230308134633.png]]

path配置的是根路径: /，redirect是重定向, 也就是我们将根路径重定向到/home的路径下

### router-link的属性

to属性：
- 是一个字符串，或者是一个对象

replace属性：
- 设置 replace 属性的话，当点击时，会调用 router.replace()，而不是 router.push()；

active-class属性：
- 设置激活a元素后应用的class，默认是router-link-active

exact-active-class属性：
- 链接精准激活时，应用于渲染的 `<a>` 的 class，默认是router-link-exact-active

## 路由懒加载

当打包构建应用时，JavaScript 包会变得非常大，影响页面加载，如果我们能把不同路由对应的组件分割成不同的代码块，然后当路由被访问的时候才加载对应组件，这样就会更加高效，也可以提高首屏的渲染效率；

这里还是我们前面讲到过的webpack的分包知识，而Vue Router默认就支持动态来导入组件：
因为component可以传入一个组件，也可以接收一个函数，该函数需要返回一个Promise，而import函数就是返回一个Promise；

```js
// 路由的懒加载
const Home = () => import("../Views/Home.vue")
const About = () => import("../Views/About.vue")

// 也可以这样写

const routes = [
    { path: "/home", component: () => import("../Views/Home.vue") },
    { path: "/about", component: () => import("../Views/About.vue") },
]

```

## 动态路由和路由嵌套

### 动态路由基本匹配

渲染用户id

Vue Router中，我们可以在路径中使用一个动态字段来实现，我们称之为 **路径参数**；

```js
{
	path: '/user/:id',
	component: () => import('../pages/User.vue')
}
```

在router/link中实现跳转

```html
<router-link to="/user/123">用户123</router-link>
```

### 获取动态路由的值

在template中，直接通过 `$route.params` 获取值；是route，不是router，router是大对象，route是小对象

在created中，通过 `this.$route.params` 获取值；

在setup中，我们要使用 vue-router库给我们提供的一个hook useRoute；该Hook会返回一个Route对象，对象中保存着当前路由相关的值；

```js
import { useRoute } from 'vue-router'

route = useRoute()
```

**如何在跳转的时候同时获取到跳转之前和跳转之后的值动态路由的值？**

使用`onBeforeRouteUpdate`

```js
  import { useRoute, onBeforeRouteUpdate } from 'vue-router'
  
  // 获取route跳转id
  onBeforeRouteUpdate((to, from) => {
    console.log("from:", from.params.id)
    console.log("to:", to.params.id)
  })
```

### NotFound

对于哪些没有匹配到的路由，我们通常会匹配到固定的某个页面，比如NotFound的错误页面中，这个时候我们可编写一个动态路由用于匹配所有的页面；

在路由表的最后添加

```js
{
  path: "/:pathMatch(.*)*",
  component: () => import("../Views/NotFound.vue")
}
```

表示当匹配以上匹配不到的所有url

```ad-note
注意：我在/:pathMatch(.*)后面又加了一个 *；
它们的区别在于解析的时候，是否解析 / 
加上会转化为数组，不加就是url格式

![[assets/Pasted image 20230308142319.png]]
```

在404组件中可以通过 `$route.params.pathMatch`获取到传入的参数：

```html
<h2>NotFound: 您当前的路径{{ $route.params.pathMatch }}不正确, 请输入正确的路径!</h2>
```

## 编程式导航

使用函数进行跳转




## 动态管理路由对象




## 路由导航守卫钩子