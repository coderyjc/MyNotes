

Node Package Manager **Node包管理工具**

我们发布自己的包其实是发布到registry上面的，当我们安装一个包时其实是从registry上面下载的包。

## StartUp

新建文件夹

假如我们要使用dayjs，那么我们可以使用`npm install dayjs`来安装dayjs

安装成功后的文件夹结构：

多了一个文件夹和两个文件

![[assets/Pasted image 20230227124737.png]]

然后在main.js中：

```js
const dayjs = require('dayjs')
console.log(dayjs)
```

输出为：

![[assets/Pasted image 20230227124828.png]]


