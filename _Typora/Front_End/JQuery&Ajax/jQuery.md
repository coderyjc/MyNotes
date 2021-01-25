# jQuery

## jQuery基础

### 初识 jQuery

平时的开发中使用正常版本的，便于阅读源代码，产品上线的时候使用min版本的，便于加载。

企业中使用的jQuery版本大多是1.x，因为可以兼容IE 678

```javascript
// 原生的js
window.onload = function(){
    alert("Hello World!");
}

// jquery风格
$(document).ready(function(){
    alert("Hello World !");
});
```

### 入口函数

#### jQuery入口函数

一共有四种写法，我们推荐第三种

```javascript
	// 1.第一种写法
	$(document).ready(function () {
	});

	// 2.第二种写法
	jQuery(document).ready(function () {
	});

	// 3.第三种写法(推荐)
	$(function () {
	});

	// 4.第四种写法
	jQuery(function () {
	});
```

#### 加载模式对比

原生JS和jQuery入口函数的加载模式不同，原生JS会等到DOM元素加载完毕,并且图片也加载完毕才会执行，jQuery会等到DOM元素加载完毕,但不会等到图片也加载完毕就会执行, 所以我们可以通过原生JS的入口函数拿到DOM元素和元素的宽和高，而通过jQuery只能拿到元素，拿不到宽和高。

原生的JS如果编写了多个入口函数,后面编写的会覆盖前面编写的，jQuery中编写多个入口函数,后面的不会覆盖前面的

#### 解决冲突问题

如果你在使用JQuery的情况下也使用了其他框架，其他框架也使用了 $ 符号，这时候就有冲突的了，我们必须解决冲突，也就是释放 \$ 的使用权。

注意点: 释放操作必须在编写其它jQuery代码之前编写，释放之后就不能再使用$,改为使用jQuery或自定义类型

```javascript
	// 释放$的使用权，自定义一个访问符号
	var nj = jQuery.noConflict();
	nj(function () {
		alert("hello lnj");
	});
```

### 核心函数

明确概念：

- 入口函数：` $(function(){  });`

- 核心函数：`$();`

注意：jQuery对象是一个<i>伪数组</i> , 有0到length-1的属性, 并且有length属性



```javascript
	// 1. 接收一个字符串选择器，返回一个jQuery对象, 对象中保存了找到的DOM元素
	var $box1 = $(".box1");
	var $box2 = $("#box2");
	// 2. 接收一个字符串代码片段，返回一个jQuery对象, 对象中保存了创建的DOM元素
	var $p = $("<p>我是段落</p>");
	$box1.append($p);
	// 3.接收一个DOM元素，如果把一个原生的js元素传递给jQuery的核心函数，它会被包装成一个jQuery对象返回给我们
	var span = document.getElementsByTagName("span")[0];
	var $span = $(span);
```

### 静态方法

明确概念：

- 静态方法：直接添加给类的就是静态方法 - 通过类名调用
- 实例方法：添加到类的原型上面的是实例方法 - 通过实例调用

#### each

注意: 原生的forEach方法只能遍历数组, **不能**遍历伪数组

利用jQuery的each静态方法遍历数组，这种方法**可以**遍历伪数组

- 第一个参数: 当前遍历到的索引
- 第二个参数: 遍历到的元素

```javascript
	var obj = {0:1, 1:3, 2:5, 3:7, 4:9, length:5};
	$.each(obj, function (index, value) {
		console.log(index, value);
	});
```

#### map

map函数的参数
- 第一个参数: 要遍历的数组
- 第二个参数: 每遍历一个元素之后执行的回调函数
回调函数的参数:
- 第一个参数: 遍历到的元素
- 第二个参数: 遍历到的索引

注意点:和jQuery中的each静态方法一样, map静态方法也可以遍历伪数组

```javascript
	var res = $.map(obj, function (value, index) {
		console.log(index, value);
		return value + index;
	});
```

jQuery中的each静态方法和map静态方法的区别:
- each静态方法默认的返回值就是, 遍历谁就返回谁；map静态方法默认的返回值是一个空数组
- each静态方法不支持在回调函数中对遍历的数组进行处理；map静态方法可以在回调函数中通过return对遍历的数组**进行处理**, 然后生成一个新的数组返回



#### 其他静态方法

**$.trim();**

作用: 去除字符串两端的空格

参数: 需要去除空格的字符串

返回值: 去除空格之后的字符串



**$.isWindow();**

作用: 判断传入的对象是否是window对象

返回值: true/false



**$.isArray();**

作用: 判断传入的对象是否是真数组

返回值: true/false



**$.isArray();**

作用: 判断传入的对象是否是一个函数

返回值: true/false

注意点:jQuery框架本质上是一个匿名函数



**$.holdReady(true)**

作用: 暂停ready执行,ready函数是jQuery的入口函数（详情见jQuery入口函数的第1、2种写法），等到我们想让ready函数执行的时候可以使用`$.holdReady(false)` 使入口函数开始执行

### jQuery对象

#### 其他选择器

```javascript
//:empty 作用:找到既没有文本内容也没有子元素的指定元素
var $div = $("div:empty");

//:parent 作用: 找到有文本内容或有子元素的指定元素
var $div = $("div:parent");

//:contains(text) 作用: 找到包含指定文本内容的指定元素
var $div = $("div:contains('我是div')");

//:has(selector) 作用: 找到包含指定子元素的指定元素
var $div = $("div:has('span')");
```

#### 属性和属性节点

明确概念：

- 属性，是对象身上保存的变量就是属性

- 属性节点：在编写HTML代码时,在HTML标签中添加的属性就是属性节点，在浏览器中找到span这个DOM元素之后, 展开看到的都是属性，在attributes属性中保存的所有内容都是属性节点
- 区别：任何对象都有属性, 但是只有DOM对象才有属性节点



1. attr(name|pro|key,val|fn)  作用: 获取或者设置属性节点的值

- 传递一个参数, 代表获取属性节点的值
- 传递两个参数, 代表设置属性节点的值

注意:
- 如果是获取:无论找到多少个元素, 都只会返回第一个元素指定的属性节点的值
- 如果是设置:找到多少个元素就会设置多少个元素
- 如果是设置:如果设置的属性节点不存在, 那么系统会自动新增

2. removeAttr(name)  作用: 删除找到元素的所有属性节点

```javascript
	$("span").attr("class", "box");
	$("span").removeAttr("class name"); //多个元素中间用空格隔开
```

1. prop方法，特点和attr方法一致
2. removeProp方法，特点和removeAttr方法一致

```javascript
$("span").eq(1) // 将span中所有元素找出，选出下标为1的元素，将其包装为jQuery对象并返回
```

**如何在attr和prop方法之间选择？**

- 注意: prop方法不仅能够操作属性, 他还能操作属性节点，官方推荐在操作属性节点时,具有 true 和 false 两个属性的属性节点，如 checked, selected 或者 disabled 使用prop()，其他的使用 attr()

#### 类、文本、CSS、尺寸等相关操作

1. addClass(class|fn)

  作用: 添加一个类

  如果要添加多个, 多个类名之间用空格隔开即可

2. removeClass([class|fn])

  作用: 删除一个类

  如果想删除多个, 多个类名之间用空格隔开即可

3. toggleClass(class|fn[,sw])

  作用: 切换类，有就删除, 没有就添加

```javascript
	var btns = document.getElementsByTagName("button");
	btns[0].onclick = function () {
		$("div").addClass("class1 class2");
	}
	btns[1].onclick = function () {
		$("div").removeClass("class2 class1");
	}
	btns[2].onclick = function () {
		$("div").toggleClass("class2 class1");
	}
```

1. html([val|fn]) 和原生JS中的innerHTML一模一样
2. text([val|fn]) 和原生JS中的innerText一模一样
3. val([val|fn|arr])

```javascript
    var btns = $("button");
    btns[0].onclick = function () {
        $("div").html("<p>我是段落<span>我是span</span></p>");
    }
    btns[2].onclick = function () {
        $("div").text("<p>我是段落<span>我是span</span></p>");
    }
    btns[4].onclick = function () {
        $("input").val("请输入内容");
    }
```

使用JQuery设置CSS相关代码

```javascript
	// 编写jQuery相关代码
	// 1.逐个设置
	$("div").css("width", "100px");
	$("div").css("height", "100px");
	$("div").css("background", "red");
	
	// 2.链式设置
	// 注意点: 链式操作如果大于3步, 建议分开
	$("div").css("width", "100px").css("height", "100px").css("background", "blue");
	
	// 3.批量设置[推荐]
	$("div").css({
		width: "100px",
		height: "100px",
		background: "red",
	});
	
	// 4.获取CSS样式值
	console.log($("div").css("background"));
```

获取元素的宽度

console.log($(".father").width());

offset([coordinates])

作用: 获取元素距离窗口的偏移位

console.log($(".son").offset().left);

position()

作用: 获取元素距离定位元素的偏移位,

console.log($(".son").position().left);

获取偏移位：

```javascript
    // 监听获取
    btns[0].onclick = function () {
        // 获取网页滚动的偏移位
        // 注意点: 为了保证浏览器的兼容, 获取网页滚动的偏移位需要按照如下写法
        console.log($("body").scrollTop()+$("html").scrollTop());
    }
    btns[1].onclick = function () {
        // 设置网页滚动偏移位
        // 注意点: 为了保证浏览器的兼容, 设置网页滚动偏移位的时候必须按照如下写法
        $("html,body").scrollTop(300);
    }
```
#### 事件操作

**事件的绑定**

jQuery中有两种绑定事件方式

1.eventName(fn); （初学者推荐）

编码效率略高（有代码提示）/ 部分事件jQuery没有实现,所以不能添加

2.on(eventName, fn);

编码效率略低（没有代码提示）/ 所有js事件都可以添加

注意点:可以添加多个相同或者不同类型的事件,不会覆盖

```javascript
    $("button").on("click", function () {
        alert("hello click1");
    });
```

**事件的移出**

off方法如果不传递参数, 会移除所有的事件 `$("button").off();`

off方法如果传递一个参数, 会移除所有指定类型的事件 `$("button").off("click");`

off方法如果传递两个参数, 会移除所有指定类型的指定事件 `$("button").off("click", test1);`



**事件冒泡和默认行为**

如何阻止事件冒泡 在回调函数最后返回 false 或接受一个event参数，在最后设置 event.stopPropagation();

如何阻止默认行为 在回调函数的最后返回 false 或者接受一个event参数，在最后设置 event.preventDefault();

```javascript
	$(".son").click(function (event) {
		alert("son");
		// return false;
		event.stopPropagation();
	});  
	$("a").click(function (event) {
		alert("弹出注册框");
		// return false;
		event.preventDefault();
	});
```

**自动触发事件和行为**

trigger: 如果利用trigger自动触发事件,会触发事件冒泡

triggerHandler: 如果利用triggerHandler自动触发事件, 不会触发事件冒泡

trigger: 如果利用trigger自动触发事件,会触发默认行为

triggerHandler: 如果利用triggerHandler自动触发事件, 不会触发默认行为







**自定义事件**

想要自定义事件, 必须满足两个条件

1. 事件必须是通过on绑定的

2. 事件必须通过trigger来触发

```javascript
	$(".son").on("myClick", function () {
		alert("son");
	});
	$(".son").triggerHandler("myClick");
```

**事件的命名空间**

情形：有多个人对同一个元素设置了多个事件

想要自定义事件, 必须满足两个条件

1. 事件必须是通过on绑定的

2. 事件必须通过trigger来触发

```javascript
	$(".son").on("click.zs", function () {
		alert("click1"); // 张三设置了一个click
	});
	$(".son").on("click.ls", function () {
		alert("click2"); // 李四设置了一个click
	});

	$(".son").trigger("click.ls");
```

注意：

- 利用trigger触发子元素**带命名空间**的事件, 那么父元素带**相同命名空间**的事件也会被触发. 而父元素没有命名空间的事件不会被触发
- 利用trigger触发子元素**不带命名空间**的事件,那么子元素所有相同类型的事件和父元素所有相同类型的事件**都会**被触发

也就是说：

```javascript
	$(".father").on("click.ls", function () { // 1 
		alert("father click1");
	});
	$(".father").on("click", function () { // 2
		alert("father click2");
	});
	$(".son").on("click.ls", function () { // 3
		alert("son click1");
	});

	$(".son").trigger("click.ls"); // 子事件带有命名空间，会触发 3 1
	$(".son").trigger("click"); // 子元素不带有命名空间， 会触发 3 1 2
```



**移入移出与事件委托**













### jQuery动画

#### 显示和隐藏

```javascript
	// 编写jQuery相关代码
	// div 是一个方块，作为我们添加动画的对象
	$("button").eq(0).click(function () {
		// $("div").css("display", "block");
		// 注意: 这里的时间是毫秒
		$("div").show(1000, function () {
			// 作用: 动画执行完毕之后调用
			alert("显示动画执行完毕");
		});
	});

	$("button").eq(1).click(function () {
		// $("div").css("display", "none");
		$("div").hide(1000, function () {
			alert("隐藏动画执行完毕");
		});
	});

	$("button").eq(2).click(function () {
		$("div").toggle(1000, function () {
			alert("切换动画执行完毕");
		});
	});
```

#### 展开收起

```javascript
	// 编写jQuery相关代码
	// div 是一个方块，作为我们添加动画的对象
	$("button").eq(0).click(function () {
		$("div").slideDown(1000, function () {
			alert("展开完毕");
		});
	});
	$("button").eq(1).click(function () {
		$("div").slideUp(1000, function () {
			alert("收起完毕");
		});
	});
	$("button").eq(2).click(function () {
		$("div").slideToggle(1000, function () {
			alert("收起完毕");
		});
	});
```

#### 淡入淡出

```javascript
	// 编写jQuery相关代码
	// div 是一个方块，作为我们添加动画的对象
	$("button").eq(0).click(function () {
		$("div").fadeIn(1000, function () {
			alert("淡入完毕");
		});
	});
	$("button").eq(1).click(function () {
		$("div").fadeOut(1000, function () {
			alert("淡出完毕");
		});
	});
	$("button").eq(2).click(function () {
		$("div").fadeToggle(1000, function () {
			alert("切换完毕");
		});
	});
	$("button").eq(3).click(function () {
		$("div").fadeTo(1000, 0.2, function () {
			alert("淡入完毕");
		})
	});
```

#### 自定义动画



#### 节点相关

**添加**





**删除**





**替换**





**复制**







### 综合实战





## JQuery + Ajax



