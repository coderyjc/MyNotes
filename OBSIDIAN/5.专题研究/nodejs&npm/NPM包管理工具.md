

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

可以做到比较方便的引入

## package.json 配置文件

这个配置文件会记录着你项目的名称、版本号、项目描述等，也会记录着你项目所依赖的其他库的信息和依赖库的版本号。

如何创建这个配置文件：
- 方式一：手动从零创建项目，`npm init –y`（所有信息都是默认的）
	- `npm init` 也可以创建项目，但是要自己输入一些项目相关的参数
- 方式二：通过脚手架创建项目，脚手架会帮助我们生成package.json，并且里面有相关的配置

### 常见字段

必须填写的属性：name、version
- name是项目的名称；
- version是当前项目的版本号；
- description是描述信息，很多时候是作为项目的基本描述；
- author是作者相关信息（发布时用到）；
- license是开源协议（发布时用到）；

private属性：
- private属性记录当前的项目是否是私有的，当值为true时，npm是不能发布它的，这是防止私有项目或模块发布出去的方式；

main属性用来设置程序的入口：
- 比如我们使用axios模块 const axios = require('axios');
- 如果有main属性，实际上是找到对应的main属性查找文件的；

下图，这个属性规定了从index.js查找文件

![[assets/Pasted image 20230227131644.png]]


==scripts==属性：
scripts属性用于配置一些脚本命令，以键值对的形式存在，配置后我们可以通过 npm run 命令的key来执行这个命令；

npm start和npm run start的区别是什么？
- 它们是等价的；
- 对于常用的 start、 test、stop、restart可以省略掉run直接通过 npm start等方式运行；
- 平时用的时候最好全都加上run

> 比如`npm run dev`来启动vue-element-admin，就是在scripts属性中有一个"dev":"具体命令"

dependencies属性
dependencies属性是指定无论开发环境还是生成环境都需要依赖的包，通常是我们项目实际开发用到的一些库模块vue、vuex、vue-router、react、react-dom、axios等等；
与之对应的是devDependencies；使用`npm install`自动安装依赖的库

devDependencies属性
一些包在生产环境是不需要的，比如webpack、babel等，这个时候我们会通过 npm install webpack --save-dev，将它安装到devDependencies属性中；使用`npm install xxx --save-dev`来安装只有在开发环境使用的库

peerDependencies属性
还有一种项目依赖关系是对等依赖，也就是你依赖的一个包，它必须是以另外一个宿主包为前提的，比如element-plus是依赖于vue3的，ant design是依赖于react、react-dom；

