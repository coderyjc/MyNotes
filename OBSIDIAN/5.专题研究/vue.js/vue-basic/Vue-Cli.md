### 安装和使用

全局安装

```bash
npm install @vue/cli -g
```

升级vue-cli

```bash
npm update @vue/cli -g
```

通过命令创建

```bash
Vue create [name]
```


### 创建项目的过程-Vue-Cli

![[assets/Pasted image 20230308091433.png]]

![[assets/Pasted image 20230308091436.png]]

![[assets/Pasted image 20230308091442.png]]

![[assets/Pasted image 20230308091445.png]]

==项目的目录结构==

![[assets/Pasted image 20230308091505.png]]

![[assets/Pasted image 20230308091509.png]]


### 创建项目的过程-Npm

vue-cli创建的项目默认是使用webpack进行管理的，npm创建的项目默认使用vite进行管理。

```bash
npm init vue@latest
```

创建过程

```bash
PS D:\code\github\workspace\vue> npm init vue@latest
Need to install the following packages:
  create-vue@3.6.1
Ok to proceed? (y) y

Vue.js - The Progressive JavaScript Framework

√ Project name: ... vue-project
√ Add TypeScript? ... No / Yes
√ Add JSX Support? ... No / Yes
√ Add Vue Router for Single Page Application development? ... No / Yes
√ Add Pinia for state management? ... No / Yes
√ Add Vitest for Unit Testing? ... No / Yes
√ Add an End-to-End Testing Solution? » No
√ Add ESLint for code quality? ... No / Yes

Scaffolding project in D:\code\github\workspace\vue\vue-project...

Done. Now run:

  cd vue-project
  npm install
  npm run dev
```

![[assets/Pasted image 20230308105017.png]]

创建成功的项目默认通过vite打包。



### 配置webpack属性

在`vue.config.js`中配置相关属性，例如配置别名的时候：

```js
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    resolve: {
      // 配置路径别名
      // @是已经配置好的路径别名: 对应的是src路径
      alias: {
        "utils": "@/utils" 
      }
    }
  }
})

```

在导出的模块中配置`configWebpack`属性，其中`@`是vue-cli内部已经配置好的路径别名，指`src`

### jsconfig.json

作用: 给VSCode来进行读取, VSCode在读取到其中的内容时, 给我们的代码更加友好的提示.

在我们自定义路径的别名之后，vscode不认识我们的别名，导致我们在写路径的时候vscode不会给出提示。

在jsconfig中配置了相关信息之后，ide会根据我们配置的路径自动寻找文件给出提示

![[assets/Pasted image 20230308101124.png]]

如图，我们配置了`utils`别名，当把别名配置到jsconfig中的时候，ide就有了utils目录下提示了。

### 引入的vue的版本

> 来自：1004--day57_jsconfig-Vue版本-组件间通信-插槽_02_(了解)Vue不同版本对template的处理

默认vue版本: runtime, vue-loader完成template的编译过程

vue.esm-bundler: runtime + compile, 对template进行编译

### 补充

**单文件Vue style是有自己的作用域**

style -> scoped

```html
<style scoped>

</style>
```

**vite创建一个Vue项目**

