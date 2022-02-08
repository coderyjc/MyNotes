# CSS3高级

在实战中查漏补缺式学习





## 计量单位

视口：浏览器的可视区域的大小/移动端的LayoutViewport，也就是 `window.innerWidth/window.innerHeight` 的大小，不包括标题栏和工具栏

vw和vh

1. vw：1vw等于视口宽度的1%。
2. vh：1vh等于视口高度的1%。
3. vmin：选取vw和vh中最小的那个。
4. vmax：选取vw和vh中最大的那个。

字体

1. px 
   1. IE无法调整那些使用px作为单位的字体大小；
   2. 国外的大部分网站能够调整的原因在于其使用了em或rem作为字体单位；
   3. Firefox能够调整px和em，rem，但是96%以上的中国网民使用IE浏览器(或内核)。
2. em 
   1. em的值并不是固定的；
   2. em会继承父级元素的字体大小。
3. rem 
   1. 与em的区别：区别在于使用rem为元素设定字体大小时，仍然是相对大小，但相对的只是HTML根元素。

font-size:100%;设置字体属性为默认大小,是相对于浏览器默认字体大小或继承body设定的字体大小来说的。





## 属性

#### box-sizing

[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 中的 **`box-sizing`** 属性定义了 [user agent](https://developer.mozilla.org/zh-CN/docs/Glossary/User_agent) 应该如何计算一个元素的总宽度和总高度。

在 [CSS 盒子模型](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model)的默认定义里，你对一个元素所设置的 [`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width) 与 [`height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/height) 只会应用到这个元素的内容区。如果这个元素有任何的 [`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border) 或 [`padding`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding) ，绘制到屏幕上时的盒子宽度和高度会加上设置的边框和内边距值。这意味着当你调整一个元素的宽度和高度时需要时刻注意到这个元素的边框和内边距。当我们实现响应式布局时，这个特点尤其烦人。

box-sizing 属性可以被用来调整这些表现:

- `content-box` 是默认值。如果你设置一个元素的宽为100px，那么这个元素的内容区会有100px 宽，并且任何边框和内边距的宽度都会被增加到最后绘制出来的元素宽度中。
- `border-box` 告诉浏览器：你想要设置的边框和内边距的值是包含在width内的。也就是说，如果你将一个元素的width设为100px，那么这100px会包含它的border和padding，内容区的实际宽度是width减去(border + padding)的值。大多数情况下，这使得我们更容易地设定一个元素的宽高。

**译者注:** `border-box`不包含`margin`

#### outline

[CSS](https://developer.mozilla.org/en-US/docs/CSS) 的 `outline` 属性是在一条声明中设置多个轮廓属性的[简写属性](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Shorthand_properties)

#### **object-fit**

**`object-fit`** [CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) 属性指定[可替换元素](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Replaced_element)的内容应该如何适应到其使用的高度和宽度确定的框。

您可以通过使用 [`object-position`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/object-position) 属性来切换被替换元素的内容对象在元素框内的对齐方式。

```
contain
```

被替换的内容将被缩放，以在填充元素的内容框时保持其宽高比。 整个对象在填充盒子的同时保留其长宽比，因此如果宽高比与框的宽高比不匹配，该对象将被添加“[黑边](https://zh.wikipedia.org/wiki/黑邊)”。

```
cover
```

被替换的内容在保持其宽高比的同时填充元素的整个内容框。如果对象的宽高比与内容框不相匹配，该对象将被剪裁以适应内容框。

```
fill
```

被替换的内容正好填充元素的内容框。整个对象将完全填充此框。如果对象的宽高比与内容框不相匹配，那么该对象将被拉伸以适应内容框。

```
none
```

被替换的内容将保持其原有的尺寸。

```
scale-down
```

内容的尺寸与 `none` 或 `contain` 中的一个相同，取决于它们两个之间谁得到的对象尺寸会更小一些。





#### flex

`flex` [CSS简写属性](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Shorthand_properties)设置了弹性项目如何增大或缩小以适应其弹性容器中可用的空间。

此属性是以下CSS属性的简写：

- [`flex-grow`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-grow)  CSS 属性 **`flex-grow`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 设置 flex 项[主尺寸](https://www.w3.org/TR/css-flexbox/#main-size) 的 flex 增长系数。
- [`flex-shrink`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-shrink)[CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) **`flex-shrink`** 属性指定了 flex 元素的收缩规则。flex 元素仅在默认宽度之和大于容器的时候才会发生收缩，其收缩的大小是依据 flex-shrink 的值。
- [`flex-basis` ](https://developer.mozilla.org/zh-CN/docs/Web/CSS/flex-basis)[CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) 属性 **`flex-basis`** 指定了 flex 元素在主轴方向上的初始大小。如果不使用  [`box-sizing`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/box-sizing) 改变盒模型的话，那么这个属性就决定了 flex 元素的内容盒（content-box）的尺寸。

#### **mix-blend-mode** 

混合模式

现用现查

#### white-space

**`white-space`** CSS 属性是用来设置如何处理元素中的 [空白 (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)。

- `normal`

  连续的空白符会被合并，换行符会被当作空白符来处理。换行在填充「行框盒子([line boxes](https://www.w3.org/TR/CSS2/visuren.html#inline-formatting))」时是必要。

- `nowrap`

  和 normal 一样，连续的空白符会被合并。但文本内的换行无效。

- `pre`

  连续的空白符会被保留。在遇到换行符或者[``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/br)元素时才会换行。 

- `pre-wrap`

  连续的空白符会被保留。在遇到换行符或者[``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/br)元素，或者需要为了填充「行框盒子([line boxes](https://www.w3.org/TR/CSS2/visuren.html#inline-formatting))」时才会换行。

- `pre-line`

  连续的空白符会被合并。在遇到换行符或者[``](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/br)元素，或者需要为了填充「行框盒子([line boxes](https://www.w3.org/TR/CSS2/visuren.html#inline-formatting))」时会换行。

`**break-spaces**`
与 `pre-wrap`的行为相同，除了：

- 任何保留的空白序列总是占用空间，包括在行尾。
- 每个保留的空格字符后都存在换行机会，包括空格字符之间。
- 这样保留的空间占用空间而不会挂起，从而影响盒子的固有尺寸（最小内容大小和最大内容大小）。

下面的表格总结了各种 white-space 值的行为：

![image-20211125153754182](image-20211125153754182.png)

#### scroll-behavior

当用户手动导航或者 CSSOM scrolling API 触发滚动操作时，[CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) 属性 **`scroll-behavior`** 为一个滚动框指定滚动行为，其他任何的滚动，例如那些由于用户行为而产生的滚动，不受这个属性的影响。在根元素中指定这个属性时，它反而适用于视窗。

```
auto
```

滚动框立即滚动。

```
smooth
```

滚动框通过一个用户代理预定义的时长、使用预定义的时间函数，来实现平稳的滚动，用户代理应遵循其平台的约定，如果有的话。

#### perspective

[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 属性 **`perspective`**指定了观察者与 z=0 平面的距离，使具有三维位置变换的元素产生透视效果。 z>0 的三维元素比正常大，而 z<0 时则比正常小，大小程度由该属性的值决定。

```
none
```

没有应用 perspective 样式时的默认值.

```
<length>
```

指定观察者距离 z=0 平面的距离，为元素及其内容应用透视变换。当值为0或负值时，无透视变换。

#### transform

transform、scale XYZ的示意图

![image-20211125190317570](image-20211125190317570.png)

rotate的示意图

![image-20211125190701305](image-20211125190701305.png)



#### 滚动条相关

- ::-webkit-scrollbar 滚动条整体部分
- ::-webkit-scrollbar-thumb 滚动条里面的小方块，能向上向下移动（或往左往右移动，取决于是垂直滚动条还是水平滚动条）
- ::-webkit-scrollbar-track 滚动条的轨道（里面装有Thumb）
- ::-webkit-scrollbar-button 滚动条的轨道的两端按钮，允许通过点击微调小方块的位置。
- ::-webkit-scrollbar-track-piece 内层轨道，滚动条中间部分（除去）
- ::-webkit-scrollbar-corner 边角，即两个滚动条的交汇处
- ::-webkit-resizer 两个滚动条的交汇处上用于通过拖动调整元素大小的小控件





## 布局

### 定位

定位 = 定位模式 + 边偏移

定位模式：position（static、relative、absolute、fixed）

边偏移（相对于其父元素的上下左右边线的举例）：top、bottom、left、right

**static** 无定位，默认、在文档流之中

**relative** 相对定位，相对于自身原来的位置进行偏移、所占的位置保留、限制绝对定位

**absolute** 绝对定位，相对于祖先元素来说、没有父元素或者父元素没有定位就以浏览器为父元素、如果父元素有定位，就以最近一级带有定位的父元素的定位为约束、 不占有原来的位置

**子绝父相** ： 如果子元素使用了绝对定位，那么父元素应该使用相对定位（父元素要占有位置，因此相对定位，子元素不需要占有位置，但需要相对于父元素定位，所以是绝对定位），如果父元素不需要占有位置， 子绝父绝也可能用到。

**fixed** 固定定位，固定于浏览器的某个位置，以浏览器的可视窗口作为基准、跟父元素没有关系，不随着滚动条滚动、不占用原来的位置。

**stick** 粘性定位，以浏览器的可视窗口为参照点移动元素、占有原来的位置、必须添加top\left\bottom\right才有效【一开始是相对定位，拉到下面的时候开始固定定位（常见导航来的做法）】兼容性差、IE不支持

![image-20211125141003716](image-20211125141003716.png)

**定位的叠放次序：z-index** 使用定位布局的时候可能会出现盒子重叠的情况，可以使用z-index控制盒子的前后次序，非负整数，默认auto、越大越靠上、没有单位、只有定位的盒子才有z-index属性

绝对定位的盒子（absolute）不能通过margin: 0 auto 居中，但是可以通过以下方式水平和垂直居中：假设盒子的大小为200px `left:50%` `margin-left: -100px` -100px 的意思是让盒子向左移动自身宽度的一半

**定位的特殊特性**

- 行内元素 添加绝对或者固定定位之后可以直接设置高度和宽度
- 块级元素 添加绝对或者固定帝国位置后，如果不给宽度或者高度，默认大小是内容的大小
- 脱标的盒子不会触发外边距塌陷

浮动元素不同，只会压住它下面标准流的盒子，不会压住下面标准流盒子中的文字和图片，但是绝对定位（固定定位）会压住下面标准流中的所有内容，因为浮动最初产生的目的是为了文字环绕效果。















### Flex弹性盒模型

![image-20211023234325376](image-20211023234325376.png)



<img src="./CSS3.imgs/flex.png" style="zoom:100%;" />

![image-20211024075016336](image-20211024075016336.png)

### Grid 网格布局







## SCSS语法

### mixin

相当于自定义了一段代码复用的片段，可以提高代码的重复使用率







