---
sidebar: auto
sidebarDepth: 3
---

# HTML

> 最权威的官方文档: https://w3.org

## HTML 超文本标记语言

- 纯文本编辑器中的内容都是纯文本,网页都是用纯文本写的
- 纯文本中只能保存文本内容. 图片, 音频, 视频, 音频等格式化的内容都不能设置
- 超 : 超链接
- 标记 :
  - 使用方式 : <标签名> 内容 </标签名>
    - 一般成对出现
- 负责网页三要素中的**结构**

单标签元素建议写法: `<img>` 而不是 `<img />` 

元素的结构: `<开始标签 属性1 属性2 .. >元素包含的内容 </结束标签>`

> 文档声明 

HTML最上面的一段文本就是`文档类型声明`, 用于声明文档类型

文档声明不是HTML元素

`<!DOCTYPE html>`

声明HTML版本是HTML5, 让浏览器用HTML5的标准解析里面的内容, 必须在HTML文档的最前面, 不能省略

那么早起的版本如何声明呢?(了解即可)

比较复杂, H5的比较严格

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```

### 浏览器

核心: 浏览器**内核(渲染引擎 Rendering Engine)**

内核的作用: 解析网页语法并渲染(显示)网页

不同的浏览器内核: 

- Trident(三叉戟): IE\ 360\ 搜狗\ 百度\ UC浏览器
- Gecko(壁虎): Mozilla Firefox
- presto(急板乐曲) -> Blink: Opera
- Webkit: Safari\ 360\ 搜狗\ 移动端浏览器
- Webkit -> Blink(目前最快): Chrome, Edge

![](assets/Pasted%20image%2020220902223843.png)

不同的浏览器内核的**解析渲染规则不同**, 同一个网页再不同的内核的浏览器的渲染效果可能不同

### 什么是HTML?

什么是标记语言?

- 由标记组成
- 对某些内容进行特殊的标记, 以供其他的解释器进行识别和处理
- 由标签和内容组成的部分成为元素

**HTML不是编程语言, 是计算机语言.**

什么是超文本?

- 不仅可以插入普通的文本(Text), 还可以插入其他元素, 图片, 音频, 视频等
- 还可以插入超链接, 从一个网页跳转到另一个链接

.htm和.html的区别

- 历史遗留问题: Win95/Win98的文件扩展名不能超过3字符, 因此是.htm
- 因此现在一律使用.html



## 基本结构

- 有且仅有有一个根标签 < html > < /html >, 网页的 **所有内容** 都会写在html标签中
- 根标签内有两个子标签 < head > < /head > < body > < /body >
- < head >标签中还有子标签< title >
- < head>中的内容**不会在网页中显示**, 他是写给浏览器看的,浏览器通过判断head中的信息来判断如何解析网页
- < body >表示网页的主体, 页面中所有可见的内容都要写到< body >标签里
- < title >中的内容会显示在网页的标题栏, 搜索引擎在检索页面的时候首先检索title里面的内容, 他是网页中对于搜索引擎来说最重要的内容, 会影响<ins>网页在搜索引擎中的排名</ins>

即:

```HTML
<html>
   <head>
      <title>
      </title>
   </head>

   <body>
   </body>
</html>
```



单标签元素建议写法: `<img>` 而不是 `<img />` 

元素的结构: `<开始标签 属性1 属性2 .. >元素包含的内容 </结束标签>`

> 文档声明 

HTML最上面的一段文本就是`文档类型声明`, 用于声明文档类型

文档声明不是HTML元素

`<!DOCTYPE html>`

声明HTML版本是HTML5, 让浏览器用HTML5的标准解析里面的内容, 必须在HTML文档的最前面, 不能省略

那么早起的版本如何声明呢?(了解即可)

比较复杂, H5的比较严格

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```



## 注释

基本语法:

```html
<!-- 注释内容 -->

<!--
   注释内容
-->
```

- 注释中的内容**不会在页面中显示**, 但是可以在源码中查看

## 标签属性

字体属性设置 < font > < /font >

属性设置 :

- 可以通过属性来设置标签如何处理标签中的内容
- 只能在**开始标签**中添加
- 实际上就是一个*名值对*的结构
- 属性名 = "属性值"
- 一个标签中可以有多个属性,但在使用的时候应该用**空格**隔开

```html
<h1>
<!-- 字体 颜色 = "颜色值" -->
   这是我的<font color = "red">第一个网页</font>
<!--这只是个例子, 在实际开发中不赞成使用, 请用CSS的样式取代他-->
</h1>
```

## 文档声明

**写网页的时候一定把声明写在最上面**如果不写, 浏览器解析页面的时候可能进入怪异模式无法正常显示

怪异模式: 为了兼容一些留的页面, 浏览器中设置了两种解析模式 标准模式和怪异模式, 怪异模式在解析网页的时候回产生一些不可预期的行为, 所以我们应该避免怪异模式的出现, 写上<span style = "color:red">doctype</span>

HTML的发展:

- 1993.6 第一个版本, 起初是一个企业内部使用的
- 1995.11 HTML 2.0
- 1997.1 HTML3.2 (W3C推荐)
- 1999.12 HTML4.01 (W3C推荐, 仍在使用)
- 2000年底 XHTML1.0 (W3C推荐, 仍在使用)
- 2014.10 HTML5 (W3C推荐, 仍在使用)

在网页最上面添加一个doctype来告诉浏览器我们是什么版本

HTML5的文档声明

```html
<!doctype html>
```

一个最基本的HTML页面

```html
<!doctype html>
<html>
   <head>
      <meta charset = "UTF-8" />
      <title> 网页标题 </title>
   </head>
   <body>
   </body>
</html>
```

## 乱码问题和字符实体

- 字符集:编码和解码所采用的规则
- 常见的字符集 :
  - ASCII(美国)
  - ISO-8859-1(欧洲)
  - GBK(中国)
  - GB2312(中文系统默认编码)
  - UTF-8(支持地球上所有文字, 也叫Unicode)
  - ANSI (自动以系统语言来保存编码)
- 在中文系统的浏览器中, 默认使用GB2312进行编码

在head标签中告诉浏览器用utf-8解析

meta标签: 用来设置网页的一些元数据, 比如网页的字符集, 关键字, 简介
meta是个自结束标签, 编写自结束标签的时候, 可以在开始标签中添加一个 /

```html
<html>
   <head>
      <meta charset = "UTF-8" />
   </head>
</html>
```

**字符实体**

在HTMl中, 一些如 < > 之类的特殊字符是不能直接使用的, 需要使用一些特殊的符号来表示这些特殊字符, 这些特殊符号叫实体(转义字符), 浏览器解析到实体时, 会将实体自动转换为对应的字符

语法:  &名字;

如:

- &lt; <小于
- &gt; >大于
- &nbsp; 空格
- &copy; 版权符号
- 更多内容查看 : W3school离线手册

```html
        <p>
            床前&nbsp;&nbsp;&nbsp;明月光<hr />
        </p>
```

## 一些常用的标签

### html标签和head标签

**html**

文档的根, 顶级元素, 根元素

W3C标准建议为html元素增加一个`lang`属性, 作用: 
- 帮助语音合成工具确定要使用的发音
- 帮助翻译工具确定要使用的翻译规则

`<html lang="zh-CN"> <html lang="zh">` 中文 CN表示简体中文

`<html lang="en">` 英文

**head**

规定文档相关的配置信息(元数据), 标题, 引用的文档样式和脚本等

元数据: 描述数据的数据, 在这里可以理解为`整个页面的配置`

meta元素: 

- 设计网页的字符编码, 一般使用utf-8 (UTF-8)

常用元素: p h img a div span



### 标题标签

- 在HTML中一共有六级标签 h1 ~ h6
- 区别: 浏览器只是给这些元素添加了不同的**CSS样式**而已.h元素和p元素本质上没有区别, 只是在css上不一样而已
- 在显示效果上, h1最大, h2最小, 但是我们**并不关心**文字的大小
- 我们关心的是标签的语义, 我们使用的标签都是语义化标签
- 六级标题中, h1最重要, 表示一个网页中的主要内容 h2 ~ h6 重要性依次降低
- 对于搜索引擎来说, h1 的 重要性仅次于 title, 搜索引擎检查完title, 会立即查看 h1
- h1 非常重要, 他会<span style = "color:red">影响页面在搜索引擎中的排名</span>
- 页面中只能写一个 h1
- 一般的页面标题中只有 h1, h2, h3 , 以后的<u>基本不使用</u>

```html
<body>
	<h1>一级标题</h1>
    <h2>二级标题</h2>
    ......
    <h6>六级标题</h6>
</body>
```

### 段落标签

- 用来表示内容中的一个**自然段**
- p标签表示一个段落
- p标签中的内容会**独占一行**
- p元素中不可以包含其他任何块元素

```html
<body>
        <p>
            内容
        </p>
</body>

```

### 换行标签

- 在html中字符之间写再多的空格或者换行, 浏览器也会当成一个空格
- 可以使用br / 自结束标签来换行

```html
        <p>
            床前明月光<br />
            疑是地上霜<br />
            夜来风雨声<br />
            花落知多少<br />
        </p>

```

### 直线标签

- hr标签也是一个自结束标签

```html
        <p>
            床前明月光<hr />
            疑是地上霜<hr />
            夜来风雨声<hr />
            花落知多少<hr />
        </p>
```

### 居中标签

<span style = "color:red">不推荐使用</span> 属于CSS的内容
center标签中的内容会自动在页面上居中显示

```html
    <body>
        <center>床前明月光</center>
        <center>化作相思泪</center>
    </body>

```

### 图片标签

使用img标签来向网页引入外部图片

img标签也是一个自结束标签

img是一个**可替换元素(replacement element)**

img在没有设置src 的时候是什么都不显示的只占据一点位置, 当设置了src 的时候, 浏览器就会从src获取图片把占据的一点位置替换

属性:

- src : 设置一个外部图片的路径
  - 相对路径 : 相对于本资源所在位置的路径，一般用相对路径
  - 绝对路径 : 资源本身在资源管理器中的位置
  - 对于网页来说(Win, Mac, Linux), 路径分隔符一律是`/`

- alt : 设置图片描述 , 只有在图片不能显示的时候才能显示
  - 主要作用 : 搜索引擎可以通过alt属性来识别不同的图片
  - 如果不写alt属性, 则搜索引擎不会对img中的图片进行收录
  - 加载失败的时候显示的文字
  - 屏幕阅读器会将这些描述读给需要使用阅读器的使用者听(障碍人士), 让他们知道这张图片的含义.
- width : 可以用来修改图片的宽度, 一般以px作为单位
- height : 可以用来修改图片的高度. 单位也是px
  - 如果调整了一个边的长度, 则另一个边的长度也按比例收缩
  - 除非指定了两个, 则按照指定的来
  - 一般开发中, 除了自适应页面, **不建议**设置 width 和 height

图片的格式:

- JPEG(JPG)
  - 支持的颜色比较多, 可以压缩, 但是不支持透明
  - 一般使用JPEG保存内容丰富的图片
- GIF
  - 支持的颜色少, 只支持简单的直线透明, 支持动态图
  - 图片颜色单一或者动态图的时候使用GIF
- PNG
  - PNG支持的颜色多, 且支持复杂的透明
  - 可以用来显示颜色更复杂的图片
  - 实际开发中用的比较多

图片的使用原则:

- 效果不一致, 使用效果好的
- 效果一致, 使用小的

```html
    <body>
        <img src = "D:\VS2019.C++code\VS 背景图\ia_10016.jpeg" alt = "This is a wallpaper!" width="960px" height="540px"/>
    </body>

```

### div 和 span

div: division: 分开, 分配
span: 跨域, 涵盖.

早期的HTML没有CSS -> 添加各种包含样式的HTML元素, 比如strong, i, del (到达了极端) -> 搭建基本的结构, 用来添加样式 -> css出现 -> HTML和CSS相互分离 -> div和span出现 -> div+span+css -> div+css(另一个极端) -> 元素语义化(平衡)

div和span的区别: 
- div默认占据整行
	- 作为其他元素的父容器, 代表一个整体
	- 用于把网页分割微不同的部分
- span默认在同一行显示
	- 用于区分特殊文本和普通文本, 区分一些关键字



### meta标签

**搜索引擎在见多页面的时候, 会同时检索页面中的关键词和描述, 但是这两个值不会影响页面在搜索引擎中的排名**

使用meta标签设置网页关键字

```html
	<meta name = "keywords" content = "HTML5, JavaScript" />

```

可以用来指定网页的描述

```html
	<meta name = "description" content = "some info about html"

```

可以用来做请求的重定向

```html
	<meta http-equiv = "refresh" content = "5;url = "https://www.baidu.com"">
	<!--meta 这一个记住就行			引号里 "间隔时间 ; 进入的页面" -->

```

还有一系列功能可以去离线手册去找

### a标签

使用超链接让我从一个页面跳转到另一个页面

a标签创建超链接

a可以包含任何元素 , 除了它本身

属性

- href : 指向超链接跳转的目标地址
  - 如果将链接地址设置为 # 则点击以后自动跳转到顶部
  - 如果在#后面加上标签的id, 则点击以后自动跳转到此id对应的标签处
- target : 用来指定开链接的位置
  - _self : 在当前窗口中打开(默认值)
  - _blank : 另起一个标签页打开
  - 可以设置为一个内联框架的name值, 将其在内联框架中打开

**html中有一个属性  id, 不能以数字开头, 在同一个页面中只能有一个**

```html
        <a href="https://www.baidu.com">点击跳转到百度</a>
```

### 文本标签

#### em 标签 和 strong 标签

em标签 语气上的强调 显示为斜体字

strong标签 内容上的强调 显示为粗体字

```html
        <em>Hello World</em>
        <strong>Hello World</strong>
```

#### i 标签 和 b 标签

i 标签 单纯的将字体变为斜体 没有任何语义

b 标签 单纯的将字体加粗, 没有任何语义

```html
        <i>Hello World</i>
        <b>Hello WOrld</b>

```

#### small 标签和 big 标签

small标签

比父元素中的内容小一些, 语义 : 表示一些细则之类的内容, 如 合同中的小子, 网站的版权声明

big 标签, 没有语义, 单纯的大一点点

```html
        <small>small</small>
        <big>Hello World</big>
```

#### cite 标签

cite标签

网页中所有的加上书名号的东西都能用cite标签, 书名, 歌名, 话剧名, 舞蹈名...

```html
        <cite><论语></cite>
```

#### q 标签和 quote 标签

q标签

表示短引用(行内引用), 引用的内容浏览器自动加上引号

```html
        <q>学而时习之</q>
```

blockquote 标签

表示长引用, 块引用, 独占一行

```html
        <blockquote>这是一个块引用</blockquote>
```

#### sup 标签 和 sub 标签

sup 上标(次方)(可以加上链接)

sub 下标(角标)

```html
        X <sub>2</sub>
        X <sup>2</sup>
```

#### ins 标签和 del 标签

ins 标签表示插入的内容, 通常会加上下划线

del 标签表示一个删除的内容, 通常会加上删除线

```html
        <ins>insert</ins>
        <del>delete</del>
```

#### pre 标签和code 标签

code 标签的语义是表示一段代码, 但是并不会加上缩进

pre标签会把其中的文本原格式保留下来(包括缩进)

我们一般结合使用pre和code标签

```html
    <pre>
        <code>
            #include<iostream>
                using namespace std;
                int main(){
                    cout << "Hello World!" << endl;
                    return 0;
                }
        </code>
    </pre>
```

#### 列表标签

##### ul 无序列表

- 使用ul标签创建一个无序列表
- 使用li在ul中创建项
- 使用无序的项目符号
- 通过type属性可以修改列表的项目符号<span style = "color:red">[不建议用]</span>
- 去掉项目符号, 修改样式的属性 list-style:none
- 如果镇的需要设置项目符号, 则可以采用为li设置背景图片的方式来设置
- ul 和  li 都是块元素

```html
    <style>
        ul{
        /*将列表的项目符号设置为无*/
            list-style: none;
        }
    </style>
...
    <body>
        <ul>
            <li>First</li>
            <li>Second</li>
        </ul>
    </body>

```

##### 有序列表

有序列表就是把 ul 换成 ol

- type属性可以指定序号的类型, 可选值
  - 1, a, A 等阿拉伯数字或字母
  - i I 罗马数字

ol 也是块元素

列表之间可以互相嵌套

```html
        <ol>
            <li>1</li>
                <ol>
                    <li style="list-style: none;">1. 1</li>
                    <li style="list-style: none;">1. 2</li>
                </ol>
            <li>2</li>
        </ol>

```

##### 定义列表

使用dl来创建一个定义列表

dl有两个子标签

- dt 名词
- dd 解释 

```html
        <dl>
            <dt>4</dt>
            <dd>2+2</dd>
            <dt>2</dt>
            <dd>1+1</dd>
        </dl>

```

dl, ul, ol 之间可以互相嵌套

### 表格标签

- 默认没有边框, 用CSS设置边框
- table标签表示创建一个表格(块元素)
- 用tr表示一行
- 用td创建单元格, 有几个td就有几个单元格
  - td属性cospan横向合并, cospan="n" 合并n个单元格
  - td属性rowspan纵向合并 用法同上

```html
        <table>
            <tr>
                <td>1.1</td>
                <td>1.2</td>
            </tr>
            <tr>
                <td>2.1</td>
                <td>2.2</td>
            </tr>
        </table>
```

th特殊的td, 可以表示表头的内容, 用法和td一样, 不同的是有自带的居中和加粗

隔行变色nth-child(even)

#### 长表格

将表格分为三个部分: 表头, 主题, 底部

在HTML中有三个标签:

- thead 表头, 在浏览器中永远在最上面显示
- tbody 表体, 最中间显示
- tfoot 表格底部, 在最底部显示
- 所以以上三个标签可以随意改变顺序

table的子标签, 直接写在table中, tr都需要直接写在这些标签中

如果表格中没有写tbody, 浏览器会自动在表格中添加tbody, 并将所有的tr都放在tbody里, 所以**注意tr并不是table的子元素, 而是tbody的子元素, 通过table > tr 无法选中行, 需要用 tbody > tr**

### 表单

#### 填写

作用: 向服务器提交信息, 比如:百度的搜索框, 登录等

创建表单用form标签

- action 指向的是服务器的地址, 当我们提交表单的时候, 将会提交到action的地址
- 使用form创建的是一个空白的表单, 我们还应该向form中创建不同的表单项
  - 文本框 input内联元素自结束标签 type属性为text 可以有多个
    - 如果希望提交到服务器中, 还应该指定一个name属性(前端一般不决定)
    - 用户填写的信息会浮在url地址后面以查询字符串的形式发送给服务器  URL地址?查询字符串  格式: 属性名=属性值
    - 使用value设置默认值
  - 提交按钮 使用input内联自结束标签创建按钮 type属性为submit 将表单中的信息提交给服务器
    - value 选项:指定按钮上的文字
  - 密码框 input 创建 属性值为password
  - checked 输入数字段是否处于被选中状态
  - name表单名称
  - disable定义输入字段不可用

```html
        <form action="a.html">
            Name<input type="text" /><br />
            Pass<input type="password" /><br />
            <input type="submit" value="Submit">
        </form>

```

#### 单选

- 单选按钮 input创建, type为radio
- 单选按钮通过name分组, name相同分为一组
- 像这种需要用户选择但是不需要用户直接填写的表单项, 还必须指定一个value属性, 这样被指定的value值才会提交给服务器

```html
        <form action="a.html">
            性别 <input type="radio" name="gender" value="male">man
                <input type="radio" name="gender" value="famale">woman
            <input type="submit" value="Submit">
        </form>

```

#### 多选

使用input创建, type为checkbox, 也要使用name来分组, 使用value来提交, 但是每个选项的value值不能一样

如果希望在单选按钮或者多选框指定默认选中的选项, 则在分项中加上值为checked的checked属性

#### 下拉列表

使用 select 创建下拉列表

- 在下拉列表中使用option标签来创建列表项
- 下拉列表的name属性要指定给select, 但是value属性要指定给option
- 当给下拉列表添加一个 mutiple="multiple" 则下拉列表变为一个多选的下拉列表
- 下拉列表中的默认选中是添加一个值为selected的selected属性
- 在select中可以用optgroup对选项进行分组

```html
        <form action="a.html">
            Your number
            <select name="name">
                <optgroup label="1开头">
                    <option value="2" selected = "selected">12</option>
                    <option value="3">134</option>
                    <option value="4">1234</option>
                </optgroup>
                <optgroup label="2开头">
                    <option value="2">22</option>
                    <option value="3">234</option>
                    <option value="4">2234</option>
                </optgroup>
            </select>
            <input type="submit" value="Submit">
        </form>

```

#### 文本域

使用textarea创建一个多行文本域

input使用type的值为reset设置一个重置按钮

使用input, type为button可以创建一个单纯的按钮, 没有任何的功能, 只能被点(结合Js扩展功能)

也可以用button标签创建一个按钮, 和input类似, 但是成对出现使他更加灵活**(推荐, 更加灵活)**

在html中专门提供了一个标签, 专门用来选中表单中的提示文字的label标签

- 该标签可以指定一个for属性, 该属性的值需要指定一个表单项的id值
- for和id的值要匹配上
- 这样在点击label选择文字的时候回会选上选项

#### 表单项分组

- 使用fieldset来对表单进行分组
- 在fieldset中可以使用legend子标签来指定分组信息

## XHTML语法规范

为什么要学Xhtml的语法? 因为比较严格

1. HTML中不区分大小写, 但是一般用小写
2. 注释不能嵌套
3. 标签必须结构完整, 要么成对出现, 要么是自结束标签(即使浏览器会尽力在解析时修正你的代码, 有时候也修正不了)
4. 标签可以嵌套, 但是不能交叉嵌套
5. 标签的属性必须有值, 且值必须加上引号, 单引号双引号都行

## 内联框架

可以引入一个外部的页面
使用iframe创建一个内联框架

属性:

- src: 指向一个外部页面的路径, 可以使用相对路径
- width
- height等
- name : 可以为内联框架指定一个内容
- 更多内容查看离线手册

```html
        <iframe src="https://www.baidu.com" height="500px"></iframe>

```

<span style="color: red">在现实开发中不推荐使用内联框架,因为内联框架中的内容不会被搜索引擎检索到</span>

一种微前端的解决方案(一页个页面中不同的区域用不同的技术)

有的页面不允许被嵌套到iframe中, 方法: 

- header中设置 `X-Frame-Options:sameorigin` 只允许同源请求(大小写可以)

nginx部署的时候可以在nginx里面设置这个东西

a元素的target属性另外的取值:

- `_self`: 在本层网页打开
  - 在用iframe嵌套了网页的时候，如果在子页面中使用了a，a指向的页面自动在a所在的页面中打开

- `_parent`: 在父窗口打开URL
  - 用iframe嵌套的时候从父页面打开url

- `_top`: 在顶层窗口打开URL
  - 使用了多层iframe页面的时候，从顶层窗口打开URL



## 框架集

和内联框架类似, 都用于在一个页面中引入其他外部页面, 框架集可以同时引入多个页面, 在h5标准中, 推荐使用框架集, 而不是内联框架

frameset创建框架集 **注意**不能和body出现在同一个页面中, 要使用框架集就不能用body标签

属性:

- rows 指定框架集中的所有框架, 一行一行排列
- cols 指定框架集中的所有框架, 一列一列排列
- 这两个属性**必须选择一个**, 并需要在属性中指定每一部分所占的大小
- frameset中有一个子标签frame自结束标签, src指向一个页面, 用来引入其他的网页
- 引入几个页面就写几个frame

```html
    <frameset cols="50%, 50%">
        <frame src="01.html" />
        <frame src="02.html">
    </frameset>

```

frameset中可以再嵌套frameset

**为什么不推荐使用 ?**

frameset和iframe一样, 里面的内容都不会被搜索引擎所检索, 使用框架集意味着页面不能有自己的内容, 只能引入其他的页面, 而我们每单独加载一个页面都会重新发送一次请求, 用户的体验比较差, 如果非得用, 建议用frameset而不是iframe

## HACK

有些情况, 有一些特殊的代码我们只需要在某些特殊的浏览器中执行，而在其他的浏览器中不需要执行，这时我们就可以使用css hack来解决该问题。

Cssheck实际上是一段特殊的代码，这段代码只在某些特殊浏览器中可以识别，而其他浏览器中不能识别，通过这种方式来为一些浏览器设置特殊代码

