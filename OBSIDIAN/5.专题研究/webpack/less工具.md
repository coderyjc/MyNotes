## less工具

安装less-loader工具

```bash
npm install less-loader -D
```


**css/title.less**

```less
@fontsize: 50px;
@fontColor: blue;

.title{
  font-size: @fontsize;
  color: @fontColor;
}
```

**add_div.js**

```js
import "../css/div.css"
import "../css/title.less"

const divEl = document.createElement('div')
divEl.textContent = 'Hello World!'
divEl.classList.add('content')
document.body.append(divEl)

// 新增
const titleEl = document.createElement('div')
titleEl.textContent = 'TITLE'
titleEl.classList.add('title')
document.body.append(titleEl)
```

```ad-warning
一定不要忘了引入less文件
```

**config.js**

```js
const path = require('path')

module.exports = {
  // 打包的入口
  entry: './src/main.js',
  // 输出设置
  output:{
    filename: 'bundle.js',
    // path必须传入一个绝对路径，我们把目标路径和绝对路径拼接
    path: path.resolve(__dirname, "./build")
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        // 多个loader不需要其他属性的时候可以直接写loader字符串数组的形式
        use: ['style-loader', 'css-loader']
      },
      {
        test: /\.less$/,
        use: ['style-loader', 'css-loader', 'less-loader']
      }
    ]
  }
}
```

成果如图：

![[assets/Pasted image 20230228104845.png]]