# Vue-Cli

首先应该下载[[Node.js]]

1. 配置环境变量和相关镜像

```markdown
## 配置Windows环境变量
NODE_HOME = nodejs 安装目录
PATH = ...; %NODE_HOMT%

## 验证是否安装完成
> node -v

## 配置淘宝镜像
> npm config set registry <https://registry.npm.taobao.org>

验证淘宝镜像配置成功：

> npm config get registry
> <https://registry.npm.taobao.org>

## 配置npm下载依赖配置中心（本地仓库）

> npm config set cache "V:\\Environment\\npm-repo"
> npm config set prefix "V:\\Environment\\npm-repo"
```

2. 安装脚手架

```markdown
> npm install -g vue-cli
```

3. 第一个脚手架项目

```bash
> vue init webpack 项目名

? Project name hello
? Project description A Vue.js project
? Author jancoyan <302848188@qq.com>
? Vue build standalone
? Install vue-router? Yes
? Use ESLint to lint your code? No
? Set up unit tests No
? Setup e2e tests with Nightwatch? No
? Should we run `npm install` for you after the project has been created? (recommended) npm

```

4. 如何运行

```
先进入到项目的根目录中

> npm start
```



目录结构解释：

```
he11o--------------------—->项目名
    -build----------------->用来使用webpack打包使用build依赖
    -config---------------->用来做整个项目配置目录
    -node_modules---------->用来管理项目中使用依赖
    -src------------------->用来书写vue的源代码[重点]
        assets—------------>用来存放静态资源[重点]
        components--------->用来书写Vue组件[重点]
        router-----------—->用来配置项目中路由[重点]
        App.vue----------—->项目中根组件[重点]
        main.js------------>项目中主入口[重点]
    -static-—-------------->其它静态
    -.babelrc-—------------>将es6语法转为es5运行
    -.editorconfig--------->项目编辑配置
    -.gitignore--—--------->git版本控制忽略文件
    -.postcssrc.js--------->源码相关js
    -index.html------------>项目主页
    -package.json---------->类似与pom.xml依赖管理jquery 不建议手动修改
    -package-lock.json----->对package.json加锁
    -README.md------------->项目说明文件
```



项目的开发方式：一切皆组件

