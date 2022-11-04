

> 当页面下滑时, 滑块以左入右入的方式进入
> 页面上滑时, 滑块以左右出的形式离开

### html

HTML中只是简单地在body里面直接写了10个Box

在前面引入了样式表, 在最后引入了js文件

```html
<body>

  <div class="box"><h2>Content</h2></div>

  <div class="box"><h2>Content</h2></div>

  <div class="box"><h2>Content</h2></div>

  <div class="box"><h2>Content</h2></div>

... 一共10个
</body>

```

### CSS

重点是transform 和transition

其他都不重要

```css

body {
  ...
  overflow-x: hidden;
}
```

> **这里为什么要把溢出元素隐藏？**
> 
> 实现动画效果的时候需要让盒子向右向左偏移，离开我们的视线，用到了translate
> translate是相对于元素的当前位置偏移，
> 偏移之后还在文档流中，这个时候为了显示完全页面，body就会自动扩展以出现滚动条
> 让溢出的内容隐藏就是为了去掉滚动条
> 实现元素的进入效果


```css
.box {
  transform: translateX(400%);
  transition: transform 0.4s ease;
}
.box:nth-of-type(even) {
  transform: translateX(-400%);
}
.box.show {
  transform: translateX(0);
}
```

`transform`

为了隐藏元素，让元素有进入效果，先让盒子向左右偏移

`transition`

对于transform属性进行变换，如果这个属性变化了，那么变化的过程为 0.4秒，变化的方式为平滑过渡

`.box.show`

带有show类的元素横向偏移置为0


### Js

```js

// 找到元素
const boxes = document.querySelectorAll('.box')

// 添加窗口滚动的响应事件
window.addEventListener('scroll', checkBoxes)

// 第一次进入页面的时候首先加载一次元素，防止闪屏
checkBoxes()

function checkBoxes() {

    const triggerBottom = window.innerHeight / 5 * 4

    boxes.forEach(box => {

        const top = box.getBoundingClientRect().top

        if(top < triggerBottom) {
            box.classList.add('show')
        } else {
            box.classList.remove('show')
        }
    })

}
```


```js
const top = box.getBoundingClientRect().top
```

这句代码中，如果缺少const关键词，会导致不加载动画，页面停留在刚刚加载进来的状态（空白）而且随着页面的下滑，依然不会显示其他的元素，并且打印出来值之后，加与不加const打印出来的值是一样的。为什么？

> 不加top是全局变量
> window.top 返回窗口层级顶级窗口的引用
> window.top 这个变量是只读的，不可修改
> 因此在这一句中top不会被赋予 box.getBoundingClientRect().top的值, 而是全返回了 window 对象
> 因此所有元素都还是原来的状态
> 
> 使用了声明关键字 let/var/const 就没事了


> 补充: ES6-const 注意点
> 1. 一定要赋初值
> 2. 一般使用大写
> 3. 常量不能修改
> 4. 块级作用域
> 5. 数组和对象只保存地址（引用）

`window.innerHeight` 浏览器窗口的视口（viewport）高度（以像素为单位）；如果有水平滚动条，也包括滚动条高度


`box.getBoundingClientRect().top` 元素盒子在视口中的位置，top是距离视口顶部的距离

当元素距离最顶部的距离小于视口的 4/5 的时候，以进入的方式加载元素

![[Pasted image 20220622212821.png]]