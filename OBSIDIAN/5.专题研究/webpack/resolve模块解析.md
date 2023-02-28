

resolve用于设置模块如何被解析：
- 在开发中我们会有各种各样的模块依赖，这些模块可能来自于自己编写的代码，也可能来自第三方库；
- resolve可以帮助webpack从每个 require/import 语句中，找到需要引入到合适的模块代码；
- webpack 使用 enhanced-resolve 来解析文件路径；


## webpack能解析三种文件路径

绝对路径
- 由于已经获得文件的绝对路径，因此不需要再做进一步解析。

相对路径
- 在这种情况下，使用 import 或 require 的资源文件所处的目录，被认为是上下文目录；
- 在 import/require 中给定的相对路径，会拼接此上下文路径，来生成模块的绝对路径；

模块路径
- 在 resolve.modules中指定的所有目录检索模块；
- 默认值是 `['node_modules']`，所以默认会从node_modules中查找文件；
- 我们可以通过设置别名的方式来替换初识模块路径，具体后面讲解alias的配置；

## webpack如何确认你写的路径是文件还是文件夹

如果是一个文件：
- 如果文件具有扩展名，则直接打包文件；
- 否则，将使用 resolve.extensions选项作为文件扩展名解析；

如果是一个文件夹：
- 会在文件夹中根据 resolve.mainFiles配置选项中指定的文件顺序查找；
- resolve.mainFiles的默认值是 ['index']；
- 再根据 resolve.extensions来解析扩展名；


## extensions和alias配置

extensions是解析到文件时自动添加扩展名：
- 默认值是 `['.wasm', '.mjs', '.js', '.json']`
- 所以如果我们代码中想要添加加载 .vue 或者 jsx 或者 ts 等文件时，我们必须自己写上扩展名；

另一个非常好用的功能是配置别名alias：
- 特别是当我们项目的目录结构比较深的时候，或者一个文件的路径可能需要 ../../../这种路径片段；
- 我们可以给某些常见的路径起一个别名；

```js
  resolve: {
    extensions: ['.js', '.json', '.jsx', '.vue', '.tx', '.tsx'],
    alias: {
      '@':path.resolve(__dirname, "./src"),
    }
  },
```

![[assets/Pasted image 20230228153258.png]]

