# CSS3高级

## 计量单位

视口：浏览器的可视区域的大小/移动端的LayoutViewport，也就是 `window.innerWidth/window.innerHeight` 的大小，不包括标题栏和工具栏

vw和vh

1. vw：1vw等于视口宽度的1%。
2. vh：1vh等于视口高度的1%。
3. vmin：选取vw和vh中最小的那个。
4. vmax：选取vw和vh中最大的那个。





## 属性

#### box-sizing

[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 中的 **`box-sizing`** 属性定义了 [user agent](https://developer.mozilla.org/zh-CN/docs/Glossary/User_agent) 应该如何计算一个元素的总宽度和总高度。

在 [CSS 盒子模型](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model)的默认定义里，你对一个元素所设置的 [`width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/width) 与 [`height`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/height) 只会应用到这个元素的内容区。如果这个元素有任何的 [`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border) 或 [`padding`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding) ，绘制到屏幕上时的盒子宽度和高度会加上设置的边框和内边距值。这意味着当你调整一个元素的宽度和高度时需要时刻注意到这个元素的边框和内边距。当我们实现响应式布局时，这个特点尤其烦人。

box-sizing 属性可以被用来调整这些表现:

- `content-box` 是默认值。如果你设置一个元素的宽为100px，那么这个元素的内容区会有100px 宽，并且任何边框和内边距的宽度都会被增加到最后绘制出来的元素宽度中。
- `border-box` 告诉浏览器：你想要设置的边框和内边距的值是包含在width内的。也就是说，如果你将一个元素的width设为100px，那么这100px会包含它的border和padding，内容区的实际宽度是width减去(border + padding)的值。大多数情况下，这使得我们更容易地设定一个元素的宽高。

**译者注:** `border-box`不包含`margin`









## 布局

### 定位







### Flex弹性盒模型

![image-20211023234325376](CSS3.imgs/image-20211023234325376.png)



<img src="./CSS3.imgs/flex.png" style="zoom:100%;" />

![image-20211024075016336](CSS3.imgs/image-20211024075016336.png)

### Grid 网格布局







## 帧动画





