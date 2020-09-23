# JavaScript

## 简介和语法基础

前身：liveScript

起源：诞生于1995年，主要的作用是处理网页中的前端验证。

最初用来做前端验证（而并不是后端服务器验证）：检查用户输入的内容是否符合一定的规则（用户名的长度，邮箱的格式）

不同的浏览器对JavaScript实现的引擎是不同的。

JavaScript一般包含以下三个部分：ECMAScript/DOM/BOM

JS的特点：

- 解释性语言
- 类似于C和Java的语法结构
- 动态语言
- 基于原型的面向对象

JS代码需要编写到script标签中，这个标签有一个type属性，默认为“text/javascript”

### 输出语句

```javascript
        
alert("Hello World！"); //发出提醒

document.write("Hello DOCUMENT"); //作用：向body中输出内容

console.log("Hello CONSOLE"); //向控制台输出内容

```

### js 代码编写位置

1. 将js代码编写到onclick属性中（耦合度大，不推荐）
2. 可以编写在超链接的href中（耦合度大，不推荐）

```javascript
    <!--可以将js代码编写到onclick属性中-->
    <button onclick="alert('讨厌，你点我干嘛！');">
        点我一下
    </button>

    <!--可以写在超链接的href中-->
    <a href="javascript:alert('让你点你就点啊？');">
        你也点我一下
    </a>
    <a href="javascript:;">
        点我一下
    </a>

```

3. （推荐）将js代码写在外部的.js 文件中，然后通过script的src属性引入

优点：降低了程序的耦合度，写道外部的文件可以在不同的页面中同时引用，也可以利用浏览器的缓存机制

注意:script 标签一旦用来引入外部文件，就不能再编写代码了，即使编写了，浏览器也会忽略，只能再写一个script标签来编写内部的代码。

```javascript

// Test.js
	alert('Hello World');
// Test.html
    <script src="js/Test.js">
    </script>
```

注释：

- 多行注释：/* */
- 单行注释：//

代码规则：

- Js中严格区分大小写（HTML不区分大小写）
- Js中每一条语句必须以英文分号 ；结尾（如果不加分号，浏览器会自动添加，但是会消耗一些系统资源， 而且有些时候，浏览器会加错分号）
- Js中会自动忽略多个空格和换行，所以在代码中可以通过缩进和换行进行美化

### 字面量和变量

- 字面量
	- 字面量都是一些不能改变的量 : 1 2 3 4 5 "hello" 
	- 字面量都是可以直接使用的，但是我一般不会直接使用字面量（用起来不方便）
 - 变量
 	- 用来保存字面量，可以任意改变

变量/标识符

使用var声明一个变量，可以同时赋值

### 标识符

1. 可以含有字母，数字，_  , $
2. 不能以数字开头
3. 不能是ES中的关键字或者保留字
4. 驼峰命名法
5. 千万不要用中文

js底层保存的标识符是采用Unicode，所以，理论上u8中所有的字符都能作为变量名

```javascript
<script>
        var a = 100;
        alert(a);
</script>
```
### 数据类型

在js中一共有6中数据类型

1. String 字符串
2. Number 数字
3. Boolean 布尔值
4. Null 空值
5. Undefined 未定义
6. Object 对象

其中12345是基本数据类型，6是引用数据类型

String:

- 字符串可以用单引号和双引号，不要混着用
- 单引号里面可以套双引号，双引号中可以套单引号
- 如果要单套单或者双套双，可以使用转义字符

Number

- js中所有数值都是Number类型，包括整数和
- 如果表示的数字超过了最大值，则显示为Infinity
- 如果不是一个数字，则返回 NaN （not a number）
- 使用 typeof 检查 Infinity或者NaN 也会返回number
-  如果进行浮点运算，可能不能得到一个精确的结果

使用方式：

```javascript
/*
    运算符 typeof 检查一个变量类型
    语法： typeof 变量
 */
    var str1 = "Hello'world'";
    str1 = 'Hello';
    //------------------------------------
    //js中所有数值都是Number类型，包括整数和
    var n1 = 123;
    var n2 = 123.456;
    //如果表示的数字超过了最大值，则显示为Infinity
    var maxNumber = Number.MAX_VALUE; //最大值
    var maxNumber = Number.MIN_VALUE; //0以上的最小值
    //如果不是一个数字，则返回 NaN （not a number）
    document.write(typeof maxNumber); //输出n1的类型
    //使用 typeof 检查 Infinity或者NaN 也会返回number
    //如果进行浮点运算，可能不能得到一个精确的结果
    //---------------------------------------
    //布尔值只有两个, 小写的 true 和 false
    var bool1 = true;
    var bool2 = false;
    //----------------------------------------
    // Null 类型的值只有一个 null， 专门用来表示一个空的对象
    var ob = null;
    //typeof 检查null值会返回object
    //Undefinned的值只有一个， 当我门声明了一个值，但是没有给他赋值的时候，值就是undefined
    //typeof 检查 undefined 值会返回 undefined
```

### 强制类型转换

类型转换主要指：将其他类型转换为 String Number Boolean转换为 String 类型：

#### 转换为String：方式：

1. 调用被转换数据类型的toString()方法（返回方法的执行结果）        注意： null 和 undefined 没有toString() 方法，调用会报错  
2. 调用 String() 函数，并将要转换的数据作为参数传入, 对于Number和Boolean，底层就是调用的toString() ，但是对于null和undefined就会直接转换为字符串。

```javascript
        // 法1
        var num = 12345;
        num = num.toString();
        // 法2
        var und = undefined;
        num = String(und);
```

转换为Number：方式：

1. 使用Number()函数
2. parseInt()函数和 parseFloat()函数 专门用来对付字符串



## 顺序/分支和循环






## 函数



