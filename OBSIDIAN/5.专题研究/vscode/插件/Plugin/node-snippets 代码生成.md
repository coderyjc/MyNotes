---
type: 代码生成
name: node-snippets 代码片段
ootb: 1
recommendation: 8
create_date: 2022-01-26
---

![[assets/Pasted image 20220126215503.png]]

# node-snippets 代码片段

https://marketplace.visualstudio.com/items?itemName=chris-noring.node-snippets

## 特点

node.js 的代码生成


## 使用

在js文件中输入以下文字
-   `node-express`, 创建一个express服务器
    
-   `node-express-get`, 创建 GET 路由
    
-   `node-express-get-params`, 创建一个 GET 路由并展示如何访问参数
    
-   `node-express-post`, 创建一个 POST 路由
    
-   `node-express-post-params`, 创建一个 POST 路由并显示如何访问上下文
    
-   `node-express-post-params-alt`，创建 POST 路由，显示如何访问上下文，适用于 express 4.16 及更高版本
    
-   `node-express-put-params`，创建一个 PUT 路由，展示如何访问 body。
    
-   `node-express-delete-params`，创建一个 DELETE 路由，展示如何访问路由参数。
    
-   `node-express-query-params`，创建一个 POST 路由，展示如何访问查询参数。
    
-   `node-express-middleware-logger`, 创建一个示例中间件
    
-   `node-express-middleware-error`, 创建一个错误处理中间件
    
-   `node-http-server`, 创建一个简单的 HTTP 服务器
    
-   `node-file-read-sync`, 同步读取文件
    
-   `node-file-read-async`, 异步读取文件，带有回调
    
-   `node-event-emitter`，创建一个事件发射器，发出事件并显示订阅所述事件
    
-   `node-promise-create`, 创建一个 Promise
    
-   `node-promise-shorthand`, 使用静态方法创建一个 Promises`resolve()`和`reject()`
    
-   `node-promise-all``Promise.all([])`, 使用方法解析 Promise 列表
    
-   `node-async-await`, 使用异步/等待
    
-   `node-express-schema-validation`，为 express 添加模式验证，
    
-   `node-regex-test-digits`, 调用`test()`测试字符串是否与数字上的正则表达式匹配的方法。
    
-   `node-regex-test-word`, 调用`test()`测试字符串是否与单词边界上的正则表达式匹配的方法。
    
-   `node-regex-match`, 调用`match()`正则表达式的方法来查找文件扩展名
    
-   `node-regex-match-named-group`, 调用`match()`正则表达式的方法并将其放在一个名为`exteension`.
    
-   `node-http-quark`[，使用框架quarkhttp](https://www.npmjs.com/package/quarkhttp)创建一个 HTTP 应用程序，
    
-   `node-http-quark-get`[，向您的quarkhttp](https://www.npmjs.com/package/quarkhttp)应用程序添加 GET 路由
    
-   `node-http-quark-post`[，向您的quarkhttp](https://www.npmjs.com/package/quarkhttp)应用程序添加 POST 路由
    
-   `node-http-quark-put`, 将 PUT 路由添加到您的[quarkhttp](https://www.npmjs.com/package/quarkhttp)应用程序
    
-   `node-http-quark-middleware`, 将中间件添加到您的[quarkhttp](https://www.npmjs.com/package/quarkhttp)应用程序
    
-   `node-jest-suite`, 添加一个测试套件
    
-   `node-jest-test`, 添加一个测试
    
-   `node-jest-test-expect`, 添加一个带有期望的测试
    
-   `node-jest-expect`, 添加一个期望, 使用 `toBe()`
    
-   `node-jest-expect-to-equal`, 添加期望, 使用 `toEqual()`
    
-   `node-jest-test-expect-to-equal`, 添加一个带有期望的测试，使用 `toEqual()`
    
-   `node-jest-expect-to-throw`, 添加一个期望, 使用 `toThrow()`
    
-   `node-jest-test-expect-to-throw`, 添加一个带有期望的测试, 使用`toThrow()`,
    
-   `node-jest-test-beforeAll`, 添加一个`beforeAll()`, 此方法在所有测试之前运行
    
-   `node-jest-test-afterAll`, 添加一个`afterAll()`, 此方法在所有测试后运行
    
-   `node-supertest-init`，为 supertest 和您将要测试的应用程序添加初始导入。我假设您要测试的应用程序看起来像这样：
    
    ```javascript
    //  app.js
    const express = require('express')
    const app = express();
    // your route definitions
    module.exports = app;
    ```
    
    并且您的文件结构如下所示：
    
    ```bash
    -| app.js    // this is where the web app goes
    -| __tests__/
    ---| app.js  // this where the tests goes
    ```
    
-   `node-supertest-beforeall`, 配置 supertest 以使用 app 实例，这是初始化 supertest 的必要步骤
    
-   `node-supertest-aftereall`, 确保 web 应用程序在测试运行后关闭，这是一个必要的步骤。
    
-   `node-supertest-testget`，一个超测测试GET路由的例子
    
-   `node-supertest-testgetwithparam`，一个超测测试带有路由参数的 GET 路由的示例
    
-   `node-supertest-testpost`，一个使用有效负载测试 POST 路由的超测试示例