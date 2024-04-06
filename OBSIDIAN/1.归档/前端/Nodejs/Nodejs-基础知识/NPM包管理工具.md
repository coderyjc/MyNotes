

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



## npm install 

安装npm包分两种情况：

- 全局安装（global install）： npm install webpack -g;
- 项目（局部）安装（local install）： npm install webpack

### 全局安装

- 全局安装是直接将某个包安装到全局：
- 比如全局安装yarn：

```bash
npm install yarn -g
```

但是很多人对全局安装有一些误会：

- 通常使用npm全局安装的包都是一些工具包：yarn、webpack等；
- 并不是类似于 axios、express、koa等库文件；
- ==所以全局安装了之后并不能让我们在所有的项目中使用 axios等库；==

### 局部安装

默认安装开发和生产依赖
```bash
npm install axios
npm i axios
```

开发依赖
```bash
npm install webpack --save-dev
npm install webpack -D
npm i webpack –D
```

根据package.json中的依赖包
```bash
npm install
```

安装之后生成了node_modules目录，关于项目如何从目录中查找文件，可以参考这个[[Node模块化开发#require查找规则]]


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

engines属性
- engines属性用于指定Node和NPM的版本号；
- 在安装的过程中，会先检查对应的引擎版本，如果不符合就会报错；
- 事实上也可以指定所在的操作系统 "os" : [ "darwin", "linux" ]，只是很少用到；

browserslist属性
- 用于配置打包后的JavaScript浏览器的兼容情况，参考；
- 否则我们需要手动的添加polyfills来让支持某些语法；
- 也就是说它是为webpack等打包工具服务的一个属性（这里不是详细讲解webpack等工具的工作原理，所以不再给出详情）；

### 版本规范

我们会发现安装的依赖版本出现：^2.0.3或~2.0.3，这是什么意思呢？

npm的包通常需要遵从semver版本规范：
- semver：https://semver.org/lang/zh-CN/
- npm semver：https://docs.npmjs.com/misc/semver

semver版本规范是X.Y.Z：
- X主版本号（major）：当你做了不兼容的 API 修改（可能不兼容之前的版本）；
- Y次版本号（minor）：当你做了向下兼容的功能性新增（新功能增加，但是兼容之前的版本）；
- Z修订号（patch）：当你做了向下兼容的问题修正（没有新功能，修复了之前版本的bug）；

做了重大更新的时候彩更新X主版本号


^和~的区别：
- x.y.z：表示一个明确的版本号；
- ^x.y.z：表示x是保持不变的，y和z永远安装最新的版本；
- ~x.y.z：表示x和y保持不变的，z永远安装最新的版本；

### npm install 原理

![[assets/Pasted image 20230227140341.png]]

npm install会检测是有package-lock.json文件：

没有lock文件
1. 分析依赖关系，这是因为我们可能包会依赖其他的包，并且多个包之间会产生相同依赖的情况；
2. 从registry仓库中下载压缩包（如果我们设置了镜像，那么会从镜像服务器下载压缩包）；
3. 获取到压缩包后会对压缩包进行缓存（从npm5开始有的）；
4. 将压缩包解压到项目的node_modules文件夹中（前面我们讲过，require的查找顺序会在该包下面查找）

有lock文件
1. 检测lock中包的版本是否和package.json中一致（会按照semver版本规范检测）；
2. 不一致，那么会重新构建依赖关系，直接会走顶层的流程；
3. 一致的情况下，会去优先查找缓存
4. 没有找到，会从registry仓库下载，直接走顶层流程；
5. 查找到，会获取缓存中的压缩文件，并且将压缩文件解压到node_modules文件夹中；

## package-lock.json


![[assets/Pasted image 20230227140712.png]]

 package-lock.json文件解析：
- name：项目的名称；
- version：项目的版本；
- lockfileVersion：lock文件的版本；
- requires：使用requires来跟踪模块的依赖关系；
- dependencies：项目的依赖

当前项目依赖axios，但是axios依赖follow-redireacts；

axios中的属性如下：
- version表示实际安装的axios的版本；
- resolved用来记录下载的地址
- registry仓库中的位置；
- requires/dependencies记录当前模块的依赖；
- integrity用来从缓存中获取索引，再通过索引去获取压缩包文件；


## npm其他命令

卸载某个依赖包

```bash
npm uninstall package
npm uninstall package --save-dev
npm uninstall package -D
```

强制重新build

```bash
npm rebuild
```

清除缓存

```bash
npm cache clean
```

更多的命令，可以根据需要查阅官方文档 https://docs.npmjs.com/cli-documentation/cli 


