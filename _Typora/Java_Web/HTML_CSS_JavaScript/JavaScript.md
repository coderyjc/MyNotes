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

优点：降低了程序的耦合度，写到外部的文件可以在不同的页面中同时引用，也可以利用浏览器的缓存机制

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
- 如果进行浮点运算，可能不能得到一个精确的结果

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

1. 调用被转换数据类型的toString()方法（返回方法的执行结果）  注意： null 和 undefined 没有toString() 方法，调用会报错  
2. 调用 String() 函数，并将要转换的数据作为参数传入, 对于Number和Boolean，底层就是调用的toString() ，但是对于null和undefined就会直接转换为字符串。

```javascript
        // 法1
        var num = 12345;
        num = num.toString();
        // 法2
        var und = undefined;
        num = String(und);
```

#### 转换为Number：方式：

1. 使用Number()函数
	
	1.如果是纯数字的字符串，则直接将其转换为数字
	
	2.如果字符串中有非数字的内容，则转换为NaN
	
	3.如果字符串是空串、全是空格的字符串、false、null，则转换为0
	
	4.undefined 为 NaN
	
2. parseInt()函数和 parseFloat()函数 专门用来对付字符串
  - 遇到第一个不是数字的时候停止
  - parseInt 有第二个参数，表示转换为多少进制的数字

3. 调用Boolean()函数来将a转换为布尔值
  - 数字转换为布尔型，除了0和NaN，其他的都是true，字符串转换为bool，除了空串，其他都是true
  - 对象也是true

在js中，如果需要表示16进制的数字，则需要以0x开头如果需要表示8进制的数字，则需要以0开头如果要要表示2进制的数字，则需要以0b开头但是不是所有的浏览器都支持，像"070"这种字符串，有些浏览器会当成8进制解析，有些会当成10进制解析

如果对非String使用parseInt()或parseFloat()它会先将其转换为String然后再操作

```javascript
	var a = "123.456px"
	alert(a); // -> 123.456
```

#### 运算符

基本和java一样

任何值和字符串相加都会转换为字符串，并做拼串操作。我们可以利用这一特点，来将一个任意的数据类型转换为String我们只需要为任意的数据类型 + 一个 "" 即可将其转换为String这是一种隐式的类型转换，由浏览器自动完成，实际上它也是调用String()函数

任何值做- * /运算时都会自动转换为Number我们可以利用这一特点做隐式的类型转换可以通过为一个值 -0 *1 /1 来将其转换为Number原理和Number()函数一样，使用起来更加简单（但是不是我们的最终方式，我们还有其他的方式）。

以下运算符和java一样：
- ++ --
- ！&& ||
- +=  -=  /=  *= 等
- < > >= <= (任何值和NaN比较都是返回 false)
-  ==  !=
-  三目运算符 ？： （不推荐使用，因为不方便阅读）
- 注意：在比较的时候通常会进行自动类型转换

= = =  全等：在比较的时候不会进行自动类型转换，如果类型不同会直接返回false

! = =  不全等 同理

- undefined 衍生自 null 所以这两个值用 == 比较的时候是相等的
- NaN 不和任何值相等，包括他本身
- 但是可以用 isNaN() 来判断一个数字是不是NaN

比较两个字符串型的数字的时候一定一定要转型

也有与或非运算符，而且我们可以对一个值取两次反（两次‘！’）来将其转换为布尔值

### 顺序/分支和循环

在JS中可以使用 {} 将语句括起来进行分组，（只有分组的作用，没有其他用途，代码块中的内容在外部是完全可见的）

prompt函数接受一个参数作为输出，弹出一个对话框，接受用户输入，作为返回值。
```javascript
var score = prompt("请输入小明的期末成绩(0-100):");
```

JS中的顺序、分支和循环语句和Java中一模一样

## 对象

### 对象基础知识

Js中的数据类型：String, Number, Boolean, Null, Undefined

只要不属于这五种数据类型，都是对象 Object

对象分为内建对象（ES标准中定义的对象 Math\String\Number\Function）、宿主对象（BOM\DOM）、自定义对象（我们自己创建的对象）

使用 new 关键字调用的函数时构造函数（专门用来创建对象的函数）



对对象的基本操作

- 对象中的保存的值称为属性，属性可以是任意类型，包括对象

- 向对象中添加属性，语法：`对象.属性名 = 属性值；`

- 读取对象中的属性，语法：``对象.属性名`；（如果对象中没有这个属性，不会报错，而是返回 undefined）或者 `对象[属性名] = 属性值`

- 修改对象的属性，语法：`对象.属性名 = 新值；`
- 删除对象的属性，语法：`delete 对象.属性名`

```javascript
	var obj = new Object();
	obj.name = "java"; //添加属性
	obj.name = "c++++"; //修改属性
	obj["name"] = "c-"; //修改属性
	alert("I am " + obj.name);//调用
	delete obj.name; //删除属性
```

in 运算符：检查一个对象中是否含有指定的属性，有就返回true，否则返回false；语法：`"属性名" in 对象`

```javascript
	console.log("name" in obj);
```

js中的变量都是保存在栈中的，但是对象是保存在堆中的，保存的都是引用

当比较两个基本数据类型的时候是比较值，但是在比较两个引用数据类型的时候，比较的是对象的内存地址，即使两个对象的内容都一样，只要地址不一样，还是会返回false



使用对象字面量创建对象：

使用对象字面量，在创建对象的时候，直接指定对象中的属性，语法：`{属性名:属性值，属性名:属性值，...}`对象字面量的属性名可以加上引号，也能不加，建议不加，如果要使用一些特殊的名字，就必须加上引号

属性名和属性值是一组一组的名值对结构，每一组之间用，隔开，名值之间用：链接

```javascript
var obj2 = {
		name:"猪八戒",
		age:13,
		gender:"男",
		test:{name:"沙僧"}
	};
```

### 函数

