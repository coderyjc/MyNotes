#Java/数组

# 数组和常用类

## 数组

Java语言中的数组是一种引用数据类型。不属于基本数据类型。数组的父类是Object

数组实际上是一个容器，可以同时容纳多个元素。（数组是一个数据的集合。）数组：字面意思是“一组数据”

数组当中可以存储“基本数据类型”的数据，也可以存储“引用数据类型”的数据

数组是存储在堆当中的

数组当中如果存储的是“java对象”的话，实际上存储的是对象的“引用（内存地址）”，数组中不能直接存储java对象。

数组长度不可变

所有的数组对象都有length**属性**(java自带的)，用来获取数组中元素的个数。

java中的数组要求数组中元素的类型统一。比如int类型数组只能存储int类型，Person类型数组只能存储Person类型。

数组在内存方面存储的时候，数组中的元素内存地址(存储的每一个元素都是有规则的挨着排列的)是连续的。内存地址连续。  这是数组存储元素的特点（特色）。数组实际上是一种简单的数据结构。

所有的数组都是拿“第一个小方框的内存地址”作为整个数组对象的内存地址。   （数组中首元素的内存地址作为整个数组对象的内存地址。）

数组中每一个元素都是有下标的，下标从0开始，以1递增。最后一个元素的下标是：length - 1

> 数组这种数据结构的优点和缺点是什么？
>
> **优点**：查询/查找/检索某个下标上的元素时效率极高。可以说是查询效率最高的一个数据结构。
>
> **缺点**：
> 1.由于为了保证数组中每个元素的内存地址连续，所以在数组上随机删除或者增加元素的时候，效率较低，因为随机增删元素会涉及到后面元素统一向前或者向后位移的操作。（注意：对于数组中最后一个元素的增删，是没有效率影响的。）
> 2.数组不能存储大数据量。为什么？   因为很难在内存空间上找到一块特别大的连续的内存空间。
>
> 为什么检索效率高？
>
> 1.每一个元素的内存地址在空间存储上是连续的。
> 2.每一个元素类型相同，所以占用空间大小一样。
> 3.知道第一个元素内存地址，知道每一个元素占用空间的大小，又知道下标，所以通过一个数学表达式就可以计算出某个下标上元素的内存地址。直接通过内存地址定位 元素，所以数组的检索效率是最高的。

```java
public class ArrayTest01 {
    public static void main(String[] args) {
        // 声明一个int类型的数组，使用静态初始化的方式
        int[] a = {1, 100, 10, 20, 55, 689};

        // 下标为6表示第7个元素，第7个元素没有，下标越界了。会出现什么异常呢？
        //System.out.println(a[6]); //ArrayIndexOutOfBoundsException
    }
}
```

什么时候采用静态初始化方式，什么时候使用动态初始化方式呢？

- 当你创建数组的时候，确定数组中存储哪些具体的元素时，采用静态初始化方式。
- 当你创建数组的时候，不确定将来数组中存储哪些数据，你可以采用动态初始化的方式，预先分配内存空间。

```java
public class ArrayTest02 {
    public static void main(String[] args) {
        // 采用动态初始化的方式
        int[] a = new int[4]; // 创建长度为4的int数组，数组中每个元素的默认值是0
        Object[] objs = new Object[3]; // 3个长度，动态初始化，所以每个元素默认值是null

        // 采用静态初始化的方式
        String[] strs2 = {"abc", "def", "xyz"};
        for (int i = 0; i < strs2.length; i++) {
            System.out.println(strs2[i]);
        }

        Object[] objects = {new Object(), new Object(), new Object()};

        }
    }
}



// 当一个方法的参数是一个数组的时候，我们还可以采用这种方式传递参数

public class ArrayTest04 {
    public static void main(String[] args) {
        // 静态初始化一维数组
        int[] a = {1,2,3};
        printArray(a);
        
        // 没有这种语法。
        //printArray({1,2,3});
        
        // 如果直接传递一个静态数组的话，语法必须这样写。
        printArray(new int[]{1,2,3});

        // 动态初始化一维数组
        int[] a2 = new int[4];
        printArray(a2);

        printArray(new int[3]);
    }
}

```

### main方法的String[] 参数

```java
/*
1、main方法上面的“String[] args”有什么用？
    分析以下：谁负责调用main方法（JVM）
    JVM调用main方法的时候，会自动传一个String数组过来。
 */
public class ArrayTest05 {
    // 这个方法程序员负责写出来，JVM负责调用。JVM调用的时候一定会传一个String数组过来。
    public static void main(String[] args) {
        // JVM默认传递过来的这个数组对象的长度？默认0
        // 通过测试得出：args不是null。
        System.out.println("JVM给传递过来的String数组参数，它这个数组的长度是？" + args.length);
	}
}
```

### 引用数据类型

```java
/**
 * 一维数组的深入，数组中存储的类型为：引用数据类型
 * 对于数组来说，实际上只能存储java对象的“内存地址”。数组中存储的每个元素是“引用”。
 */
public class ArrayTest07 {
    public static void main(String[] args) {

        // 创建一个Animal类型的数组，数组当中存储Cat和Bird
        Cat c = new Cat();
        Bird b = new Bird();
        Animal[] anis = {c, b};

        //Animal[] anis = {new Cat(), new Bird()}; // 该数组中存储了两个对象的内存地址。
        for (int i = 0; i < anis.length; i++){
            // 这个取出来的可能是Cat，也可能是Bird，不过肯定是一个Animal
            // 如果调用的方法是父类中存在的方法不需要向下转型。直接使用父类型引用调用即可。
            //anis[i]
            //Animal an = anis[i];
            //an.move();

            //Animal中没有sing()方法。
            //anis[i].sing();

            // 调用子对象特有方法的话，需要向下转型！！！
            if(anis[i] instanceof Cat){
                Cat cat = (Cat)anis[i];
                cat.catchMouse();
            }else if(anis[i] instanceof Bird){
                Bird bird = (Bird)anis[i];
                bird.sing();
            }
        }
    }
}
```

### 数组的扩容和拷贝

关于一维数组的扩容。

在java开发中，数组长度一旦确定不可变，那么数组满了怎么办？扩容。

java中对数组的扩容是：先新建一个大容量的数组，然后将小容量数组中的数据一个一个拷贝到大数组当中。

结论：数组扩容效率较低。因为涉及到拷贝的问题。所以在以后的开发中请注意：尽可能少的进行数组的拷贝。

可以在创建数组对象的时候预估计以下多长合适，最好预估准确，这样可以减少数组的扩容次数。提高效率。

```java
public class ArrayTest08 {
    public static void main(String[] args) {
        // java中的数组是怎么进行拷贝的呢？
        //System.arraycopy(5个参数);

        // 拷贝源（从这个数组中拷贝）
        int[] src = {1, 11, 22, 3, 4};

        // 拷贝目标（拷贝到这个目标数组上）
        int[] dest = new int[20]; // 动态初始化一个长度为20的数组，每一个元素默认值0

        System.arraycopy(src, 0, dest, 0, src.length);


        // 数组中如果存储的元素是引用，可以拷贝吗？当然可以。
        String[] strs = {"hello", "world!", "study", "java", "oracle", "mysql", "jdbc"};
        String[] newStrs = new String[20];
        System.arraycopy(strs, 0, newStrs, 0, strs.length);

        System.out.println("================================");
        Object[] objs = {new Object(), new Object(), new Object()};
        Object[] newObjs = new Object[5];
        // 思考一下：这里拷贝的时候是拷贝对象，还是拷贝对象的地址。（地址。）
        System.arraycopy(objs, 0, newObjs, 0, objs.length);
    }
}

```

### 二维数组

```java
public class ArrayTest11 {
    public static void main(String[] args) {

        // 二维数组
        String[][] array = {
                {"java", "oracle", "c++", "python", "c#"},
                {"张三", "李四", "王五"},
                {"lucy", "jack", "rose"}
        };

        // 合并代码
        for(int i = 0; i < array.length; i++){ // 外层循环3次。（负责纵向。）
            for(int j = 0; j < array[i].length; j++){
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
    }
}


/*
动态初始化二维数组。
 */
public class ArrayTest12 {
    public static void main(String[] args) {
        // 3行4列。
        // 3个一维数组，每一个一维数组当中4个元素。
        int[][] array = new int[3][4];

        // 静态初始化
        int[][] a = {{1,2,3,4},{4,5,6,76},{1,23,4}};
        printArray(a);

        // 可以这样写。
        printArray(new int[][]{{1,2,3,4},{4,5,6,76},{1,23,4}});
    }

    public static void printArray(int[][] array){
        // 遍历二维数组。
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

**每次都重写toString和equals方法 ！！！！**

- 第一：空间存储上，内存地址是连续的。
- 第二：每个元素占用的空间大小相同。
- 第三：知道首元素的内存地址。
- 第四：通过下标可以计算出偏移量。

优点：检索效率高。直接通过内存地址定位，效率非常高。
缺点：随机增删效率较低，数组无法存储大数据量。
注意：数组最后一个元素的增删效率不受影响。

### 排序和查找

```java
import java.util.Arrays;

/**
 * 使用以下数组工具类：java.util.Arrays;
 */
public class ArraysTest01 {
    public static void main(String[] args) {

        int[] arr = {112,3,4,56,67,1};

        // 工具类当中的方法大部分都是静态的。
        Arrays.sort(arr);

        // 遍历输出
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}

import java.util.Arrays;

/**
 * 好消息：
 *  SUN公司已经为我们程序员写好了一个数组工具类。
 *  java.util.Arrays;
 */
public class ArraysTest02 {
    public static void main(String[] args) {
        // java.util.Arrays; 工具类中有哪些方法，我们开发的时候要参考API帮助文档
        // 不要死记硬背。
        int[] arr = {3,6,4,5,12,1,2,32,5,5};
        // 排序
        Arrays.sort(arr);
        // 输出
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
        // 二分法查找（建立在排序基础之上。）
        int index = Arrays.binarySearch(arr, 5);

        System.out.println(index == -1 ? "该元素不存在" : "该元素下标是：" + index);
    }
}

```

## 常用类

### String类

##### 基础认知

`java.lang.String`

String表示字符串类型，属于引用数据类型，不属于基本数据类型。

在java中随便使用双引号括起来的都是String对象。例："abc"，"def"，"hello world!"，这是3个String对象。

java中规定，双引号括起来的字符串，是不可变的，也就是说"abc"自出生到最终死亡，不可变，不能变成"abcd"，也不能变成"ab"

在JDK当中双引号括起来的字符串，例如："abc" "def"都是直接存储在“方法区”的“字符串常量池”当中的。为什么SUN公司把字符串存储在一个“字符串常量池”当中呢。因为字符串在实际的开发中使用太频繁。为了执行效率，所以把字符串放到了`方法区的字符串常量池`当中。

```java
public class StringTest01 {
    public static void main(String[] args) {
        // 这两行代码表示底层创建了3个字符串对象，都在字符串常量池当中。
        String s1 = "abcdef";
        String s2 = "abcdef" + "xy";

        // 分析：这是使用new的方式创建的字符串对象。这个代码中的"xy"是从哪里来的？
        // 凡是双引号括起来的都在字符串常量池中有一份。
        // new对象的时候一定在堆内存当中开辟空间。
        String s3 = new String("xy");

        // i变量中保存的是100这个值。
        int i = 100;
        // s变量中保存的是字符串对象的内存地址。
        // s引用中保存的不是"abc"，是0x1111
        // 而0x1111是"abc"字符串对象在“字符串常量池”当中的内存地址。
        String s = "abc";
    }
}
```

```java

public class StringTest02 {
    public static void main(String[] args) {
        String s1 = "hello";
        // "hello"是存储在方法区的字符串常量池当中
        // 所以这个"hello"不会新建。（因为这个对象已经存在了。）
        String s2 = "hello";
        // 分析结果是true还是false？
        // == 双等号比较的是不是变量中保存的内存地址？是的。
        System.out.println(s1 == s2); // true

        String x = new String("xyz");
        String y = new String("xyz");
        // 分析结果是true还是false？
        // == 双等号比较的是不是变量中保存的内存地址？是的。
        System.out.println(x == y); //false

        // 通过这个案例的学习，我们知道了，字符串对象之间的比较不能使用“==”
        // "=="不保险。应该调用String类的equals方法。
        // String类已经重写了equals方法，以下的equals方法调用的是String重写之后的equals方法。
        System.out.println(x.equals(y)); // true

        String k = new String("testString");
        //String k = null;
        // "testString"这个字符串可以后面加"."呢？
        // 因为"testString"是一个String字符串对象。只要是对象都能调用方法。
        System.out.println("testString".equals(k)); // 建议使用这种方式，因为这个可以避免空指针异常。
        System.out.println(k.equals("testString")); // 存在空指针异常的风险。不建议这样写。
    }
}
```

分析以下程序，一共创建了几个对象

```java
public class StringTest03 {
    public static void main(String[] args) {
        String s1 = new String("hello");
        String s2 = new String("hello");
    }
}
```

一共3个对象：

- 方法区字符串常量池中有1个："hello"堆内存当中有两个String对象，一共3个。

##### 构造方法

关于String类中的构造方法。

- 第一个：String s = new String("");
- 第二个：String s = ""; 最常用
- 第三个：String s = new String(char数组);
- 第四个：String s = new String(char数组,起始下标,长度);
- 第五个：String s = new String(byte数组);
- 第六个：String s = new String(byte数组,起始下标,长度)

```java
public class StringTest04 {
    public static void main(String[] args) {

        // 创建字符串对象最常用的一种方式
        String s1 =  "hello world!";
        // s1这个变量中保存的是一个内存地址。
        // 按说以下应该输出一个地址。
        // 但是输出一个字符串，说明String类已经重写了toString()方法。
        System.out.println(s1);//hello world!
        System.out.println(s1.toString()); //hello world!

        // 这里只掌握常用的构造方法。
        byte[] bytes = {97, 98, 99}; // 97是a，98是b，99是c
        String s2 = new String(bytes);

        // 前面说过：输出一个引用的时候，会自动调用toString()方法，默认Object的话，会自动输出对象的内存地址。
        // 通过输出结果我们得出一个结论：String类已经重写了toString()方法。
        // 输出字符串对象的话，输出的不是对象的内存地址，而是字符串本身。
        System.out.println(s2.toString()); //abc
        System.out.println(s2); //abc

        // String(字节数组,数组元素下标的起始位置,长度)
        // 将byte数组中的一部分转换成字符串。
        String s3 = new String(bytes, 1, 2);
        System.out.println(s3); // bc

        // 将char数组全部转换成字符串
        char[] chars = {'我','是','中','国','人'};
        String s4 = new String(chars);
        System.out.println(s4);
        // 将char数组的一部分转换成字符串
        String s5 = new String(chars, 2, 3);
        System.out.println(s5);

        String s6 = new String("helloworld!");
        System.out.println(s6); //helloworld!
    }
}

```

##### 常用方法

```java
public class StringTest05 {
    public static void main(String[] args) {

        // String类当中常用方法。
        //1（掌握）.char charAt(int index)
        char c = "中国人".charAt(1); // "中国人"是一个字符串String对象。只要是对象就能“点.”
        System.out.println(c); // 国

        // 2（了解）.int compareTo(String anotherString)
        // 字符串之间比较大小不能直接使用 > < ，需要使用compareTo方法。
        int result = "abc".compareTo("abc");
        System.out.println(result); //0（等于0） 前后一致  10 - 10 = 0

        int result2 = "abcd".compareTo("abce");
        System.out.println(result2); //-1（小于0） 前小后大 8 - 9 = -1

        int result3 = "abce".compareTo("abcd");
        System.out.println(result3); // 1（大于0） 前大后小 9 - 8 = 1

        // 拿着字符串第一个字母和后面字符串的第一个字母比较。能分胜负就不再比较了。
        System.out.println("xyz".compareTo("yxz")); // -1

        // 3（掌握）.boolean contains(CharSequence s)
        // 判断前面的字符串中是否包含后面的子字符串。
        System.out.println("HelloWorld.java".contains(".java")); // true

        // 4（掌握）. boolean endsWith(String suffix)
        // 判断当前字符串是否以某个子字符串结尾。
        System.out.println("test.txt".endsWith(".java")); // false
        System.out.println("test.txt".endsWith(".txt")); // true

        // 5（掌握）.boolean equals(Object anObject)
        // 比较两个字符串必须使用equals方法，不能使用“==”
        // equals方法有没有调用compareTo方法？ 老版本可以看一下。JDK13中并没有调用compareTo()方法。
        // equals只能看出相等不相等。
        // compareTo方法可以看出是否相等，并且同时还可以看出谁大谁小。
        System.out.println("abc".equals("abc")); // true

        // 6（掌握）.boolean equalsIgnoreCase(String anotherString)
        // 判断两个字符串是否相等，并且同时忽略大小写。
        System.out.println("ABc".equalsIgnoreCase("abC")); // true

        // 7（掌握）.byte[] getBytes()
        // 将字符串对象转换成字节数组
        byte[] bytes = "abcdef".getBytes();
        for(int i = 0; i < bytes.length; i++){
            System.out.println(bytes[i]);
        }

        // 8（掌握）.int indexOf(String str)
        // 判断某个子字符串在当前字符串中第一次出现处的索引（下标）。
System.out.println("oraclejavac++.netc#phppythonjavaoraclec++".indexOf("java")); // 6

        // 9（掌握）.boolean isEmpty()
        // 判断某个字符串是否为“空字符串”。底层源代码调用的应该是字符串的length()方法。
        //String s = "";
        String s = "a";
        System.out.println(s.isEmpty());

        // 10（掌握）. int length()
        // 面试题：判断数组长度和判断字符串长度不一样
        // 判断数组长度是length属性，判断字符串长度是length()方法。
        System.out.println("abc".length()); // 3
        System.out.println("".length()); // 0

        // 11（掌握）.int lastIndexOf(String str)
        // 判断某个子字符串在当前字符串中最后一次出现的索引（下标）
        System.out.println("oraclejavac++javac#phpjavapython".lastIndexOf("java")); //22

        // 12（掌握）. String replace(CharSequence target, CharSequence replacement)
        // 替换。
        // String的父接口就是：CharSequence
        String newString = "http://www.baidu.com".replace("http://", "https://");
        System.out.println(newString); //https://www.baidu.com
        // 把以下字符串中的“=”替换成“:”
        String newString2 = "name=zhangsan&password=123&age=20".replace("=", ":");
        System.out.println(newString2); //name:zhangsan&password:123&age:20

        // 13（掌握）.String[] split(String regex)
        // 拆分字符串
        String[] ymd = "1980-10-11".split("-"); //"1980-10-11"以"-"分隔符进行拆分。

        // 14（掌握）、boolean startsWith(String prefix)
        // 判断某个字符串是否以某个子字符串开始。
        System.out.println("http://www.baidu.com".startsWith("http")); // true

        // 15（掌握）、 String substring(int beginIndex) 参数是起始下标。
        // 截取字符串
        System.out.println("http://www.baidu.com".substring(7)); //www.baidu.com

        // 16（掌握）、String substring(int beginIndex, int endIndex)
        // beginIndex起始位置（包括）
        // endIndex结束位置（不包括）
        System.out.println("http://www.baidu.com".substring(7, 10)); //www

        // 17(掌握)、char[] toCharArray()
        // 将字符串转换成char数组
        char[] chars = "我是中国人".toCharArray();
        for(int i = 0; i < chars.length; i++){
            System.out.println(chars[i]);
        }

        // 18（掌握）、String toLowerCase()
        // 转换为小写。
        System.out.println("ABCDefKXyz".toLowerCase());

        // 19（掌握）、String toUpperCase();
        System.out.println("ABCDefKXyz".toUpperCase());

        // 20（掌握）. String trim();
        // 去除字符串前后空白
        System.out.println("           hello      world             ".trim());

        // 21（掌握）. String中只有一个方法是静态的，不需要new对象
        // 这个方法叫做valueOf
        // 作用：将“非字符串”转换成“字符串”
        //String s1 = String.valueOf(true);
        //String s1 = String.valueOf(100);
        //String s1 = String.valueOf(3.14);

        // 这个静态的valueOf()方法，参数是一个对象的时候，会自动调用该对象的toString()方法吗？
        String s1 = String.valueOf(new Customer());
        //System.out.println(s1); // 没有重写toString()方法之前是对象内存地址 com.bjpowernode.javase.string.Customer@10f87f48
        System.out.println(s1); //我是一个VIP客户！！！！

        // 我们是不是可以研究一下println()方法的源代码了？
        System.out.println(100);
        System.out.println(3.14);
        System.out.println(true);

        Object obj = new Object();
        // 通过源代码可以看出：为什么输出一个引用的时候，会调用toString()方法!!!!
        //　本质上System.out.println()这个方法在输出任何数据的时候都是先转换成字符串，再输出。
        System.out.println(obj);

        System.out.println(new Customer());
    }
}

class Customer {
    // 重写toString()方法
    @Override
    public String toString() {
        return "我是一个VIP客户！！！！";
    }
}
```

如果以后需要进行大量字符串的拼接操作，建议使用JDK中自带的：

- java.lang.StringBuffer
- java.lang.StringBuilder

如何优化StringBuffer的性能？

- 在创建StringBuffer的时候尽可能给定一个初始化容量。
- 最好减少底层数组的扩容次数。预估计一下，给一个大一些初始化容量。
- 关键点：给一个合适的初始化容量。可以提高程序的执行效率。

```java
public class StringBufferTest02 {
    public static void main(String[] args) {

        // 创建一个初始化容量为16个byte[] 数组。（字符串缓冲区对象）
        StringBuffer stringBuffer = new StringBuffer();

        // 拼接字符串，以后拼接字符串统一调用 append()方法。
        // append是追加的意思。
        stringBuffer.append("a");
        stringBuffer.append(3.14);
        stringBuffer.append(true);
        // append方法底层在进行追加的时候，如果byte数组满了，会自动扩容。
        stringBuffer.append(100L);

        System.out.println(stringBuffer.toString());

        // 指定初始化容量的StringBuffer对象（字符串缓冲区对象）
        StringBuffer sb = new StringBuffer(100);
        sb.append("hello");
        System.out.println(sb);
    }
}
```

面试题：String为什么是不可变的？

- 我看过源代码，String类中有一个byte[]数组，这个byte[]数组采用了final修饰，因为数组一旦创建长度不可变。并且被final修饰的引用一旦指向某个对象之后，不可再指向其它对象，所以String是不可变的！"abc" 无法变成 "abcd"

StringBuilder/StringBuffer为什么是可变的呢？

- 我看过源代码，StringBuffer/StringBuilder内部实际上是一个byte[]数组，    这个byte[]数组没有被final修饰，StringBuffer/StringBuilder的初始化容量我记得应该是16，当存满之后会进行扩容，底层调用了数组拷贝的方法System.arraycopy()...是这样扩容的。所以StringBuilder/StringBuffer适合于使用字符串的频繁拼接操作。

```java
package com.bjpowernode.javase.stringbuffer;

public class StringBufferTest04 {
    public static void main(String[] args) {

        // 字符串不可变是什么意思？
        // 是说双引号里面的字符串对象一旦创建不可变。
        String s = "abc"; //"abc"放到了字符串常量池当中。"abc"不可变。

        // s变量是可以指向其它对象的。
        // 字符串不可变不是说以上变量s不可变。说的是"abc"这个对象不可变。
        s = "xyz";//"xyz"放到了字符串常量池当中。"xyz"不可变。
    }
}
```

java.lang.StringBuilder

StringBuffer和StringBuilder的区别？

- StringBuffer中的方法都有：synchronized关键字修饰。表示StringBuffer在多线程环境下运行是安全的。
- StringBuilder中的方法都没有：synchronized关键字修饰，表示StringBuilder在多线程环境下运行是不安全的。
 
```java
public class StringBuilderTest01 {
    public static void main(String[] args) {

        // 使用StringBuilder也是可以完成字符串的拼接。
        StringBuilder sb = new StringBuilder();
        sb.append(100);
        sb.append(true);
        sb.append("hello");
        sb.append("kitty");
        System.out.println(sb);
    }
}
```

### 基本数据类型对应的包装类

包装类存在有什么用？方便编程。

八种包装类的类名是什么？

- Byte
- Short
- Integer
- Long
- Float
- Double
- Boolean
- Character

所有数字的父类Number
照葫芦画瓢：学习Integer，其它的模仿Integer。

**这里只写Integer的包装类，其他照葫芦画瓢**

```java
/*
1、java中为8种基本数据类型又对应准备了8种包装类型。8种包装类属于引用数据类型，父类是Object。
2、思考：为什么要再提供8种包装类呢？因为8种基本数据类型不够用。所以SUN又提供对应的8种包装类型。
 */
public class IntegerTest01 {
    //入口
    public static void main(String[] args) {
        // 有没有这种需求：调用doSome()方法的时候需要传一个数字进去。
        // 但是数字属于基本数据类型，而doSome()方法参数的类型是Object。
        // 可见doSome()方法无法接收基本数据类型的数字。那怎么办呢？可以传一个数字对应的包装类进去。
    }

    public static void doSome(Object obj){
        //System.out.println(obj);
        System.out.println(obj.toString());
    }
}
```

|基本数据类型|包装类型|
|-----|-----|
 |   byte         |           java.lang.Byte（父类Number）|
|    short        |           java.lang.Short（父类Number）|
|    int            |         java.lang.Integer（父类Number）|
|    long         |           java.lang.Long（父类Number）|
|    float          |         java.lang.Float（父类Number）|
|    double       |           java.lang.Double（父类Number）|
 |   boolean     |            java.lang.Boolean（父类Object）|
  |  char             |       java.lang.Character（父类Object）|

以上八种包装类中，重点以java.lang.Integer为代表进行学习，其它的类型照葫芦画瓢就行。

八种包装类中其中6个都是数字对应的包装类，他们的父类都是Number，可以先研究一下Number中公共的方法：Number是一个抽象类，无法实例化对象。
Number类中有这样的方法：
- byte byteValue() 以 byte 形式返回指定的数值。
- abstract  double doubleValue()以 double 形式返回指定的数值。
- abstract  float floatValue()以 float 形式返回指定的数值。
- abstract  int intValue()以 int 形式返回指定的数值。
- abstract  long longValue()以 long 形式返回指定的数值。
- short shortValue()以 short 形式返回指定的数值。

这些方法其实所有的数字包装类的子类都有，这些方法是负责拆箱的。

```java
public class IntegerTest02 {
    public static void main(String[] args) {

        // 123这个基本数据类型，进行构造方法的包装达到了：基本数据类型向引用数据类型的转换。
        // 基本数据类型 -(转换为)->引用数据类型（装箱）
        Integer i = new Integer(123);

        // 将引用数据类型--(转换为)-> 基本数据类型
        float f = i.floatValue();
        System.out.println(f); //123.0

        // 将引用数据类型--(转换为)-> 基本数据类型（拆箱）
        int retValue = i.intValue();
        System.out.println(retValue); //123
    }
}

/*
关于Integer类的构造方法，有两个：
    Integer(int)
    Integer(String)
*/


/**
 * 好消息：在java5之后，引入了一种新特性，自动装箱和自动拆箱
 *  自动装箱：基本数据类型自动转换成包装类。
 *  自动拆箱：包装类自动转换成基本数据类型。
 *
 * 有了自动拆箱之后，Number类中的方法就用不着了！
 *
 * 自动装箱和自动拆箱的好处？
 *      方便编程。
 */
public class IntegerTest05 {
    public static void main(String[] args) {

        // 900是基本数据类型
        // x是包装类型
        // 基本数据类型 --(自动转换)--> 包装类型：自动装箱
        Integer x = 900;

        // x是包装类型
        // y是基本数据类型
        // 包装类型 --(自动转换)--> 基本数据类型：自动拆箱
        int y = x;

        // z是一个引用，z是一个变量，z还是保存了一个对象的内存地址。
        Integer z = 1000; // 等同于：Integer z = new Integer(1000);
        // 分析为什么这个没有报错呢？
        // +两边要求是基本数据类型的数字，z是包装类，不属于基本数据类型，这里会进行自动拆箱。将z转换成基本数据类型
        // 在java5之前你这样写肯定编译器报错。
        System.out.println(z + 1);

        Integer a = 1000; // Integer a = new Integer(1000); a是个引用，保存内存地址指向对象。
        Integer b = 1000; // Integer b = new Integer(1000); b是个引用，保存内存地址指向对象。
        // == 比较的是对象的内存地址，a和b两个引用中保存的对象内存地址不同。
        // == 这个运算符不会触发自动拆箱机制。（只有+ - * /等运算的时候才会。）
        System.out.println(a == b); //false
    }
}

/*
这个题目是Integer非常重要的面试题。
 */
public class IntegerTest06 {
    public static void main(String[] args) {

        Integer a = 128;
        Integer b = 128;
        System.out.println(a == b); //false

        /*
        java中为了提高程序的执行效率，将[-128到127]之间所有的包装对象提前创建好，
        放到了一个方法区的“整数型常量池”当中了，目的是只要用这个区间的数据不需要
        再new了，直接从整数型常量池当中取出来。

        原理：x变量中保存的对象的内存地址和y变量中保存的对象的内存地址是一样的。
         */
        Integer x = 127;
        Integer y = 127;
        // == 永远判断的都是两个对象的内存地址是否相同。
        System.out.println(x == y); //true
    }
}
```

**总结一下以前遇到的经典的异常**

```java
/*
总结一下之前所学的经典异常？
    空指针异常：NullPointerException
    类型转换异常：ClassCastException
    数组下标越界异常：ArrayIndexOutOfBoundsException
    数字格式化异常：NumberFormatException

Integer类当中有哪些常用的方法呢？
 */
public class IntegerTest07 {
    public static void main(String[] args) {

        // 手动装箱
        Integer x = new Integer(1000);

        // 手动拆箱。
        int y = x.intValue();
        Integer a = new Integer("123");

        // 编译的时候没问题，一切符合java语法，运行时会不会出问题呢？
        // 不是一个“数字”可以包装成Integer吗？不能。运行时出现异常。
        // java.lang.NumberFormatException
        //Integer a = new Integer("中文");

        // 重点方法
        // static int parseInt(String s)
        // 静态方法，传参String，返回int
        //网页上文本框中输入的100实际上是"100"字符串。后台数据库中要求存储100数字，此时java程序需要将"100"转换成100数字。
        int retValue = Integer.parseInt("123"); // String -转换-> int
        //int retValue = Integer.parseInt("中文"); // NumberFormatException
        System.out.println(retValue + 100);

        // 照葫芦画瓢
        double retValue2 = Double.parseDouble("3.14");
        System.out.println(retValue2 + 1); //4.140000000000001（精度问题）

        float retValue3 = Float.parseFloat("1.0");
        System.out.println(retValue3 + 1); //2.0

        // -----------------------------------以下内容作为了解，不需要掌握---------------------------------------
        // static String toBinaryString(int i)
        // 静态的：将十进制转换成二进制字符串。
        String binaryString = Integer.toBinaryString(3);
        System.out.println(binaryString); //"11" 二进制字符串

        // static String toHexString(int i)
        // 静态的：将十进制转换成十六进制字符串。
        String hexString = Integer.toHexString(16);
        System.out.println(hexString); // "10"

        // 十六进制：1 2 3 4 5 6 7 8 9 a b c d e f 10 11 12 13 14 15 16 17 18 19 1a
        hexString = Integer.toHexString(17);
        System.out.println(hexString); // "11"

        //static String toOctalString(int i)
        // 静态的：将十进制转换成八进制字符串。
        String octalString = Integer.toOctalString(8);
        System.out.println(octalString); // "10"

        System.out.println(new Object()); //java.lang.Object@6e8cf4c6

        // valueOf方法作为了解
        //static Integer valueOf(int i)
        // 静态的：int-->Integer
        Integer i1 = Integer.valueOf(100);
        System.out.println(i1);

        // static Integer valueOf(String s)
        // 静态的：String-->Integer
        Integer i2 = Integer.valueOf("100");
        System.out.println(i2);
    }
}

```

Integer String int三种类型互相转换

![1593166561323](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1593166561323.png)

### 日期类

```java
import java.text.SimpleDateFormat;
import java.util.Date;

/*
java中对日期的处理
    这个案例最主要掌握：
        知识点1：怎么获取系统当前时间
        知识点2：String ---> Date
        知识点3：Date ---> String
 */
public class DateTest01 {
    public static void main(String[] args) throws Exception {

        // 获取系统当前时间（精确到毫秒的系统当前时间） 直接调用无参数构造方法就行。
        Date nowTime = new Date();

        // java.util.Date类的toString()方法已经被重写了。
        // 输出的应该不是一个对象的内存地址，应该是一个日期字符串。
        //System.out.println(nowTime); //Thu Mar 05 10:51:06 CST 2020

        // 日期可以格式化吗？
        // 将日期类型Date，按照指定的格式进行转换：Date --转换成具有一定格式的日期字符串-->String
        // SimpleDateFormat是java.text包下的。专门负责日期格式化的。
        /*
        yyyy 年(年是4位)
        MM 月（月是2位）
        dd 日
        HH 时
        mm 分
        ss 秒
        SSS 毫秒（毫秒3位，最高999。1000毫秒代表1秒）
        注意：在日期格式中，除了y M d H m s S这些字符不能随便写之外，剩下的符号格式自己随意组织。
         */
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss SSS");
        String nowTimeStr = sdf.format(nowTime);
        System.out.println(nowTimeStr);

        // 假设现在有一个日期字符串String，怎么转换成Date类型？
        // String --> Date
        String time = "2008-08-08 08:08:08 888";
        //SimpleDateFormat sdf2 = new SimpleDateFormat("格式不能随便写，要和日期字符串格式相同");
        // 注意：字符串的日期格式和SimpleDateFormat对象指定的日期格式要一致。不然会出现异常：java.text.ParseException
        SimpleDateFormat sdf2 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss SSS");
        Date dateTime = sdf2.parse(time);
        System.out.println(dateTime); //Fri Aug 08 08:08:08 CST 2008
    }
}


/*
获取自1970年1月1日 00:00:00 000到当前系统时间的总毫秒数。
1秒 = 1000毫秒

简单总结一下System类的相关属性和方法：
    System.out 【out是System类的静态变量。】
    System.out.println() 【println()方法不是System类的，是PrintStream类的方法。】
    System.gc() 建议启动垃圾回收器
    System.currentTimeMillis() 获取自1970年1月1日到系统当前时间的总毫秒数。
    System.exit(0) 退出JVM。
 */
public class DateTest02 {
    public static void main(String[] args) {
        // 获取自1970年1月1日 00:00:00 000到当前系统时间的总毫秒数。
        long nowTimeMillis = System.currentTimeMillis();
        System.out.println(nowTimeMillis); //1583377912981

        // 统计一个方法耗时
        // 在调用目标方法之前记录一个毫秒数
        long begin = System.currentTimeMillis();
        print();
        // 在执行完目标方法之后记录一个毫秒数
        long end = System.currentTimeMillis();
        System.out.println("耗费时长"+(end - begin)+"毫秒");
    }

    // 需求：统计一个方法执行所耗费的时长
    public static void print(){
        for(int i = 0; i < 1000000000; i++){
            System.out.println("i = " + i);
        }
    }
}


public class DateTest03 {
    public static void main(String[] args) {

        // 这个时间是什么时间？
        // 1970-01-01 00:00:00 001
        Date time = new Date(1); // 注意：参数是一个毫秒

        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss SSS");
        String strTime = sdf.format(time);
        // 北京是东8区。差8个小时。
        System.out.println(strTime); // 1970-01-01 08:00:00 001

        // 获取昨天的此时的时间。
        Date time2 = new Date(System.currentTimeMillis() - 1000 * 60 * 60 * 24);
        String strTime2 = sdf.format(time2);
        System.out.println(strTime2); //2020-03-04 11:44:14 829

        // 获取“去年的今天”的时间
        // 自己玩。
    }
}

```

获取系统当前时间

- Date d = new Date();
- 日期格式化：Date --> String
- yyyy-MM-dd HH:mm:ss SSS
- SimpleDateFormat sdf = new SimpleDate("yyyy-MM-dd HH:mm:ss SSS");
- String s = sdf.format(new Date());
- String --> Date
- SimpleDateFormat sdf = new SimpleDate("yyyy-MM-dd HH:mm:ss");
- Date d = sdf.parse("2008-08-08 08:08:08");
- 获取毫秒数
- long begin = System.currentTimeMillis();
- Date d = new Date(begin - 1000 * 60 * 60 * 24);

### 数字类

```java

import java.math.BigDecimal;
import java.text.DecimalFormat;

/*
关于数字的格式化。（了解）
 */
public class DecimalFormatTest01 {
    public static void main(String[] args) {
        // java.text.DecimalFormat专门负责数字格式化的。
        //DecimalFormat df = new DecimalFormat("数字格式");

        /*
        数字格式有哪些？
            # 代表任意数字
            , 代表千分位
            . 代表小数点
            0 代表不够时补0

            ###,###.##
                表示：加入千分位，保留2个小数。
         */
        DecimalFormat df = new DecimalFormat("###,###.##");
        //String s = df.format(1234.56);
        String s = df.format(1234.561232);
        System.out.println(s); // "1,234.56"

        DecimalFormat df2 = new DecimalFormat("###,###.0000"); //保留4个小数位，不够补上0
        String s2 = df2.format(1234.56);
        System.out.println(s2); // "1,234.5600"

    }
}

/*
1、BigDecimal 属于大数据，精度极高。不属于基本数据类型，属于java对象（引用数据类型）
这是SUN提供的一个类。专门用在财务软件当中。

2、注意：财务软件中double是不够的。咱们之前有一个学生去用友面试，经理就问了这样一个问题：
    你处理过财务数据吗？用的哪一种类型？
        千万别说double，说java.math.BigDecimal
 */
public class BigDecimalTest01 {
    public static void main(String[] args) {

        // 这个100不是普通的100，是精度极高的100
        BigDecimal v1 = new BigDecimal(100);
        // 精度极高的200
        BigDecimal v2 = new BigDecimal(200);
        // 求和
        // v1 + v2; // 这样不行，v1和v2都是引用，不能直接使用+求和。
        BigDecimal v3 = v1.add(v2); // 调用方法求和。
        System.out.println(v3); //300

        BigDecimal v4 = v2.divide(v1);
        System.out.println(v4); // 2
    }
}

```

- DecimalFormat数字格式化

###,###.## 表示加入千分位，保留两个小数。
###,###.0000 表示加入千分位，保留4个小数，不够补0

- - BigDecimal

财务软件中通常使用BigDecimal

### 随机数

```java

/**
 * 随机数
 */
public class RandomTest01 {
    public static void main(String[] args) {
        // 创建随机数对象
        Random random = new Random();

        // 随机产生一个int类型取值范围内的数字。
        int num1 = random.nextInt();

        System.out.println(num1);

        // 产生[0~100]之间的随机数。不能产生101。
        // nextInt翻译为：下一个int类型的数据是101，表示只能取到100.
        int num2 = random.nextInt(101); //不包括101
        System.out.println(num2);
    }
}


```

- 怎么产生int类型随机数。

Random r = new Random();
int i = r.nextInt();

- 怎么产生某个范围之内的int类型随机数。

Random r = new Random();
int i = r.nextInt(101); // 产生[0-100]的随机数。

### 枚举

```java
public class SwitchTest {
    public static void main(String[] args) {
        // switch语句支持枚举类型
        // switch也支持String、int
        // 低版本的JDK，只支持int
        // 高版本的JDK，支持int、String、枚举。
        // byte short char也可以，因为存在自动类型转换。
        switch (Season.SPRING) {
            // 必须省略Season.
            case SPRING:
                System.out.println("春天");
                break;
            case SUMMER:
                System.out.println("夏天");
                break;
            case AUTUMN:
                System.out.println("秋天");
                break;
            case WINTER:
                System.out.println("冬天");
                break;
        }

    }
}


package com.bjpowernode.javase.enum2; // 标识符，关键字不能做标识符。enum是关键字。
/*
这个案例没有使用java中的枚举，分析以下程序，在设计方面有什么缺陷？
    以下代码可以编译，也可以运行。这些都没有问题。
    就是设计上你觉得有什么缺陷？

 */
public class EnumTest01 {
    public static void main(String[] args) {

        //System.out.println(10 / 0); //java.lang.ArithmeticException: / by zero
        /*
        int retValue = divide(10, 2);
        System.out.println(retValue == 1 ? "计算成功" : "计算失败"); // 1

        int retValue2 = divide(10, 0);
        System.out.println(retValue2 == 0 ? "计算失败" : "计算成功"); // 0
         */

        boolean success = divide(10, 0);
        System.out.println(success ? "计算成功" : "计算失败");
    }

    /**
     * 需求（这是设计者说的！）：以下程序，计算两个int类型数据的商，计算成功返回1，计算失败返回0
     * @param a int类型的数据
     * @param b int类型的数据
     * @return 返回1表示成功，返回0表示失败！
     */
    /*
    public static int divide(int a, int b){
        try {
            int c = a / b;
            // 程序执行到此处表示以上代码没有发生异常。表示执行成功！
            return 1;
        } catch (Exception e){
            // 程序执行到此处表示以上程序出现了异常！
            // 表示执行失败！
            return 0;
        }
    }
     */

    // 设计缺陷？在这个方法的返回值类型上。返回一个int不恰当。
    // 既然最后的结果只是成功和失败，最好使用布尔类型。因为布尔类型true和false正好可以表示两种不同的状态。
    /*
    public static int divide(int a, int b){
        try {
            int c = a / b;
            // 返回10已经偏离了需求，实际上已经出错了，但是编译器没有检查出来。
            // 我们一直想追求的是：所有的错误尽可能让编译器找出来，所有的错误越早发现越好！
            return 10;
        } catch (Exception e){
            return 0;
        }
    }
    */

    // 这种设计不错。
    public static boolean divide(int a, int b){
        try {
            int c = a / b;
            return true;
        } catch (Exception e){
            return false;
        }
    }

    /*
    思考：以上的这个方法设计没毛病，挺好，返回true和false表示两种情况，
    但是在以后的开发中，有可能遇到一个方法的执行结果可能包括三种情况，
    四种情况，五种情况不等，但是每一个都是可以数清楚的，一枚一枚都是可以
    列举出来的。这个布尔类型就无法满足需求了。此时需要使用java语言中的
    枚举类型。
     */

}

// 采用枚举的方式改造程序
/*
总结：
    1、枚举是一种引用数据类型
    2、枚举类型怎么定义，语法是？
        enum 枚举类型名{
            枚举值1,枚举值2
        }
    3、结果只有两种情况的，建议使用布尔类型。
    结果超过两种并且还是可以一枚一枚列举出来的，建议使用枚举类型。
        例如：颜色、四季、星期等都可以使用枚举类型。
 */
public class EnumTest02 {
    public static void main(String[] args) {
        Result r = divide(10, 2);
        System.out.println(r == Result.SUCCESS ? "计算成功" : "计算失败");
    }

    /**
     * 计算两个int类型数据的商。
     * @param a int数据
     * @param b int数据
     * @return Result.SUCCESS表示成功，Result.FAIL表示失败！
     */
    public static Result divide(int a, int b){
        try {
            int c = a / b;
            return Result.SUCCESS;
        } catch (Exception e){
            return Result.FAIL;
        }
    }
}

// 枚举：一枚一枚可以列举出来的，才建议使用枚举类型。
// 枚举编译之后也是生成class文件。
// 枚举也是一种引用数据类型。
// 枚举中的每一个值可以看做是常量。
enum Result{
    // SUCCESS 是枚举Result类型中的一个值
    // FAIL 是枚举Result类型中的一个值
    // 枚举中的每一个值，可以看做是“常量”
    SUCCESS, FAIL
}

```

- 枚举是一种引用数据类型。
- 枚举编译之后也是class文件。
- 枚举类型怎么定义？
- enum 枚举类型名{

枚举值,枚举值2,枚举值3
}

- 当一个方法执行结果超过两种情况，并且是一枚一枚可以列举出来

的时候，建议返回值类型设计为枚举类型。
