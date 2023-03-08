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

hash的优势就是兼容性更好，在老版IE中都可以运行，但是缺陷是有一个#，显得不像一个真实的路径。

![[assets/Pasted image 20230308132326.png]]

history接口是HTML5新增的, 它有六种模式改变URL而不刷新页面：
- replaceState：替换原来的路径；
- pushState：使用新的路径；
- popState：路径的回退；
- go：向前或向后改变路径；
- forward：向前改变路径；
- back：向后改变路径

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

使用组件`router-link`





## 路由懒加载


## 动态路由和路由嵌套


## 编程式导航


## 动态管理路由对象


## 路有导航守卫钩子