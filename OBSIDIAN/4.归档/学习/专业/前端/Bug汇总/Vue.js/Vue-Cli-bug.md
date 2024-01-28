---
type: DeBug
skill: Vue-Cli
create_date: 2022-01-31
---

#前端/Vue #前端/前端框架 

# Vue-Cli-bug


>在构建 vue-admin-template 的时候模块加载异常


```info
These dependencies were not found:

-   codemirror/lib/codemirror.css in ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/components/MarkdownEditor/index.vue?vue&type=script&lang=js&
-   tui-editor in ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/components/MarkdownEditor/index.vue?vue&type=script&lang=js&
-   tui-editor/dist/tui-editor-contents.css in ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/components/MarkdownEditor/index.vue?vue&type=script&lang=js&
-   tui-editor/dist/tui-editor.css in ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/components/MarkdownEditor/index.vue?vue&type=script&lang=js&

```

解决方案：

手动安装了两个模块之后项目能打开了

npm install —save codemirror

npm install —save tui-editor

然后项目能跑了，但是打开之后是空白页

报错如下：

![[../../../数据库/Redis/Bug汇总/assets/Pasted image 20220131013537.png]]

修复方法：

1.  停掉服务
2.  删除所有依赖的modules
3.  在目录下运行 npm install 重新安装

成功。

>vue-router中动态添加的路由跳转到空白页

如果不能直接用addRoute添加的话应该先在router.option中添加，然后再用addRouter动态添加路由表。

```jsx
await store.dispatch('user/getInfo')
const roles = store.getters.roles
console.log(roles)
store.dispatch('GenerateRoutes', { roles }).then(() => { // 生成可访问的路由表
  const routersToAppend = store.getters.addRouters
  routersToAppend.forEach(item => {
    router.options.routes.push(item)
  })
  router.addRoutes(routersToAppend) // 动态添加可访问路由表
  // hack方法 确保addRoutes已完成
  next({ ...to, replace: true })
})
```

>控制台报错 Duplicate keys detected 并且可以通过vue-router进后台的页面，但是刷新的时候是空白页, 并且每次刷新的时候 都会报三个错：

```jsx
Error in beforeCreate hook: "InternalError: too much recursion"
Error in render: "TypeError: route is undefined"
route is undefined
```

经过检查是 router/index.js 中 404 页面 重定义了。

虽说 404 页面是必须在最后加载的，但是 constantRouterMap 和 asyncRouterMap 中只有一个中定义了就行了, constantRouterMap可以不要。

vue中标签写 `<view>` 不会渲染文字，而是应该写 `<div>`

> We're sorry but readingnotes doesn't work properly without JavaScript enabled. Please enable it to continue.

-   可能是科学上网了
-  Axios 的 BASE_URL 不对