## Webpack搭建本地服务器

目的：
- 我们希望可以做到，当文件发生变化时，可以自动的完成 编译 和 展示；
- 我们希望在不适用live-server的情况下，可以具备live reloading（实时重新加载）的功能；

webpack提供的方法：
- webpack watch mode；
- webpack-dev-server（常用）；
- webpack-dev-middleware；

安装webpack-dev-server

```bash
npm install webpack-dev-server -D
```

打包好的东西不会放在磁盘中，不会写文件，而是直接放在内存中。



### 开启本地服务器

命令行为 `webpack serve`

在package.json中添加相关启动命令

![[assets/Pasted image 20230228183547.png]]

启动成功

![[assets/Pasted image 20230228183633.png]]

报错，要设置mode

![[assets/Pasted image 20230228183727.png]]

在config文件中设置mode

![[assets/Pasted image 20230228183907.png]]

再次启动，成功

![[assets/Pasted image 20230228183851.png]]


### HMR热模块替换

什么是HMR呢？
- HMR的全称是Hot Module Replacement，翻译为模块热替换；
- 模块热替换是指在 应用程序运行过程中，替换、添加、删除模块，而无需重新刷新整个页面；

HMR通过如下几种方式，来提高开发的速度：
- 不重新加载整个页面，这样可以保留某些应用程序的状态不丢失；
- 只更新需要变化的内容，节省开发的时间；
- 修改了css、js源代码，会立即在浏览器更新，相当于直接在浏览器的devtools中直接修改样式；

如何使用HMR呢？
- 默认情况下，webpack-dev-server已经支持HMR，我们只需要开启即可（默认已经开启）；
- 在不开启HMR的情况下，当我们修改了源代码之后，整个页面会自动刷新，使用的是live reloading；

![[assets/Pasted image 20230228185058.png]]

hot设置为true即可

![[assets/Pasted image 20230228185129.png]]

有一个问题：在开发其他项目时，我们是否需要经常手动去写入 module.hot.accpet相关的API呢？
- 比如开发Vue、React项目，我们修改了组件，希望进行热更新，这个时候应该如何去操作呢？

事实上社区已经针对这些有很成熟的解决方案了：
- 比如vue开发中，我们使用vue-loader，此loader支持vue组件的HMR，提供开箱即用的体验；
- 比如react开发中，有React Hot Loader，实时调整react组件（目前React官方已经弃用了，改成使用react-refresh）；

### devServer配置

host默认是localhost，如果希望其他地方也可以访问，可以设置为 0.0.0.0

port设置监听的端口，默认情况下是8080

open是否打开浏览器：
- 默认值是false，设置为true会打开浏览器；
- 也可以设置为类似于 Google Chrome等值；

compress是否为静态文件开启gzip compression：
- 默认值是false，可以设置为true；

![[assets/Pasted image 20230228185320.png]]

### 开发和生产环境



