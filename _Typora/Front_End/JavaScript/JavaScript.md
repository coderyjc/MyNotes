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
    <script src="js/Test.js"></script>
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

- js中所有数值都是Number类型，包括整数和浮点数
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

每个对象中都有一个constructor属性，它引用了当前对象的构造函数。

对对象的基本操作

- 对象中的保存的值称为属性，属性可以是任意类型，包括对象，也可以是个函数

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
        obj.objAdd = function(num1, num2){
            return num1 + num2;
        }
        alert(obj.objAdd(1, 90));
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

#### 函数的创建

函数也是对象，而且  `typeof 函数 = function`

```javascript
        // 将代码以字符串的形式传递给对象(函数表达式)
        var fun = new Function("document.write('Hello World!<br/>');");
        fun();

        // 以函数声明的方式创建一个函数
        function HelloFunction(){
            document.write("Hello World!<br/>");
        }
        HelloFunction();

        // 创建匿名函数(函数表达式)
        var fun2 = function(){
            document.write("Hello World!<br/>")
        }
        fun2();
```

含参数的函数的声明：

```javascript
        function sum(a, b){
            return a + b;
        }
        alert(sum(234, 34));
```

调用函数时解析器**不会检查实参的类型**,所以要注意，是否有可能会接收到非法的参数，如果有可能则需要对参数进行类型的检查函数的实参可以是任意的数据类型

调用函数时，解析器也**不会检查实参的数量**, 多余实参不会被赋值如果实参的数量少于形参的数量，则没有对应实参的形参将是undefined

函数中不写return，会返回undefined

- call()
- apply()
	- 这两个方法都是函数对象的方法需要通过函数对象来调用
	- 通过两个方法可以直接调用函数，并且可以通过第一个实参来指定函数中this
	- 不同的是call是直接传递函数的实参而apply需要将实参封装到一个数组中传递
- arguments
	- arguments和this类似，都是函数中的隐含的参数
	- arguments是一个类数组元素，它用来封装函数执行过程中的实参
		所以即使不定义形参，也可以通过arguments来使用实参
	- arguments中有一个属性callee表示当前执行的函数对象

声明完毕立即执行的函数：

```javascript
        (function(a, b){
            alert("a + b = " + (a + b));
        })(32, 48);
```

枚举对象中的属性

```javascript
        var student = {
            name:'张三',
            age:23,
            email:'zhangsan@qq.com', 
            address:'Beijing China'
        }

        /**
         * 注意: 只是枚举函数的变量的属性名，每一次遍历都会按照变量声明的顺序将变量名赋值给vars 
         * 想要取出其中的属性，应该用[]取出
         */
        for(var vars in student){
            console.log(vars + student[vars]);
        }
```

#### 作用域

作用域指一个变量的作用的范围

在JS中一共有两种作用域：

全局作用域 和 函数作用域

全局作用域：

- 直接编写在script标签中的JS代码，都在全局作用域
- 全局作用域在页面打开时创建，在页面关闭时销毁
- 在全局作用域中有一个全局对象window，它代表的是一个浏览器的窗口，它由浏览器创建我们可以直接使用
- 在全局作用域中：创建的变量都会作为window对象的属性保存; 创建的函数都会作为window对象的方法保存
- 全局作用域中的变量都是全局变量，在页面的任意的部分都可以访问的到
- 尽量不要在全局作用域中创建变量

函数作用域：

- 调用函数时创建函数作用域，函数执行完毕以后，函数作用域销毁
- 每调用一次函数就会创建一个新的函数作用域，他们之间是互相独立的
- 在函数作用域中可以访问到全局作用域的变量，在全局作用域中无法访问到函数作用域的变量
- 当在函数作用域操作一个变量时，它会先在自身作用域中寻找，如果有就直接使用，如果没有则向上一级作用域中寻找，直到找到全局作用域，如果全局作用域中依然没有找到，则会报错ReferenceError
- 在函数中要访问全局变量可以使用window对象
- 在函数作用域也有声明提前的特性，使用var关键字声明的变量，会在函数中所有的代码执行之前被声明，函数声明也会在函数中所有的代码执行之前执行
- 在函数中，不使用var声明的变量都会成为全局变量

变量声明提前：

变量的声明提前: 使用var关键字声明的变量，会在所有的代码执行之前被声明（但是不会赋值，如果这时候输出，会显示undefined），但是如果声明变量时不适用var关键字，则变量不会被声明提前

函数的声明提前: 使用函数声明形式创建的函数 function 函数(){}它会在所有的代码执行之前就被创建，所以我们可以在函数声明前来调用函数, 使用函数表达式创建的函数，不会被声明提前，所以不能在声明前调用	

```javascript
			//函数声明，会被提前创建
			function fun(){
				console.log("我是一个fun函数");
			}
			
			//函数表达式，不会被提前创建
			var fun2 = function(){
				console.log("我是fun2函数");
			};
```

#### this

解析器在调用函数每次都会向函数内部传递进一个隐含的参数,这个隐含的参数就是this，this指向的是一个对象，	这个对象我们称为函数执行的 上下文对象，根据函数的调用方式的不同，this会指向不同的对象

1.以函数的形式调用时，this永远都是window

2.以方法的形式调用时，this就是调用方法的那个对象

```javascript
        this.name = 'windows!!'

        function fun(){
            console.log(this.name);
        }
        
        var sun = {
            name:'sun',
            getName: fun
        }
        
        sun.getName();
        fun();
        
        //控制台输出结果为 : sun windows!!
```

函数中还有一个对象arguments，这个对象是一个数组，用来保存函数的参数，并且这个对象还有一个属性callee来表示当前的函数

#### 构造函数

使用工厂方法创造对象：

```javascript
			function createPerson(name , age ,gender){
				//创建一个新的对象 
				var obj = new Object();
				//向对象中添加属性
				obj.name = name;
				obj.age = age;
				obj.gender = gender;
				obj.sayName = function(){
					alert(this.name);
				};
				//将新的对象返回
				return obj;
			}
			
			
			var obj2 = createPerson("猪八戒",28,"男");
			var obj3 = createPerson("白骨精",16,"女");
			var obj4 = createPerson("蜘蛛精",18,"女");
```

缺点：创建的对象都是Object这个类型，就导致我们无法区分出多种不同类型的对象

**构造函数：**

构造函数和普通函数的区别就是调用方式的不同，普通函数是直接调用，而构造函数需要使用new关键字来调用

构造函数的执行流程：
1. 立刻创建一个新的对象
2. 将新建的对象设置为函数中this,在构造函数中可以使用this来引用新建的对象
3. 逐行执行函数中的代码
4. 将新建的对象作为返回值返回

this的情况：
1. 当以函数的形式调用时，this是window
2. 当以方法的形式调用时，谁调用方法this就是谁
3. 当以构造函数的形式调用时，this就是新创建的那个对象

```javascript
			function Person(name , age , gender){
				this.name = name;
				this.age = age;
				this.gender = gender;
				this.sayName = function(){
					alert(this.name);
				};
			}
			
			var per = new Person("孙悟空",18,"男");
			var per2 = new Person("玉兔精",16,"女");
			var per3 = new Person("奔波霸",38,"男");
```

使用instanceof可以检查一个对象是否是一个类的实例

语法：对象 instanceof 构造函数. 如果是，则返回true，否则返回false

所有的对象都是Object的后代，所以任何对象和Object左instanceof检查时都会返回true

### 原型

- 创建一个函数以后，解析器都会默认在函数中添加一个属性prototype，prototype属性指向的是一个对象，这个对象我们称为原型对象。如果函数作为普通函数调用prototype没有任何作用

- 当函数作为构造函数使用，它所创建的对象中都会有一个隐含的属性执行该原型对象。这个隐含的属性可以通过 `对象. __proto__`来访问。

- 原型对象就相当于一个公共的区域，凡是通过同一个构造函数创建的对象他们通常都可以访问到相同的原型对象。我们可以将对象中共有的属性和方法统一添加到原型对象中，这样我们只需要添加一次，就可以使所有的对象都可以使用。

- 当我们去访问对象的一个属性或调用对象的一个方法时，它会先自身中寻找，如果在自身中找到了，则直接使用。如果没有找到，则去原型对象中寻找，如果找到了则使用，如果没有找到，则去原型的原型中寻找，依此类推。直到找到Object的原型为止，Object的原型的原型为null，如果依然没有找到则返回undefined

- hasOwnProperty()

	- 这个方法可以用来检查对象自身中是否含有某个属性
	
	- 语法：对象.hasOwnProperty("属性名")


toString 方法：

```javascript
		function Person(name , age , gender){
			this.name = name;
			this.age = age;
			this.gender = gender;
		}
		
		//修改Person原型的toString
		Person.prototype.toString = function(){
			return "Person[name="+this.name+",age="+this.age+",gender="+this.gender+"]";
		};
```

### 数组

**成员变量**

创建数组：`var arr = new Array();`  或者 `var arr = [1,2,3,4,5];` 第一种方法如果是一个参数，就代表元素的个数，如果是多个，就代表每个元素的值

获取数组的长度`数组名称.length`

修改length的时候，如果修改的length大于原长度，则多出部分会空出来，如果修改的length小于原长度，则多出的元素会被删除

向数组的最后一个位置添加元素，语法：数组[数组.length] = 值;


如果读取不存在的索引，他不会报错而是返回undefined

**方法**

- push()
	- 向数组的末尾添加一个或多个元素，并返回数组新的长度
	- 语法：数组.push(元素1,元素2,元素N)
- pop()
	
	- 用来删除数组的最后一个元素，并返回被删除的元素
- unshift()
	
	- 向数组的前边添加一个或多个元素(参数顺序不变，添加完毕之后第一个参数是添加后数组的首元素)，并返回数组的新的长度
- shift()
	
	- 删除数组的前边的一个元素，并返回被删除的元素
- slice()
	- 可以从一个数组中截取指定的元素，封装为一个新的数组并返回
	- 参数：左闭右开
		- 第二个参数可以省略不写，如果不写则一直截取到最后
		- 参数可以传递一个负值，如果是负值，则从后往前数
- splice()
	- 可以用来删除数组中指定元素，并使用新的元素替换，该方法会将删除的元素封装到新数组中返回
	- 参数：
		1. 删除开始位置的索引
		2. 删除的个数
		3. 三个以后，都是替换的元素，这些元素将会插入到开始位置索引的前边

- reverse()
	
	- 反转一个数组，它会对原数组产生影响
- concat()
	
	- 可以连接两个或多个数组，它不会影响原数组，而是新数组作为返回值返回
- join()
	- 可以将一个数组转换为一个字符串
	- 参数：需要一个字符串作为参数，这个字符串将会作为连接符来连接数组中的元素如果不指定连接符则默认使用','
- sort()
	- 可以对一个数组中的内容进行排序，默认是按照Unicode编码进行排序调用以后，会直接修改原数组。
	- 可以自己指定排序的规则，需要一个回调函数作为参数：
	```javascript
    function(a,b){
    			//升序排列
    			//return a-b;
    			//降序排列
    			return b-a;
    		}
  ```



数组的遍历：

1. 普通的for循环
2. forEach

forEach()方法需要一个函数作为参数

- 这个方法只能遍历数组，不能遍历伪数组

- 像这种函数，由我们创建但是不由我们调用的，我们称为回调函数
- 数组中有几个元素函数就会执行几次，每次执行时，浏览器会将遍历到的元素以实参的形式传递进来，我们可以来定义形参，来读取这些内容
- 浏览器会在回调函数中传递三个参数：
	- 第一个参数，就是当前正在遍历的元素
	- 第二个参数，就是当前正在遍历的元素的索引
	- 第三个参数，就是正在遍历的数组

```javascript
	arr.forEach(function(value , index , obj){
		console.log(value);
	});
```

## 包装类和工具类

String() Boolean() Number()

当我们去操作一个基本数据类型的属性和方法时，解析器会临时将其转换为对应的包装类，然后再去操作属性和方法，操作完成以后再将这个临时对象进行销毁。

### String

- length()
	- 长度
- charAt()
	- 根据索引获取指定的字符
- charCodeAt()
	- 根据索引获取指定的字符编码
- String.fromCharCode()
	- 根据字符编码获取字符
- indexOf()从前向后找
- lastIndexOf()从后向前找
	- 从一个字符串中检索指定内容
	- 需要一个字符串作为参数，这个字符串就是要检索的内容，如果找到该内容，则会返回其第一次出现的索引，如果没有找到则返回-1。
	- 可以指定一个第二个参数，来表示开始查找的位置
- slice()
	- 可以从一个字符串中截取指定的内容，并将截取到内容返回，不会影响原变量
	- 参数：
		第一个：截取开始的位置（包括开始）
		第二个：截取结束的位置（不包括结束）
	- 可以省略第二个参数，如果省略则一直截取到最后
	- 可以传负数，如果是负数则从后往前数
- substr()	
	- 和slice()基本一致，不同的是它第二个参数不是索引，而是截取的数量
- substring()
	- 和slice()基本一致，不同的是它不能接受负值作为参数，如果设置一个负值，则会自动修正为0，substring()中如果第二个参数小于第一个，自动调整位置
- toLowerCase() 
	- 将字符串转换为小写并返回
- toUpperCase() 
	- 将字符串转换为大写并返回
- split()
	- 可以根据指定内容将一个字符串拆分为一个数组
	- 参数：需要一个字符串作为参数，将会根据字符串去拆分数组。可以接收一个正则表达式，此时会根据正则表达式去拆分数组
- match() 
	- 可以将字符串中和正则表达式匹配的内容提取出来
	- 参数：正则表达式，可以根据该正则表达式将字符串中符合要求的内容提取出来，并且封装到一个数组中返回
- replace()  
	- 可以将字符串中指定内容替换为新的内容
	- 参数：
		- 第一个：被替换的内容，可以是一个正则表达式
		- 第二个：替换的新内容
- search() 
	- 可以根据正则表达式去字符串中查找指定的内容
	- 参数：正则表达式，将会根据该表达式查询内容，并且将第一个匹配到的内容的索引返回，如果没有匹配到任何内容，则返回-1。

### Date

构造函数：`var d = new Date();` 默认是当前代码的执行时间。

带参构造：`var d2 = new Date("2/18/2011 11:10:30");`日期的格式  月份/日/年 时:分:秒

get相关的函数

```javascript
	//getDate() 获取当前日期对象是几日
	var date = d.getDate();
	
	//getDay() 获取当前日期对象时周几，0-6
	var day = d.getDay();

	//getMonth()，获取当前时间对象的月份，返回一个0-11的值
	var month = d2.getMonth();
	
	//getFullYear()，获取当前日期对象的年份
	var year = d2.getFullYear();
	
	/*
	 * getTime()
	 * 	- 获取当前日期对象的时间戳
	 * 	- 时间戳，指的是从格林威治标准时间的1970年1月1日，0时0分0秒 到当前日期所花费的毫秒数（1秒 = 1000毫秒）
	 * 	- 计算机底层在保存时间时使用都是时间戳
	 *  - 时间戳可以测试代码的执行性能
	 */
	var time = d2.getTime();

```

### Math

```javascript
	Math.PI //表示的圆周率
	abs()// 绝对值
	Math.ceil()// 向上取整
	Math.floor()	//向下取整
	Math.round()	//四舍五入取整
	Math.random() //返回一个0-1之间的随机数
	max()// 可以获取多个数中的最大值
	min() //可以获取多个数中的最小值
	Math.pow(x,y) //返回x的y次幂
	Math.sqrt() //开方
```



### 正则表达式

创建正则表达式对象：`var 变量 = new RegExp("表达式", "匹配模式")；` 

typeof 正则表达式 = object

在构造函数中可以传递一个匹配模式作为第二个参数，可以是i 忽略大小写 ，g 全局匹配模式

test() 使用这个方法可以用来检查一个字符串是否符合正则表达式的规则，如果符合则返回true，否则返回false

使用字面量来创建正则表达式语法：`var 变量 = /正则表达式/匹配模式`

使用字面量的方式创建更加简单，使用构造函数创建更加灵活

`var reg = /a/i;`

正则表达式的相关内容查看 `正则表达式.pdf`

## DOM

### 概念

DOM，全称Document Object Model文档对象模型。以面向对象的方式操作网页。

- 文档 – 文档表示的就是整个的HTML网页文档

- 对象 – 对象表示将网页中的每一个部分都转换为了一个对象。

- 模型 – 使用模型来表示对象之间的关系，这样方便我们获取对象。

节点：Node——构成HTML文档最基本的单元

常见节点:

- 文档节点：整个HTML文档

- 元素节点：HTML文档中的HTML标签 

- 属性节点：元素的属性

- 文本节点：HTML标签中的文本内容

<img src="D:\GITHUB\MyNotes\_Typora\Front_End\JavaScript\JavaScript.imgs\image-20210116082739708.png" alt="image-20210116082739708" style="zoom:50%;" />

节点的属性：

|          | nodeName  | nodeType | nodeValue |
| -------- | --------- | -------- | --------- |
| 文档节点 | #document | 9        | null      |
| 元素节点 | 标签名    | 1        | null      |
| 属性节点 | 属性名    | 2        | 属性值    |
| 文本节点 | #text     | 3        | 文本内容  |

document对象作为window对象的属性存在的，我们不用获取可以直接使用。通过该对象我们可以在整个文档访问内查找节 点对象，并可以通过该对象创建各种节点对象。

举例：通过id获取一个元素节点的对象：`– document.getElementById()`

### 事件处理

事件处理有两种方法

1. 我们可以在事件对应的属性中设置一些js代码，比如`<button id="btn" onclick="alert('点我干嘛？');">我是一个按钮</button>`这样当事件被触发时，这些代码将会执行这种写法我们称为结构和行为耦合，不方便维护，**不推荐使用**。
2. 可以为按钮的对应事件绑定处理函数的形式来响应事件这样当事件被触发时，其对应的函数将会被调用

```html
	<button id="btn">我是一个按钮</button>
	<script type="text/javascript">

		//获取按钮对象
		var btn = document.getElementById("btn");
		
		//绑定一个单击事件，像这种为单击事件绑定的函数，我们称为单击响应函数
		btn.onclick = function(){
			alert("你还点~~~");
		};
	</script>
```

注意：

浏览器在加载一个页面时，是按照自上向下的顺序加载的，读取到一行就运行一行,如果将script标签写到页面的上边，在代码执行时，页面还没有加载，页面没有加载DOM对象也没有加载会导致无法获取到DOM对象

如何在写到上面的同时使其在页面加载完之后执行？

onload事件会在整个页面加载完成之后才触发, 为window绑定一个onload事件该事件对应的响应函数将会在页面加载完成之后执行，这样可以确保我们的代码执行时所有的DOM对象已经加载完毕了。

```javascript
	window.onload = function(){
		//获取id为btn的按钮
		var btn = document.getElementById("btn");
		//为按钮绑定一个单击响应函数
		btn.onclick = function(){
			alert("hello");
		};
	};
```

### DOM查询

获取元素节点：

通过document对象调用

```javascript
// 通过id属性获取一个元素节点对象
var node1 = document.getElementById();

//通过标签名获取一组元素节点对象
var node2 = document.getElementsByTagName();

//通过name属性获取一组元素节点对象
var node3 = document.getElementsByName();
```

获取元素节点的子节点：

通过具体的元素节点调用。

```javascript
//方法，返回当前节点的指定标签名后代节点
getElementsByTagName()

//属性，表示当前节点的所有子节点
childNodes

//属性，表示当前节点的第一个子节点
firstChild

//属性，表示当前节点的最后一个子节点
lastChild
```

注意:

childNodes属性会获取包括文本节点在内的所有节点，根据DOM标签标签间空白也会当成文本节点。注意：在IE8及以下的浏览器中，不会将空白文本当成子节点，所以该属性在IE8中会返回4个子元素而其他浏览器是9个

firstElementChild不支持IE8及以下的浏览器，如果需要兼容他们尽量不要使用



获取父节点和兄弟节点：

通过具体节点调用

```javascript
//属性，表示当前节点的父节点
parentNode

//属性，表示当前节点的前一个兄弟节点
previousSibling

//属性，表示当前节点的后一个兄弟节点
nextSibling
```

元素节点的属性

```javascript
//--------------获取-----------
element.value
element.id
element.className

//--------------修改------------
element.value = “hello”
element.id = “id01”
element.className = “newClass”
```

文本框的value属性值，就是文本框中填写的内容

文本节点可以通过nodeValue属性获取和设置文本节点的内容

元素节点通过innerHTML属性获取和设置标签内部的 html代码

innerText属性可以获取到元素内部的文本内容，它和innerHTML类似，不同的是它会自动将html去除

为指定元素绑定单击响应函数的快捷方法：函数

```javascript
	/*
	 * 定义一个函数，专门用来为指定元素绑定单击响应函数
	 * 	参数：
	 * 		idStr 要绑定单击响应函数的对象的id属性值
	 * 		fun 事件的回调函数，当单击元素时，该函数将会被触发
	 */
	function myClick(idStr , fun){
		var btn = document.getElementById(idStr);
		btn.onclick = fun;
	}
	
	//为id为btn07的按钮绑定一个单击响应函数
	myClick("btn07",function(){
		//获取id为bj的节点
		var bj = document.getElementById("bj");
		//返回#bj的父节点
		var pn = bj.parentNode;
		alert(pn.innerHTML);	
	});

```

多选框的选中状态是元素的属性，值为布尔类型，通过设置checked属性可以设置选中和未选中。在事件的响应函数中，响应函数是给谁绑定的this就是谁。



```javascript
	//在document中有一个属性body，它保存的是body的引用
	var body = document.body;
	
	//document.documentElement保存的是html根标签
	var html = document.documentElement;
	
	//document.all代表页面中所有的元素
	var all = document.all;
```

class的选择

根据元素的class属性值查询一组元素节点对象： getElementsByClassName()可以根据class属性值获取一组元素节点对象，但是该方法不支持IE8及以下的浏览器

`document.querySelector()`

- 需要一个选择器的字符串作为参数，可以根据一个CSS选择器来查询一个元素节点对象
- 虽然IE8中没有getElementsByClassName()但是可以使用querySelector()代替
- 使用该方法总会返回唯一的一个元素，如果满足条件的元素有多个，那么它只会返回第一个
- 举例`var div = document.querySelector(".box1 div");`

`document.querySelectorAll()`

- 该方法和querySelector()用法类似，不同的是它会将符合条件的元素封装到一个数组中返回
- 即使符合条件的元素只有一个，它也会返回数组
- 举例`box1 = document.querySelectorAll("#box2");`



### DOM对元素的增删改

`document.createElement()`可以用于创建一个元素节点对象，它需要一个标签名作为参数，将会根据该标签名创建元素节点对象，并将创建好的对象作为返回值返回

`document.createTextNode()`可以用来创建一个文本节点对象，需要一个文本内容作为参数，将会根据该内容创建文本节点，并将新的节点返回

`appendChild()`用于向一个父节点中添加一个新的子节点，用法：父节点.appendChild(子节点);

`insertBefore()`可以在指定的子节点前插入新的子节点.语法，父节点.insertBefore(新节点对象, 子节点对象);

`replaceChild()`可以使用指定的子节点替换已有的子节点，语法：父节点.replaceChild(新节点,旧节点);

`removeChild()`删除一个子节点，语法：父节点.removeChild(子节点);子节点.parentNode.removeChild(子节点);

注意:使用innerHTML也可以完成DOM的增删改的相关操作，一般我们会两种方式结合使用

```javascript
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>

	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>添加删除记录练习</title>
		<link rel="stylesheet" type="text/css" href="ex_2_style/css.css" />
		<script type="text/javascript">
		
			/*
			 * 删除tr的响应函数
			 */
			function delA() {

				//点击超链接以后需要删除超链接所在的那行
				//这里我们点击那个超链接this就是谁
				//获取当前tr
				var tr = this.parentNode.parentNode;

				//获取要删除的员工的名字
				//var name = tr.getElementsByTagName("td")[0].innerHTML;
				var name = tr.children[0].innerHTML;

				//删除之前弹出一个提示框
				/*
				 * confirm()用于弹出一个带有确认和取消按钮的提示框
				 * 	需要一个字符串作为参数，该字符串将会作为提示文字显示出来
				 * 如果用户点击确认则会返回true，如果点击取消则返回false
				 */
				var flag = confirm("确认删除" + name + "吗?");

				//如果用户点击确认
				if(flag) {
					//删除tr
					tr.parentNode.removeChild(tr);
				}

				/*
				 * 点击超链接以后，超链接会跳转页面，这个是超链接的默认行为，
				 * 	但是此时我们不希望出现默认行为，可以通过在响应函数的最后return false来取消默认行为
				 */
				return false;
			};

			window.onload = function() {

				/*
				 * 点击超链接以后，删除一个员工的信息
				 */

				//获取所有额超链接
				var allA = document.getElementsByTagName("a");

				//为每个超链接都绑定一个单击响应函数
				for(var i = 0; i < allA.length; i++) {
					allA[i].onclick = delA;
				}

				/*
				 * 添加员工的功能
				 * 	- 点击按钮以后，将员工的信息添加到表格中
				 */

				//为提交按钮绑定一个单击响应函数
				var addEmpButton = document.getElementById("addEmpButton");
				addEmpButton.onclick = function() {

					//获取用户添加的员工信息
					//获取员工的名字
					var name = document.getElementById("empName").value;
					//获取员工的email和salary
					var email = document.getElementById("email").value;
					var salary = document.getElementById("salary").value;

					//需要将获取到的信息保存到tr中

					//创建一个tr
					var tr = document.createElement("tr");

					//设置tr中的内容
					tr.innerHTML = "<td>"+name+"</td>"+
									"<td>"+email+"</td>"+
									"<td>"+salary+"</td>"+
									"<td><a href='javascript:;'>Delete</a></td>";
									
					//获取刚刚添加的a元素，并为其绑定单击响应函数				
					var a = tr.getElementsByTagName("a")[0];
					a.onclick = delA;
					
					//获取table
					var employeeTable = document.getElementById("employeeTable");
					//获取employeeTable中的tbody
					var tbody = employeeTable.getElementsByTagName("tbody")[0];
					//将tr添加到tbodye中
					tbody.appendChild(tr);
				};

			};
		</script>
	</head>

	<body>

		<table id="employeeTable">
			<tr>
				<th>Name</th>
				<th>Email</th>
				<th>Salary</th>
				<th>&nbsp;</th>
			</tr>
			<tr>
				<td>Tom</td>
				<td>tom@tom.com</td>
				<td>5000</td>
				<td>
					<a href="javascript:;">Delete</a>
				</td>
			</tr>
			<tr>
				<td>Jerry</td>
				<td>jerry@sohu.com</td>
				<td>8000</td>
				<td>
					<a href="deleteEmp?id=002">Delete</a>
				</td>
			</tr>
			<tr>
				<td>Bob</td>
				<td>bob@tom.com</td>
				<td>10000</td>
				<td>
					<a href="deleteEmp?id=003">Delete</a>
				</td>
			</tr>
		</table>

		<div id="formDiv">

			<h4>添加新员工</h4>

			<table>
				<tr>
					<td class="word">name: </td>
					<td class="inp">
						<input type="text" name="empName" id="empName" />
					</td>
				</tr>
				<tr>
					<td class="word">email: </td>
					<td class="inp">
						<input type="text" name="email" id="email" />
					</td>
				</tr>
				<tr>
					<td class="word">salary: </td>
					<td class="inp">
						<input type="text" name="salary" id="salary" />
					</td>
				</tr>
				<tr>
					<td colspan="2" align="center">
						<button id="addEmpButton">
						Submit
					</button>
					</td>
				</tr>
			</table>
		</div>
	</body>
</html>
```




### DOM操作CSS

`元素.style.样式名 = 样式值`, 通过JS修改元素的样式：注意：如果CSS的样式名中含有-，这种名称在JS中是不合法的比如background-color需要将这种样式名修改为驼峰命名法，也就是去掉-，然后将-后的字母大写. 我们通过style属性设置的样式都是内联样式，而内联样式有较高的优先级，所以通过JS修改的样式往往会立即显示, 但是如果在样式中写了!important，则此时样式会有最高的优先级，即使通过JS也不能覆盖该样式，此时将会导致JS修改样式失效,	所以尽量不要为样式添加!important, 通过style属性设置和读取的都是内联样式,无法读取样式表中的样式

`元素.currentStyle.样式名`, 获取元素的当前显示的样式。**currentStyle只有IE浏览器支持**，其他的浏览器都不支持。它可以用来读取当前元素正在显示的样式, 如果当前元素没有设置该样式，则获取它的默认值

`window.getComputedStyle(box1,null).backgroundColor`, 在其他浏览器中可以使用,getComputedStyle()这个方法来获取元素当前的样式；需要两个参数: 第一个：要获取样式的元素; 第二个：可以传递一个伪元素，一般都传null。 该方法会返回一个对象，对象中封装了当前元素对应的样式,可以通过对象.样式名来读取样式,如果获取的样式没有设置，则会获取到真实的值，而不是默认值比如：没有设置width，它不会获取到auto，而是一个长度; 但是该方法不支持IE8及以下的浏览器, 通过currentStyle和getComputedStyle()读取到的样式都是只读的，不能修改，如果要修改必须通过style属性

定义一个函数，用来获取指定元素的当前的样式

```javascript
	//obj 要获取样式的元素
	//name 要获取的样式名
	function getStyle(obj , name){
		//正常浏览器的方式，具有getComputedStyle()方法
		//IE8的方式，没有getComputedStyle()方法
		return window.getComputedStyle ? getComputedStyle(obj , null)[name] : obj.currentStyle[name];
	}
```

clientWidth/clientHeight
- 这两个属性可以获取元素的可见宽度和高度
- 这些属性都是不带px的，返回都是一个数字，可以直接进行计算
- 会获取元素宽度和高度，包括内容区和内边距
- 这些属性都是只读的，不能修改

offsetWidth/offsetHeight
- 获取元素的整个的宽度和高度，包括内容区、内边距和边框

offsetParent
- 可以用来获取当前元素的定位父元素
- 会获取到离当前元素最近的开启了定位的祖先元素,如果所有的祖先元素都没有开启定位，则返回body

offsetLeft
- 当前元素相对于其定位父元素的水平偏移量
offsetTop
- 当前元素相对于其定位父元素的垂直偏移量

scrollWidth/scrollHeight
- 可以获取元素整个滚动区域的宽度和高度

scrollLeft
- 可以获取水平滚动条滚动的距离
scrollTop
- 可以获取垂直滚动条滚动的距离

判断滚动条是否滚动到底
- 垂直滚动条		scrollHeight - scrollTop = clientHeight
- 水平滚动		scrollWidth - scrollLeft = clientWidth


## 事件

### 事件对象

事件对象：在DOM对象上的某个事件被触发时，会产生一个事件对象Event，这个对象中包含着所有事件有关的信息。包括导致事件的元素、事件的类型以及其他与特定事件相关的信息。

例如，鼠标操作导致的事件对象中，会包含鼠标位置的信息，而键盘操作导致的事件对象中，会包含与按下的键有关的信息。所有浏览器都支持 event对象，但支持方式不同。

DOM标准的浏览器会将一个event对象传入到事件的处理程序当中。无论事件处理程序是什么都会传入一个event对象。Event对象包含与创建它的特定事件有关的属性和方法。触发的事件类型不一样，可用的属性和方法也不一样。

事件的发生主要是由用户操作引起的。,比如mousemove这个事件就是由于用户移动鼠标引起的，在鼠标指针移动的过程中该事件会持续发生。当指定事件被触发时，浏览器就会调用对应的函数去响应事件，一般情况下事件没触发一次，函数就会执行一次。因此设置鼠标移动的事件可能会影响到鼠标的移动速度。所以设置该类事件时一定要谨慎。

<img src="JavaScript.imgs\image-20210118085815422.png" alt="image-20210118085815422" style="zoom:67%;" />

<img src="D:\GITHUB\MyNotes\_Typora\Front_End\JavaScript\JavaScript.imgs\image-20210118100137806.png" alt="image-20210118100137806" style="zoom:67%;" />



获取方式：
```javascript
	// 向其中传入一个event参数
	btn.onclick = function(event){
		alert(event.type);
	};
```

当鼠标在areaDiv中移动时，在showMsg中来显示鼠标的坐标

```javascript
	/*
	 * onmousemove - 该事件将会在鼠标在元素中移动时被触发
	 * 事件对象 - 当事件的响应函数被触发时，浏览器每次都会将一个事件对象作为实参传递进响应函数,在事件对象中封装了当前事件相关的一切信息，比如：鼠标的坐标键盘哪个按键被按下鼠标滚轮滚动的方向。
	 */
	areaDiv.onmousemove = function(event){
		// 在IE8中，响应函数被触发时，浏览器不会传递事件对象，在IE8及以下的浏览器中，是将事件对象作为window对象的属性保存的
		//解决事件对象的兼容性问题
		event = event || window.event;
		// clientX/cilentY可以获取鼠标指针的水平和垂直坐标
		var x = event.clientX;
		var y = event.clientY;
	};
```


### 事件冒泡

事件的冒泡（Bubble）
- 所谓的冒泡指的就是事件的向上传导，当后代元素上的事件被触发时，其祖先元素的相同事件也会被触发
- 在开发中大部分情况冒泡都是有用的,如果不希望发生事件冒泡可以通过事件对象来取消冒泡

`event.cancelBubble = true;`可以将事件对象的cancelBubble设置为true，即可取消冒泡

#### 事件委派

我们希望，只绑定一次事件，即可应用到多个的元素上，即使元素是后添加的, 因此我们可以尝试将其绑定给元素的共同的祖先元素

事件的委派, 指将事件统一绑定给元素的**共同的祖先元素**，这样当后代元素上的事件触发时，会一直冒泡到祖先元素, 从而通过祖先元素的响应函数来处理事件。事件委派是利用了冒泡，通过委派可以减少事件绑定的次数，提高程序的性能

#### 事件绑定

使用 对象.事件 = 函数 的形式绑定响应函数，它只能同时为一个元素的一个事件绑定一个响应函数，不能绑定多个，如果绑定了多个，则后边会覆盖掉前边的。

`addEventListener()` 通过这个方法也可以为元素绑定响应函数

参数：

1. 事件的字符串，不要on

2. 回调函数，当事件触发时该函数会被调用

3. 是否在捕获阶段触发事件，需要一个布尔值，一般都传false

使用addEventListener()可以同时为一个元素的相同事件同时绑定多个响应函数，这样当事件被触发时，响应函数将会按照**函数的绑定顺序**执行,这个方法不支持IE8及以下的浏览器

`attachEvent()`在IE8中可以使用attachEvent()来绑定事件

参数：
1. 事件的字符串，要on
2. 回调函数

这个方法也可以同时为一个事件绑定多个处理函数，不同的是它是后绑定先执行，执行顺序和addEventListener()相反

定义一个函数用来为指定元素绑定响应函数

```javascript
	/*
	 * 参数：
	 * 	obj 要绑定事件的对象
	 * 	eventStr 事件的字符串(不要on)
	 *  callback 回调函数
	 */
	function bind(obj , eventStr , callback){
		if(obj.addEventListener){
			//大部分浏览器兼容的方式
			obj.addEventListener(eventStr , callback , false);
		}else{
			/*
			 * this是谁由调用方式决定
			 * callback.call(obj)
			 */
			//IE8及以下
			obj.attachEvent("on"+eventStr , function(){
				//在匿名函数中调用回调函数
				callback.call(obj);
			});
		}
	}

```

#### 事件的传播

关于事件的传播网景公司和微软公司有不同的理解: 微软公司认为事件应该是由内向外传播，也就是当事件触发时，应该先触发当前元素上的事件，然后再向当前元素的祖先元素上传播，也就说事件应该在冒泡阶段执行;网景公司认为事件应该是由外向内传播的，也就是当前事件触发时，应该先触发当前元素的最外层的祖先元素的事件, 然后在向内传播给后代元素

W3C综合了两个公司的方案，将事件传播分成了三个阶段

1. 捕获阶段 - 在捕获阶段时从最外层的祖先元素，向目标元素进行事件的捕获，但是默认此时**不会触发事件**
2. 目标阶段 - 事件捕获到目标元素，捕获结束开始在目标元素上触发事件
3. 冒泡阶段 - 事件从目标元素向他的祖先元素传递，依次**触发祖先元素上的事件**

- 如果希望在捕获阶段就触发事件，可以将addEventListener()的第三个参数设置为true, 一般情况下我们不会希望在捕获阶段触发事件，所以这个参数一般都是false

- IE8及以下的浏览器中没有捕获阶段

事件的传播流程

<img src="D:\GITHUB\MyNotes\_Typora\Front_End\JavaScript\JavaScript.imgs\image-20210118100758900.png" alt="image-20210118100758900" style="zoom:67%;" />

捕获阶段 – 这一阶段会从window对象开始向下一直遍历到目标对象，如果发现有对 象绑定了响应事件则做相应的处理。

目标阶段 – 这一阶段已经遍历结束，则会执行目标对象上绑定的响应函数。 

事件冒泡阶段 – 这一阶段，事件的传播方式和捕获阶段正好相反，会从事件目标一直向遍历，直至window对象结束，这时对象上绑定的响应函数也会执行

我们可以使用event对象的两个方法完成： – stopPropagation() – stopImmediatePropagation() 

取消默认行为： – preventDefault()

#### 事件举例

拖拽事件, 滚轮事件, 键盘事件等略, 都是调用api, 在使用的时候查阅即可


## BOM

BOM将浏览器中的各个部分转换成了一个一个的对象，我们通过修改这些对象的属性，调用他们的方法，从而控制浏览器的各种行为。



### window对象

window对象是BOM的核心，它表示一个浏览器的实例。在浏览器中我们可以通过window对象来访问操作浏览器，同时window也是作为全局对象存在的。全局作用域： window对象是浏览器中的全局对象，因此所有在全局作用域中声明的变量、对象、函数都会变成window对象的属性和方法。

窗口大小

浏览器中提供了四个属性用来确定窗口的大小：

– 网页窗口的大小 innerWidth / innerHeight 

– 浏览器本身的尺寸 outerWidth / outerHeight



打开窗口

使用 window.open() 方法既可以导航到一个特定的 URL，也可以打开一个新的浏览器窗口。 这个方法需要四个参数： – 需要加载的url地址 –窗口的目标 –一个特性的字符串 –是否创建新的历史记录



超时调用

setTimeout() 超过一定时间以后执行指定函数 – 需要两个参数： 要执行的内容/超过的时间 

延时调用一个函数不马上执行，而是隔一段时间以后在执行，而且只会执行一次

延时调用和定时调用的区别，定时调用会执行多次，而延时调用只会执行一次

延时调用和定时调用实际上是可以互相代替的，在开发中可以根据自己需要去选择

取消超时调用 – clearTimeout() 超时调用都是在全局作用域中执行的。



间歇调用

setInterval() 每隔一段时间执行指定代码 , 需要两个参数: 要执行的代码(回调函数) ; 间隔的时间,单位是毫秒; 返回一个Number类型的数据,这个数据用来作为定时器的唯一标识

取消间隔调用： – clearInterval()

```javascript
	var timer = setInterval(function(){
		count.innerHTML = num++;
		if(num == 11){ //关闭定时器
			clearInterval(timer);
		}
	},1000);
```

系统对话框

浏览器通过 alert() 、 confirm() 和 prompt() 方法可以调用系统对话框向用户显示消息。它们的外观由操作系统及（或）浏览器设置决定，而不是由 CSS 决定。显示系统对话框时会导致程序终止，当关闭对话框程序会恢复执行。





### location对象

location代表当前浏览器的地址栏信息，还提供了一些导航功能，通过Location可以获取地址栏信息，或者操作浏览器跳转页面。

如果直接将location属性修改为一个完整的路径，或相对路径,则我们页面会自动跳转到该路径，并且会生成相应的历史记录

href属性：

- href属性可以获取或修改当前页面的完整的URL地址，使浏览器跳转到指定页面。

assign() 方法

- 所用和href一样，使浏览器跳转页面，新地址错误参数传递到assign ()方法中，作用和直接修改location一样

replace()方法

-  功能一样，只不过使用replace方法跳转地址不会体现到历史记录中，不能使用回退按钮回退

reload() 方法

- 用于强制刷新当前页面，作用和刷新按钮一样,如果在方法中传递一个true，作为参数，则会强制清空缓存刷新页面

### navigator对象

代表的当前浏览器的信息，通过该对象可以来识别不同的浏览器, 由于历史原因，Navigator对象中的大部分属性都已经不能帮助我们识别浏览器了, 一般我们只会使用userAgent来判断浏览器的信息，userAgent是一个字符串，这个字符串中包含有用来描述浏览器信息的内容，不同的浏览器会有不同的userAgent

- navigator 对象包含了浏览器的版本、浏览器所支持的插件、浏览器所使用的语言等各种与浏览器相关的信息。

- 我们有时会使用navigator的userAgent属性来检查用户浏览器的版本。

### screen对象

- screen 对象基本上只用来表明客户端的能力，其中包括浏览器窗口外部的显示器的信息，如像素宽度和高度等。
- 该对象作用不大，我们一般不太使用。

### history对象

history 对象保存着用户上网的历史记录，从窗口被打开的那一刻算起。由于隐私原因，该对象不能获取到具体的历史记录，只能操作浏览器向前或向后翻页而且该操作只在当次访问时有效

go()

- 使用 go() 方法可以在用户的历史记录中任意跳转，可以向后也可以向前。
- 可以用来跳转到指定的页面
- 它需要一个整数作为参数
- 1:表示向前跳转一个页面 相当于forward()
- 2:表示向前跳转两个页面
- -1:表示向后跳转一个页面
- -2:表示向后跳转两个页面

back()

- 向后跳转，作用和浏览器的回退按钮一样

forward()

- 向前跳转，作用和浏览器的前进按钮一样

### document

- document对象也是window的一个属性，这个对象代表的是整个网页的文档对象。
- 我们对网页的大部分操作都需要以document对象作为起点。
- 关于document对象的内容，我们后边还要具体讲解。

## JSON

JSON
- JS中的对象只有JS自己认识，其他的语言都不认识
- JSON就是一个特殊格式的字符串，这个字符串可以被任意的语言所识别，
	并且可以转换为任意语言中的对象，JSON在开发中主要用来数据的交互
- JSON
	- JavaScript Object Notation JS对象表示法
	- JSON和JS对象的格式一样，只不过JSON字符串中的属性名必须加双引号
		其他的和JS语法一致
JSON分类：
1. 对象 {}
2. 数组 []

JSON中允许的值:

1.字符串

2.数值

3.布尔值

4.null

5.对象

6.数组

---

json --> js对象

JSON.parse()

  - 可以将以JSON字符串转换为js对象. 它需要一个JSON字符串作为参数，会将该字符串转换为JS对象并返回

JS对象 ---> JSON

JSON.stringify()

  - 可以将一个JS对象转换为JSON字符串. 需要一个js对象作为参数，会返回一个JSON字符串

eval()
- 这个函数可以用来执行一段字符串形式的JS代码，并将执行结果返回
- 如果使用eval()执行的字符串中含有{},它会将{}当成是代码块, 如果不希望将其当成代码块解析，则需要在字符串前后各加一个()
- eval()这个函数的功能很强大，可以直接执行一个字符串中的js代码，但是在开发中尽量不要使用，首先它的执行性能比较差，然后它还具有安全隐患