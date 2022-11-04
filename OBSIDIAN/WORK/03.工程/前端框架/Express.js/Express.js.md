## 初步使用

```js
// express框架，用于搭建后端服务器
const express = require('express')
// express用于返回静态目录的文件
const exStatic = require("express-static")
// js中调用shell的依赖
const shell = require('shelljs')
// 将请求消息体规格化成json文件
const bodyParser = require('body-parser')

// 创建应用实例
var app = express()
// 过滤所有的请求，转化为json
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: true}))

// 映射根目录
app.get('/', function (req, res) {
		// 发送静态HTML文件
        res.sendFile('/www/wwwroot/goodnotes/index.html')
})

// 映射URL
app.get('/goodnotes', function (req, res) {
        console.log('getPicture--', req.query.img)
	    // 请求状态
        res.status(200);
        var file = '/www/wwwroot/goodnotes/imgs/' + req.query.img
        res.sendFile(file)
})

// 映射生成URL
app.post('/generate', function (req, res) {
        console.log('gengrate--', req.body.cmd)
        let cmd = 'python3 DIY.py ' + req.body.cmd
        // shell js 执行命令行
        shell.exec(cmd)
        res.status(200)
        res.end()
})

// 启动服务
var server = app.listen(8002)
```

