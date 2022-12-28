## 面向对象

面向过程有什么缺点？（耦合度高，扩展力差。）

- 面向过程最主要是每一步与每一步的因果关系，其中A步骤因果关系到B步骤，A和B联合起来形成一个子模块，子模块和子模块之间又因为因果关系结合在一起，假设其中任何一个因果关系出现问题（错误），此时整个系统的运转都会出现问题。（代码和代码之间的耦合度太高，扩展力太差。）

面向过程有什么优点？（快速开发）

- 对于小型项目（功能），采用面向过程的方式进行开发，效率较高。不需要前期进行对象的提取，模型的建立，采用面向过程方式可以直接开始干活。一上来直接写代码，编写因果关系，从而实现功能。

什么是面向对象的开发方式？

- 采用面向对象的方式进行开发，更符合人类的思维方式。（面向对象成为主流的原因）人类就是以“对象”的方式去认识世界的。所以面向对象更容易让我们接受。

- 面向对象就是将现实世界分割成不同的单元，然后每一个单元都实现成对象，然后给一个环境驱动一下，让各个对象之间协作起来形成一个系统。

- 采用面向对象的方式进行开发：耦合度低，扩展力强。

- 面向对象当中最主要“一词”是：对象。

什么是类？

- 实际上在现实世界当中是不存在的，是一个抽象的概念。是一个模板。是我们人类大脑进行“思考、总结、抽象”的一个结果。(主要是因为人类的大脑不一般才有了类的概念。)

- 类本质上是现实世界当中某些事物具有共同特征，将这些共同特征提取出来形成的概念就是一个“类”，“类”就是一个模板。

什么是对象？对象是实际存在的个体。（真实存在的个体）

这几个术语你需要自己能够阐述出来：

- 类：不存在的，人类大脑思考总结一个模板（这个模板当中描述了共同特征。）

- 对象：实际存在的个体。

- 实例：对象还有另一个名字叫做实例。

- 实例化：通过类这个模板创建对象的过程，叫做：实例化。

- 抽象：多个对象具有共同特征，进行思考总结抽取共同特征的过程。

类 --【实例化】--> 对象(实例)

对象 --【抽象】--> 类

类是一个模板，是描述共同特征的一个模板，那么共同特征包括什么呢？

类 = 属性 + 方法

属性来源于：状态

方法来源于：动作

思考：“java软件工程师”在开发中起到的一个作用是什么？

我们为什么要做软件开发？说的大一些是为了人民服务。解决现实生活当中的问题。软件开发既然是为了解决现实世界当中的问题，那么首先java软件必须能够模拟现实世界。其实软件是一个虚拟的世界。这个虚拟的世界需要和现实世界一一对应，这才叫模拟。

### 类的定义

```java
[修饰符列表] class 类名{
	// 类体 = 属性 + 方法
	// 属性在代码上以“变量”的形式体现
	//方法描述动作、行为
}
```

```java
`public class XueSheng{ // 这个程序编译之后，会生成XueSheng.class字节码文件。
	// 属性
	// 学号（成员变量）
	int xueHao;
	// 姓名
	String xingMing;
	// 年龄
	int nianLing;
	// 性别
	boolean xingBie;
	// 住址
	String zhuZhi;
}
```

注意：修饰符列表可以省略。

为什么属性是“以”变量的形式存在的？是因为属性对应的是“数据”，数据在程序中只能放到变量中。结论：属性其实就是变量。

变量根据出现位置进行划分：

- 方法体当中声明的变量：局部变量。

- 方法体外声明的变量：成员变量。（这里的成员变量就是“属性”）

关于编译的过程

- 按说应该先编译XueSheng.java，然后再编译XueShengTest.java

- 但是对于编译器来说，编译XueShengTest.java文件的时候，会自动找XueSheng.class，如果没有，会自动编译XueSheng.java文件，生成XueSheng.class文件。

编译方法：

第一种方式：

- javac XueSheng.java

- javac XueShengTest.java

第二种方式：

- javac XueShengTest.java

第三种方式：

- javac *.java

在语法级别上是怎么完成对象创建的呢？

- 类名 变量名 = new 类名();

什么是实例变量？

- 对象又被称为实例。
- 实例变量实际上就是：对象级别的变量。

```java
public class 明星类{
	double height;
}
```

- 身高这个属性所有的明星对象都有，但是每一个对象都有“自己的身高值”。

- 假设创建10个明星对象，height变量应该有10份。

- 所以这种变量被称为对象级别的变量。属于实例变量。

实例变量在访问的时候，是不是必须先创建对象？是

对象和引用的区别？

- 对象是通过new出来的，在堆内存中存储。

- 引用是：但凡是变量，并且该变量中保存了内存地址指向了堆内存当中的对象的。

成员变量的默认值

|类型|默认值|
| ----- | ----- |
|   byte | 0 |
| short | 0|
| int | 0|
| long | 0L|
|float | 0.0F|
|double | 0.0|
| boolean | flase|
|char | \u0000|
|引用数据类型| null|

### 内存图

1、画内存图注意事项：

- 第一：大家在内存图上不要体现出代码。内存上应该主要体现“数据”。

- 第二：大家画图的时候，图上的图形应该有先后顺序，先画什么，再画什么，必须是有顺序的，而不是想起来这个画这个，想起来那个画那个。程序代码是有执行顺序的，程序执行到哪里你就画哪里就行了。

2、为什么要画内存图（非常重要）？

- 第一：有了内存图，程序不运行，我也知道结果。（可以推算出结果）

- 第二：有了内存图，有助于你调试程序。画内存图是对Java运行机制的一种理解。不知道运行机制，以后复杂的程序出现错误之后你是不会调试的。

所有的实例变量（属性）都是通过“引用.”来访问的。
	
引用和对象怎么区分？

- “引用”是是存储对象内存地址的一个变量。

- “对象”是堆里new出来的。
	
通俗一点：

- 只要这个变量中保存的是一个对象的内存地址，那么这个变量就叫做“引用”。
	
思考：

- 引用一定是局部变量吗？不一定。

```java
public class Test{
	public static void main(String[] args){

		// 家庭住址对象
		Address a = new Address();
		a.city = "北京";
		a.street = "大兴区";
		a.zipcode = "121221";
		
		// 用户对象
		User u = new User();
		System.out.println(u.id); // 0
		System.out.println(u.username); // null
		System.out.println(u.addr); // null

		u.id = 11111;
		u.username = "zhangsan";
		u.addr = a;

	}
}

public class User{
	int id; // 实例变量
	String username; // 实例变量
	Address addr; 
}


// 住址类
public class Address{

	// 一个家庭住址有3个属性。
	// 城市
	String city; // 实例变量
	// 街道
	String street;
	// 邮编
	String zipcode;
}

```

### 空指针异常

空指针异常。（NullPointerException）

关于垃圾回收器：GC

- 在java语言中，垃圾回收器主要针对的是堆内存。当一个java对象没有任何引用指向该对象的时候，GC会考虑将该垃圾数据释放回收掉。

出现空指针异常的前提条件是？"空引用"访问实例【对象相关】相关的数据时，都会出现空指针异常。

```java
public class NullPointerTest{
	public static void main(String[] args){
		// 创建客户对象
		Customer c = new Customer();
		// 访问这个客户的id
		System.out.println(c.id); // 0

		// 重新给id赋值
		c.id = 9521; // 终身代号
		System.out.println("客户的id是=" + c.id);
		//c = null;
		// NullPointerException
		// 编译器没问题，因为编译器只检查语法，编译器发现c是Customer类型，
		// Customer类型中有id属性，所以可以：c.id。语法过了。
		// 但是运行的时候需要对象的存在，但是对象没了，尴尬了，就只能出现一个异常。
		System.out.println(c.id);
	}
}

class Customer{
	// 客户id
	int id; // 成员变量中的实例变量，应该先创建对象，然后通过“引用.”的方式访问。
}
```

方法在调用的时候参数是如何传递的？

- 实际上，在java语言中，方法调用时参数传递，和类型无关，都是将变量中保存的那个“值”传过去，这个“值”可能是一个数字100，也可能是一个java对象的内存地址：0x1234记住这句话：不管是哪一种数据类型的传递，都是将“变量中保存的那个值复制一份传递过去。”


java中关于方法调用时参数传递实际上只有一个规则：

- 不管你是基本数据类型，还是引用数据类型，实际上在传递的时候都是将变量中保存的那个“值”复制一份，传过去。

```java
int x = 1;
int y = x; // 把x中保存1复制一份传给y
// x和y都是两个局部变量。

Person p1 = 0x1234;
Person p2 = p1; 把p1中保存的0x1234复制一份传给p2
// p1和p2都是两个局部变量。
```

你和你媳妇，都有你家大门上的钥匙，钥匙是两把。
但是都可以打开你家的大门。

```java
public class Test2{
	public static void main(String[] args){
		Person p = new Person();
		p.age = 10;
		add(p);
		System.out.println("main--->" + p.age); //11
	}
	// 方法的参数可以是基本数据类型，也可以是引用数据类型，只要是合法的数据类型就行。
	public static void add(Person p){ // p是add方法的局部变量。
		p.age++;
		System.out.println("add--->" + p.age); //11
	}
}

class Person{
	// 年龄属性，成员变量中的实例变量。
	int age;
}
```

### 构造方法

当一个类中没有提供任何构造方法，系统默认提供一个无参数的构造方法。这个无参数的构造方法叫做缺省构造器。

当一个类中手动的提供了构造方法，那么系统将不再默认提供无参数构造方法。

建议将无参数构造方法手动的写出来，这样一定不会出问题。

无参数构造方法和有参数的构造方法都可以调用。

```java
Student x = new Student();

Student y = new Student(123);
```

构造方法支持方法重载吗？

- 构造方法是支持方法重载的。

- 在一个类当中构造方法可以有多个。

- 并且所有的构造方法名字都是一样的。

- 特点：在同一个类中，方法名相同，参数列表不同。

对于实例变量来说，只要你在构造方法中没有手动给它赋值，统一都会默认赋值。默认赋系统值。

构造方法需要掌握的知识点：

1. 构造方法有什么作用？

2. 构造方法怎么定义，语法是什么？

3. 构造方法怎么调用，使用哪个运算符？

4. 什么是缺省构造器？

5. 怎么防止缺省构造器丢失？

6. 实例变量在类加载是初始化吗？实例变量在什么时候初始化？


构造方法

1、什么是构造方法，有什么用？

- 构造方法是用来创建对象，并且同时给对象的属性赋值。（注意：实例变量没有手动赋值的时候，系统会赋默认值。）

2、当一个类没有提供任何构造方法，系统会默认提供一个无参数的构造方法。（而这个构造方法被称为缺省构造器。）

3、调用构造方法怎么调用呢？使用哪个运算符呢？使用new运算符来调用构造方法。`new 构造方法名(实际参数列表);`

4、构造方法的语法结构是？

```java
[修饰符列表] 构造方法名(形式参数列表){
	构造方法体;
	通常在构造方法体当中给属性赋值，完成属性的初始化。
}
```

注意：

1. 修饰符列表目前统一写：public。千万不要写public static。

2. 构造方法名和类名必须一致。

3. 构造方法不需要指定返回值类型，也不能写void，写上void表示普通方法，就不是构造方法了。

普通方法的语法结构是？

```java
[修饰符列表] 返回值类型 方法名(形式参数列表){
	方法体;
}
```

1、构造方法对应的英语单词：Constructor【构造器】

2、构造方法作用：

- 创建对象，并且创建对象的过程中给属性赋值（初始化。）

以后开发的时候最好自己写出来一个默认无参构造函数

```java

public class ConstructorTest01{
	public static void main(String[] args){

		// 调用Student类的无参数构造方法
		new Student();

		// 调用普通方法
		ConstructorTest01.doSome();
		doSome();

		// 创建Student类型的对象
		Student s1 = new Student();

		// 输出“引用”
		//只要输出结果不是null，说明这个对象一定是创建完成了。
		// 此处的输出结果大家目前是看不懂的，后期再说。
		System.out.println(s1); //Student@54bedef2

		// 这是调用另一个有参数的构造方法。
		Student s3 = new Student(100);
		System.out.println(s3); //Student@5caf905d
	}

	public static void doSome(){
		System.out.println("do some!!!!");
	}
}
```

## 封装、this和static

### 封装

有了封装，才有继承，有了继承，才能说多态。

封装的作用有两个：

- 第一个作用：保证内部结构的安全。

- 第二个作用：屏蔽复杂，暴露简单。

在代码级别上，封装有什么用？

- 一个类体当中的数据，假设封装之后，对于代码的调用人员来说，不需要关心代码的复杂实现，只需要通过一个简单的入口就可以访问了。

- 类体中安全级别较高的数据封装起来，外部人员不能随意访问，来保证数据的安全性。

怎么进行封装

- 第一步：属性私有化（使用private关键字进行修饰。）

- 第二步：对外提供简单的操作入口。

第一步：属性私有化

第二步：1个属性对外提供两个set和get方法。外部程序只能通过set方法修改，只能通过get方法读取，可以在set方法中设立关卡来保证数据的安全性。

在强调一下：

- set和get方法都是实例方法，**不能带static**。

- 不带static的方法称为实例方法，实例方法的调用必须先new对象。

#### 封装过程

```java
public class Person{
	// private 表示私有的，被这个关键字修饰之后，该数据只能在本类中访问。
	// 出了这个类，age属性就无法访问了。私有的。
	private int age; // 每一个人年龄值不同，对象级别的属性。

	// 写一个方法专门来完成读。(get)
	// 写一个方法专门来完成写。(set)
	// get和set方法应该带有static，还是不应该有static,get和set方法应该定义为实例方法吗？
	// get读年龄，set改年龄，这个读和改都是操作的一个对象的年龄。（没有对象何来年龄）
	// 封装的第二步：对外提供公开的set方法和get方法作为操作入口。并且都不带static。都是实例方法。
	/*
		[修饰符列表] 返回值类型 方法名(形式参数列表){
		}

		注意：
			java开发规范中有要求，set方法和get方法要满足以下格式。
				get方法的要求：
					public 返回值类型 get+属性名首字母大写(无参){
						return xxx;
					}
				set方法的要求：
					public void set+属性名首字母大写(有1个参数){
						xxx = 参数;
					}
			
			大家尽量按照java规范中要求的格式提供set和get方法。
			如果不按照这个规范格式来，那么你的程序将不是一个通用的程序。

	*/
	// get方法
	public int getAge(){
		return age;
	}

	// set方法
	public void setAge(int nianLing){
		// 能不能在这个位置上设置关卡！！！！
		if(nianLing < 0 || nianLing > 150){
			System.out.println("对不起，年龄值不合法，请重新赋值！");
			return; //直接终止程序的执行。
		}
		//程序能够执行到这里，说明年龄一定是合法的。
		age = nianLing;
	}
}

```

#### static方法调用方式

```java
//带有static的方法
//没有static的方法
//分别怎么调用？
	//带有static的方法怎么调用？通过“类名.”的方式访问。

//对象被称为实例。
//实例相关的有：实例变量、实例方法。
//实例变量是对象变量。实例方法是对象方法。
//实例相关的都需要先new对象，通过“引用.”的方式去访问。
public class MethodTest{

	/*
	public MethodTest(){
	
	}
	*/

	public static void main(String[] args){
		MethodTest.doSome();
		//类名. 可以省略（在同一个类中。）
		doSome();
		// 尝试使用“类名.”的方式访问“实例方法”
		// 错误的
		//MethodTest.doOther();
		
		// 创建对象
		MethodTest mt = new MethodTest();
		// 通过"引用."的方式访问实例方法。
		mt.doOther();

	}	

	// 带有static
	public static void doSome(){
		System.out.println("do some!");
	}

	//这个方法没有static，这样的方法被称为：实例方法。（对象方法，对象级别的方法）
	//这个没法解释，大家目前死记硬背。
	public void doOther(){
		System.out.println("do other....");
	}

}
```

#### 再探空指针异常

```java

/*
空指针异常导致的最本质的原因是？
	空引用访问“实例相关的数据”，会出现空指针异常。
	实例相关的包括：实例变量 + 实例方法。
*/
public class NullPointerTest{
	public static void main(String[] args){
		User u = new User();
		System.out.println(u.id); // 0
		u.doSome();

		// 引用变成空null
		u = null;

		// id的访问，需要对象的存在。
		//System.out.println(u.id); // 空指针异常

		// 一个实例方法的调用也必须有对象的存在。
		//u.doSome(); // 空指针异常。
	}
}


// 类 = 属性 + 方法
// 属性描述状态
// 方法描述行为动作
class User{

	// 实例变量
	int id;

	// 实例方法（对象相关的方法，对象级别的方法，应该是一个对象级别的行为。）
	// 方法模拟的是对象的行为动作。
	public void doSome(){
		System.out.println("do some!");
	}

	// 考试的行为，由于每一个人考试之后的分数不一样，所以考试行为应该必须有对象的参与。
	public void exam(){
		
	}
}
```

### static

static修饰的统一都是静态的，都是类相关的，不需要new对象。直接采用“类名.”访问。

当一个属性是类级别的属性，所有对象的这个属性的值是一样的，建议定义为静态变量。

#### 实例和静态

```java
/*
	static:
		1、static翻译为“静态”
		2、所有static关键字修饰的都是类相关的，类级别的。
		3、所有static修饰的，都是采用“类名.”的方式访问。
		4、static修饰的变量：静态变量
		5、static修饰的方法：静态方法

	变量的分类：
		变量根据声明的位置进行划分：
			在方法体当中声明的变量叫做：局部变量。
			在方法体外声明的变量叫做：成员变量。

		成员变量又可以分为：
			实例变量
			静态变量
*/

class VarTest{

	// 以下实例的，都是对象相关的，访问时采用“引用.”的方式访问。需要先new对象。
	// 实例相关的，必须先有对象，才能访问，可能会出现空指针异常。
	// 成员变量中的实例变量
	int i;

	// 实例方法
	public void m2(){
		// 局部变量
		int x = 200;
	}


	// 以下静态的，都是类相关的，访问时采用“类名.”的方式访问。不需要new对象。
	// 不需要对象的参与即可访问。没有空指针异常的发生。
	// 成员变量中的静态变量
	static int k;

	// 静态方法
	public static void m1(){
		// 局部变量
		int m = 100;
	}
	
}

/*
	什么时候变量声明为实例的，什么时候声明为静态的？
		如果这个类型的所有对象的某个属性值都是一样的，不建议定义为实例变量，浪费内存空间。建议定义为类级别特征，定义为静态变量，在方法区中只保留一份，节省内存开销。

	一个对象一份的是实例变量。
	所有对象一份的是静态变量。
*/

// 定义一个类：中国人
class Chinese{

	// 身份证号
	// 每一个人的身份证号不同，所以身份证号应该是实例变量，一个对象一份。
	String idCard; 

	// 姓名
	// 姓名也是一个人一个姓名，姓名也应该是实例变量。
	String name;

	// 国籍
	// 重点重点五颗星：加static的变量叫做静态变量
	// 静态变量在类加载时初始化，不需要new对象，静态变量的空间就开出来了。
	// 静态变量存储在方法区。
	static String country = "中国";

	// 无参数
	public Chinese(){
	
	}

	// 有参数
	public Chinese(String s1,String s2){
		idCard = s1;
		name = s2;
	}
}



/*
	实例的：一定需要使用“引用.”来访问。

	静态的：
		建议使用“类名.”来访问，但使用“引用.”也行（不建议使用"引用."）。
		静态的如果使用“引用.”来访问会让程序员产生困惑：程序员以为是实例的呢。
	
	结论：
		空指针异常只有在什么情况下才会发生呢?只有在“空引用”访问“实例”相关的，都会出现空指针异常。
*/

/*
	关于方法来说，什么时候定义为实例方法？什么时候定义为静态方法？
		有没有参考标准。

		此方法一般都是描述了一个行为，如果说该行为必须由对象去触发。
		那么该方法定义为实例方法。

		参考标准：
			当这个方法体当中，直接访问了实例变量，这个方法一定是实例方法。

			我们以后开发中，大部分情况下，如果是工具类的话，工具类当中的方法
			一般都是静态的。(静态方法有一个优点，是不需要new对象，直接采用类名
			调用，极其方便。工具类就是为了方便，所以工具类中的方法一般都是static的。)

			什么是工具类？？？？？
				以后讲。（工具类就是为了方便编程而开发的一些类。）
	
	类 = 属性 + 方法
		属性描述的是：状态
		方法描述的是：行为动作
	
	一个方法代表了一个动作。

*/
```

#### 静态代码块

```java

/*
	1、使用static关键字可以定义：静态代码块
	2、什么是静态代码块，语法是什么？
		static {
			java语句;
			java语句;
		}
	3、static静态代码块在什么时候执行呢？
		类加载时执行。并且只执行一次。
		静态代码块有这样的特征/特点。

	4、注意：静态代码块在类加载时执行，并且在main方法执行之前执行。

	5、静态代码块一般是按照自上而下的顺序执行。

	6、静态代码块有啥作用，有什么用？
		第一：静态代码块不是那么常用。（不是每一个类当中都要写的东西。）
		第二：静态代码块这种语法机制实际上是SUN公司给我们java程序员的一个特殊的时刻/时机。这个时机叫做：类加载时机。

	具体的业务：
		项目经理说了：大家注意了，所有我们编写的程序中，只要是类加载了，请记录一下类加载的日志信息（在哪年哪月哪日几时几分几秒，哪个类加载到JVM当中了）。
	思考：这些记录日志的代码写到哪里呢？
		写到静态代码块当中。
		
*/
public class StaticTest06{

	// 静态代码块（特殊的时机：类加载时机。）
	static {
		System.out.println("A");
	}

	// 一个类当中可以编写多个静态代码块
	static {
		System.out.println("B");
	}

	// 入口
	public static void main(String[] args){
		System.out.println("Hello World!");
	}

	// 编写一个静态代码块
	static{
		System.out.println("C");
	}
}

/*
A
B
C
Hello World!
*/


/*
	栈：方法只要执行，会压栈。（局部变量）
	堆：new出来的对象都在堆中。垃圾回收器主要针对。（实例变量）
	方法区：类的信息，字节码信息，代码片段。（静态变量）

	方法的代码片段放在方法区，但是方法执行过程当中需要的内存在栈中。
*/
public class StaticTest07{
	
	// 静态变量在什么时候初始化？类加载时初始化。
	// 静态变量存储在哪里？方法区
	static int i = 100;

	// 静态代码块什么时候执行？类加载时执行。
	static {
		// 这里可以访问i吗？
		System.out.println("i = " + i);
	}

	// 实例变量
	int k = 111; // k变量是实例变量，在构造方法执行时内存空间才会开辟。

	static {
		//k变量可以访问吗？
		// static静态代码块在类加载时执行，并且只执行一次。
		// 类加载时，k变量空间还没有开辟出来呢。
		//错误: 无法从静态上下文中引用非静态 变量 k
		//System.out.println("k = " + k);

		// 这里可以访问name吗？
		//错误: 非法前向引用
		// 静态代码块和静态变量都在类加载的时候执行，时间相同，只能靠代码的顺序来决定谁先谁后。
		//System.out.println("name = " + name);
	}

	// 静态变量在静态代码块下面。
	static String name = "zhangsan";


	//入口(main方法执行之前实际上执行了很多代码)
	public static void main(String[] args){
		System.out.println("main begin");
		System.out.println("main over");
	}
}

/*
总结：
	到目前为止，你遇到的所有java程序，有顺序要求的是哪些？
		第一：对于一个方法来说，方法体中的代码是有顺序的，遵循自上而下的顺序执行。
		第二：静态代码块1和静态代码块2是有先后顺序的。
		第三：静态代码块和静态变量是有先后顺序的。(代码的顺序)
*/
```

#### 实例语句块

```java
/*
1、除了静态代码块之外，还有一种语句块叫做：实例语句块
2、实例语句在类加载是并没有执行。
3、实例语句语法？
	{
		java语句;
		java语句;
		java语句;
	}
4、实例语句块在什么时候执行？
	只要是构造方法执行，必然在构造方法执行之前，自动执行“实例语句块”中的代码。
	实际上这也是SUN公司为java程序员准备一个特殊的时机，叫做对象构建时机。
*/
public class InstanceCode{

	//入口
	public static void main(String[] args){
		System.out.println("main begin");
		new InstanceCode();
		new InstanceCode();

		new InstanceCode("abc");
		new InstanceCode("xyz");
	}


	//实例语句块
	{
		System.out.println("实例语句块执行！");	
	}

	// Constructor
	public InstanceCode(){
		System.out.println("无参数构造方法");
	}

	// Constructor
	public InstanceCode(String name){
		System.out.println("有参数的构造方法");
	}

}
```

#### 代码执行顺序

```java
//判断以下程序的执行顺序
public class CodeOrder{
	
	// 静态代码块
	static{
		System.out.println("A");
	}

	// 入口
	// A X Y C B Z
	public static void main(String[] args){
		System.out.println("Y");
		new CodeOrder();
		System.out.println("Z");
	}

	// 构造方法
	public CodeOrder(){
		System.out.println("B");
	}

	// 实例语句块
	{
		System.out.println("C");
	}

	// 静态代码块
	static {
		System.out.println("X");
	}

}
```

### this

- this是一个关键字，是一个引用，保存内存地址指向自身。
- this可以使用在实例方法中，也可以使用在构造方法中。
- this出现在实例方法中其实代表的是当前对象。
- this不能使用在静态方法中。
- this. 大部分情况下可以省略，但是用来区分局部变量和实例变量的时候不能省略。
- this() 这种语法只能出现在构造方法第一行，表示当前构造方法调用本类其他的构造方法，目的是代码复用。

```java
/*
	this：
		1、this是一个关键字，全部小写。
		2、this是什么，在内存方面是怎样的？
			一个对象一个this。
			this是一个变量，是一个引用。this保存当前对象的内存地址，指向自身。
			所以，严格意义上来说，this代表的就是“当前对象”
			this存储在堆内存当中对象的内部。

		3、this只能使用在实例方法中。谁调用这个实例方法，this就是谁。所以this代表的是：当前对象。

		4、“this.”大部分情况下是可以省略的。

		5、为什么this不能使用在静态方法中？this代表当前对象，静态方法中不存在当前对象。
*/

// 顾客类
class Customer{

	// 属性
	// 实例变量（必须采用“引用.”的方式访问）
	String name;   

	//构造方法
	public Customer(){
	
	}

	public Customer(String s){
		this.name = s;
	}

	// 顾客购物的方法
	// 实例方法
	public void shopping(){
		// 这里的this是谁？this是当前对象。
		// c1调用shopping(),this是c1
		// c2调用shopping(),this是c2
		//System.out.println(this.name + "正在购物!");

		// this. 是可以省略的。
		// this. 省略的话，还是默认访问“当前对象”的name。
		System.out.println(name + "正在购物!");
	}

	// 静态方法
	public static void doSome(){
		// this代表的是当前对象，而静态方法的调用不需要对象。矛盾了。
		// 错误: 无法从静态上下文中引用非静态 变量 this
		//System.out.println(this);
	}
}

class Student{

	// 实例变量，怎么访问？必须先new对象，通过“引用.”来访问。
	String name = "zhangsan";

	// 静态方法
	public static void m1(){
		//System.out.println(name);

		// this代表的是当前对象。
		//System.out.println(this.name);

		// 除非你这样
		Student s = new Student();
		System.out.println(s.name);

	}

	//为什么set和get方法是实例方法？this不能出现在静态方法中
	public static void setName(String s){
		name = s;
	}
	public String getName(){
		return name;
	}

	// 又回到上午的问题了？什么时候方法定义为实例方法，什么时候定义为静态方法？
	// 如果方法中直接访问了实例变量，该方法必须是实例方法。
}
```


![1592899792382](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1592899792382.png)

```java

// 分析：i变量在main方法中能不能访问？？？？

public class ThisTest02{

	// 实例变量
	int i = 100; // 这个i变量是不是必须先new对象才能访问。

	// 静态变量
	static int k = 111;

	// 静态方法
	public static void main(String[] args){
		// 错误: 无法从静态上下文中引用非静态 变量 i
		// System.out.println(i);

		// 怎么样访问i
		ThisTest02 tt = new ThisTest02();
		System.out.println(tt.i);

		// 静态变量用“类名.”访问。
		System.out.println(ThisTest02.k);

		// 类名. 能不能省略？
		// 可以
		System.out.println(k);
	}
}
```

this什么时候可以省略？

```java

/*
1、this可以使用在实例方法中，不能使用在静态方法中。
2、this关键字大部分情况下可以省略，什么时候不能省略呢？
	在实例方法中，或者构造方法中，为了区分局部变量和实例变量，
	这种情况下：this. 是不能省略的。
*/
public class ThisTest03{
	public static void main(String[] args){

		Student s = new Student();
		s.setNo(111);
		s.setName("张三");
		System.out.println("学号：" + s.getNo());
		System.out.println("姓名：" + s.getName());
	}
}

// 分析一下：以下代码哪里写的不好。
// 学生类
class Student{
	//学号
	private int no;

	//姓名
	private String name;

	// setter and getter方法
	/*
	public void setNo(int i){
		no = i;
	}
	*/
	/*
	public void setNo(int no){ // 就近原则。
		no = no; //这两个no都是局部变量no，和实例变量no没关系。
	}
	*/
	public void setNo(int no){ 
		//no是局部变量
		//this.no 是指的实例变量。
		this.no = no; // this. 的作用是：区分局部变量和实例变量。
	}
	
	public String getName(){ // getName实际上获取的是“当前对象”的名字。
		//return this.name; // 严格来说，这里是有一个 this. 的。只不过这个 this. 是可以省略的。
		return name;
	}
}
```

this()的使用时机

```java
/*
	1、this除了可以使用在实例方法中，还可以用在构造方法中。
	2、新语法：通过当前的构造方法去调用另一个本类的构造方法，可以使用以下语法格式：
		this(实际参数列表);
			通过一个构造方法1去调用构造方法2，可以做到代码复用。
			但需要注意的是：“构造方法1”和“构造方法2” 都是在同一个类当中。

	3、this() 这个语法作用是什么？
		代码复用。
	
	4、死记硬背：
		对于this()的调用只能出现在构造方法的第一行。
*/
public class ThisTest04{
	public static void main(String[] args){
		// 调用无参数构造方法
		Date d1 = new Date();
		d1.detail();

		// 调用有参数构造方法
		Date d2 = new Date(2008, 8, 8);
		d2.detail();
	}
}

/*
需求：
	1、定义一个日期类，可以表示年月日信息。
	2、需求中要求：
		如果调用无参数构造方法，默认创建的日期为：1970年1月1日。
		当然，除了调用无参数构造方法之外，也可以调用有参数的构造方法来创建日期对象。
*/
class Date{ // 以后写代码都要封装，属性私有化，对外提供setter and getter
	//年
	private int year;
	//月
	private int month;
	//日
	private int day;

	// 构造方法无参
	// 调用无参数构造方法，初始化的日期是固定值。
	public Date(){
		//错误: 对this的调用必须是构造器中的第一个语句
		this(1970, 1, 1);
	}
	// 构造方法有参数
	public Date(int year, int month, int day){
		this.year = year;
		this.month = month;
		this.day = day;
	}
}
```

this 复习
```java

public class Review{ // 类
	// 类加载机制中，是这样的：在程序执行之前，凡是需要加载的类全部加载到JVM当中。
	// 先完成加载才会执行main方法。
	static{
		System.out.println("Review类加载时执行！");
	}
	// 入口
	// 静态方法
	public static void main(String[] args){
		// 局部变量
		int i = 100;
		// 完成一个对象的一连串动作。
		// 一个学生在教室先学习，学习完成之后去餐厅吃饭。
		Student s1 = new Student();
		// 先学习，所有调用学习这个实例方法。
		s1.study();
		Student s2 = new Student();
	}
}

```

## 继承

继承的作用：
基本作用：子类继承父类，代码可以得到复用。（这个不是重要的作用，是基本作用。）
主要(重要)作用：因为有了继承关系，才有了后期的方法覆盖和多态机制。

举例

```java

// 使用继承机制来解决代码复用问题。
// 继承也是存在缺点的：耦合度高，父类修改，子类受牵连。

// 银行账户类
// 账户的属性：账号、余额
class Account{ // 父类
	// 属性
	private String actno;
	private double balance;

	// 构造方法
	public Account(){
	
	}
	public Account(String actno, double balance){
		this.actno = actno;
		this.balance = balance;
	}

	// setter and getter
	public void setActno(String actno){
		this.actno = actno;
	}
	public String getActno(){
		return actno;
	}
	public void setBalance(double balance){
		this.balance = balance;
	}
	public double getBalance(){
		return balance;
	}
}

// 其它类型的账户：信用卡账户
// 账号、余额、信誉度
class CreditAccount extends Account{ //子类

	// 属性
	private double credit;

	// 构造方法
	public CreditAccount(){
	
	}

	public void doSome(){
		//错误: actno 在 Account 中是 private 访问控制
		//System.out.println(actno);
		// 间接访问
		//System.out.println(this.getActno());
		System.out.println(getActno());
	}

	// setter and getter方法
	public void setCredit(double credit){
		this.credit = credit;
	}
	public double getCredit(){
		return credit;
	}
	
}
```

### 相关特性

1. ①B类继承A类，则称A类为超类(superclass)、父类、基类，B类则称为子类(subclass)、派生类、扩展类。
class A{}
class B extends A{}
我们平时聊天说的比较多的是：父类和子类。superclass 父类, subclass 子类

2. java 中的继承只支持单继承，**不支持多继承**，C++中支持多继承，这也是 java 体现简单性的一点，换句话说，java 中不允许这样写代码：class B extends A,C{ } 这是错误的。

3. 虽然 java 中不支持多继承，但有的时候会产生间接继承的效果，例如：class C extends B，class B extends A，也就是说，C 直接继承 B，其实 C 还间接继承 A。

4.  java 中规定，子类继承父类，除构造方法不能继承之外，剩下都可以继承。但是私有的属性无法在子类中直接访问。(父类中private修饰的不能在子类中直接访问。可以通过间接的手段来访问。)

5.  java 中的类没有显示的继承任何类，则**默认继承 Object类**，Object类是java 语言提供的根类（老祖宗类），也就是说，一个对象与生俱来就有Object类型中所有的特征。

6.  继承也存在一些缺点，例如：CreditAccount 类继承 Account 类会导致它们之间的耦合度非常高，Account 类发生改变之后会马上影响到 CeditAccount 类

子类继承父类之后，能使用子类对象调用父类方法吗？可以，因为子类继承了父类之后，这个方法就属于子类了。当然可以使用子类对象来调用。

在实际开发中，满足什么条件的时候，我可以使用继承呢？
凡是采用“is a”能描述的，都可以继承。
例如：
Cat is a Animal：猫是一个动物
Dog is a Animal：狗是一个动物
CreditAccount is a Account：信用卡账户是一个银行账户
....

假设以后的开发中有一个A类，有一个B类，A类和B类确实也有重复的代码，
那么他们两个之间就可以继承吗？不一定，还是要看一看它们之间是否能够
使用is a来描述。

我们研究了一下Object类当中有很多方法，大部分看不懂，其中有一个叫做toString()的，我们进行了测试，发现：System.out.println(引用); 当直接输出一个“引用”的时候，println()方法会先自动调用“引用.toString()”，然后输出toString()方法的执行结果。

## 方法覆盖和多态

### 方法覆盖

#### 何时使用

- 父类中的方法无法满足子类的业务需求，子类有必要对继承过来的方法进行覆盖。

什么条件满足的时候构成方法覆盖？

- 第一：有继承关系的两个类
- 第二：具有相同方法名、返回值类型、形式参数列表
- 第三：访问权限不能更低。
- 第四：抛出异常不能更多。

```java
/*
	回顾一下方法重载！！！！
		什么时候考虑使用方法重载overload？
			当在一个类当中，如果功能相似的话，建议将名字定义的一样，这样
			代码美观，并且方便编程。
		
		什么条件满足之后能够构成方法重载overload？
			条件一：在同一个类当中
			条件二：方法名相同
			条件三：参数列表不同（个数、顺序、类型）

	--------------------------------------------------------------------------------

	什么时候我们会考虑使用“方法覆盖”呢？
		子类继承父类之后，当继承过来的方法无法满足当前子类的业务需求时，
		子类有权利对这个方法进行重新编写，有必要进行“方法的覆盖”。
	
	方法覆盖又叫做：方法重写（重新编写），英语单词叫做：Override、Overwrite，都可以。
	比较常见的：方法覆盖、方法重写、override

	重要结论：
		当子类对父类继承过来的方法进行“方法覆盖”之后，
		子类对象调用该方法的时候，一定执行覆盖之后的方法。

	当我们代码怎么编写的时候，在代码级别上构成了方法覆盖呢？
		条件一：两个类必须要有继承关系。
		条件二：重写之后的方法和之前的方法具有：
					相同的返回值类型、
					相同的方法名、
					相同的形式参数列表。
		条件三：访问权限不能更低，可以更高。（这个先记住。）
		条件四：重写之后的方法不能比之前的方法抛出更多的异常，可以更少。（这个先记住）
	
	这里还有几个注意事项：（这几个注意事项，当学习了多态语法之后自然就明白了！）
		注意1：方法覆盖只是针对于方法，和属性无关。
		注意2：私有方法无法覆盖。
		注意3：构造方法不能被继承，所以构造方法也不能被覆盖。
		注意4：方法覆盖只是针对于“实例方法”，“静态方法覆盖”没有意义。

*/
public class OverrideTest02{
	public static void main(String[] args){
		Bird b = new Bird();
		b.move();
		b.sing(1000); //Animal sing....

		Cat c = new Cat();
		c.move();
	}
}

class Animal{
	public void move(){
		System.out.println("动物在移动！");
	}

	public void sing(int i){
		System.out.println("Animal sing....");
	}
}

class Bird extends Animal{

	// 对move方法进行方法覆盖，方法重写，override
	// 最好将父类中的方法原封不动的复制过来。（不建议手动编写）
	// 方法覆盖，就是将继承过来的那个方法给覆盖掉了。继承过来的方法没了。
	public void move(){
		System.out.println("鸟儿在飞翔！！！");
	}

	//protected表示受保护的。没有public开放。
	// 错误：正在尝试分配更低的访问权限; 以前为public
	/*
	protected void move(){
		System.out.println("鸟儿在飞翔！！！");
	}
	*/

	//错误：被覆盖的方法未抛出Exception
	/*
	public void move() throws Exception{
		System.out.println("鸟儿在飞翔！！！");
	}
	*/

	// 分析：这个sing()和父类中的sing(int i)有没有构成方法覆盖呢？
	// 没有，原因是，这两个方法根本就是两个完全不同的方法。
	// 可以说这两个方法构成了方法重载吗？可以。
	public void sing(){
		System.out.println("Bird sing.....");
	}
}
```


#### 关于Object类中toString()方法的覆盖

toString()方法存在的作用就是：将java对象转换成字符串形式。大多数的java类toString()方法都是需要覆盖的。因为Object类中提供的toString()方法输出的是一个java对象的内存地址。

至于toString()方法具体怎么进行覆盖？格式可以自己定义，或者听需求的。

```java
/*
	关于Object类中的toString()方法
		1、toString()方法的作用是什么？
			作用：将“java对象”转换成“字符串的形式”。

		2、Object类中toString()方法的默认实现是什么？
			public String toString() {
				return getClass().getName() + "@" + Integer.toHexString(hashCode());
			}
			toString: 方法名的意思是转换成String
			含义：调用一个java对象的toString()方法就可以将该java对象转换成字符串的表示形式。

		3、那么toString()方法给的默认实现够用吗？
*/
public class OverrideTest04{
	public static void main(String[] args){
		// 创建一个日期对象
		MyDate t1 = new MyDate();

		// 大家是否还记得：当输出一个引用的时候，println方法会自动调用引用的toString方法。
		System.out.println(t1);

		//创建学生对象
		Student s = new Student(1111, "zhangsan");
		// 重写toString()方法之前
		//System.out.println(s); //Student@87aac27
		// 重写toString()方法之后
		// 输出一个学生对象的时候，可能更愿意看到学生的信息，不愿意看到对象的内存地址。
		System.out.println(s.toString());
		System.out.println(s);//自动调用toString方法
	}
}

// 日期类
class MyDate {
	private int year;
	private int month;
	private int day;
	public MyDate(){
		this(1970,1,1);
	}
	// constructor
	...
	// setters and getters 
	...

	// 从Object类中继承过来的那个toString()方法已经无法满足我业务需求了。
	// 我在子类MyDate中有必要对父类的toString()方法进行覆盖/重写。
	// 我的业务要求是：调用toString()方法进行字符串转换的时候，
	// 希望转换的结果是：xxxx年xx月xx日，这种格式。
	// 重写一定要复制粘贴，不要手动编写，会错的。
	public String toString() {
		return year + "年" + month + "月" + day + "日";
	}
}

class Student{
	int no;
	String name;
	public Student(int no, String name){
		this.no = no;
		this.name = name;
	}
	// 重写  方法覆盖
	public String toString() {
		return "学号：" + no + "，姓名：" + name;
	}
}
```

#### 方法重载和方法覆盖的区别

方法重载发生在同一个类当中。
方法覆盖是发生在具有继承关系的父子类之间。
方法重载是一个类中，方法名相同，参数列表不同。
方法覆盖是具有继承关系的父子类，并且重写之后的方法必须和之前的方法一致：方法名一致、参数列表一致、返回值类型一致。


### 多态

#### 多态的基础语法

向上转型和向下转型的概念

![1592956803661](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1592956803661.png)

向上转型：子--->父 (upcasting)
又被称为自动类型转换：Animal a = new Cat();

向下转型：父--->子 (downcasting)
又被称为强制类型转换：Cat c = (Cat)a; 需要添加强制类型转换符。

什么时候需要向下转型？
- 需要调用或者执行子类对象中特有的方法。必须进行向下转型，才可以调用。

向下转型有风险吗？
- 容易出现ClassCastException（类型转换异常）

怎么避免这个风险？
- instanceof运算符，可以在程序运行阶段动态的判断某个引用指向的对象
是否为某一种类型。

-> 养成好习惯，向下转型之前一定要使用instanceof运算符进行判断。

不管是向上转型还是向下转型，首先他们之间必须有继承关系，这样编译器就不会报错。

```java
/*
	多态的基础语法：
		1、学习多态基础语法之前，我们需要普及两个概念：
			第一个：向上转型
				子 ---> 父（自动类型转换）
			第二个：向下转型
				父 ---> 子（强制类型转换，需要加强制类型转换符）

			注意：
				java中允许向上转型，也允许向下转型。

				*****（五颗星）无论是向上转型，还是向下转型，两种类型之间必须有继承关系，没有继承关系编译器报错。
				
				以后在工作过程中，和别人聊天的时候，要专业一些，说向上转型和向下转型，不要说自动类型转换，也不要说强制类型转换，因为自动类型转换和强制类型转换是使用在基本数据类型方面的，在引用类型转换这里只有向上和向下转型。
		
		2、多态指的是：
			父类型引用指向子类型对象。
			包括编译阶段和运行阶段。
			编译阶段：绑定父类的方法。
			运行阶段：动态绑定子类型对象的方法。
			多种形态。
		
		3、什么时候必须使用“向下转型”？
			不要随便做强制类型转换。当你需要访问的是子类对象中“特有”的方法。此时必须进行向下转型。
*/
public class Test01{

	public static void main(String[] args){

		Animal a1 = new Animal();
		a1.move(); //动物在移动！

		Cat c1 = new Cat();
		c1.move(); //cat走猫步！

		Bird b1 = new Bird();
		b1.move(); //鸟儿在飞翔！

		// 代码可以这样写吗？
		/*
			1、Animal和Cat之间有继承关系吗？有的。
			2、Animal是父类，Cat是子类。
			3、Cat is a Animal，这句话能不能说通？能。
			4、经过测试得知java中支持这样的一个语法：
				父类型的引用允许指向子类型的对象。
				Animal a2 = new Cat();
				a2就是父类型的引用。new Cat()是一个子类型的对象。允许a2这个父类型引用指向子类型的对象。
		*/
		Animal a2 = new Cat();
		Animal a3 = new Bird();

		// 没有继承关系的两个类型之间存在转型吗？
		// 错误: 不兼容的类型: Dog无法转换为Animal
		// Animal a4 = new Dog();（Dog没有继承Animal）

		// 调用a2的move()方法
		/*
			什么是多态？
				多种形态，多种状态。
			分析：a2.move();
				java程序分为编译阶段和运行阶段。
				先来分析编译阶段：
					对于编译器来说，编译器只知道a2的类型是Animal，所以编译器在检查语法的时候，会去Animal.class字节码文件中找move()方法，找到了，绑定上move()方法，编译通过，静态绑定成功。（编译阶段属于静态绑定。）
				再来分析运行阶段：
					运行阶段的时候，实际上在堆内存中创建的java对象是Cat对象，所以move的时候，真正参与move的对象是一只猫，所以运行阶段会动态执行Cat对象的move()方法。这个过程属于运行阶段绑定。（运行阶段绑定属于动态绑定。）

			多态表示多种形态：
				编译的时候一种形态。
				运行的时候另一种形态。
		*/
		a2.move(); //cat走猫步！
		
		// 调用a3的move()方法
		a3.move(); //鸟儿在飞翔！！！

		// ======================================================================
		Animal a5 = new Cat(); // 底层对象是一只猫。

		// 分析这个程序能否编译和运行呢？
		// 分析程序一定要分析编译阶段的静态绑定和运行阶段的动态绑定。
		// 只有编译通过的代码才能运行。没有编译，根本轮不到运行。
		// 错误: 找不到符号
		// why??? 因为编译器只知道a5的类型是Animal，去Animal.class文件中找catchMouse()方法
		// 结果没有找到，所以静态绑定失败，编译报错。无法运行。（语法不合法。）
		//a5.catchMouse(); 
		
		// 假设代码写到了这里，我非要调用catchMouse()方法怎么办？
		// 这个时候就必须使用“向下转型”了。（强制类型转换）
		// 以下这行代码为啥没报错？？？？
		// 因为a5是Animal类型，转成Cat，Animal和Cat之间存在继承关系。所以没报错。
		Cat x = (Cat)a5;
		x.catchMouse(); //猫正在抓老鼠！！！！

		// 向下转型有风险吗？
		Animal a6 = new Bird(); //表面上a6是一个Animal，运行的时候实际上是一只鸟儿。
		/*
			分析以下程序，编译报错还是运行报错？？？
				编译器检测到a6这个引用是Animal类型，
				而Animal和Cat之间存在继承关系，所以可以向下转型。
				编译没毛病。

				运行阶段，堆内存实际创建的对象是：Bird对象。
				在实际运行过程中，拿着Bird对象转换成Cat对象就不行了。因为Bird和Cat之间没有继承关系。
			
			运行是出现异常，这个异常和空指针异常一样非常重要，也非常经典：
				java.lang.ClassCastException：类型转换异常。
			
			java.lang.NullPointerException：空指针异常。这个也非常重要。
		*/
		//Cat y = (Cat)a6;
		//y.catchMouse();

		// 怎么避免ClassCastException异常的发生？？？
		/*	
			新的内容，运算符：
				instanceof （运行阶段动态判断）
			第一：instanceof可以在运行阶段动态判断引用指向的对象的类型。
			第二：instanceof的语法：(引用 instanceof 类型)
			第三：instanceof运算符的运算结果只能是：true/false
			第四：c是一个引用，c变量保存了内存地址指向了堆中的对象。
				假设(c instanceof Cat)为true表示:c引用指向的堆内存中的java对象是一个Cat。
				假设(c instanceof Cat)为false表示:c引用指向的堆内存中的java对象不是一个Cat。
			
			程序员要养成一个好习惯：
				任何时候，任何地点，对类型进行向下转型时，一定要使用instanceof 运算符进行判断。（java规范中要求的。）
				这样可以很好的避免：ClassCastException
		*/
		System.out.println(a6 instanceof Cat); //false

		if(a6 instanceof Cat){ // 如果a6是一只Cat
			Cat y = (Cat)a6;  // 再进行强制类型转换
			y.catchMouse();
		}
	}
}
```

多种形态，多种状态，编译和运行有两个不同的状态。
编译期叫做静态绑定。
运行期叫做动态绑定。
Animal a = new Cat();
// 编译的时候编译器发现a的类型是Animal，所以编译器会去Animal类中找move()方法
// 找到了，绑定，编译通过。但是运行的时候和底层堆内存当中的实际对象有关
// 真正执行的时候会自动调用“堆内存中真实对象”的相关方法。
a.move();

多态的典型代码：父类型的引用指向子类型的对象。（java中允许这样写代码！！！）

什么时候必须进行向下转型？调用子类对象上特有的方法时。


#### 为什么要用instanceof

```java
public class AnimalTest{
	
	// test方法是程序员B负责编写。
	// 这个test()方法的参数是一个Animal
	public void test(Animal a){ // 实例方法
		// 你写的这个方法别人会去调用。
		// 别人调用的时候可能给你test()方法传过来一个Bird
		// 当然也可能传过来一个Cat
		// 对于我来说，我不知道你调用的时候给我传过来一个啥。
		if(a instanceof Cat){
			Cat c = (Cat)a;
			c.catchMouse();
		}else if(a instanceof Bird){
			Bird b = (Bird)a;
			b.sing();
		}
	}

}
```

#### 多态在开发中的作用

```java
/*

	注意这里的分析：
		主人起初的时候只喜欢养宠物狗狗
		随着时间的推移，主人又喜欢上养“猫咪”
		在实际的开发中这就表示客户产生了新的需求。
		作为软件的开发人员来说，必须满足客户的需求。
		我们怎么去满足客户的需求呢？
			在不使用多态机制的前提下，目前我们只能在Master类中添加一个新的方法。
	
	思考：软件在扩展新需求过程当中，修改Master这个类有什么问题？
		一定要记住：软件在扩展过程当中，修改的越少越好。
		修改的越多，你的系统当前的稳定性就越差，未知的风险就越多。

		其实这里涉及到一个软件的开发原则：
			软件开发原则有七大原则（不属于java，这个开发原则属于整个软件业）：
				其中有一条最基本的原则：OCP（开闭原则）

		什么是开闭原则？
			对扩展开放（你可以额外添加，没问题），对修改关闭（最好很少的修改现有程序）。
			在软件的扩展过程当中，修改的越少越好。


	高手开发项目不是仅仅为了实现客户的需求，还需要考虑软件的扩展性。

	什么是软件扩展性？
		假设电脑中的内存条部件坏了，我们可以买一个新的插上，直接使用。
		这个电脑的设计就考虑了“扩展性”。内存条的扩展性很好。

	面向父类型编程，面向更加抽象进行编程，不建议面向具体编程。
	因为面向具体编程会让软件的扩展力很差。

*/
```

非常重要：五颗星。

多态在开发中的作用是：降低程序的耦合度，提高程序的扩展力。

```java
public class Master{
public void feed(Dog d){}
public void feed(Cat c){}
}

//以上的代码中表示：Master和Dog以及Cat的关系很紧密（耦合度高）。导致扩展力很差。

public class Master{
public void feed(Pet pet){
pet.eat();
}
}
//以上的代表中表示：Master和Dog以及Cat的关系就脱离了，Master关注的是Pet类。
//这样Master和Dog以及Cat的耦合度就降低了，提高了软件的扩展性。
```

有了封装，有了这种整体的概念之后。
对象和对象之间产生了继承。
有了继承之后，才有了方法的覆盖和多态。

这里提到了一个软件开发原则：
七大原则最基本的原则：OCP（对扩展开放，对修改关闭）
目的是：降低程序耦合度，提高程序扩展力。
面向抽象编程，不建议面向具体编程。


#### 解释之前遗留的问题

私有方法无法覆盖。

方法覆盖只是针对于“实例方法”，“静态方法覆盖”没有意义。（这是因为方法覆盖通常和多态联合起来）

总结两句话：私有不能覆盖。静态不谈覆盖。

在方法覆盖中，关于方法的返回值类型。
什么条件满足之后，会构成方法的覆盖呢？

1. 发生具有继承关系的两个类之间。
2. 父类中的方法和子类重写之后的方法：具有相同的方法名、相同的形式参数列表、相同的返回值类型。


```java
/*
	1、方法覆盖需要和多态机制联合起来使用才有意义。
		Animal a = new Cat();
		a.move();
		要的是什么效果？
			编译的时候move()方法是Animal的。
			运行的时候自动调用到子类重写move()方法上。

		假设没有多态机制，只有方法覆盖机制，你觉得有意义吗？
			没有多态机制的话，方法覆盖可有可无。

			没有多态机制，方法覆盖也可以没有，如果父类的方法无法满足
			子类业务需求的时候，子类完全可以定义一个全新的方法。

		方法覆盖和多态不能分开。

	2、静态方法存在方法覆盖吗？
		多态自然就和对象有关系了。
		而静态方法的执行不需要对象。
		所以，一般情况下，我们会说静态方法“不存在”方法覆盖。
		不探讨静态方法的覆盖。

*/
public class OverrideTest05{
	public static void main(String[] args){
		// 静态方法可以使用“引用.”来调用吗？可以
		// 虽然使用“引用.”来调用，但是和对象无关。
		Animal a = new Cat(); //多态
		// 静态方法和对象无关。
		// 虽然使用“引用.”来调用。但是实际运行的时候还是：Animal.doSome()
		a.doSome();
		
		Animal.doSome();
		Cat.doSome();
	}
}

```

“相同的返回值类型”可以修改一下吗？

- 对于返回值类型是基本数据类型来说，必须一致。
- 对于返回值类型是引用数据类型来说，重写之后返回值类型可以变的更小（但意义不大，实际开发中没人这样写。）。

## super

### 与this相比

- super能出现在实例方法和构造方法中。
- super的语法是：“super.”、“super()”
- super不能使用在静态方法中。
- super. 大部分情况下是可以省略的。


```java
/*
	1、super是一个关键字，全部小写。
	2、super和this对比着学习。
		this:
			this能出现在实例方法和构造方法中。
			this的语法是：“this.”、“this()”
			this不能使用在静态方法中。
			this. 大部分情况下是可以省略的。
			this.什么时候不能省略呢？ 在区分局部变量和实例变量的时候不能省略。
				public void setName(String name){
					this.name = name;
				}
			this() 只能出现在构造方法第一行，通过当前的构造方法去调用“本类”中
			其它的构造方法，目的是：代码复用。

		super:
			super能出现在实例方法和构造方法中。
			super的语法是：“super.”、“super()”
			super不能使用在静态方法中。
			super. 大部分情况下是可以省略的。
			super.什么时候不能省略呢？ 
			super() 只能出现在构造方法第一行，通过当前的构造方法去调用“父类”中
			的构造方法，目的是：创建子类对象的时候，先初始化父类型特征。

	3、super()
		表示通过子类的构造方法调用父类的构造方法。
		模拟现实世界中的这种场景：要想有儿子，需要先有父亲。
	
	4、重要的结论：
		当一个构造方法第一行：
			既没有this()又没有super()的话，默认会有一个super();
			表示通过当前子类的构造方法调用父类的无参数构造方法。
			所以必须保证父类的无参数构造方法是存在的。
	
	5、注意：
		this()和super() 不能共存，它们都是只能出现在构造方法第一行。
	
	6、无论是怎样折腾，父类的构造方法是一定会执行的。（百分百的。）
	
*/
public class SuperTest01{
	public static void main(String[] args){
		// 创建子类对象
		/*
			A类的无参数构造方法！
			B类的无参数构造方法！
		*/
		new B();
	}
}

class A{

	// 建议手动的将一个类的无参数构造方法写出来。
	public A(){
		//super(); // 这里也是默认有这一行代码的。
		System.out.println("A类的无参数构造方法！");
	}

	// 一个类如果没有手动提供任何构造方法，系统会默认提供一个无参数构造方法。
	// 一个类如果手动提供了一个构造方法，那么无参数构造系统将不再提供。
	public A(int i){
		//super();
		System.out.println("A类的有参数构造方法(int)");
	}
}

class B extends A{
	/*
	public B(){
		super();
		System.out.println("B类的无参数构造方法！");
	}
	*/

	public B(){
		this("zhangsan");
		// 调用父类中有参数的构造方法
		//super(123);
		System.out.println("B类的无参数构造方法！");
	}

	public B(String name){
		super();
		System.out.println("B类的有参数构造方法(String)");
	}
}
```



```java
/*
	1、举个例子：在恰当的时间使用：super(实际参数列表);
	2、注意：在构造方法执行过程中一连串调用了父类的构造方法，
	父类的构造方法又继续向下调用它的父类的构造方法，但是实际上
	对象只创建了一个。

	3、思考：“super(实参)”到底是干啥的？
		super(实参)的作用是：初始化当前对象的父类型特征。
		并不是创建新对象。实际上对象只创建了1个。
	
	4、super关键字代表什么？
		super关键字代表的就是“当前对象”的那部分父类型特征。
		
	5、 super和this都不能出现在静态方法中。
*/

```

super的使用：
super.属性名   【访问父类的属性】
super.方法名(实参)   【访问父类的方法】
super(实参)   【调用父类的构造方法】


### 什么时候可以省略

super.什么时候不能省略呢？
- 父类和子类中有同名属性，或者说有同样的方法，想在子类中访问父类的，super. 不能省略。

super() 只能出现在构造方法第一行，通过当前的构造方法去调用“父类”中
的构造方法，目的是：创建子类对象的时候，先初始化父类型特征。

```java

/*
	1、“this.”和“super.”大部分情况下都是可以省略的。
	2、this. 什么时候不能省略？
		public void setName(String name){
			this.name = name;
		}
	3、super. 什么时候不能省略？
		父中有，子中又有，如果想在子中访问“父的特征”，super. 不能省略。
*/
	public void shopping(){
		/*
			java是怎么来区分子类和父类的同名属性的？
				this.name：当前对象的name属性
				super.name：当前对象的父类型特征中的name属性。
		*/
		System.out.println(this.name + "正在购物!"); // null 正在购物
		System.out.println(super.name + "正在购物!"); // 张三正在购物
		System.out.println(name + "正在购物!"); //null 正在购物
	}
}



/*
	在父和子中有同名的属性，或者说有相同的方法，
	如果此时想在子类中访问父中的数据，必须使用“super.”加以区分。

	super.属性名    【访问父类的属性】
	super.方法名(实参) 【访问父类的方法】
	super(实参)  【调用父类的构造方法】
*/



/*
	通过这个测试得出的结论：
		super 不是引用。super也不保存内存地址，super也不指向任何对象。
		super 只是代表当前对象内部的那一块父类型的特征。
*/
public class SuperTest06 {

	// 实例方法
	public void doSome(){
		// SuperTest06@2f92e0f4
		System.out.println(this);
		// 输出“引用”的时候，会自动调用引用的toString()方法。
		//System.out.println(this.toString());

		//编译错误: 需要'.'
		//System.out.println(super);
	}

	// this和super不能使用在static静态方法中。
	/*
	public static void doOther(){
		System.out.println(this);
		System.out.println(super.xxx);
	}
	*/

	// 静态方法，主方法
	public static void main(String[] args){
		SuperTest06 st = new SuperTest06();
		st.doSome();

		// main方法是静态的
		// 错误的。
		/*
		System.out.println(this);
		System.out.println(super.xxxx);
		*/
	}
}
```


### final关键字

```java
/*
	final
	1、final是java语言中的一个关键字。
	2、final表示最终的，不可变的。
	3、final可以修饰变量以及方法，还有类等。
	4、final修饰的变量？
	5、final修饰的方法？
	6、final修饰的类？

*/

class A{
}

//B类继承A类，相当于对A类的功能进行扩展。如果你不希望别人对A类型进行扩展。
//你可以给A类加final关键字，这样的话A类就无法继承了。
//错误 ：final修饰的类无法被继承
final class B extends A{

}

//--------------------------------------

class C{
	public final void f(){}
}

class D extends C{
	//public void f(){}
	// 错误：final修饰的方法无法被覆盖和重写
}

//----------------------------------------

class E{
	public static void main(String[] args){
		final int i = 10;
		//i = 20;
		//错误：final修饰的局部变量不能重新赋值（只能赋一次值）
	}
}

//-----------------------------------------

//final修饰的引用变量
/*
	引用是一个变量, 如果用final修饰了，那么他里面的地址就不能变了，但是地址里的东西还是可以变化的，就相当于C++中的 const int*
*/

/*
	final修饰的引用：
	该引用只能指向1个对象，并且它只能永远指向该对象，无法再指向其它对象。并且在该方法执行过程中，该引用指向对象之后，该对象不会被垃圾回收器回收。直到当前方法结束，才会释放空间。
*/

//-----------------------------------------

//final修饰的实例变量

/*
	也是变量，系统会赋上默认值的变量，加上之后，系统就不会自动赋值了，我们必须手动赋值。
	可以在声明的时候赋值（本质也是在构造方法里赋值）
	也能在构造方法里赋值（在构造方法里也不能重新赋值，只能赋值一次）
	只要在系统赋默认值之前赋值就行（构造方法里赋默认值）
*/

//常量：static final 修饰的变量称为常量。建议全部大写，每个单词之间用下划线链接
//永远不变的量建议声明为常量，
//常量和静态变量都是存储在方法区，并且都是在类加载的时候初始化

//常量一般都是public的，所以大多写为 public static final int PI = 3.14;
```

- final修饰的类无法继承。
- final修饰的方法无法覆盖。
- final修饰的变量只能赋一次值。
- final修饰的引用一旦指向某个对象，则不能再重新指向其它对象，但该引用
- 指向的对象内部的数据是可以修改的。
- final修饰的实例变量必须手动初始化，不能采用系统默认值。
- final修饰的实例变量一般和static联合使用，称为常量。
- public static final double PI = 3.1415926;

### 抽象类

![1593007439866](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1593007439866.png)

```java
/*

	类到对象是实例化。对象到类是抽象。

	抽象类：
		1、什么是抽象类？
			类和类之间具有共同特征，将这些共同特征提取出来，形成的就是抽象类。
			类本身是不存在的，所以抽象类无法创建对象《无法实例化》。

		2、抽象类属于什么类型？
			抽象类也属于引用数据类型。

		3、抽象类怎么定义？《能把基础语法先学会》
			语法：
				[修饰符列表] abstract class 类名{
					类体;
				}

		4、抽象类是无法实例化的，无法创建对象的，所以抽象类是用来被子类继承的。

		5、final和abstract不能联合使用，这两个关键字是对立的。

		6、抽象类的子类可以是抽象类。也可以是非抽象类。

		7、抽象类虽然无法实例化，但是抽象类有构造方法，这个构造方法是供子类使用的。super

		8、抽象类关联到一个概念：抽象方法。什么是抽象方法呢？
			抽象方法表示没有实现的方法，没有方法体的方法。例如：
				public abstract void doSome();
				抽象方法特点是：
					特点1：没有方法体，以分号结尾。
					特点2：前面修饰符列表中有abstract关键字。

		9、抽象类中不一定有抽象方法，抽象方法必须出现在抽象类中。
*/
public class AbstractTest01{
	public static void main(String[] args){
		// 错误: Account是抽象的; 无法实例化
		//Account act = new Account();
	}
}

// 银行账户类
/*
final abstract class Account{}
错误: 非法的修饰符组合: abstract和final
*/

abstract class Account{
	/*
	public Account(){}
	public Account(String s){}
	*/
	// 非抽象方法
	public void doOther(){}

	// 抽象方法
	public abstract void withdraw();
}

// 子类继承抽象类，子类可以实例化对象
/*
class CreditAccount extends Account{
	public CreditAccount(){
		super();
	}
}
*/

// 抽象类的子类可以是抽象类吗？可以
/*
abstract class CreditAccount extends Account{}
*/

/*
	抽象类：

		1、抽象类中不一定有抽象方法，抽象方法必须出现在抽象类中。

		2、重要结论：重要结论五颗星*****（必须记住）
			一个非抽象的类继承抽象类，必须将抽象类中的所有抽象方法实现了。
			这是java语法上强行规定的，必须的，不然编译器就报错了。

			这里的覆盖或者说重写，也可以叫做实现。（对抽象的实现。）

*/
public class AbstractTest02{
	public static void main(String[] args){
		// 能不能使用多态?
		// 父类型引用指向子类型对象。
		Animal a = new Bird();  // 向上转型。（自动类型转换）

		// 这就是面向抽象编程。
		// 以后你都是调用的a.XXXX
		// a的类型是Animal，Animal是抽象的
		// 面向抽象编程，不要面向具体编程，降低程序的耦合度，提高程序的扩展力。
		// 这种编程思想符合OCP原则。
		/*
			分析以下：
				编译的时候这个move()方法是谁的？
				运行的时候这个move()方法又是谁的？
		*/
		a.move();

		// 多态（当对多态不是很理解的时候，以后写代码能用多态就用多态。慢慢就理解了。）
		Animal x = new Cat();
		x.move();
	}


// 动物类（抽象类）
abstract class Animal{

	// 抽象方法
	public abstract void move();
}

// 子类（非抽象的）
// 错误: Bird不是抽象的, 并且未覆盖Animal中的抽象方法move()
/*
class Bird extends Animal{
}
*/

class Bird extends Animal{
	// 需要将从父类中继承过来的抽象方法进行覆盖/重写，或者也可以叫做“实现”。
	// 把抽象的方法实现了。
	public void move(){
		System.out.println("鸟儿在飞翔！");
	}
}

class Cat extends Animal{
	public void move(){
		System.out.println("猫在走猫步！");
	}
}

// 如果Bird是抽象类的话，那么这个Animal中继承过来的抽象方法也可以不去重写/覆盖/实现。
/*
abstract class Bird extends Animal{
}
*/
```

- 抽象类怎么定义？在class前添加abstract关键字就行了。
- 抽象类是无法实例化的，无法创建对象的，所以抽象类是用来被子类继承的。
- final和abstract不能联合使用，这两个关键字是对立的。
- 抽象类的子类可以是抽象类。也可以是非抽象类。
- 抽象类虽然无法实例化，但是抽象类有构造方法，这个构造方法是供子类使用的。
- 抽象类中不一定有抽象方法，抽象方法必须出现在抽象类中。
- 抽象方法怎么定义？public abstract void doSome();
- 一个非抽象的类，继承抽象类，必须将抽象类中的抽象方法进行覆盖/重写/实现。

面试题（判断题）：java语言中凡是没有方法体的方法都是抽象方法。错误的。
Object类中就有很多方法都没有方法体，都是以“;”结尾的，但他们都不是抽象方法，例如：public native int hashCode();这个方法底层调用了C++写的动态链接库程序。前面修饰符列表中没有：abstract。有一个native。表示调用JVM本地程序。

### 接口

#### 基础语法

```java
/*
	接口：
		1、接口也是一种“引用数据类型”。编译之后也是一个class字节码文件。
		2、接口是完全抽象的。（抽象类是半抽象。）或者也可以说接口是特殊的抽象类。
		3、接口怎么定义，语法是什么？
			[修饰符列表] interface 接口名{}
		4、接口支持多继承，一个接口可以继承多个接口。
		5、接口中只包含两部分内容，一部分是：常量。一部分是：抽象方法。接口中没有其它内容了。只有以上两部分。
		6、接口中所有的元素都是public修饰的。（都是公开的。）
		7、接口中的抽象方法定义时：public abstract修饰符可以省略。
		8、接口中的方法都是抽象方法，所以接口中的方法不能有方法体。
		9、接口中的常量的public static final可以省略。
*/
public class Test01{
	public static void main(String[] args){

		// 访问接口的常量。
		System.out.println(MyMath.PI);

		// 常量能重新赋值吗？
		//错误: 无法为最终变量PI分配值
		//MyMath.PI = 3.1415928;
	}
}

// 定义接口
interface A{

}

// 接口支持继承
interface B extends A{

}

// 一个接口可以继承多个接口（支持多继承）
interface C extends A, B{
}

// 我的数学接口
interface MyMath{

	// 常量
	//public static final double PI = 3.1415926;

	// public static final可以省略吗？
	double PI = 3.1415926;

	// 抽象方法
	//public abstract int sum(int a, int b);

	// 接口当中既然都是抽象方法，那么在编写代码的时候，public abstract可以省略吗？可以
	int sum(int a, int b);

	// 接口中的方法可以有方法体吗？
	// 错误: 接口抽象方法不能带有主体
	/*
	void doSome(){}
	*/

	// 相减的抽象方法
	int sub(int a, int b);

}

```

- 接口是一种“引用数据类型”。
- 接口是完全抽象的。
- 接口怎么定义：[修饰符列表] interface 接口名{}
- 接口支持多继承。
- 接口中只有常量+抽象方法。
- 接口中所有的元素都是public修饰的
- 接口中抽象方法的public abstract可以省略。
- 接口中常量的public static final可以省略。
- 接口中方法不能有方法体。

```java
/*
	接口的基础语法：
		1、类和类之间叫做继承，类和接口之间叫做实现。
		别多想：你仍然可以将"实现"看做“继承”。
		继承使用extends关键字完成。
		实现使用implements关键字完成。

		2、五颗星（*****）：当一个非抽象的类实现接口的话，必须将接口中所有的
		抽象方法全部实现（覆盖、重写）。
*/

public class Test02{
	public static void main(String[] args){
		//错误: MyMath是抽象的; 无法实例化
		//new MyMath();

		// 能使用多态吗？可以。
		//Animal a = new Cat();

		// 父类型的引用指向子类型的对象
		MyMath mm = new MyMathImpl();
		// 调用接口里面的方法（面向接口编程。）
		int result1 = mm.sum(10, 20);
		System.out.println(result1);
	}
}

// 特殊的抽象类，完全抽象的，叫做接口。
interface MyMath{
	double PI = 3.1415926;
	int sum(int a, int b);
	int sub(int a, int b);
}

// 这样没问题
/*
abstract class MyMathImpl implements MyMath {}
*/

// 编写一个类（这个类是一个“非抽象”的类）
// 这个类的名字是随意的。
//错误: MyMathImpl不是抽象的, 并且未覆盖MyMath中的抽象方法sub(int,int)
/*
class MyMathImpl implements MyMath {}
*/

//修正
class MyMathImpl implements MyMath {

	//错误：正在尝试分配更低的访问权限; 以前为public
	/*
	int sum(int a, int b){
		return a + b;
	}
	*/

	// 重写/覆盖/实现 接口中的方法（通常叫做实现。）
	public int sum(int a, int b){	return a + b;	}

	public int sub(int a, int b){	return a - b;	}
}

```

```java

/*
	接口和接口之间支持多继承，那么一个类可以同时实现多个接口吗？对于计算机来说，一个机箱上有多个接口，一个接口是接键盘的，一个接口是接鼠标的，一个接口是接电源的，一个接口是接显示器的.....

	重点（五颗星*****）：一个类可以同时实现多个接口。

	这种机制弥补了java中的哪个缺陷？
		java中类和类只支持单继承。实际上单继承是为了简单而出现的，现实世界中存在多继承，java中的接口弥补了单继承带来的缺陷。接口A和接口B虽然没有继承关系，但是写代码的时候，可以互转。编译器没意见。但是运行时可能出现：ClassCastException

	之前有一个结论：
		无论向上转型还是向下转型，两种类型之间必须要有继承关系，没有继承关系编译器会报错。（这句话不适用在接口方面。）

		最终实际上和之前还是一样，需要加：instanceof运算符进行判断。向下转型养成好习惯。转型之前先if+instanceof进行判断。
*/
public class Test03{
	public static void main(String[] args){
		// 多态该怎么用呢？
		// 都是父类型引用指向子类型对象
		A a = new D();
		//a.m2(); // 编译报错。A接口中没有m2()方法。
		B b = new D();
		C c = new D();

		// 这个编译没问题，运行也没问题。
		// 调用其他接口中的方法，你需要转型（接口转型。）
		B b2 = (B)a;
		b2.m2();

		// 直接向下转型为D可以吗？可以
		D d = (D)a;
		d.m2();

		M m = new E();
		// 经过测试：接口和接口之间在进行强制类型转换的时候，没有继承关系，也可以强转。
		// 但是一定要注意，运行时可能会出现ClassCastException异常。
		// 编译没问题，运行有问题。
		//K k = (K)m;
		if(m instanceof K){
			K k = (K)m;
		}
	}
}

interface K{}

interface M{}

class E implements M{}

// --------------------------------------------------------------------

interface X{}
interface Y{}
interface Z extends X,Y{ //接口和接口支持多继承。}

//------------------------------------------------------------------

interface A{void m1();}
interface B{void m2();}
interface C{void m3();}

// 实现多个接口，其实就类似于多继承。
class D implements A,B,C{
	public void m1(){}
	public void m2(){}
	public void m3(){}
}
```

```java
/*
	继承和实现都存在的话，代码应该怎么写？
		extends 关键字在前。
		implements 关键字在后。
*/
public class Test04{
	public static void main(String[] args){
		// 创建对象（表面看Animal类没起作用！）
		Flyable f = new Cat(); //多态。
		f.fly();

		// 同一个接口
		Flyable f2 = new Pig();
		// 调用同一个fly()方法，最后的执行效果不同。
		f2.fly();

		Flyable f3 = new Fish();
		f3.fly();
	}
}

// 动物类：父类
class Animal{}

// 接口通常提取的是行为动作。
interface Flyablevoid fly();}

// 动物类子类：猫类
// Flyable是一个接口，是一对翅膀的接口，通过接口插到猫身上，让猫变的可以飞翔。
class Cat extends Animal implements Flyable{
	public void fly(){
		System.out.println("飞猫起飞，翱翔太空的一只猫，很神奇，我想做一只猫！！");
	}
}

// 蛇类，如果你不想让它飞，可以不实现Flyable接口
// 没有实现这个接口表示你没有翅膀，没有给你插翅膀，你肯定不能飞。
class Snake extends Animal{
}

// 想飞就插翅膀这个接口。
class Pig extends Animal implements Flyable{
	public void fly(){
		System.out.println("我是一只会飞的猪！！！");
	}
}

// 鱼（默认实际上是存在继承的，默认继承Object。）
/*
class Fish extends Object implements Flyable{
}
*/
class Fish implements Flyable{ //没写extends，也是有的，默认继承Object。
	public void fly(){
		System.out.println("我是六眼飞鱼（流言蜚语）！！！");
	}
}
```

- 一个非抽象的类，实现接口的时候，必须将接口中所有方法加以实现。
- 一个类可以实现多个接口。
- extends和implements可以共存，extends在前，implements在后。
- 使用接口，写代码的时候，可以使用多态（父类型引用指向子类型对象）。

#### 在开发中的作用(解耦合)

```java
// 顾客
public class Customer{
	// 顾客手里有一个菜单
	// Customer has a FoodMenu!（这句话什么意思：顾客有一个菜单）
	// 记住：以后凡是能够使用 has a 来描述的，统一以属性的方式存在。
	// 实例变量，属性
	// 面向抽象编程，面向接口编程。降低程序的耦合度，提高程序的扩展力。
	private FoodMenu foodMenu;

	// 如果以下这样写，就表示写死了（焊接了。没有可插拔了。）
	// 中餐厨师
	//ChinaCooker cc;

	// 西餐厨师
	//AmericCooker ac

	// 构造方法
	public Customer(){
	}
	public Customer(FoodMenu foodMenu){
		this.foodMenu = foodMenu;
	}

	// setter and getter
	public void setFoodMenu(FoodMenu foodMenu){
		this.foodMenu = foodMenu;
	}
	public FoodMenu getFoodMenu(){
		return foodMenu;
	}

	// 提供一个点菜的方法
	public void order(){
		// 先拿到菜单才能点菜
		// 调用get方法拿菜单。
		//FoodMenu fm = this.getFoodMenu();
		// 也可以不调用get方法，因为在本类中私有的属性是可以访问
		foodMenu.shiZiChaoJiDan();
		foodMenu.yuXiangRouSi();
	}
}

/*
	Cat is a Animal，但凡满足is a的表示都可以设置为继承。
	Customer has a FoodMenu，但凡是满足has a的表示都以属性的形式存在。
*/

//西餐厨师
// 实现菜单上的菜
// 厨师是接口的实现者。
public class AmericCooker implements FoodMenu{

	// 西红柿炒蛋
	public void shiZiChaoJiDan(){
		System.out.println("西餐师傅做的西红柿炒鸡蛋！");
	}

	// 鱼香肉丝
	public void yuXiangRouSi(){
		System.out.println("西餐师傅做的鱼香肉丝！");
	}
}

//中餐厨师
// 实现菜单上的菜
// 厨师是接口的实现者。
public class ChinaCooker implements FoodMenu{

	// 西红柿炒蛋
	public void shiZiChaoJiDan(){
		System.out.println("中餐师傅做的西红柿炒鸡蛋，东北口味！");
	}

	// 鱼香肉丝
	public void yuXiangRouSi(){
		System.out.println("中餐师傅做的鱼香肉丝，东北口味！");
	}
}


/*
	接口：菜单，抽象的
*/
public interface FoodMenu{

	// 西红柿炒蛋
	void shiZiChaoJiDan();

	// 鱼香肉丝
	void yuXiangRouSi();

}

public class Test{
	public static void main(String[] args){

		// 创建厨师对象
		//FoodMenu cooker1 = new ChinaCooker();
		FoodMenu cooker1 = new AmericCooker();

		// 创建顾客对象
		Customer customer = new Customer(cooker1);

		// 顾客点菜
		customer.order();
	}

```

注意：接口在开发中的作用，类似于多态在开发中的作用。

多态：面向抽象编程，不要面向具体编程。降低程序的耦合度。提高程序的扩展力。

接口在开发中的作用？
接口是不是完全的？是。
而我们以后正好要求，面向抽象编程。面向抽象编程这句话以后可以修改为：面向接口编程。有了接口就有了可插拔。可插拔表示扩展力很强。不是焊接死的。
主板和内存条之间有插槽，这个插槽就是接口，内存条坏了，可以重新买一个换下来。这叫做高扩展性。（低耦合度。）

接口有什么用？扩展性好。可插拔。
接口是一个抽象的概念。

总结一句话：三个字“解耦合”
面向接口编程，可以降低程序的耦合度，提高程序的扩展力。符合OCP开发原则。接口的使用离不开多态机制。（接口+多态才可以达到降低耦合度。）

接口可以解耦合，解开的是谁和谁的耦合 ? 任何一个接口都有调用者和实现者。接口可以将调用者和实现者解耦合。调用者面向接口调用。实现者面向接口编写实现。

以后进行大项目的开发，一般都是将项目分离成一个模块一个模块的，
模块和模块之间采用接口衔接。降低耦合度。

#### 类型之间的关系

```java

/*
is a（继承）、has a（关联）、like a（实现）
is a：
    Cat is a Animal（猫是一个动物）
    凡是能够满足is a的表示“继承关系”
A extends B
*/

/*
has a：
    I has a Pen（我有一支笔）
    凡是能够满足has a关系的表示“关联关系”
    关联关系通常以“属性”的形式存在。
A{
B b;
}
*/

/*
like a：
    Cooker 1ike a Foodienu（厨师像一个菜单一样）凡是能够满足likea关系的表示实现关系”
    实现关系通常是：类实现接口。
A implements B
*/
```


#### 抽象类和接口的区别

在这里我们只说一下抽象类和接口在语法上的区别。
至于以后抽象类和接口应该怎么进行选择，通过后面的项目去体会/学习。

抽象类是半抽象的。
接口是完全抽象的。

抽象类中有构造方法。
接口中没有构造方法。

接口和接口之间支持多继承。
类和类之间只能单继承。

一个类可以同时实现多个接口。
一个抽象类只能继承一个类（单继承）。

接口中只允许出现常量和抽象方法。

这里先透露一个信息：
以后接口使用的比抽象类多。一般抽象类使用的还是少。
接口一般都是对“行为”的抽象。

### package和import

```java
/*
	关于java语言中的package和import机制：

		1、为什么要使用package？
			package是java中包机制。包机制的作用是为了方便程序的管理。不同功能的类分别存放在不同的包下。（按照功能划分的，不同的软件包具有不同的功能。）

		2、package怎么用？
			package是一个关键字，后面加包名。例如：	package com.bjpowernode.javase.chapter17;  		注意：package语句只允许出现在java源代码的第一行。

		3、包名有没有命名规范？有
			一般都采用公司域名倒序的方式（因为公司域名具有全球唯一性。）
			包名命名规范：
				公司域名倒序 + 项目名 + 模块名 + 功能名

		4、对于带有package的java程序怎么编译？怎么运行？

			采用之前的编译和运行不行了。
			类名不再是：HelloWorld了。
			类名是：com.bjpowernode.javase.chapter17.HelloWorld

			编译：
				javac -d . HelloWorld.java
				解释一下：
					javac 负责编译的命令
					-d		带包编译
					.		代表编译之后生成的东西放到当前目录下（点代表当前目录）
					HelloWorld.java  被编译的java文件名。

			运行：
				java com.bjpowernode.javase.chapter17.HelloWorld

		5、关于import的使用。

			import什么时候使用？
				A类中使用B类。
				A和B类都在同一个包下。不需要import。
				A和B类不在同一个包下。需要使用import。
				java.lang.*;这个包下的类不需要使用import导入。

			import怎么用？
				import语句只能出现在package语句之下，class声明语句之上。
				import语句还可以采用星号的方式。(导入所有类)
*/
package com.bjpowernode.javase.chapter17;
import com.bjpowernode.javase.chapter17.*;

public class HelloWorld{
	public static void main(String[] args){
		System.out.println("Hello World!");
	}
}

//-------------------Scanner解释---------------------

//import java.util.Scanner;
import java.util.*;

public class Test03{
	public static void main(String[] args){

		// 为什么要这样写？
		// Test03类和Scanner类不在同一个包下。
		// java.util就是Scanner类的包名。
		//java.util.Scanner s = new java.util.Scanner(System.in);

		Scanner s = new Scanner(System.in);
		String str = s.next();
		System.out.println("您输入的字符串是--->" + str);
	}
}
```

- package出现在java源文件第一行。
- 带有包名怎么编译？javac -d . xxx.java
- 怎么运行？java 完整类名

补充：以后说类名的时候，如果带着包名描述，表示完整类名。
如果没有带包，描述的话，表示简类名。
java.util.Scanner 完整类名。
Scanner 简类名

import什么时候不需要？
java.lang不需要。
同包下不需要。
其它一律都需要。

怎么用？
import 完整类名;
import 包名.*;

import java.util.Scanner; // 完整类名。

// 同学的疑问：这样是不是效率比较低。
// 这个效率不低，因为编译器在编译的时候，会自动把*变成具体的类名。
import java.util.*;

// 想省懒劲你不能太省了。
import java.*; 这是不允许的，因为在java语言中规定，这里的*只代表某些类的名字。

### objective类

目前为止我们只需要知道这几个方法即可：

- protected Object clone()   // 负责对象克隆的。
- int hashCode()// 获取对象哈希值的一个方法。
- boolean equals(Object obj)  // 判断两个对象是否相等
- String toString()  // 将对象转换成字符串形式
- protected void finalize()  // 垃圾回收器负责调用的方法

#### toString()

```java
/*
	关于Object类中的toString()方法

		1、源代码长什么样？
			public String toString() {
				return this.getClass().getName() + "@" + Integer.toHexString(hashCode());
			}
			源代码上toString()方法的默认实现是：
				类名@对象的内存地址转换为十六进制的形式

		2、SUN公司设计toString()方法的目的是什么？
			toString()方法的作用是什么？
				toString()方法的设计目的是：通过调用这个方法可以将一个“java对象”转换成“字符串表示形式”

		3、其实SUN公司开发java语言的时候，建议所有的子类都去重写toString()方法。toString()方法应该是一个简洁的、详实的、易阅读的.
*/
public class Test01{
	public static void main(String[] args){
		MyTime t1 = new MyTime(1970, 1, 1);
		// 一个日期对象转换成字符串形式的话，我可能还是希望能看到具体的日期信息。
		String s1 = t1.toString();

		//MyTime类重写toString()方法之前
		//System.out.println(s1); // MyTime@28a418fc

		//MyTime类重写toString()方法之后
		System.out.println(s1); // 1970年1月1日


		// 注意：输出引用的时候，会自动调用该引用的toString()方法。
		System.out.println(t1);
	}
}
class MyTime{
	int year;
	int month;
	int day;

	public MyTime(){

	}

	public MyTime(int year, int month, int day){
		this.year = year;
		this.month = month;
		this.day = day;
	}

	// 重写toString()方法
	// 这个toString()方法怎么重写呢？
	// 越简洁越好，可读性越强越好。
	// 向简洁的、详实的、易阅读的方向发展
	public String toString(){
		//return this.year + "年" + this.month + "月" + this.day + "日";
		return this.year + "/" + this.month + "/" + this.day;
	}
}
```

- 以后所有类的toString()方法是需要重写的。
- 重写规则，越简单越明了就好。
- System.out.println(引用); 这里会自动调用“引用”的toString()方法。
- ring类是SUN写的，toString方法已经重写了。

#### equals()

```java
/*
	关于Object类中的equals方法
		1、equals方法的源代码
			public boolean equals(Object obj) {
				return (this == obj);
			}
			以上这个方法是Object类的默认实现。

		2、SUN公司设计equals方法的目的是什么？
			以后编程的过程当中，都要通过equals方法来判断两个对象是否相等。equals方法是判断两个对象是否相等的。

		3、我们需要研究一下Object类给的这个默认的equals方法够不够用！！！！
				在Object类中的equals方法当中，默认采用的是“==”判断两个java对象是否相等。而“==”判断的是两个java对象的内存地址，我们应该判断两个java对象的内容是否相等。所以老祖宗的equals方法不够用，需要子类重写equals。

		4、判断两个java对象是否相等，不能使用“==”，因为“==”比较的是两个对象的内存地址。
*/
public class Test02{
	public static void main(String[] args){

		// 判断两个基本数据类型的数据是否相等直接使用“==”就行。
		int a = 100;int b = 100;
		// 这个“==”是判断a中保存的100和b中保存的100是否相等。
		System.out.println(a == b); //true（相等） false(不相等)

		// 判断两个java对象是否相等，我们怎么办？能直接使用“==”吗？
		// 创建一个日期对象是：2008年8月8日。
		MyTime t1 = new MyTime(2008, 8, 8); //MyTime t1 = 0x1234;
		// 创建了一个新的日期对象，但表示的日期也是：2008年8月8日。
		MyTime t2 = new MyTime(2008, 8, 8); //MyTime t2 = 0x3698;

		//测试以下，比较两个对象是否相等，能不能使用“==”？？？
		// 这里的“==”判断的是：t1中保存的对象内存地址和t2中保存的对象内存地址是否相等。
		System.out.println(t1 == t2); // false

		// 重写Object equals方法之前（比较的是对象内存地址）
		// 重写Object equals方法之后（比较的是内容。）
		boolean flag = t1.equals(t2);
		System.out.println(flag); //true

		// 再创建一个新的日期
		MyTime t3 = new MyTime(2008, 8, 9);
		// 两个日期不相等，就是false。
		System.out.println(t1.equals(t3)); // false

		// 我们这个程序有bug吗？可以运行，但是效率怎么样？低（怎么改造。）
		MyTime t4 = null;
		System.out.println(t1.equals(t4)); //false
	}
}

class MyTime { //extends Object{
	int year;int month;int day;

	public MyTime(){}
	public MyTime(int year, int month, int day){
		this.year = year;
		this.month = month;
		this.day = day;
	}

	// 默认的equals方法
	/*
	public boolean equals(Object obj) {
		return (this == obj);
	}
	*/


	// 重写Object类的equals方法
	// 怎么重写？复制粘贴。相同的返回值类型、相同的方法名、相同的形式参数列表。
	// equals到底应该怎么重写？你自己定，你认为两个对象什么相等的时候表示相等，你就怎么重写。
	public boolean equals(Object obj) {
		// 当年相同，月相同，并且日也相同的时候，表示两个日期相同。两个对象相等。
		// 获取第一个日期的年月日
		int year1 = this.year;
		int month1 = this.month;
		int day1 = this.day;

		// 获取第二个日期的年月日
		//int year2 = obj.year;
		//int month2 = obj.month;
		//int day2 = obj.day;

		if(obj instanceof MyTime){
			MyTime t = (MyTime)obj;
			int year2 = t.year;
			int month2 = t.month;
			int day2 = t.day;
			if(year1 == year2 && month1 == month2 && day1 == day2){
				return true;
			}
		}
		// 程序能够执行到此处表示日期不相等。
		return false;
	}

	//改良。

	public boolean equals(Object obj) {
		// 如果obj是空，直接返回false
		if(obj == null){
			return false;
		}
		// 如果obj不是一个MyTime，没必要比较了 ，直接返回false
		if(!(obj instanceof MyTime)){
			return false;
		}
		// 如果this和obj保存的内存地址相同，没必要比较了，直接返回true。
		// 内存地址相同的时候指向的堆内存的对象肯定是同一个。
		if(this == obj){
			return true;
		}
		// 程序能够执行到此处说明什么？
		// 说明obj不是null，obj是MyTime类型。
		MyTime t = (MyTime)obj;
		return this.year == t.year && this.month == t.month && this.day == t.day ;
	}

//===最终版本===
	public boolean equals(Object obj) {
		if(obj == null || !(obj instanceof MyTime)){
			return false;
		}
		if(this == obj){
			return true;
		}
		MyTime t = (MyTime)obj;
		return this.year == t.year && this.month == t.month && this.day == t.day ;
	}

}

/*
class Person{
	private String idCard;
}
*/


/*
	java语言当中的字符串String有没有重写toString方法，有没有重写equals方法。

	总结：
		1、String类已经重写了equals方法，比较两个字符串不能使用==，必须使用equals。equals是通用的。

		2、String类已经重写了toString方法。

	大结论：
		java中什么类型的数据可以使用“==”判断java中基本数据类型比较是否相等，使用==

		java中什么类型的数据需要使用equals判断java中所有的引用数据类型统一使用equals方法来判断是否相等。

		这是规矩。
*/
public class Test03{
	public static void main(String[] args){

		// 大部分情况下，采用这样的方式创建字符串对象
		String s1 = "hello";
		String s2 = "abc";

		// 实际上String也是一个类。不属于基本数据类型。
		// 既然String是一个类，那么一定存在构造方法。
		String s3 = new String("Test1");
		String s4 = new String("Test1");
		// new两次，两个对象内存地址，s3保存的内存地址和s4保存的内存地址不同。
		// == 判断的是内存地址。不是内容。
		System.out.println(s3 == s4); // false

		// 比较两个字符串能不能使用双等号？
		// 不能，必须调用equals方法。
		// String类已经重写equals方法了。
		System.out.println(s3.equals(s4)); // true

		// String类有没有重写toString方法呢？
		String x = new String("动力节点");
		// 如果String没有重写toString()方法，输出结果：java.lang.String@十六进制的地址
		// 经过测试：String类已经重写了toString()方法。
		System.out.println(x.toString()); //动力节点
		System.out.println(x); //动力节点
	}
}

class Student{
	// 学号
	int no; //基本数据类型，比较时使用：==
	// 所在学校
	String school; //引用数据类型，比较时使用：equals方法。

	public Student(){}
	public Student(int no,String school){
		this.no = no;
		this.school = school;
	}

	// 重写toString方法
	public String toString(){
		return "学号" + no + "，所在学校名称" + school;
	}

	// 重写equals方法
	// 需求：当一个学生的学号相等，并且学校相同时，表示同一个学生。
	// 思考：这个equals该怎么重写呢？
	// equals方法的编写模式都是固定的。架子差不多。
	public boolean equals(Object obj){
		if(obj == null || !(obj instanceof Student)) return false;
		if(this == obj) return true;
		Student s = (Student)obj;
		return this.no == s.no && this.school.equals(s.school);

		//字符串用双等号比较可以吗？
		// 不可以
		//return this.no == s.no && this.school == s.school;
	}
}

// equals方法重写的时候要彻底。

public class Test05{
	public static void main(String[] args){

		// 多态（自动类型转换。）
		Object o1 = new String("hello world!");
		Object o2 = new User();
		Object o3 = new Address();

		User u1 = new User("zhangsan", new Address("北京","大兴区","11111"));
		User u2 = new User("zhangsan", new Address("北京","大兴区","11111"));

		System.out.println(u1.equals(u2)); // true

		User u3 = new User("zhangsan", new Address("北京","朝阳区","11112"));
		System.out.println(u1.equals(u3)); // false
	}
}

class User{
	// 用户名
	String name;
	// 用户的住址
	Address addr;

	public User(){
	}
	public User(String name, Address addr){
		this.name = name;
		this.addr = addr;
	}

	// 重写equals方法
	// 重写规则：当一个用户的用户名和家庭住址都相同，表示同一个用户。
	// 这个equals判断的是User对象和User对象是否相等。
	public boolean equals(Object obj){
		// 用户名和用户名相同，住址和住址相同的时候，认定是同一个用户。
		if(obj == null || !(obj instanceof User)) return false;
		if(this == obj) return true;

		User u = (User)obj;
		if(this.name.equals(u.name) && this.addr.equals(u.addr)){
			return true;
		}
		return false;
	}
}

class Address{
	String city;
	String street;
	String zipcode;

	public Address(){

	}
	public Address(String city,String street,String zipcode){
		this.city = city;
		this.street = street;
		this.zipcode = zipcode;
	}

	// 注意：这里并没有重写equals方法。
	// 这里的equals方法判断的是：Address对象和Address对象是否相等。
	public boolean equals(Object obj){
		if(obj == null || !(obj instanceof Address)) return false;
		if(this == obj) return true;
		// 怎么算是家庭住址相同呢？
		// 城市相同，街道相同，邮编相同，表示相同。
		Address a = (Address)obj;
		if(this.city.equals(a.city)
			&& this.street.equals(a.street)
			&& this.zipcode.equals(a.zipcode)){
			return true;
		}
		return false;
	}
}
```

- 以后所有类的equals方法也需要重写，因为Object中的equals方法比较的是两个对象的内存地址，我们应该比较内容，所以需要重写。
- 重写规则：自己定，主要看是什么和什么相等时表示两个对象相等。
- 基本数据类型比较实用：==
- 对象和对象比较：调用equals方法
- String类是SUN编写的，所以String类的equals方法重写了。
- 以后判断两个字符串是否相等，最好不要使用==，要调用字符串对象的equals方法。
- 注意：重写equals方法的时候要彻底。

#### finalize()【非重点】【jdk9之后就没了】

```java
/*
	关于Object类中的finalize()方法。（非重点  非重点  非重点  了解即可。）

		1、在Object类中的源代码：
			protected void finalize() throws Throwable { }

			GC：负责调用finalize()方法。

		2、finalize()方法只有一个方法体，里面没有代码，而且这个方法是protected修饰的。

		3、这个方法不需要程序员手动调用，JVM的垃圾回收器负责调用这个方法。
		不像equals toString，equals和toString()方法是需要你写代码调用的。
		finalize()只需要重写，重写完将来自动会有程序来调用。

		4、finalize()方法的执行时机：
			当一个java对象即将被垃圾回收器回收的时候，垃圾回收器负责调用
			finalize()方法。

		5、finalize()方法实际上是SUN公司为java程序员准备的一个时机，垃圾销毁时机。
		如果希望在对象销毁时机执行一段代码的话，这段代码要写到finalize()方法当中。

		6、静态代码块的作用是什么？
			static {
				....
			}
			静态代码块在类加载时刻执行，并且只执行一次。
			这是一个SUN准备的类加载时机。

			finalize()方法同样也是SUN为程序员准备的一个时机。
			这个时机是垃圾回收时机。

		7、提示：
			java中的垃圾回收器不是轻易启动的，
			垃圾太少，或者时间没到，种种条件下，
			有可能启动，也有可能不启动。
*/
public class Test06{
	public static void main(String[] args){
		/*
		// 创建对象
		Person p = new Person();

			// 有一段代码可以建议垃圾回收器启动。
			if(i % 2 == 0){
				System.gc(); // 建议启动垃圾回收器。（只是建议，可能不启动，也可能启动。启动的概率高了一些。）
			}

	}
}

// 项目开发中有这样的业务需求：所有对象在JVM中被释放的时候，请记录一下释放时间！！！
// 记录对象被释放的时间点，这个负责记录的代码写到哪里？
// 写到finalize()方法中。
class Person{

	// 重写finalize()方法
	// Person类型的对象被垃圾回收器回收的时候，垃圾回收器负责调用：p.finalize();
	protected void finalize() throws Throwable {
		// this代表当前对象
		System.out.println(this + "即将被销毁！");
	}
}
```

这个方法是protected修饰的，在Object类中这个方法的源代码是？
protected void finalize() throws Throwable { }

#### hashCode

```java
/*
	hashCode方法：
		在Object中的hashCode方法是怎样的？
			public native int hashCode();

			这个方法不是抽象方法，带有native关键字，底层调用C++程序。

		hashCode()方法返回的是哈希码：
			实际上就是一个java对象的内存地址，经过哈希算法，得出的一个值。
			所以hashCode()方法的执行结果可以等同看做一个java对象的内存地址。
*/
public class Test07{
	public static void main(String[] args){
		Object o = new Object();
		int hashCodeValue = o.hashCode();

		// 对象内存地址经过哈希算法转换的一个数字。可以等同看做内存地址。
		System.out.println(hashCodeValue); //798154996

		MyClass mc = new MyClass();
		int hashCodeValue2 = mc.hashCode();
		System.out.println(hashCodeValue2); //1392838282

		MyClass mc2 = new MyClass();
		System.out.println(mc2.hashCode()); // 523429237
	}
}

class MyClass
{
}
```

#### 匿名内部类

```java
/*
	匿名内部类：

		1、什么是内部类？
			内部类：在类的内部又定义了一个新的类。被称为内部类。

		2、内部类的分类：
			静态内部类：类似于静态变量
			实例内部类：类似于实例变量
			局部内部类：类似于局部变量

		3、使用内部类编写的代码，可读性很差。能不用尽量不用。

		4、匿名内部类是局部内部类的一种。
			因为这个类没有名字而得名，叫做匿名内部类。

		5、学习匿名内部类主要是让大家以后在阅读别人代码的时候，能够理解。
		并不代表以后都要这样写。因为匿名内部类有两个缺点：
			缺点1：太复杂，太乱，可读性差。
			缺点2：类没有名字，以后想重复使用，不能用。

		6、不理解算了，你只要记住这种写法就行。
*/

class Test01{

	// 静态变量
	static String country;
	// 该类在类的内部，所以称为内部类
	// 由于前面有static，所以称为“静态内部类”
	static class Inner1{
	}

	// 实例变量
	int age;
	// 该类在类的内部，所以称为内部类
	// 没有static叫做实例内部类。
	class Inner2{
	}

	// 方法
	public void doSome(){
		// 局部变量
		int i = 100;
		// 该类在类的内部，所以称为内部类
		// 局部内部类。
		class Inner3{
		}
	}

	public void doOther(){
		// doSome()方法中的局部内部类Inner3，在doOther()中不能用。
	}

	// main方法，入口
	public static void main(String[] args){
		// 调用MyMath中的mySum方法。
		MyMath mm = new MyMath();
		/*
		Compute c = new ComputeImpl();
		mm.mySum(c, 100, 200);
		*/

		//合并（这样写代码，表示这个类名是有的。类名是：ComputeImpl）
		//mm.mySum(new ComputeImpl(), 100, 200);

		// 使用匿名内部类，表示这个ComputeImpl这个类没名字了。
		// 这里表面看上去好像是接口可以直接new了，实际上并不是接口可以new了。
		// 后面的{} 代表了对接口的实现。
		// 不建议使用匿名内部类，为什么？
		// 因为一个类没有名字，没有办法重复使用。另外代码太乱，可读性太差。
		mm.mySum(new Compute(){
			public int sum(int a, int b){
				return a + b;
			}
		}, 200, 300);
	}
}

// 负责计算的接口
interface Compute{
	// 抽象方法
	int sum(int a, int b);
}

// 数学类
class MyMath{
	// 数学求和方法
	public void mySum(Compute c, int x, int y){
		int retValue = c.sum(x, y);
		System.out.println(x + "+" + y + "=" + retValue);
	}
}

```



### 访问控制权限

访问控制权限都有哪些？4个。

- private私有 只能在本类中访问
- public 公开 任何地方都能访问
- protected受保护 只能在本类、同包、子类中访问。
- 默认 只能在本类，以及同包下访问。

|访问控制修饰符| 本类| 同包| 子类 |任意位置|
|-------------|-----|-----|---|----|
|public|可以|可以|可以|可以|
|protected|可以|可以|可以|不行|
|private|可以|不行|不行|不行|
|默认|可以|可以|不行|不行|

这个不要死记硬背，自己下去之后编写代码自己测试。

范围从大到小排序：public > protected > 默认 > private

访问控制权限修饰符可以修饰什么？

- 属性（4个都能用）
- 方法（4个都能用）
- 类（public和默认能用，其它不行。）
- 接口（public和默认能用，其它不行。）
