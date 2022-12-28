
#Java/异常处理


## 异常处理

### 是什么

```java
/*
1、什么是异常，java提供异常处理机制有什么用？
    以下程序执行过程中发生了不正常的情况，而这种不正常的情况叫做：异常
    java语言是很完善的语言，提供了异常的处理方式，以下程序执行过程中出现了不正常情况，
    java把该异常信息打印输出到控制台，供程序员参考。程序员看到异常信息之后，可以对
    程序进行修改，让程序更加的健壮。

    什么是异常：程序执行过程中的不正常情况。
    异常的作用：增强程序的健壮性。

2、以下程序执行控制台出现了：
    Exception in thread "main" java.lang.ArithmeticException: / by zero
	    at com.bjpowernode.javase.exception.ExceptionTest01.main(ExceptionTest01.java:14)
	这个信息被我们称为：异常信息。这个信息是JVM打印的。
 */
public class ExceptionTest01 {
    public static void main(String[] args) {
        int a = 10;
        int b = 0;
        // 实际上JVM在执行到此处的时候，会new异常对象：new ArithmeticException("/ by zero");
        // 并且JVM将new的异常对象抛出，打印输出信息到控制台了。
        int c = a / b;
        System.out.println(a + "/" + b + "=" + c);

        // 此处运行也会创建一个：ArithmeticException类型的异常对象。
        //System.out.println(100 / 0);

        // 我观察到异常信息之后，对程序进行修改，更加健壮。
    }
}


/*
java语言中异常是以什么形式存在的呢？
    1、异常在java中以类的形式存在，每一个异常类都可以创建异常对象。
    2、异常对应的现实生活中是怎样的？
        火灾(异常类)：
            2008年8月8日,小明家着火了（异常对象）

        类是：模板。
        对象是：实际存在的个体。

        钱包丢了（异常类）：
            2008年1月8日，小明的钱包丢了（异常对象）
 */
public class ExceptionTest02 {
    public static void main(String[] args) {

		// 通过“异常类”创建“异常对象”
        NullPointerException npe = new NullPointerException("空指针异常发生了！");

        //java.lang.NullPointerException: 空指针异常发生了！
        System.out.println(npe);
    }
}

public class ExceptionTest03 {
    public static void main(String[] args) {
    /*
        程序执行到此处发生了ArithmeticException异常，底层new了一个ArithmeticException异常对象，然后抛出了，由于是main方法调用了100 / 0，所以这个异常ArithmeticException抛给了main方法，main方法没有处理，将这个异常自动抛给了JVM。JVM最终终止程序的执行。
        ArithmeticException 继承 RuntimeException，属于运行时异常。
        在编写程序阶段不需要对这种异常进行预先的处理。
     */
        System.out.println(100 / 0);
        // 这里的HelloWorld没有输出，没有执行。
        System.out.println("Hello World!");
    }
}

/*
以下代码报错的原因是什么？
    因为doSome()方法声明位置上使用了：throws ClassNotFoundException
    而ClassNotFoundException是编译时异常。必须编写代码时处理，没有处理
    编译器报错。
 */
public class ExceptionTest04 {
    public static void main(String[] args) {
        // main方法中调用doSome()方法
        // 因为doSome()方法声明位置上有：throws ClassNotFoundException
        // 我们在调用doSome()方法的时候必须对这种异常进行预先的处理。
        // 如果不处理，编译器就报错。
        //编译器报错信息： Unhandled exception: java.lang.ClassNotFoundException
        //doSome();
    }

    /**
     * doSome方法在方法声明的位置上使用了：throws ClassNotFoundException
     * 这个代码表示doSome()方法在执行过程中，有可能会出现ClassNotFoundException异常。
     * 叫做类没找到异常。这个异常直接父类是：Exception，所以ClassNotFoundException属于编译时异常。
     * @throws ClassNotFoundException
     */
    public static void doSome() throws ClassNotFoundException{
        System.out.println("doSome!!!!");
    }

}


```

- java中异常的作用是：增强程序健壮性。
- java中异常以类和对象的形式存在。

Object
Object下有Throwable（可抛出的）
Throwable下有两个分支：

- Error（不可处理，直接退出JVM）
- Exception（可处理的）
	- Exception下有两个分支：
	- Exception的直接子类：编译时异常（要求程序员在编写程序阶段必须预先对这些异常进行处理，如果不处理编译器报错，因此得名编译时异常。）。
	- RuntimeException：运行时异常。（在编写程序阶段程序员可以预先处理，也可以不管，都行。）


编译时异常和运行时异常，都是发生在运行阶段。编译阶段异常是不会发生的。

编译时异常因为什么而得名？
因为编译时异常必须在编译(编写)阶段预先处理，如果不处理编译器报错，因此得名。所有异常都是在运行阶段发生的。因为只有程序运行阶段才可以new对象。因为异常的发生就是new异常对象。
编译时异常和运行时异常的区别？编译时异常一般发生的概率比较高。
举个例子：
你看到外面下雨了，倾盆大雨的。你出门之前会预料到：如果不打伞，我可能会生病（生病是一种异常）。而且这个异常发生的概率很高，所以我们出门之前要拿一把伞。“拿一把伞”就是对“生病异常”发生之前的一种处理方式。

对于一些发生概率较高的异常，需要在运行之前对其进行预处理。

运行时异常一般发生的概率比较低。
举个例子：
小明走在大街上，可能会被天上的飞机轮子砸到。被飞机轮子砸到也算一种异常。但是这种异常发生概率较低。在出门之前你没必要提前对这种发生概率较低的异常进行预处理。如果你预处理这种异常，你将活的很累。

假设你在出门之前，你把能够发生的异常都预先处理，你这个人会更加的安全，但是你这个人活的很累。

假设java中没有对异常进行划分，没有分为：编译时异常和运行时异常，所有的异常都需要在编写程序阶段对其进行预处理，将是怎样的效果呢？首先，如果这样的话，程序肯定是绝对的安全的。
但是程序员编写程序太累，代码到处都是处理异常的代码。

编译时异常还有其他名字：
- 受检异常：CheckedException
- 受控异常
运行时异常还有其它名字：
- 未受检异常：UnCheckedException
- 非受控异常

再次强调：所有异常都是发生在运行阶段的。

### 怎样处理


```java
public class ExceptionTest05 {
    // 第一种处理方式：在方法声明的位置上继续使用：throws，来完成异常的继续上抛。抛给调用者。上抛类似于推卸责任。（继续把异常传递给调用者。）

	/*
		public static void main(String[] args) throws ClassNotFoundException {
			doSome();
		}
     */

    // 第二种处理方式：try..catch进行捕捉。
    // 捕捉等于把异常拦下了，异常真正的解决了。（调用者是不知道的。）
    public static void main(String[] args) {
        try {
            doSome();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void doSome() throws ClassNotFoundException{
        System.out.println("doSome!!!!");
    }
}


import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

/*
处理异常的第一种方式：
    在方法声明的位置上使用throws关键字抛出，谁调用我这个方法，我就抛给谁。抛给调用者来处理。
    这种处理异常的态度：上报。

处理异常的第二种方式：
    使用try..catch语句对异常进行捕捉。这个异常不会上报，自己把这个事儿处理了。异常抛到此处为止，不再上抛了。

注意：
    只要异常没有捕捉，采用上报的方式，此方法的后续代码不会执行。另外需要注意，try语句块中的某一行出现异常，该行后面的代码不会执行。try..catch捕捉异常之后，后续代码可以执行。

在以后的开发中，处理编译时异常，应该上报还是捕捉呢，怎么选？
    如果希望调用者来处理，选择throws上报。
    其它情况使用捕捉的方式。
 */
public class ExceptionTest06 {
    // 一般不建议在main方法上使用throws，因为这个异常如果真正的发生了，一定会抛给JVM。JVM只有终止。
    // 异常处理机制的作用就是增强程序的健壮性。怎么能做到，异常发生了也不影响程序的执行。所以
    // 一般main方法中的异常建议使用try..catch进行捕捉。main就不要继续上抛了。
    /*
    public static void main(String[] args) throws FileNotFoundException {
        System.out.println("main begin");
        m1();
        System.out.println("main over");
    }
     */
    public static void main(String[] args) {

        // 100 / 0这是算术异常，这个异常是运行时异常，你在编译阶段，可以处理，也可以不处理。编译器不管。
        //System.out.println(100 / 0); // 不处理编译器也不管
        // 你处理也可以。

        System.out.println("main begin");
        try {
            // try尝试
            m1();
            // 以上代码出现异常，直接进入catch语句块中执行。
            System.out.println("hello world!");
        } catch (FileNotFoundException e){ // catch后面的好像一个方法的形参。
            // 这个分支中可以使用e引用，e引用保存的内存地址是那个new出来异常对象的内存地址。
            // catch是捕捉异常之后走的分支。
            // 在catch分支中干什么？处理异常。
            System.out.println("文件不存在，可能路径错误，也可能该文件被删除了！");
            System.out.println(e); //java.io.FileNotFoundException: D:\course\01-课\学习方法.txt (系统找不到指定的路径。)
        }

        // try..catch把异常抓住之后，这里的代码会继续执行。
        System.out.println("main over");
    }

    private static void m1() throws FileNotFoundException {
        System.out.println("m1 begin");
        m2();
        // 以上代码出异常，这里是无法执行的。
        System.out.println("m1 over");
    }

    // 抛别的不行，抛ClassCastException说明你还是没有对FileNotFoundException进行处理
    //private static void m2() throws ClassCastException{

    // 抛FileNotFoundException的父对象IOException，这样是可以的。因为IOException包括FileNotFoundException
    //private static void m2() throws IOException {

    // 这样也可以，因为Exception包括所有的异常。
    //private static void m2() throws Exception{

    // throws后面也可以写多个异常，可以使用逗号隔开。
    //private static void m2() throws ClassCastException, FileNotFoundException{
    private static void m2() throws FileNotFoundException {
        System.out.println("m2 begin");
        // 编译器报错原因是：m3()方法声明位置上有：throws FileNotFoundException
        // 我们在这里调用m3()没有对异常进行预处理，所以编译报错。
        // m3();

        m3();
        // 以上如果出现异常，这里是无法执行的！
        System.out.println("m2 over");
    }

    private static void m3() throws FileNotFoundException {
        /*
        编译报错的原因是什么？
            第一：这里调用了一个构造方法：FileInputStream(String name)
            第二：这个构造方法的声明位置上有：throws FileNotFoundException
            第三：通过类的继承结构看到：FileNotFoundException父类是IOException，IOException的父类是Exception，最终得知，FileNotFoundException是编译时异常。

            错误原因？编译时异常要求程序员编写程序阶段必须对它进行处理，不处理编译器就报错。
         */
        //new FileInputStream("D:\\course\\01-开课\\学习方法.txt");

        // 第一种处理方式：在方法声明的位置上使用throws继续上抛。
        // 一个方法体当中的代码出现异常之后，如果上报的话，此方法结束。
        new FileInputStream("D:\\course\\01-课\\学习方法.txt");
        System.out.println("如果以上代码出异常，这里会执行吗??不会！！！");
    }
}

```

第一种方式：在方法声明的位置上，使用throws关键字，抛给上一级。谁调用我，我就抛给谁。抛给上一级。

第二种方式：使用try..catch语句进行异常的捕捉。这件事发生了，谁也不知道，因为我给抓住了。

举个例子：
我是某集团的一个销售员，因为我的失误，导致公司损失了1000元，“损失1000元”这可以看做是一个异常发生了。我有两种处理方式，第一种方式：我把这件事告诉我的领导【异常上抛】第二种方式：我自己掏腰包把这个钱补上。【异常的捕捉】

张三 --> 李四 ---> 王五 --> CEO

思考：
异常发生之后，如果我选择了上抛，抛给了我的调用者，调用者需要对这个异常继续处理，那么调用者处理这个异常同样有两种处理方式。

注意：Java中异常发生之后如果一直上抛，最终抛给了main方法，main方法继续向上抛，抛给了调用者JVM，JVM知道这个异常发生，只有一个结果。终止java程序的执行。

### 深入理解try cache机制

```java
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

/*
深入try..catch
    1、catch后面的小括号中的类型可以是具体的异常类型，也可以是该异常类型的父类型。
    2、catch可以写多个。建议catch的时候，精确的一个一个处理。这样有利于程序的调试。
    3、catch写多个的时候，从上到下，必须遵守从小到大。
 */
public class ExceptionTest07 {

    public static void main(String[] args) {

        // 编译报错。

        try {
            //创建输入流
            FileInputStream fis = new FileInputStream("\JavaSE进阶-01-面向对象.pdf");
            //读文件
            fis.read();
        } catch(IOException e){
            System.out.println("读文件报错了！");
        } catch(FileNotFoundException e) {
            System.out.println("文件不存在！");
        }

//-------------------------------------------------


        // JDK8的新特性！
        try {
            //创建输入流
            FileInputStream fis = new FileInputStream("\JavaSE进阶-01-面向对象.pdf");
            // 进行数学运算
            System.out.println(100 / 0); // 这个异常是运行时异常，编写程序时可以处理，也可以不处理。
        } catch(FileNotFoundException | ArithmeticException | NullPointerException e) {
			//可以使用或符号进行声明异常类型
            System.out.println("文件不存在？数学异常？空指针异常？都有可能！");
        }
    }
}
```

### 异常对象的常用方法

```java
import java.io.FileInputStream;
import java.io.FileNotFoundException;

/*
异常对象有两个非常重要的方法：

    获取异常简单的描述信息：
        String msg = exception.getMessage();

    打印异常追踪的堆栈信息：
        exception.printStackTrace();
 */
public class ExceptionTest08 {
    public static void main(String[] args) {
        // 这里只是为了测试getMessage()方法和printStackTrace()方法。
        // 这里只是new了异常对象，但是没有将异常对象抛出。JVM会认为这是一个普通的java对象。
        NullPointerException e = new NullPointerException("空指针异常");
        // 获取异常简单描述信息：这个信息实际上就是构造方法上面String参数。
        String msg = e.getMessage(); //msg = 空指针异常

        // 打印异常堆栈信息
        // java后台打印异常堆栈追踪信息的时候，采用了异步线程的方式打印的。
        e.printStackTrace();

    }
}


/*
异常对象的两个方法：
    String msg = e.getMessage();
    e.printStackTrace(); // 一般都是使用这个。

我们以后查看异常的追踪信息，我们应该怎么看，可以快速的调试程序呢？
    异常信息追踪信息，从上往下一行一行看。
    但是需要注意的是：SUN写的代码就不用看了(看包名就知道是自己的还是SUN的。)。
    主要的问题是出现在自己编写的代码上。
 */
public class ExceptionTest09 {
    public static void main(String[] args) {
        try {
            m1();
        } catch (FileNotFoundException e) {
            // 获取异常的简单描述信息
            String msg = e.getMessage();
            System.out.println(msg); //C:\jetns-agent.jar (系统找不到指定的文件。)

            //在实际的开发中，建议使用这个。养成好习惯！
            // 这行代码要写上，不然出问题你也不知道！
            //打印异常堆栈追踪信息！
            //e.printStackTrace();
            /*
				java.io.FileNotFoundException: C:\jetns-agent.jar (系统找不到指定的文件。)
                at com.bjpowernode.javase.exception.ExceptionTest09.m3(ExceptionTest09.java:31)
                at com.bjpowernode.javase.exception.ExceptionTest09.m2(ExceptionTest09.java:27)
                at com.bjpowernode.javase.exception.ExceptionTest09.m1(ExceptionTest09.java:23)
                at com.bjpowernode.javase.exception.ExceptionTest09.main(ExceptionTest09.java:14)
                因为31行出问题导致了27行
                27行出问题导致23行
                23行出问题导致14行。
                应该先查看31行的代码。31行是代码错误的根源。
             */
        }

        // 这里程序不耽误执行，很健壮。《服务器不会因为遇到异常而宕机》
        System.out.println("Hello World!");
    }

    private static void m1() throws FileNotFoundException {
        m2();
    }

    private static void m2() throws FileNotFoundException {
        m3();
    }

    private static void m3() throws FileNotFoundException {
        new FileInputStream("C:\\jetns-agent.jar");
    }
}

```

### finally子句的使用

```java
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

/*
关于try..catch中的finally子句：
    1、在finally子句中的代码是最后执行的，并且是一定会执行的，即使try语句块中的代码出现了异常。（除非退出JVM）
        finally子句必须和try一起出现，不能单独编写。

    2、finally语句通常使用在哪些情况下呢？
        通常在finally语句块中完成资源的释放/关闭。
		因为finally中的代码比较有保障。
		即使try语句块中的代码出现异常，finally中代码也会正常执行。
 */

public class ExceptionTest10 {
    public static void main(String[] args) {
        FileInputStream fis = null; // 声明位置放到try外面。这样在finally中才能用。

		try {
            // 创建输入流对象
            fis = new FileInputStream("D:\\course\\02-JavaSE\\document\\JavaSE进阶讲义\\JavaSE进阶-01-面向对象.pdf");
            // 开始读文件....

            String s = null;
            // 这里一定会出现空指针异常！
            s.toString();
            System.out.println("hello world!");

            // 流使用完需要关闭，因为流是占用资源的。
            // 即使以上程序出现异常，流也必须要关闭！
            // 放在这里有可能流关不了。
            //fis.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch(IOException e){
            e.printStackTrace();
        } catch(NullPointerException e) {
            e.printStackTrace();
        } finally {
            System.out.println("hello Finally ！");
            // 流的关闭放在这里比较保险。
            // finally中的代码是一定会执行的。
            // 即使try中出现了异常！
            if (fis != null) { // 避免空指针异常！
                try {
                    // close()方法有异常，采用捕捉的方式。
                    fis.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}


/*
finally语句：
    放在finally语句块中的代码是一定会执行的（除非退出JVM）【再次强调！！！】
 */
public class ExceptionTest11 {
    public static void main(String[] args) {
        /*
        try和finally，没有catch可以吗？可以。
            try不能单独使用。
            try finally可以联合使用。
        以下代码的执行顺序：
            先执行try...
            再执行finally...
            最后执行 return （return语句只要执行方法必然结束。）
         */
        try {
            System.out.println("try...");
            return;
        } finally {
            // finally中的语句会执行。能执行到。
            System.out.println("finally...");
        }
        // 这里不能写语句，因为这个代码是无法执行到的。
        //System.out.println("Hello World!");
    }
}


public class ExceptionTest12 {
    public static void main(String[] args) {
        try {
            System.out.println("try...");
            // 退出JVM
            System.exit(0); // 退出JVM之后，finally语句中的代码就不执行了！
        } finally {
            System.out.println("finally...");
        }
    }
}


//----------------面试题

/*
【面试题】【特殊情况】
 */
public class ExceptionTest13 {
    public static void main(String[] args) {
        int result = m();
        System.out.println(result); //100
    }

    /*
    java语法规则（有一些规则是不能破坏的，一旦这么说了，就必须这么做！）：
        java中有一条这样的规则：
            方法体中的代码必须遵循自上而下顺序依次逐行执行（亘古不变的语法！）
        java中还有一条语法规则：
            return语句一旦执行，整个方法必须结束（亘古不变的语法！）
     */
    public static int m(){
        int i = 100;
        try {
            // 这行代码出现在int i = 100;的下面，所以最终结果必须是返回100
            // return语句还必须保证是最后执行的。一旦执行，整个方法结束。
            return i;
        } finally {
            i++;
        }
    }
}

/*
反编译之后的效果
public static int m(){
    int i = 100;
    int j = i;
    i++;
    return j;
}
 */

```

### finally finalize final

```java
/*
final finally finalize有什么区别？
    final 关键字
        final修饰的类无法继承
        final修饰的方法无法覆盖
        final修饰的变量不能重新赋值。

    finally 关键字
        和try一起联合使用。
        finally语句块中的代码是必须执行的。

    finalize 标识符
        是一个Object类中的方法名。
        这个方法是由垃圾回收器GC负责调用的。
 */
public class ExceptionTest14 {
    public static void main(String[] args) {

        // final是一个关键字。表示最终的。不变的。
        final int i = 100;
        //i = 200;

        // finally也是一个关键字，和try联合使用，使用在异常处理机制中
        // 在fianlly语句块中的代码是一定会执行的。
        try {

        } finally {
            System.out.println("finally....");
        }

        // finalize()是Object类中的一个方法。作为方法名出现。
        // 所以finalize是标识符。
        // finalize()方法是JVM的GC垃圾回收器负责调用。
        Object obj;
    }
}

// final修饰的类无法继承
final class A {
    // 常量。
    public static final double MATH_PI = 3.1415926;
}

class B {
    // final修饰的方法无法覆盖
    public final void doSome(){

    }
}
```

### 自定义异常

```java
/*
1、SUN提供的JDK内置的异常肯定是不够的用的。在实际的开发中，有很多业务，
这些业务出现异常之后，JDK中都是没有的。和业务挂钩的。那么异常类我们
程序员可以自己定义吗？
    可以。

2、Java中怎么自定义异常呢？
    两步：
        第一步：编写一个类继承Exception或者RuntimeException.
        第二步：提供两个构造方法，一个无参数的，一个带有String参数的。

    死记硬背。
 */
public class MyException extends Exception{ // 编译时异常
    public MyException(){

    }
    public MyException(String s){
        super(s);
    }
}

/*
public class MyException extends RuntimeException{ // 运行时异常

}
 */


public class ExceptionTest15 {
    public static void main(String[] args) {

        // 创建异常对象（只new了异常对象，并没有手动抛出）
        MyException e = new MyException("用户名不能为空！");

        // 打印异常堆栈信息
        e.printStackTrace();

        // 获取异常简单描述信息
        String msg = e.getMessage();
        System.out.println(msg);
    }
}
```

### 例题

```java
/*
	编写程序，使用一维数组，模拟栈数据结构。
	【有删减】
 */
public class MyStack {

    private Object[] elements;



    /**
     * 压栈的方法
     * @param obj 被压入的元素
     */
    public void push(Object obj) throws MyStackOperationException {
        if(index >= elements.length - 1){
            // 手动抛出异常！
            throw new MyStackOperationException("压栈失败，栈已满！");
        }

	}
    /**
     * 弹栈的方法，从数组中往外取元素。每取出一个元素，栈帧向下移动一位。
     * @return
     */
    public void pop() throws MyStackOperationException {
        if(index < 0){
            throw new MyStackOperationException("弹栈失败，栈已空！");
        }
        // 程序能够执行到此处说明栈没有空。

    }

/**
 * 栈操作异常：自定义异常！
 */
public class MyStackOperationException extends Exception{ // 编译时异常！

    public MyStackOperationException(){

    }

    public MyStackOperationException(String s){
        super(s);
    }

}

```