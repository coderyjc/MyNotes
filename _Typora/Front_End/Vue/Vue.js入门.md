# Vue.js

## Vue基础

特点：

- Javascript框架
- 简化DOM操作
- 响应式驱动

### 第一个vue程序

步骤：
1. 导入开发版本的vue `<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>`
2. 创建vue实例对象，设置el属性和data属性
3. 使用模板语法把实例渲染到页面上

源码
```html
<body>
    <div id="app">
        {{message}}
    </div>
    <script>
        var app = new Vue({
            el:"#app",
            data:{
                message:"Hello"
            }
        });
    </script>
</body>
```

### el和data

el：挂载点

Vue实例的作用范围是什么？
- el命中的元素内部（可以无限嵌套）。外部则不行

是否能使用其他的选择器？
- 可以，但是在开发的时候建议使用id选择器

是否可以设置其他的DOM元素？
- 除了html标签和body标签，其他都可以。

data：数据对象

渲染复杂数据的时候遵循原生js的语法


## 本地应用

### 内容和事件绑定

**v-text 设置标签的文本值**

相当于设置innerText

当标签内部没有使用插值表达式的时候，自动更改标签内部的全部文本；

当使用了插值表达式，就按照表达式的内容进行更改

```html
<body>
    <div id="app">
        <div v-text="message"></div>
        <div>
            Hello {{info}} <br>
            {{message}} World
        </div>
    </div>
    <script>
        var app = new Vue({
            el:"#app",
            data:{
                message:"Hello",
                info:"world"
            }
        });
    </script>
</body>
```

**v-html 设置标签的 innerHTML**

 ```html
    <div id="app">
        <!-- 普通的文字信息 -->
        <p v-text="message"></p> 
        <!-- 超链接信息 -->
        <p v-html="superLink"></p>
    </div>
    <script>
        var app = new Vue({
            el:"#app",
            data:{
                message:"www.baidu.com",
                superLink:"<a href='http://kaifa.baidu.com/home'>www.kaifa.baidu.com</a>"
            }
        });
    </script>
 ```

**v-on为元素绑定事件**

```html
    <div id="app">
        <!-- 可以使用 @事件名称=“” 的方式 -->
        <input type="button" id="btn" value="0" @click="addOne"/>
        <!-- 也可以使用 v-on：事件名称=“” 的方式 -->
        <input type="button" id="btn2" value="0" v-on:click="addOne"/>
    </div>
    <script>
        var app = new Vue({
            el:"#app",
            methods:{
                addOne:function(){
                    // 点击之后value值会 + 1
                    var data = document.getElementById("btn").getAttribute("value");
                    data = parseInt(data) + 1;
                    document.getElementById("btn").setAttribute("value", String(data));
                }
            }
        });
```

**小程序 - 计数器**

```html
    <div id="main">    
        <button class="btn btn-primary" @click="add"><span class="btn-font">+</span></button>
        <div style="display: inline;">{{digit}}</div>
        <button class="btn btn-primary" v-on:click="minus"><span class="btn-font">-</span></button>
    </div>
    <script>
        var vue = new Vue({
            el: "#main",
            data:{
                digit:0
            },
            methods:{
                add:function(){
                    if(this.digit == 10){
                        alert("Max!!!");
                    }else{
                        this.digit += 1;
                    }
                },
                minus:function(){
                    if(this.digit == 0){
                        alert("Min!!!");
                    }else{
                        this.digit -= 1;
                    }
                }
            }
        })
    </script>
```

### 显示切换和属性绑定

**v-show  根据表达式的真假，切换元素的显示和隐藏，原理为改变元素的display值**

**v-if  根据表达式的真假，切换元素的显示和隐藏，原理为直接把标签变成一行注释（可以理解为直接删除标签）**

表达式中可以引用data中的数据。

```html
<!--点击按钮，图片改变显示和隐藏的状态-->
<div id="main">    
    <button @click="change">toggle</button>
    <img v-show="isShow" src="imgs/2020-07-17  08：59：03.jpg" alt="this is a picture">
</div>
<script>
    var vue = new Vue({
        el: "#main",
        data:{
            isShow: true
        },
        methods:{
            change:function(){
                this.isShow = (this.isShow == true ? false : true);
            }
        }
    })
</script>
```

```html
<!--年龄大于18的时候才显示图片-->
    <div id="main">    
        <button @click="addAge">当前年龄：{{age}}</button>
        <img v-show="age >= 18" src="imgs/2020-07-17  08：59：03.jpg" alt="this is a picture">
    </div>
    <script>
        var vue = new Vue({
            el: "#main",
            data:{
                age: 15
            },
            methods:{
                addAge:function(){
                    this.age++
                }
            }
        })
    </script>
```

在什么时机使用呢？频繁切换用 v-show，反之用v-if

**v-bind 设置元素的属性**

`v-bind:attrName="expression"`

简写省略v-bind： `：属性名="expression"`

表达式举例：

```html
<!-- 属性名 -->
<img v-bind:src="imgSrc" alt="this is a picture">
<!-- 表达式： 属性名 + 字符串 -->
<img v-bind:src="imgSrc + '!!!!'" alt="this is a picture">
<!-- 三元表达式 -->
<img v-bind:src="isActive?'active':''" alt="this is a picture">
<!-- data对象属性中的属性 -->
<img v-bind:src="{active:isActive}" alt="this is a picture">
```

```html
<!--点击按钮显示下一张图片-->
<div id="main">
    <br>
    <button @click="nextPic" style="display: block;" >下一张</button>
    <br>
    <img  v-bind:src="'imgs/'+String(this.imgIndex)+'.jpg'"  alt="this is a picture">
</div>
<script>
    var vue = new Vue({
        el: "#main",
        data:{
            imgIndex: 0,
        },
        methods:{
            nextPic:function(){
                this.imgIndex = (++this.imgIndex) % 4;
            }
        }
    })
</script>
```

### 列表循环和表单元素绑定

**v-for 根据数据生成列表结构**

语法：

<img src=".\Vue.js入门.imgs\image-20210129161903292.png" alt="image-20210129161903292" style="zoom:50%;" />

基本写法：

```html
<div class="main">
	<ol>
		<li v-for="city in cities">
				城市 ：{{city}}
		</li>
	</ol>
</div>
<script type="text/javascript">
	new Vue({
		el: ".main",
		data:{
			cities: ['bj', 'sh', 'gz', 'ls']
		}
	})
</script>
```

高级写法：

```html
<div class="main">
	<ul>
		<!-- in 是修饰符，不可改变 -->
		<li v-for="(item, index) in arr" :title="item">
			{{index}} {{item}}
		</li>
		<li v-for="(item, index) in objArr">
			{{item.name}}
		</li>
	</ul>
</div>

<script type="text/javascript">
	new Vue({
		el: ".main",
		data: {
			arr: [1, 3, 4, 5, 6, 8],
			objArr: [
				{name: "lili"},
				{name: "dali"},
				{name: "xiaoli"}
			]
		}
	})
</script>
```

**v-on补充：传参**

```html
<div class="main">
	<input type="text" id="delta"/>
	<button type="button" @click="addOne" > {{this.times}} </button>
	<input type="text" value="点这里然后敲回车试试" @keyup.enter="sayHello">
</div>
<script type="text/javascript">
	new Vue({
		el: ".main",
		data: {
			times: 0
		},
		methods: {
			addOne: function(delta){
				this.times += delta;
			},
			sayHello: function() {
				alert("Hello!");
			}
		}
	})
</script>

```

**v-model 获取和设置表单元素的值（双向绑定）**

```html
<div class="main">
	姓名：<input type="text" id="delta" v-model="data"/>
	<br> <br>
	你好：<span type="button">{{data}}</span>
</div>
<script type="text/javascript">
	new Vue({
		el:".main",
		data : {
			data: 0
		},
		methods:{
			change: function(){
					var v = $("#delta")[0];
					this.data = v.value;
			}
		}
	})
</script>
```

## 网络应用








## 综合应用


