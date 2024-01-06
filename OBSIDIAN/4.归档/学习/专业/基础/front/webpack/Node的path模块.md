## Node的path模块

path模块用于对路径和文件进行处理，提供了很多好用的方法。

我们知道在Mac OS、Linux和window上的路径是不一样的：window上会使用 \或者 \\ 来作为文件路径的分隔符，当然目前也支持 /；在Mac OS、Linux的Unix操作系统上使用 / 来作为文件路径的分隔符；

那么如果我们在window上使用 \ 来作为分隔符开发了一个应用程序，要部署到Linux上面应该怎么办呢，显示路径会出现一些问题，所以为了屏蔽他们之间的差异，在开发中对于路径的操作我们可以使用 path 模块；

==获取路径中的信息==

dirname：获取文件的父文件夹；
basename：获取文件名；
extname：获取文件扩展名

```js
const path = require('path')

const filepath = 'C://dir1/dir2/dir3'

// 从路径中获取信息
console.log(path.extname(filepath))

// 获取文件名
console.log(path.basename(filepath))

// 获取文件夹所在路径
console.log(path.dirname(filepath))
```


==路径的拼接==

如果我们希望将多个路径进行拼接，但是不同的操作系统可能使用的是不同的分隔符；
这个时候我们可以使用path.join函数；

```js
// 将多个路径拼接在一起
const path1 = '/aaa/bbb'
const path2 = '../nodejs'
console.log(path.join(path1, path2))
```

==绝对路径的拼接==

path.resolve() 方法会把一个路径或路径片段的序列解析为一个绝对路径；

给定的路径的序列是从右往左被处理的，后面每个 path 被依次解析，直到构造完成一个绝对路径；如果在处理完所有给定path的段之后，还没有生成绝对路径，则使用当前工作目录；生成的路径被规范化并删除尾部斜杠，零长度path段被忽略；如果没有path传递段，path.resolve()将返回当前工作目录的绝对路径；

```js
const path = require('path')

// 多个路径拼接在一起，最后返回一个绝对路径

// 从后向前查找，直到查找到绝对路径

console.log(path.resolve("./abc/test", "/root/", "/a.txt"))
console.log(path.resolve("./abc/test", "/root/", "a.txt"))
console.log(path.resolve("/abc/test", "root/", "a.txt"))
console.log(path.resolve("./abc/test", "root/", "a.txt"))

```

![[assets/Pasted image 20230228090007.png]]