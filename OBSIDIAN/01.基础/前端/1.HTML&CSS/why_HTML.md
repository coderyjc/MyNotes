# 前置知识

> 最权威的官方文档: https://w3.org

## 浏览器

核心: 浏览器**[[内核]](渲染引擎 Rendering Engine)**

内核的作用: 解析网页语法并渲染(显示)网页

不同的浏览器内核: 
- Trident(三叉戟): IE\ 360\ 搜狗\ 百度\ UC浏览器
- Gecko(壁虎): Mozilla Firefox
- presto(急板乐曲) -> Blink: Opera
- Webkit: Safari\ 360\ 搜狗\ 移动端浏览器
- [[Webkit]] -> Blink(目前最快): Chrome, Edge

![](assets/Pasted%20image%2020220902223843.png)

不同的浏览器内核的**解析渲染规则不同**, 同一个网页再不同的内核的浏览器的渲染效果可能不同


## 什么是HTML?

什么是[[标记语言]]?
- 由标记组成
- 对某些内容进行特殊的标记, 以供其他的解释器进行识别和处理
- 由标签和内容组成的部分成为元素

**HTML不是编程语言, 是计算机语言.**

什么是[[超文本]]?
- 不仅可以插入普通的文本(Text), 还可以插入其他元素, 图片, 音频, 视频等
- 还可以插入超链接, 从一个网页跳转到另一个链接

.htm和.html的区别
- 历史遗留问题: Win95/Win98的文件扩展名不能超过3字符, 因此是.htm
- 因此现在一律使用.html


## HTML结构

插件: Atom One Dark Theme

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

## 元素

### html

文档的根, 顶级元素, 根元素

W3C标准建议为html元素增加一个`lang`属性, 作用: 
- 帮助语音合成工具确定要使用的发音
- 帮助翻译工具确定要使用的翻译规则

`<html lang="zh-CN"> <html lang="zh">` 中文 CN表示简体中文

`<html lang="en">` 英文

### head

规定文档相关的配置信息(元数据), 标题, 引用的文档样式和脚本等

元数据: 描述数据的数据, 在这里可以理解为`整个页面的配置`

[[meta元素]]: 

- 设计网页的字符编码, 一般使用utf-8 (UTF-8)

常用元素: p h img a div span

 ### h1--h6, p, img

h元素和[[SEO优化]]有关系.

区别: 浏览器只是给这些元素添加了不同的**CSS样式**而已.

h元素和p元素本质上没有区别, 只是在css上不一样而已

p元素表示 paragraphs 段落, 通常适用于大段的文字, 段落之间有空隙

---

img是一个**可替换元素(replacement element)**

img在没有设置src 的时候是什么都不显示的只占据一点位置, 当设置了src 的时候, 浏览器就会从src获取图片把占据的一点位置替换

src中绝对路径基本上不会用吗, 一般用相对路径

对于网页来说(Win, Mac, Linux), 路径分隔符一律是`/`

img的属性alt的作用: 
- 加载失败的时候显示的文字
- 屏幕阅读器会将这些描述读给需要使用阅读器的使用者听(障碍人士), 让他们知道这张图片的含义.


### a, iframe

href : Hypertext Reference

锚点链接: 可以跳转到网页中的具体位置

1. 在目标元素上添加id
2. 定义a元素, 指向对应的id

```html

<a href="#anchor"></a>

<h2 id="anchor"></h2>

```


---

一种微前端的解决方案(一页个页面中不同的区域用不同的技术)

有的页面不允许被嵌套到iframe中, 方法: 
- header中设置 `X-Frame-Options:sameorigin` 只允许同源请求(大小写可以)

nginx部署的时候可以在nginx里面设置这个东西

a元素的另外的取值:
- `_parent`: 在父窗口打开URL
- `_top`: 在顶层窗口打开URL

这两个主要用在a元素和iframe相结合时候的使用

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


### 其他元素

- strong(内容加粗, 表示强调) -> 可以用css代替
- i(倾斜) -> 一般用来做图标(icon)
- code(等宽字体) -> 有时候用来显示代码
- br(换行) -> 现在还用这个换行的人, 乱棍打死 !

## HTML全局属性

> https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes


常用全局属性: id, class, style(内联样式), title(提示信息)

## 补充知识

### 字符实体

`&`开头, `;`结尾的文本, 用于显示保留字符和不可见字符, 比如`\n`, 比如`<`

### URL和URI

[[URI]]标识Web技术使用的逻辑或者物理**资源**, [[URL]]是网络地址

URL是URI的一个子集

