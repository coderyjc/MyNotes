
## 数组和常用类

### 数组

#### 数组

```java
package com.bjpowernode.javase.array;
/*
Array
    1、Java语言中的数组是一种引用数据类型。不属于基本数据类型。数组的父类是Object。
    2、数组实际上是一个容器，可以同时容纳多个元素。（数组是一个数据的集合。）数组：字面意思是“一组数据”
    3、数组当中可以存储“基本数据类型”的数据，也可以存储“引用数据类型”的数据。
    4、数组是存储在堆当中的
    5、数组当中如果存储的是“java对象”的话，实际上存储的是对象的“引用（内存地址）”，数组中不能直接存储java对象。
    6、数组长度不可变
    7、数组的分类：一维数组、二维数组、三维数组、多维数组...（一维数组较多，二维数组偶尔使用！）
    8、所有的数组对象都有length属性(java自带的)，用来获取数组中元素的个数。
    9、java中的数组要求数组中元素的类型统一。比如int类型数组只能存储int类型，Person类型数组只能存储Person类型。
    10、数组在内存方面存储的时候，数组中的元素内存地址(存储的每一个元素都是有规则的挨着排列的)是连续的。内存地址连续。  这是数组存储元素的特点（特色）。数组实际上是一种简单的数据结构。
    11、所有的数组都是拿“第一个小方框的内存地址”作为整个数组对象的内存地址。   （数组中首元素的内存地址作为整个数组对象的内存地址。）
    12、数组中每一个元素都是有下标的，下标从0开始，以1递增。最后一个元素的下标是：length - 1   下标非常重要，因为我们对数组中元素进行“存取”的时候，都需要通过下标来进行。
    13、数组这种数据结构的优点和缺点是什么？
        优点：查询/查找/检索某个下标上的元素时效率极高。可以说是查询效率最高的一个数据结构。
            为什么检索效率高？
                第一：每一个元素的内存地址在空间存储上是连续的。
                第二：每一个元素类型相同，所以占用空间大小一样。
                第三：知道第一个元素内存地址，知道每一个元素占用空间的大小，又知道下标，所以通过一个数学表达式就可以计算出某个下标上元素的内存地址。直接通过内存地址定位 元素，所以数组的检索效率是最高的。

                数组中存储100个元素，或者存储100万个元素，在元素查询/检索方面，效率是相同的，
                因为数组中元素查找的时候不会一个一个找，是通过数学表达式计算出来的。（算出一个
                内存地址，直接定位的。）
        缺点：
            第一：由于为了保证数组中每个元素的内存地址连续，所以在数组上随机删除或者增加元素的时候，
        效率较低，因为随机增删元素会涉及到后面元素统一向前或者向后位移的操作。
            第二：数组不能存储大数据量，为什么？   因为很难在内存空间上找到一块特别大的连续的内存空间。

        注意：对于数组中最后一个元素的增删，是没有效率影响的。
    14、怎么声明/定义一个一维数组？
        语法格式：
            int[] array1;
            double[] array2;
            Object[] array5;
    15、怎么初始化一个一维数组呢？
        包括两种方式：静态初始化一维数组，动态初始化一维数组。
        静态初始化语法格式：
            int[] array = {100, 2100, 300, 55};
        动态初始化语法格式：
            int[] array = new int[5]; // 这里的5表示数组的元素个数。
                                        // 初始化一个5个长度的int类型数组，每个元素默认值0
            String[] names = new String[6]; // 初始化6个长度的String类型数组，每个元素默认值null。

 */
public class ArrayTest01 {
    public static void main(String[] args) {
        // 声明一个int类型的数组，使用静态初始化的方式
        int[] a = {1, 100, 10, 20, 55, 689};

        // 下标为6表示第7个元素，第7个元素没有，下标越界了。会出现什么异常呢？
        //System.out.println(a[6]); //ArrayIndexOutOfBoundsException（比较著名的异常。）

        // 从最后一个元素遍历到第1个元素
        for (int i = a.length - 1; i >= 0; i--) {
            System.out.println("颠倒顺序输出-->" + a[i]);
        }
    }
}

package com.bjpowernode.javase.array;

/*
 什么时候采用静态初始化方式，什么时候使用动态初始化方式呢？
    当你创建数组的时候，确定数组中存储哪些具体的元素时，采用静态初始化方式。
    当你创建数组的时候，不确定将来数组中存储哪些数据，你可以采用动态初始化的方式，预先分配内存空间。
 */
public class ArrayTest02 {
    public static void main(String[] args) {
        // 声明/定义一个数组，采用动态初始化的方式创建
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



// 当一个方法的参数是一个数组的时候，我们还可以采用这种方式传。

public class ArrayTest04 {
    public static void main(String[] args) {
        // 静态初始化一维数组
        int[] a = {1,2,3};
        printArray(a);

        System.out.println("============================");
        // 没有这种语法。
        //printArray({1,2,3});
        // 如果直接传递一个静态数组的话，语法必须这样写。
        printArray(new int[]{1,2,3});

        // 动态初始化一维数组
        int[] a2 = new int[4];
        printArray(a2);

        System.out.println("=============================");
        printArray(new int[3]);
    }
}

```

#### main方法的String[] 参数

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

#### 引用数据类型

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

#### 数组的扩容和拷贝

```java

/**
 * 关于一维数组的扩容。
 * 在java开发中，数组长度一旦确定不可变，那么数组满了怎么办？
 *      数组满了，需要扩容。
 *      java中对数组的扩容是：
 *          先新建一个大容量的数组，然后将小容量数组中的数据一个一个拷贝到大数组当中。
 *
 * 结论：数组扩容效率较低。因为涉及到拷贝的问题。所以在以后的开发中请注意：尽可能少的进行数组的拷贝。
 * 可以在创建数组对象的时候预估计以下多长合适，最好预估准确，这样可以减少数组的扩容次数。提高效率。
 */
public class ArrayTest08 {
    public static void main(String[] args) {
        // java中的数组是怎么进行拷贝的呢？
        //System.arraycopy(5个参数);

        // 拷贝源（从这个数组中拷贝）
        int[] src = {1, 11, 22, 3, 4};

        // 拷贝目标（拷贝到这个目标数组上）
        int[] dest = new int[20]; // 动态初始化一个长度为20的数组，每一个元素默认值0

        // 调用JDK System类中的arraycopy方法，来完成数组的拷贝
        //System.arraycopy(src, 1, dest, 3, 2);

        // 遍历目标数组
        /*
        for (int i = 0; i < dest.length; i++) {
            System.out.println(dest[i]); // 0 0 0 11 22 ... 0
        }
         */

        System.arraycopy(src, 0, dest, 0, src.length);
        for (int i = 0; i < dest.length; i++) {
            System.out.println(dest[i]);
        }

        // 数组中如果存储的元素是引用，可以拷贝吗？当然可以。
        String[] strs = {"hello", "world!", "study", "java", "oracle", "mysql", "jdbc"};
        String[] newStrs = new String[20];
        System.arraycopy(strs, 0, newStrs, 0, strs.length);
        for (int i = 0; i < newStrs.length; i++) {
            System.out.println(newStrs[i]);
        }

        System.out.println("================================");
        Object[] objs = {new Object(), new Object(), new Object()};
        Object[] newObjs = new Object[5];
        // 思考一下：这里拷贝的时候是拷贝对象，还是拷贝对象的地址。（地址。）
        System.arraycopy(objs, 0, newObjs, 0, objs.length);
        for (int i = 0; i < newObjs.length; i++) {
            System.out.println(newObjs[i]);
        }
    }
}

```

#### 二维数组


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

        // 二维数组遍历
        /*
        for (int i = 0; i < array.length; i++) { // 循环3次。
            for (int j = 0; j < array[i].length; j++) {
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
         */

        // 静态初始化
        int[][] a = {{1,2,3,4},{4,5,6,76},{1,23,4}};
        printArray(a);

        // 没有这种语法
        //printArray({{1,2,3,4},{4,5,6,76},{1,23,4}});

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


#### 排序和查找

```java
import java.util.Arrays;

/**
 * 使用以下SUN公司提供的数组工具类：java.util.Arrays;
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

### 常用类【注意看帮助文档】

#### String类

##### 基础认知

```java
/*
关于Java JDK中内置的一个类：java.lang.String
    1、String表示字符串类型，属于引用数据类型，不属于基本数据类型。
    2、在java中随便使用双引号括起来的都是String对象。例如："abc"，"def"，"hello world!"，这是3个String对象。
    3、java中规定，双引号括起来的字符串，是不可变的，也就是说"abc"自出生到最终死亡，不可变，不能变成"abcd"，也不能变成"ab"
    4、在JDK当中双引号括起来的字符串，例如："abc" "def"都是直接存储在“方法区”的“字符串常量池”当中的。为什么SUN公司把字符串存储在一个“字符串常量池”当中呢。因为字符串在实际的开发中使用太频繁。为了执行效率，所以把字符串放到了方法区的字符串常量池当中。
	5、字符串常量池在方法区中
 */
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

public class StringTest02 {
    public static void main(String[] args) {
        String s1 = "hello";
        // "hello"是存储在方法区的字符串常量池当中
        // 所以这个"hello"不会新建。（因为这个对象已经存在了！）
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

/*
分析以下程序，一共创建了几个对象
 */
public class StringTest03 {
    public static void main(String[] args) {
        /*
        一共3个对象：
            方法区字符串常量池中有1个："hello"
            堆内存当中有两个String对象。
            一共3个。
         */
        String s1 = new String("hello");
        String s2 = new String("hello");
    }
}



```

##### 构造方法

```java
package com.bjpowernode.javase.string;

/**
 * 关于String类中的构造方法。
 *  第一个：String s = new String("");
 *  第二个：String s = ""; 最常用
 *  第三个：String s = new String(char数组);
 *  第四个：String s = new String(char数组,起始下标,长度);
 *  第五个：String s = new String(byte数组);
 *  第六个：String s = new String(byte数组,起始下标,长度)
 */
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
package com.bjpowernode.javase.string;

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
        System.out.println("http://www.baidu.com".contains("https://")); // false

        // 4（掌握）. boolean endsWith(String suffix)
        // 判断当前字符串是否以某个子字符串结尾。
        System.out.println("test.txt".endsWith(".java")); // false
        System.out.println("test.txt".endsWith(".txt")); // true
        System.out.println("fdsajklfhdkjlsahfjkdsahjklfdss".endsWith("ss")); // true

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
        for(int i = 0; i < ymd.length; i++){
            System.out.println(ymd[i]);
        }
        String param = "name=zhangsan&password=123&age=20";
        String[] params = param.split("&");
        for(int i = 0; i <params.length; i++){
            System.out.println(params[i]);
            // 可以继续向下拆分，可以通过“=”拆分。
        }

        // 14（掌握）、boolean startsWith(String prefix)
        // 判断某个字符串是否以某个子字符串开始。
        System.out.println("http://www.baidu.com".startsWith("http")); // true
        System.out.println("http://www.baidu.com".startsWith("https")); // false

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


/**
 * 如果以后需要进行大量字符串的拼接操作，建议使用JDK中自带的：
 *      java.lang.StringBuffer
 *      java.lang.StringBuilder
 *
 * 如何优化StringBuffer的性能？
 *      在创建StringBuffer的时候尽可能给定一个初始化容量。
 *      最好减少底层数组的扩容次数。预估计一下，给一个大一些初始化容量。
 *      关键点：给一个合适的初始化容量。可以提高程序的执行效率。
 */
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


package com.bjpowernode.javase.stringbuffer;
/*
1、面试题：String为什么是不可变的？
    我看过源代码，String类中有一个byte[]数组，这个byte[]数组采用了final修饰，
    因为数组一旦创建长度不可变。并且被final修饰的引用一旦指向某个对象之后，不
    可再指向其它对象，所以String是不可变的！
        "abc" 无法变成 "abcd"

2、StringBuilder/StringBuffer为什么是可变的呢？
    我看过源代码，StringBuffer/StringBuilder内部实际上是一个byte[]数组，
    这个byte[]数组没有被final修饰，StringBuffer/StringBuilder的初始化
    容量我记得应该是16，当存满之后会进行扩容，底层调用了数组拷贝的方法
    System.arraycopy()...是这样扩容的。所以StringBuilder/StringBuffer
    适合于使用字符串的频繁拼接操作。

 */
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


/*
java.lang.StringBuilder
StringBuffer和StringBuilder的区别？
    StringBuffer中的方法都有：synchronized关键字修饰。表示StringBuffer在多线程环境下运行是安全的。
    StringBuilder中的方法都没有：synchronized关键字修饰，表示StringBuilder在多线程环境下运行是不安全的。

    StringBuffer是线程安全的。
    StringBuilder是非线程安全的。

 */
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

对String在内存存储方面的理解：

- 第一：字符串一旦创建不可变。
- 第二：双引号括起来的字符串存储在字符串常量池中。
- 第三：字符串的比较必须使用equals方法。
- 第四：String已经重写了toString()和equals()方法。

String的构造方法。

- String s = "abc";

- String s = new String("abc");

- String s = new String(byte数组);

- String s = new String(byte数组, 起始下标, 长度);

- String s = new String(char数组);

- String s = new String(char数组, 起始下标, 长度);

String类常用的21个方法。

- StringBuffer/StringBuilder
- StringBuffer/StringBuilder可以看做可变长度字符串。
- StringBuffer/StringBuilder初始化容量16.
- StringBuffer/StringBuilder是完成字符串拼接操作的，方法名：append
- StringBuffer是线程安全的。StringBuilder是非线程安全的。
- 频繁进行字符串拼接不建议使用“+”

#### 基本数据类型对应的包装类

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

/*
1、8种基本数据类型对应的包装类型名是什么？
    基本数据类型              包装类型
    -------------------------------------
    byte                    java.lang.Byte（父类Number）
    short                   java.lang.Short（父类Number）
    int                     java.lang.Integer（父类Number）
    long                    java.lang.Long（父类Number）
    float                   java.lang.Float（父类Number）
    double                  java.lang.Double（父类Number）
    boolean                 java.lang.Boolean（父类Object）
    char                    java.lang.Character（父类Object）

2、以上八种包装类中，重点以java.lang.Integer为代表进行学习，其它的类型照葫芦画瓢就行。

3、八种包装类中其中6个都是数字对应的包装类，他们的父类都是Number，可以先研究一下Number中公共的方法：
    Number是一个抽象类，无法实例化对象。
    Number类中有这样的方法：
        byte byteValue() 以 byte 形式返回指定的数值。
        abstract  double doubleValue()以 double 形式返回指定的数值。
        abstract  float floatValue()以 float 形式返回指定的数值。
        abstract  int intValue()以 int 形式返回指定的数值。
        abstract  long longValue()以 long 形式返回指定的数值。
        short shortValue()以 short 形式返回指定的数值。
        这些方法其实所有的数字包装类的子类都有，这些方法是负责拆箱的。

 */
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

#### 日期类

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

#### 数字类

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

#### 随机数


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

#### 枚举


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

## 集合

什么是集合？有什么用？

- 数组其实就是一个集合。集合实际上就是一个容器。可以来容纳其它类型的数据。

集合为什么说在开发中使用较多？

- 集合是一个容器，是一个载体，可以一次容纳多个对象。在实际开发中，假设连接数据库，数据库当中有10条记录，那么假设把这10条记录查询出来，在java程序中会将10条数据封装成10个java对象，然后将10个java对象放到某一个集合当中，将集合传到前端，然后遍历集合，将一个数据一个数据展现出来。

注意：

- 集合不能直接存储基本数据类型，另外集合也不能直接存储java对象，集合当中存储的都是java对象的内存地址。（或者说集合中存储的是引用。）
- 集合在java中本身是一个容器，是一个对象。
- 集合中任何时候存储的都是“引用”。

在java中每一个不同的集合，底层会对应不同的数据结构。往不同的集合中存储元素，等于将数据放到了不同的数据结构当中。什么是数据结构？数据存储的结构就是数据结构。不同的数据结构，数据存储方式不同。例如：数组、二叉树、链表、哈希表...以上这些都是常见的数据结构。

new ArrayList(); 创建一个集合，底层是数组。
new LinkedList(); 创建一个集合对象，底层是链表。
new TreeSet(); 创建一个集合对象，底层是二叉树。
.....

集合在java JDK中哪个包下？

- java.util.*;所有的集合类和集合接口都在java.util包下。

为了让大家掌握集合这块的内容，最好能将集合的继承结构图背会！！！

在java中集合分为两大类：
- 一类是单个方式存储元素：单个方式存储元素，这一类集合中超级父接口：java.util.Collection;
- 一类是以键值对儿的方式存储元素以键值对的方式存储元素，这一类集合中超级父接口：java.util.Map;

![1595553406932](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1595553406932.png)

![1595553421651](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1595553421651.png)

重点：

- 第一个重点：把集合继承结构图背会。
- 第二个重点：把Collection接口中常用方法测试几遍。
- 第三个重点：把迭代器弄明白。
- 第四个重点：Collection接口中的remove方法和contains方法底层都会调用equals，
这个弄明白。

总结：所有实现类

- ArrayList 底层是数组
- LinkedList 底层是双向链表
- Vector 底层是数组，线程安全，效率比较低，使用较少
- HashSet 底层是HashMap，放在HashSet集合中的元素等同于放到HashMap集合key部分了
- TreeSet 底层是TreeMap，放在TreeSet集合中的元素等同于放到TreeMap集合的key部分了
- HashMap 底层是哈希表
- HashTable 底层也是哈希表，不过是线程安全的，效率较低，使用较少
- Properties 是线程安全的，并且k和v只能存储字符串String
- TreeMap 底层是二叉树。TreeMap集合的key可以自动按照大小顺序排序


List 集合存储元素特点

- 有序可重复
- 有序：存进去的顺序和取出得到顺序相同，每一个元素都有下标
- 可重复：存进去1， 可以再存储一个1

Set(Map) 集合存储元素特点

- 无序不可重复
- 无序：存进去的顺序和去除的顺序不一定相同，另外Set集合中没有下标
- 不可重复：存进去1，不能再存储1了

SortedSet（SortedMap） 集合存储元素特点

- 无序不可重复但是可以排序
- 可排序：可以按照大小顺序排列

Map集合的Key就是一个Set集合，往Set中放数据就相当于放到了map的key部分

### Collection

关于java.util.Collection接口中常用的方法。

Collection中能存放什么元素？
- 没有使用“泛型”之前，Collection中可以存储Object的所有子类型，且**可以不同**，因为存的是地址
- 使用了“泛型”之后，Collection中只能存储某个具体的类型。
- Collection中什么都能存只要是Object的子类型就行。
- 集合中不能直接存储基本数据类型,也不能存java对象，只是存储java对象的内存地址。

Collection中的常用方法

- boolean add(Object e) 向集合中添加元素(自动装箱)
- int size()  获取集合中元素的个数
- void clear() 清空集合
- boolean contains(Object o) 判断当前集合中是否包含元素o，包含返回true，不包含返回false
- boolean remove(Object o) 删除集合中的某个元素。
- boolean isEmpty()  判断该集合中元素的个数是否为0
- Object[] toArray()  调用这个方法可以把集合转换成数组。【作为了解，使用不多。】

#### 迭代器

```java
public class CollectionTest02 {
    public static void main(String[] args) {
        // 注意：以下讲解的遍历方式/迭代方式，是所有Collection通用的一种方式。
        // 在Map集合中不能用。在所有的Collection以及子类中使用。
        // 创建集合对象
        Collection c = new ArrayList(); // 后面的集合无所谓，主要是看前面的Collection接口，怎么遍历/迭代。
        // 添加元素
        c.add("abc");
        c.add(new Object());
        // 对集合Collection进行遍历/迭代
        // 第一步：获取集合对象的迭代器对象Iterator
        Iterator it = c.iterator();
        // 第二步：通过以上获取的迭代器对象开始迭代/遍历集合。
        /*
            以下两个方法是迭代器对象Iterator中的方法：
                boolean hasNext()如果仍有元素可以迭代，则返回 true。
                Object next() 返回迭代的下一个元素。
         */
        while(it.hasNext()){
            Object obj = it.next();
            System.out.println(obj);
        }
    //等价于：
		while(it2.hasNext()){
            System.out.println(it2.next());
        }
        // 一直取，不判断，会出现异常：java.util.NoSuchElementException
    }
}

```

#### contains

深入Collection集合的contains方法：

boolean contains(Object o)
判断集合中是否包含某个对象o
如果包含返回true， 如果不包含返回false。

contains方法是用来判断集合中是否包含某个元素的方法，那么它在底层是怎么判断集合中是否包含某个元素的呢？
调用了equals方法进行比对。equals方法返回true，就表示包含这个元素。

```java
public class CollectionTest04 {
    public static void main(String[] args) {
        // 创建集合对象
        Collection c = new ArrayList();

        // 向集合中存储元素
        String s1 = new String("abc"); // s1 = 0x1111
        c.add(s1); // 放进去了一个"abc"

        String s2 = new String("def"); // s2 = 0x2222
        c.add(s2);

        // 集合中元素的个数
        System.out.println("元素的个数是：" + c.size()); // 2

        // 新建的对象String
        String x = new String("abc"); // x = 0x5555
        // c集合中是否包含x？结果猜测一下是true还是false？
        System.out.println(c.contains(x));
    }
}

//包含，因为底层调用了String的equals方法，比较的是内容，内容一样所以是true
//和字符串常量值

```

结论：**放在集合中的元素一定要重写equals方法**

#### remove

- 当集合的结构发生改变时，迭代器必须重新获取，如果还是用以前老的迭代器，会出现异常：java.util.ConcurrentModificationException
- 在迭代集合元素的过程中，不能调用集合对象的remove方法，删除元素：c.remove(o); 迭代过程中不能这样。会出现：java.util.ConcurrentModificationException
- 在迭代元素的过程当中，一定要使用迭代器Iterator的remove方法，删除元素不要使用集合自带的remove方法删除元素。

```java
public class CollectionTest06 {
    public static void main(String[] args) {
        // 创建集合
        Collection c = new ArrayList();

        // 注意：此时获取的迭代器，指向的是那是集合中没有元素状态下的迭代器。
        // 一定要注意：集合结构只要发生改变，迭代器必须重新获取。
        // 当集合结构发生了改变，迭代器没有重新获取时，调用next()方法时：java.util.ConcurrentModificationException
        Iterator it = c.iterator();

        // 添加元素
        c.add(1); // Integer类型
        c.add(2);

        // 获取迭代器
        //Iterator it = c.iterator();
        /*while(it.hasNext()){
            // 编写代码时next()方法返回值类型必须是Object。
            // Integer i = it.next();
            Object obj = it.next();
            System.out.println(obj);
        }*/

        Collection c2 = new ArrayList();
        c2.add("abc");
        c2.add("def");
        c2.add("xyz");

        Iterator it2 = c2.iterator();
        while(it2.hasNext()){
            Object o = it2.next();
            // 删除元素
            // 删除元素之后，集合的结构发生了变化，应该重新去获取迭代器
            // 但是，循环下一次的时候并没有重新获取迭代器，所以会出现异常：java.util.ConcurrentModificationException
            // 出异常根本原因是：集合中元素删除了，但是没有更新迭代器（迭代器不知道集合变化了）
            //c2.remove(o); // 直接通过集合去删除元素，没有通知迭代器。（导致迭代器的快照和原集合状态不同。）
            // 使用迭代器来删除可以吗？
            // 迭代器去删除时，会自动更新迭代器，并且更新集合（删除集合中的元素）。
            it2.remove(); // 删除的一定是迭代器指向的当前元素。
            System.out.println(o);
        }

        System.out.println(c2.size()); //0
    }
}

```


### List

List集合存储元素特点：有序可重复

- 有序：List集合中的元素有下标。
- 从0开始，以1递增。
- 可重复：存储一个1，还可以再存储1.

List既然是Collection接口的子接口，那么肯定List接口有自己“特色”的方法：
以下只列出List接口特有的常用的方法：

- void add(int index, Object element)
- Object set(int index, Object element)
- Object get(int index)
- int indexOf(Object o)
- int lastIndexOf(Object o)
- Object remove(int index)

以上几个方法不需要死记硬背，可以自己编写代码测试一下，理解一下, 以后开发的时候，还是要翻阅帮助文档。

迭代器迭代元素的过程中不能使用集合对象的remove方法删除元素，要使用迭代器Iterator的remove方法来删除元素，防止出现异常： ConcurrentModificationException

怎么得到一个线程安全的List：
Collections.synchronizedList(list);


```java

public class ListTest01 {
    public static void main(String[] args) {
        // 创建List类型的集合。
        List myList = new ArrayList();

        // 添加元素
        myList.add("A"); // 默认都是向集合末尾添加元素。
        myList.add("B");

        //在列表的指定位置插入指定元素（第一个参数是下标）
        // 这个方法使用不多，因为对于ArrayList集合来说效率比较低。
        myList.add(1, "KING");

        // 迭代
        Iterator it = myList.iterator();
        while(it.hasNext()){
            Object elt = it.next();
            System.out.println(elt);
        }

        // 根据下标获取元素
        Object firstObj = myList.get(0);
        System.out.println(firstObj);

        // 因为有下标，所以List集合有自己比较特殊的遍历方式
        // 通过下标遍历。【List集合特有的方式，Set没有。】
        for(int i = 0; i < myList.size(); i++){
            Object obj = myList.get(i);
            System.out.println(obj);
        }

        // 获取指定对象第一次出现处的索引。
        System.out.println(myList.indexOf("C")); // 3

        // 获取指定对象最后一次出现处的索引。
        System.out.println(myList.lastIndexOf("C")); // 4

        // 删除下标为0的元素
        myList.remove(0);

        // 修改指定位置的元素
        myList.set(2, "Soft");

        // 遍历集合
        for(int i = 0; i < myList.size(); i++){
            Object obj = myList.get(i);
            System.out.println(obj);
        }
    }
}

```

#### ArrayList

- 默认初始化容量10（底层先创建了一个长度为0的数组，当添加第一个元素的时候，初始化容量10。）扩容为原容量1.5倍。
- 集合底层是一个Object[]数组。
- 构造方法：
	- new ArrayList();
	- new ArrayList(20);
- ArrayList集合的扩容：        增长到原容量的1.5倍。
- ArrayList集合底层是数组，怎么优化？
	- 尽可能少的扩容。因为数组扩容效率比较低，建议在使用ArrayList集合的时候预估计元素的个数，给定一个初始化容量。
- 数组优点：
	- 检索效率比较高。（每个元素占用空间大小相同，内存地址是连续的，知道首元素内存地址，知道下标，通过数学表达式计算出元素的内存地址，所以检索效率最高。）
- 数组缺点：
	- 随机增删元素效率比较低。
	- 另外数组无法存储大数据量。（很难找到一块非常巨大的连续的内存空间。）
- 向数组末尾添加元素，效率很高，不受影响。
- 面试官经常问的一个问题？ 这么多的集合中，你用哪个集合最多？
	- 答：ArrayList集合。因为往数组末尾添加元素，效率不受影响。另外，我们检索/查找某个元素的操作比较多。
- ArrayList集合是非线程安全的。（不是线程安全的集合。）
- ArrayList之所以检索效率比较高，不是单纯因为下标的原因。是因为底层数组发挥的作用。
- LinkedList集合照样有下标，但是检索/查找某个元素的时候效率比较低，因为只能从头节点开始一个一个遍历。

怎么将一个线程不安全的ArrayList集合转换成线程安全的呢？
使用集合工具类：java.util.Collections;

java.util.Collection 是集合接口。

java.util.Collections 是集合工具类。

#### LinkedList

链表的优点：
    由于链表上的元素在空间存储上内存地址不连续。所以随机增删元素的时候不会有大量元素位移，因此随机增删效率较高。在以后的开发中，如果遇到**随机增删集合中元素**的业务比较多时，建议使用LinkedList。

链表的缺点：
    不能通过数学表达式计算被查找元素的内存地址，每一次查找都是从头节点开始遍历，直到找到为止。所以LinkedList集合检索/查找的效率较低。

- LinkedList集合底层也是有下标的。
- LinkedList集合有初始化容量吗？没有。
- 最初这个链表中没有任何元素。first和last引用都是null。


ArrayList：把检索发挥到极致。（末尾添加元素效率还是很高的。）
LinkedList：把随机增删发挥到极致。
加元素都是往末尾添加，所以ArrayList用的比LinkedList多。

#### Vector

Vector初始化容量是10.

扩容为原容量的2倍。

底层是数组。

Vector底层是线程安全的。

Vector中所有的方法都是线程同步的，都带有synchronized关键字，是线程安全的。效率比较低，使用较少了。

### 泛型

#### 使用泛型

- JDK5.0之后推出的新特性：泛型
- 泛型这种语法机制，只在程序编译阶段起作用，只是给编译器参考的。（运行阶段泛型没用！）
- 使用了泛型好处是什么？
	- 第一：集合中存储的元素类型统一了。
	- 第二：从集合中取出的元素类型是泛型指定的类型，不需要进行大量的“向下转型”！
- 泛型的缺点是什么？
    - 导致集合中存储的元素缺乏多样性！
    - 大多数业务中，集合中元素的类型还是统一的。所以这种泛型特性被大家所认可。

 ```java
public class GenericTest01 {
    public static void main(String[] args) {

        // 使用泛型List<Animal>之后，表示List集合中只允许存储Animal类型的数据。
        // 用泛型来指定集合中存储的数据类型。
        List<Animal> myList = new ArrayList<Animal>();

        // 指定List集合中只能存储Animal，那么存储String就编译报错了。
        // 这样用了泛型之后，集合中元素的数据类型更加统一了。
        Cat c = new Cat(); Bird b = new Bird();
        myList.add(c); myList.add(b);

        // 获取迭代器
        // 这个表示迭代器迭代的是Animal类型。
        Iterator<Animal> it = myList.iterator();
        while(it.hasNext()){
            // 使用泛型之后，每一次迭代返回的数据都是Animal类型。
            //Animal a = it.next();
            // 这里不需要进行强制类型转换了。直接调用。
            //a.move();

            // 调用子类型特有的方法还是需要向下转换的！
            Animal a = it.next();
            if(a instanceof Cat) {
                Cat x = (Cat)a;
                x.catchMouse();
            }
            if(a instanceof Bird) {
                Bird y = (Bird)a;
                y.fly();
            }
        }
    }
}

class Animal {
    // 父类自带方法
    public void move(){
        System.out.println("动物在移动！");
    }
}

class Cat extends Animal {
    // 特有方法
    public void catchMouse(){
        System.out.println("猫抓老鼠！");
    }
}

class Bird extends Animal {
    // 特有方法
    public void fly(){
        System.out.println("鸟儿在飞翔！");
    }
}

 ```


#### 钻石表达式（自动类型推断）

```java

public class GenericTest02 {
    public static void main(String[] args) {

        // ArrayList<这里的类型会自动推断>()，前提是JDK8之后才允许。
        // 自动类型推断，钻石表达式！
        List<Animal> myList = new ArrayList<>();

        myList.add(new Animal());
        myList.add(new Cat());
        myList.add(new Bird());

        // 遍历
        Iterator<Animal> it = myList.iterator();
        while(it.hasNext()){
            Animal a = it.next();
            a.move();
            //调用子类中的方法还是要转型
        }

        List<String> strList = new ArrayList<>();

        // 遍历
        Iterator<String> it2 = strList.iterator();
        while(it2.hasNext()){
            // 直接通过迭代器获取了String类型的数据
            String s = it2.next();
            // 直接调用String类的substring方法截取字符串。
            String newString = s.substring(7);
            System.out.println(newString);
        }
    }
}

```

#### 自定义泛型

//不太明白这个

自定义泛型可以吗？可以

- 自定义泛型的时候，<> 尖括号中的是一个标识符，随便写。
- java源代码中经常出现的是： <E>和<T>
- E是Element单词首字母。
- T是Type单词首字母。

```java
public class GenericTest03<标识符随便写> {

    public void doSome(标识符随便写 o){
        System.out.println(o);
    }

    public static void main(String[] args) {

        // new对象的时候指定了泛型是：String类型
        GenericTest03<String> gt = new GenericTest03<>();

        gt.doSome("abc");

        // =============================================================
        GenericTest03<Integer> gt2 = new GenericTest03<>();
        gt2.doSome(100);

        // 类型不匹配
        //gt2.doSome("abc");

        MyIterator<String> mi = new MyIterator<>();
        String s1 = mi.get();

        MyIterator<Animal> mi2 = new MyIterator<>();
        Animal a = mi2.get();

        // 不用泛型就是Object类型。
        /*GenericTest03 gt3 = new GenericTest03();
        gt3.doSome(new Object());*/
    }
}

class MyIterator<T> {
    public T get(){
        return null;
    }
}
```

### Map

- Map和Collection没有继承关系。
- Map集合以key和value的方式存储数据：键值对
	+ key和value都是引用数据类型。
	+ key和value都是存储对象的内存地址。
	+ key起到主导的地位，value是key的一个附属品。
- Map接口中常用方法：
	+ V put(K key, V value) 向Map集合中添加键值对
	+ V get(Object key) 通过key获取value
	+ void clear()    清空Map集合
	+ boolean containsKey(Object key) 判断Map中是否包含某个key
	+ boolean containsValue(Object value) 判断Map中是否包含某个value
	+ boolean isEmpty()   判断Map集合中元素个数是否为0
	+ V remove(Object key) 通过key删除键值对
	+ int size() 获取Map集合中键值对的个数。
	+ Collection<V> values() 获取Map集合中所有的value，返回一个Collection
	+ Set<K> keySet() 获取Map集合所有的key（所有的键是一个set集合）
	+ Set<Map.Entry<K,V>> entrySet()  将Map集合转换成Set集合

	假设现在有一个Map集合，如下所示：
    map1集合对象
    key             value
    ----------------------------
    1               zhangsan
    2               lisi
    3               wangwu
    4               zhaoliu

Set set = map1.entrySet();
set集合对象
1=zhangsan 【注意：Map集合通过entrySet()方法转换成的这个Set集合，Set集合中元素的类型是 Map.Entry<K,V>】
2=lisi【Map.Entry和String一样，都是一种类型的名字，只不过：Map.Entry是静态内部类，是Map中的静态内部类】
3=wangwu
4=zhaoliu ---> 这个东西是个什么？ Map.Entry

#### 使用方式：

```java
public class MapTest01 {
    public static void main(String[] args) {
        // 创建Map集合对象
        Map<Integer, String> map = new HashMap<>();
        // 向Map集合中添加键值对
        map.put(1, "zhangsan"); // 1在这里进行了自动装箱。
        map.put(2, "lisi");
        map.put(3, "wangwu");
        // 通过key获取value
        String value = map.get(2);
        System.out.println(value);
        // 获取键值对的数量
        System.out.println("键值对的数量：" + map.size());
        // 通过key删除key-value
        map.remove(2);
        // 判断是否包含某个key
        // contains方法底层调用的都是equals进行比对的，所以自定义的类型需要重写equals方法。
        System.out.println(map.containsKey(new Integer(4))); // true
        // 判断是否包含某个value
        System.out.println(map.containsValue(new String("wangwu"))); // true

        // 获取所有的value
        Collection<String> values = map.values();
        // foreach
        for(String s : values){
            System.out.println(s);
        }

        // 清空map集合
        map.clear();
        System.out.println("键值对的数量：" + map.size());
        // 判断是否为空
        System.out.println(map.isEmpty()); // true
    }
}

```

#### 遍历方式

```java
public class MapTest02 {
    public static void main(String[] args) {

        // 第一种方式：获取所有的key，通过遍历key，来遍历value
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "zhangsan");
        map.put(2, "lisi");
        map.put(3, "wangwu");
        map.put(4, "zhaoliu");
        // 遍历Map集合
        // 获取所有的key，所有的key是一个Set集合
        Set<Integer> keys = map.keySet();
        // 遍历key，通过key获取value
        // 迭代器可以
        /*Iterator<Integer> it = keys.iterator();
        while(it.hasNext()){
            // 取出其中一个key
            Integer key = it.next();
            // 通过key获取value
            String value = map.get(key);
            System.out.println(key + "=" + value);
        }*/
        // foreach也可以
        for(Integer key : keys){
            System.out.println(key + "=" + map.get(key));
        }

        // 第二种方式：Set<Map.Entry<K,V>> entrySet()
        // 以上这个方法是把Map集合直接全部转换成Set集合。
        // Set集合中元素的类型是：Map.Entry
        Set<Map.Entry<Integer,String>> set = map.entrySet();
        // 遍历Set集合，每一次取出一个Node
        // 迭代器
        /*Iterator<Map.Entry<Integer,String>> it2 = set.iterator();
        while(it2.hasNext()){
            Map.Entry<Integer,String> node = it2.next();
            Integer key = node.getKey();
            String value = node.getValue();
            System.out.println(key + "=" + value);
        }*/

        // foreach
        // 这种方式效率比较高，因为获取key和value都是直接从node对象中获取的属性值。
        // 这种方式比较适合于大数据量。
        for(Map.Entry<Integer,String> node : set){
            System.out.println(node.getKey() + "--->" + node.getValue());
        }
    }
}
```

### 哈希表（散列表）

HashMap集合：
- HashMap集合底层是哈希表/散列表的数据结构。
- 哈希表是一个怎样的数据结构呢？
    - 哈希表是一个数组和单向链表的结合体。
    - 数组：在查询方面效率很高，随机增删方面效率很低。
    - 单向链表：在随机增删方面效率较高，在查询方面效率很低。
    - 哈希表将以上的两种数据结构融合在一起，充分发挥它们各自的优点。"中庸"
- HashMap集合底层的源代码：
    ```java
        public class HashMap{
            // HashMap底层实际上就是一个数组。（一维数组）
            Node<K,V>[] table;
            // 静态的内部类HashMap.Node
            static class Node<K,V> {
                final int hash; // 哈希值（哈希值是key的hashCode()方法的执行结果。hash值通过哈希函数/算法，可以转换存储成数组的下标。）
                final K key; // 存储到Map集合中的那个key
                V value; // 存储到Map集合中的那个value
                Node<K,V> next; // 下一个节点的内存地址。
            }
        }
    ```
- 哈希表/散列表：一维数组，这个数组中每一个元素是一个单向链表。（数组和链表的结合体。）
- 最主要掌握的是：
    - map.put(k,v)
    - v = map.get(k)
    - 以上这两个方法的实现原理，是必须掌握的。
- HashMap集合的key部分特点：
    - 无序，不可重复。
    - 为什么无序？ 因为不一定挂到哪个单向链表上。
    - 不可重复是怎么保证的？ equals方法来保证HashMap集合的key不可重复。如果key重复了，value会覆盖。
    - 放在HashMap集合key部分的元素其实就是放到HashSet集合中了。
    - 所以HashSet集合中的元素也需要同时重写hashCode()+equals()方法。
- 哈希表HashMap使用不当时无法发挥性能！
- 假设将所有的hashCode()方法返回值固定为某个值，那么会导致底层哈希表变成了纯单向链表。这种情况我们称为：散列分布不均匀。
	- 什么是散列分布均匀？
	- 假设有100个元素，10个单向链表，那么每个单向链表上有10个节点，这是最好的，是散列分布均匀的。
	- 假设将所有的hashCode()方法返回值都设定为不一样的值，可以吗，有什么问题？
	- 不行，因为这样的话导致底层哈希表就成为一维数组了，没有链表的概念了。也是散列分布不均匀。散列分布均匀需要你重写hashCode()方法时有一定的技巧。
- 重点：放在HashMap集合key部分的元素,以及放在HashSet集合中的元素,需要同时重写hashCode和equals方法.
- HashMap集合的默认初始化容量是16，默认加载因子是0.75, 这个默认加载因子是当HashMap集合底层数组的容量达到75%的时候，数组开始扩容。
- 重点，记住：HashMap集合初始化容量**必须是2的倍数**，这也是官方推荐的，这是因为达到散列均匀，为了提高HashMap集合的存取效率，所必须的。

这里有个图

测试:
```java
public class HashMapTest01 {
    public static void main(String[] args) {
        // 测试HashMap集合key部分的元素特点
        // Integer是key，它的hashCode和equals都重写了。
        Map<Integer,String> map = new HashMap<>();
        map.put(1111, "zhangsan");
        map.put(6666, "lisi");
        map.put(7777, "wangwu");
        map.put(2222, "zhaoliu");
        map.put(2222, "king"); //key重复的时候value会自动覆盖。

        System.out.println(map.size()); // 4

        // 遍历Map集合
        Set<Map.Entry<Integer,String>> set = map.entrySet();
        for(Map.Entry<Integer,String> entry : set){
            // 验证结果：HashMap集合key部分元素：无序不可重复。
            System.out.println(entry.getKey() + "=" + entry.getValue());
        }
    }
}
```

#### 必须重写hashcode和equals

- 向Map集合中存，以及从Map集合中取，都是先调用key的hashCode方法，然后再调用equals方法！
equals方法有可能调用，也有可能不调用。
    - 拿put(k,v)举例，什么时候equals不会调用？k.hashCode()方法返回哈希值，哈希值经过哈希算法转换成数组下标。数组下标位置上如果是null，equals不需要执行。
    - 拿get(k)举例，什么时候equals不会调用？k.hashCode()方法返回哈希值，哈希值经过哈希算法转换成数组下标。数组下标位置上如果是null，equals不需要执行。

- 注意：如果一个类的equals方法重写了，那么hashCode()方法必须重写。
    - 并且equals方法返回如果是true，hashCode()方法返回的值必须一样。equals方法返回true表示两个对象相同，在同一个单向链表上比较。那么对于同一个单向链表上的节点来说，他们的哈希值都是相同的。所以hashCode()方法的返回值也应该相同。
    
- hashCode()方法和equals()方法不用研究了，直接使用IDEA工具生成，但是这两个方法需要同时生成。

- 对于哈希表数据结构来说：如果o1和o2的hash值相同，一定是放到同一个单向链表上。 如果o1和o2的hash值不同，但由于哈希算法执行结束之后转换的数组下标可能相同，此时会发生“哈希碰撞”。

- HashMap集合key部分允许null吗？  允许  但是要注意：HashMap集合的key null值只能有一个。

- 终极结论：放在HashMap集合key部分的，以及放在HashSet集合中的元素，需要**同时重写hashCode方法和equals方法**。


#### HashMap和Hashtable的区别。

Hashtable和HashMap一样，底层都是哈希表数据结构。

HashMap：
- 初始化容量16，扩容2倍。非线程安全。key和value可以为null。
- HashMap集合的key和value都是可以为null的。

Hashtable：
- 初始化容量11，默认加载因子是：0.75f，扩容2倍+1。线程安全。key和value都不能是null。
- Hashtable的key和value都是不能为null的。

Hashtable方法都带有synchronized：线程安全的。线程安全有其它的方案，这个Hashtable对线程的处理导致效率较低，使用较少了。


### Properties

目前只需要掌握Properties属性类对象的相关方法即可。
Properties是一个Map集合，继承Hashtable，Properties的key和value都是String类型。
Properties被称为属性类对象。
Properties是线程安全的。

```java
public class PropertiesTest01 {
    public static void main(String[] args) {

        // 创建一个Properties对象
        Properties pro = new Properties();

        // 需要掌握Properties的两个方法，一个存，一个取。
        pro.setProperty("url", "jdbc:mysql://localhost:3306/bjpowernode");
        pro.setProperty("driver","com.mysql.jdbc.Driver");

        // 通过key获取value
        String url = pro.getProperty("url");
        String driver = pro.getProperty("driver");


        System.out.println(url);
        System.out.println(driver);

    }
}
```

### TreeMap/TreeSet


TreeSet集合存储元素特点：

- 无序不可重复的，但是存储的元素可以自动按照大小顺序排序！称为：可排序集合。
- 无序：这里的无序指的是存进去的顺序和取出来的顺序不同。并且没有下标。
- TreeSet集合底层实际上是一个TreeMap
- TreeMap集合底层是一个二叉树。
- 放到TreeSet集合中的元素，等同于放到TreeMap集合key部分了。
- 无法对自定义类型排序castException
- 可以不写equals方法，因为底层调用了comparable方法进行比较了

#### 自定义排序规则

TreeMap的key或者TreeSet集合中的元素要想排序，有两种实现方式：

- 第一种：实现java.lang.Comparable接口。
- 第二种：单独编写一个比较器Comparator接口。

##### 第一种

```java
public class TreeSetTest04 {
    public static void main(String[] args) {
        Customer c1 = new Customer(32);
        Customer c2 = new Customer(20);
        // 创建TreeSet集合
        TreeSet<Customer> customers = new TreeSet<>();
        // 添加元素
        customers.add(c1);
        customers.add(c2);
        // 遍历
        for (Customer c : customers){
            System.out.println(c);
        }
    }
}

// 放在TreeSet集合中的元素需要实现java.lang.Comparable接口。
// 并且实现compareTo方法。equals可以不写。
class Customer implements Comparable<Customer>{

    int age;
    public Customer(int age){
        this.age = age;
    }

    // 需要在这个方法中编写比较的逻辑，或者说比较的规则，按照什么进行比较！
    // k.compareTo(t.key)
    // 拿着参数k和集合中的每一个k进行比较，返回值可能是>0 <0 =0
    // 比较规则最终还是由程序员指定的：例如按照年龄升序。或者按照年龄降序。
    @Override
    public int compareTo(Customer c) { // c1.compareTo(c2);
        return c.age - this.age;
    }

    public String toString(){
        return "Customer[age="+age+"]";
    }
//----------------------------------------------------------------
 /*
先按照年龄升序，如果年龄一样的再按照姓名升序。
 */
    @Override
    public int compareTo(Vip v) {
        // 写排序规则，按照什么进行比较。
        if(this.age == v.age){
            // 年龄相同时按照名字排序。
            // 姓名是String类型，可以直接比。调用compareTo来完成比较。
            return this.name.compareTo(v.name);
        } else {
            // 年龄不一样
            return this.age - v.age;
        }
    }

}
```

##### 第二种

使用比较器的方式

最终的结论：放到TreeSet或者TreeMap集合key部分的元素要想做到排序,包括两种方式
	- 第一种：放在集合中的元素实现java.lang.Comparable接口。
	- 第二种：在构造TreeSet或者TreeMap集合的时候给它传一个比较器对象。

Comparable和Comparator怎么选择呢？
- 当比较规则不会发生改变的时候，或者说当比较规则只有1个的时候，建议实现Comparable接口。
- 如果比较规则有多个，并且需要多个比较规则之间频繁切换，建议使用Comparator接口。

- Comparator接口的设计符合OCP原则。


```java
public class TreeSetTest06 {
    public static void main(String[] args) {
        // 创建TreeSet集合的时候，需要使用这个比较器。
        // TreeSet<WuGui> wuGuis = new TreeSet<>();//这样不行，没有通过构造方法传递一个比较器进去。

        // 给构造方法传递一个比较器。
        //TreeSet<WuGui> wuGuis = new TreeSet<>(new WuGuiComparator());

        // 大家可以使用匿名内部类的方式（这个类没有名字。直接new接口。）
        TreeSet<WuGui> wuGuis = new TreeSet<>(new Comparator<WuGui>() {
            @Override
            public int compare(WuGui o1, WuGui o2) {
                return o1.age - o2.age;
            }
        });

        wuGuis.add(new WuGui(1000));
        wuGuis.add(new WuGui(800));
        wuGuis.add(new WuGui(810));

        for(WuGui wuGui : wuGuis){
            System.out.println(wuGui);
        }
    }
}

// 乌龟
class WuGui{

    int age;

    public WuGui(int age){
        this.age = age;
    }

    @Override
    public String toString() {
        return "小乌龟[" +
                "age=" + age +
                ']';
    }
}

// 单独在这里编写一个比较器
//比较器实现java.util.Comparator接口。（Comparable是java.lang包下的。Comparator是java.util包下的。）

class WuGuiComparator implements Comparator<WuGui> {

    @Override
    public int compare(WuGui o1, WuGui o2) {
        // 指定比较规则
        // 按照年龄排序
        return o1.age - o2.age;
    }
}

```


#### 自平衡二叉树



图片



### Collections工具类

synchronizedList方法

sort方法（要求集合中元素实现Comparable接口。）

```java

/*
java.util.Collection 集合接口
java.util.Collections 集合工具类，方便集合的操作。
 */
public class CollectionsTest {
    public static void main(String[] args) {

        // ArrayList集合不是线程安全的。
        List<String> list = new ArrayList<>();

        // 变成线程安全的
        Collections.synchronizedList(list);

        // 排序
        list.add("abf");
        list.add("abx");

        Collections.sort(list);
        for(String s : list){
            System.out.println(s);
        }

        List<WuGui2> wuGuis = new ArrayList<>();
        wuGuis.add(new WuGui2(1000));
        wuGuis.add(new WuGui2(8000));
        // 注意：对List集合中元素排序，需要保证List集合中的元素实现了：Comparable接口。
        Collections.sort(wuGuis);
        for(WuGui2 wg : wuGuis){
            System.out.println(wg);
        }

        // 对Set集合怎么排序呢？
        Set<String> set = new HashSet<>();
        set.add("king");
        set.add("kingsoft");
        // 将Set集合转换成List集合
        List<String> myList = new ArrayList<>(set);
        Collections.sort(myList);
        for(String s : myList) {
            System.out.println(s);
        }

        // 这种方式也可以排序。
        //Collections.sort(list集合, 比较器对象);
    }
}

class WuGui2 implements Comparable<WuGui2>{
    int age;
    public WuGui2(int age){
        this.age = age;
    }

    @Override
    public int compareTo(WuGui2 o) {
        return this.age - o.age;
    }

    @Override
    public String toString() {
        return "WuGui2{" +
                "age=" + age +
                '}';
    }
}

```

## IO流

IDEA的默认当前路径是在哪？工程的根目录

有多种分类方式：

- 一种方式是按照流的方向进行分类：以内存作为参照物
	- 往内存中去，叫做输入(Input)。或者叫做读(Read)。
	- 从内存中出来，叫做输出(Output)。或者叫做写(Write)。

- 另一种方式是按照读取数据方式不同进行分类：
- 有的流是按照字节的方式读取数据，一次读取1个字节byte，等同于一次读取8个二进制位。这种流是万能的，什么类型的文件都可以读取。包括：文本文件，图片，声音文件，视频文件等....
假设文件file1.txt，采用字节流的话是这样读的：
a中国bc张三fe
第一次读：一个字节，正好读到'a'
第二次读：一个字节，正好读到'中'字符的一半。
第三次读：一个字节，正好读到'中'字符的另外一半。

- 有的流是按照字符的方式读取数据的，一次读取一个字符，这种流是为了方便读取普通文本文件而存在的，这种流不能读取：图片、声音、视频等文件。只能读取纯文本文件，连word文件都无法读取。
假设文件file1.txt，采用字符流的话是这样读的：
a中国bc张三fe
第一次读：'a'字符（'a'字符在windows系统中占用1个字节。）
第二次读：'中'字符（'中'字符在windows系统中占用2个字节。）

流的分类

- 输入流、输出流
- 字节流、字符流

java中所有的流都是在：java.io.*;下。

java中主要还是研究：
怎么new流对象。调用流对象的哪个方法是读，哪个方法是写。

java IO流这块有四大家族：
四大家族的首领：
四大家族的首领都是抽象类。(abstract class)

- java.io.InputStream  字节输入流
- java.io.OutputStream 字节输出流

- java.io.Reader字符输入流
- java.io.Writer字符输出流

所有的**流**都实现了：
java.io.Closeable接口，都是可关闭的，都有close()方法。
流毕竟是一个管道，这个是内存和硬盘之间的通道，用完之后一定要关闭，不然会耗费(占用)很多资源。养成好习惯，用完流一定要关闭。

所有的**输出流**都实现了：
java.io.Flushable接口，都是可刷新的，都有flush()方法。
养成一个好习惯，输出流在最终输出之后，一定要记得flush()刷新一下。这个刷新表示将通道/管道当中剩余未输出的数据强行输出完（清空管道！）刷新的作用就是清空管道。
**注意：如果没有flush()可能会导致丢失数据。**

注意：在java中只要“类名”以Stream结尾的都是字节流。以“Reader/Writer”结尾的都是字符流。

java.io包下需要掌握的流有16个：

文件专属：
java.io.FileInputStream（掌握）
java.io.FileOutputStream（掌握）
java.io.FileReader
java.io.FileWriter

转换流：（将字节流转换成字符流）
java.io.InputStreamReader
java.io.OutputStreamWriter

缓冲流专属：
java.io.BufferedReader
java.io.BufferedWriter
java.io.BufferedInputStream
java.io.BufferedOutputStream

数据流专属：
java.io.DataInputStream
java.io.DataOutputStream

标准输出流：
java.io.PrintWriter
java.io.PrintStream（掌握）

对象专属流：
java.io.ObjectInputStream（掌握）
java.io.ObjectOutputStream（掌握）

java.io.File类。
File类的常用方法。

java io这块还剩下什么内容：
第一：ObjectInputStream ObjectOutputStream的使用。
第二：IO流+Properties集合的联合使用。

### FileInputStream

1、文件字节输入流，万能的，任何类型的文件都可以采用这个流来读。

2、字节的方式，完成输入的操作，完成读的操作（硬盘---> 内存）

最终版：背模板

```java
public class FileInputStreamTest04 {
    public static void main(String[] args) {
        FileInputStream fis = null; //定义一个 null 的流对象
        try {
            fis = new FileInputStream("chapter23/src/tempfile3"); //流对象赋值
            // 准备一个byte数组
            byte[] bytes = new byte[4];
            /*while(true){
                int readCount = fis.read(bytes);
                if(readCount == -1){
                    break;
                }
                // 把byte数组转换成字符串，读到多少个转换多少个。
                System.out.print(new String(bytes, 0, readCount));
            }*/

            int readCount = 0;
            while((readCount = fis.read(bytes)) != -1) {
                System.out.print(new String(bytes, 0, readCount)); //取已经更新了的字符串输出
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fis != null) {
                try {
                    fis.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```


FileInputStream类的其它常用方法：
- int available()：返回流当中剩余的没有读到的字节数量
- long skip(long n)：跳过几个字节不读。

```java
public class FileInputStreamTest05 {
    public static void main(String[] args) {
        FileInputStream fis = null;
        try {
            fis = new FileInputStream("tempfile");
            System.out.println("总字节数量：" + fis.available());
            // 读1个字节
            //int readByte = fis.read();
            // 还剩下可以读的字节数量是：5
            //System.out.println("剩下多少个字节没有读：" + fis.available());
            // 这个方法有什么用？
            //byte[] bytes = new byte[fis.available()];
            // 这种方式不太适合太大的文件，因为byte[]数组不能太大。
            // 不需要循环了。
            // 直接读一次就行了。
            //int readCount = fis.read(bytes); // 6
            //System.out.println(new String(bytes)); // abcdef

            // skip跳过几个字节不读取，这个方法也可能以后会用！
            fis.skip(3);
            System.out.println(fis.read()); //100

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fis != null) {
                try {
                    fis.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```


### FileOutputStream

```java

public class FileOutputStreamTest01 {
    public static void main(String[] args) {
        FileOutputStream fos = null;
        try {
            // 文件不存在的时候会自动新建！
            // 这种方式谨慎使用，这种方式会先将原文件清空，然后重新写入。

            // 以追加的方式在文件末尾写入。不会清空原文件内容。 加个true
            fos = new FileOutputStream("chapter23/src/tempfile3", true);
            // 开始写。
            byte[] bytes = {97, 98, 99, 100};
            // 将byte数组全部写出！
            fos.write(bytes); // abcd
            // 将byte数组的一部分写出！
            fos.write(bytes, 0, 2); // 再写出ab

            // 字符串
            String s = "我是一个中国人，我骄傲！！！";
            // 将字符串转换成byte数组。
            byte[] bs = s.getBytes();
            // 写
            fos.write(bs);

            // 写完之后，最后一定要刷新
            fos.flush();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fos != null) {
                try {
                    fos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```


### FileReader

- 文件字符输入流，只能读取普通文本。
- 读取文本内容时，比较方便，快捷。

```java
public class FileReaderTest {
    public static void main(String[] args) {
        FileReader reader = null;
        try {
            // 创建文件字符输入流
            reader = new FileReader("tempfile");

            //准备一个char数组
            char[] chars = new char[4];
            // 往char数组中读
            // 开始读
            char[] chars = new char[4]; // 一次读取4个*字符*
            int readCount = 0;
            while((readCount = reader.read(chars)) != -1) {
                System.out.print(new String(chars,0,readCount));
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

### FileWriter

- 文件字符输出流。写。
- 只能输出普通文本，普通文本，不能输出图片声音等文件
- 能用记事本编辑的都是普通文件
- word不是普通文本

```java
public class FileWriterTest {
    public static void main(String[] args) {
        FileWriter out = null;
        try {
            // 创建文件字符输出流对象
            out = new FileWriter("file", true); // true 表示追加

            // 开始写。
            char[] chars = {'我','是','中','国','人'};
            out.write(chars);
            out.write(chars, 2, 3); //“中国人”

            out.write("我是一名java软件工程师！");
            // 写出一个换行符。
            out.write("\n");

            // 刷新
            out.flush();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (out != null) {
                try {
                    out.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

```

### BufferedReader

- 这个流没有前面那些快
- 带有缓冲区的字符输入流。
- 使用这个流的时候**不需要自定义char数组，或者说不需要自定义byte数组。自带缓冲**。

```java
public class BufferedReaderTest01 {
    public static void main(String[] args) throws Exception{

        FileReader reader = new FileReader("Copy02.java");
        // 当一个流的构造方法中需要一个流的时候，这个被传进来的流叫做：节点流。
        // 外部负责包装的这个流，叫做：包装流（处理流）
        // 像当前这个程序来说：FileReader就是一个节点流。BufferedReader就是包装流/处理流。
        BufferedReader br = new BufferedReader(reader);

        // br.readLine()方法读取一个文本行，但不带换行符。
        String s = null;
        while((s = br.readLine()) != null){ //一行一行地读
            System.out.print(s);
        }

        // 关闭流
        // 对于包装流来说，只需要关闭最外层流就行，里面的节点流会自动关闭。（可以看源代码。）
        br.close();
    }
}
```

### BufferedWriter

```java
public class BufferedWriterTest {
    public static void main(String[] args) throws Exception{
        // 带有缓冲区的字符输出流
        //BufferedWriter out = new BufferedWriter(new FileWriter("copy"));

        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("copy", true)));
        // 开始写。
        out.write("hello world!");
        // 刷新
        out.flush();
        // 关闭最外层
        out.close();
    }
}
```

### 转换流(少用)

#### InputStreamReader

把字节流转换为字符流

```java
public class BufferedReaderTest02 {
    public static void main(String[] args) throws Exception{

        /*// 字节流
        FileInputStream in = new FileInputStream("Copy02.java");

        // 通过转换流转换（InputStreamReader将字节流转换成字符流。）
        // in是节点流。reader是包装流。
        InputStreamReader reader = new InputStreamReader(in);

        // 这个构造方法只能传一个字符流。不能传字节流。
        // reader是节点流。br是包装流。
        BufferedReader br = new BufferedReader(reader);*/

        // 合并
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("Copy02.java")));

        String line = null;
        while((line = br.readLine()) != null){
            System.out.println(line);
        }

        // 关闭最外层
        br.close();
    }
}

```

### 数据流（了解）

- java.io.DataOutputStream：数据专属的流。
- 这个流可以将数据连同数据的类型一并写入文件。
- 注意：这个文件不是普通文本文档。（这个文件使用记事本**打不开**。）

写入文件之后，相当于“加密了”。
用普通的记事本文件打开是乱码，在“解密”的时候，必须按照**一样的顺序**读入流中

```java
public class DataOutputStreamTest {
    public static void main(String[] args) throws Exception{
        // 创建数据专属的字节输出流
        // 抽象类不能创建对象，所以创建文件流
        DataOutputStream dos = new DataOutputStream(new FileOutputStream("data"));
        // 写数据
        byte b = 100;
        short s = 200;
        int i = 300;
        long l = 400L;
        float f = 3.0F;
        double d = 3.14;
        boolean sex = false;
        char c = 'a';
        // 写
        dos.writeByte(b); // 把数据以及数据的类型一并写入到文件当中。
        dos.writeShort(s);
        dos.writeInt(i);
        dos.writeLong(l);
        dos.writeFloat(f);
        dos.writeDouble(d);
        dos.writeBoolean(sex);
        dos.writeChar(c);

        // 刷新
        dos.flush();
        // 关闭最外层
        dos.close();
    }
}

```

- DataInputStream:数据字节输入流。
- DataOutputStream写的文件，只能使用DataInputStream去读。并且读的时候你需要提前知道写入的顺序。
- 读的顺序需要和写的顺序一致。才可以正常取出数据。

```java
public class DataInputStreamTest01 {
    public static void main(String[] args) throws Exception{
        DataInputStream dis = new DataInputStream(new FileInputStream("data"));
        // 开始读
        byte b = dis.readByte();
        short s = dis.readShort();
        int i = dis.readInt();
        long l = dis.readLong();
        float f = dis.readFloat();
        double d = dis.readDouble();
        boolean sex = dis.readBoolean();
        char c = dis.readChar();

        System.out.println(b);
        System.out.println(s);
        System.out.println(i + 1000);
        System.out.println(l);
        System.out.println(f);
        System.out.println(d);
        System.out.println(sex);
        System.out.println(c);

        dis.close();
    }
}
```

### 标准输出流

```java
/*
java.io.PrintStream：标准的字节输出流。默认输出到控制台。
 */
public class PrintStreamTest {
    public static void main(String[] args) throws Exception{

        // 联合起来写
        System.out.println("hello world!");

        // 分开写
        PrintStream ps = System.out;
        ps.println("hello zhangsan");

        // 标准输出流不需要手动close()关闭。
        // 可以改变标准输出流的输出方向吗？ 可以
        /*
        // 这些是之前System类使用过的方法和属性。
        System.gc();
        System.currentTimeMillis();
        PrintStream ps2 = System.out;
        System.exit(0);
        System.arraycopy(....);
         */

        // 标准输出流不再指向控制台，指向“log”文件。
        PrintStream printStream = new PrintStream(new FileOutputStream("log"));
        // 修改输出方向，将输出方向修改到"log"文件。
        System.setOut(printStream);
        // 再输出
        System.out.println("hello world");//这些就输出在log文件中了（日志框架）
    }
}

```

记录日志：

```java
/*
日志工具
 */
public class Logger {
    /*
    记录日志的方法。
     */
    public static void log(String msg) {
        try {
            // 指向一个日志文件
            PrintStream out = new PrintStream(new FileOutputStream("log.txt", true));
            // 改变输出方向
            System.setOut(out);
            // 日期当前时间
            Date nowTime = new Date();
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss SSS");
            String strTime = sdf.format(nowTime);

            System.out.println(strTime + ": " + msg);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

### 对象流

java.io.NotSerializableException:
- Student对象不支持序列化

- 参与序列化和反序列化的对象，必须实现Serializable接口。

- 注意：通过源代码发现，Serializable接口只是一个标志接口：
    - public interface Serializable {}这个接口当中什么代码都没有。
    - 那么它起到一个什么作用呢？
        - 起到标识的作用，标志的作用，java虚拟机看到这个类实现了这个接口，可能会对这个类进行特殊待遇。
        Serializable这个标志接口是给java虚拟机参考的，java虚拟机看到这个接口之后，会为该类自动生成
        一个序列化版本号。

- 序列化版本号有什么用呢？
    java.io.InvalidClassException:
        com.bjpowernode.java.bean.Student;
        local class incompatible:
            stream classdesc serialVersionUID = -684255398724514298（十年后）,
            local class serialVersionUID = -3463447116624555755（十年前）

- java语言中是采用什么机制来区分类的？
	+ 第一：首先通过类名进行比对，如果类名不一样，肯定不是同一个类。
	+ 第二：如果类名一样，再怎么进行类的区别？靠序列化版本号进行区分。

- 小鹏编写了一个类：com.bjpowernode.java.bean.Student implements Serializable
- 胡浪编写了一个类：com.bjpowernode.java.bean.Student implements Serializable
- 不同的人编写了同一个类，但“这两个类确实不是同一个类”。这个时候序列化版本就起上作用了:对于java虚拟机来说，java虚拟机是可以区分开这两个类的，因为这两个类都实现了Serializable接口，都有默认的序列化版本号，他们的序列化版本号不一样。所以区分开了。（这是自动生成序列化版本号的好处）

请思考？

- 这种自动生成序列化版本号有什么缺陷？
- 这种自动生成的序列化版本号缺点是：一旦代码确定之后，不能进行后续的修改，
- 因为只要修改，必然会重新编译，此时会生成全新的序列化版本号，这个时候java
- 虚拟机会认为这是一个全新的类。（这样就不好了！）

最终结论：

- 凡是一个类实现了Serializable接口，建议给该类提供一个固定不变的序列化版本号。这样，以后这个类即使代码修改了，但是版本号不变，java虚拟机会认为是同一个类。
- private static final long serialVersionUID = -123456789;(自己指定)
- IDEA生成

```java

//序列化

//一个一个存，存多个对象报错，只能通过序列化集合

public class ObjectOutputStreamTest01 {
    public static void main(String[] args) throws Exception{
        // 创建java对象
        Student s = new Student(1111, "zhangsan");
        // 序列化
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("students"));

        // 序列化对象
        oos.writeObject(s);

        // 刷新
        oos.flush();
        // 关闭
        oos.close();
    }
}

/*
一次序列化多个对象呢？
    可以，可以将对象放到集合当中，序列化集合。
提示：
    参与序列化的ArrayList集合以及集合中的元素User都需要实现 java.io.Serializable接口。
 */
public class ObjectOutputStreamTest02 {
    public static void main(String[] args) throws Exception{
        List<User> userList = new ArrayList<>();
        userList.add(new User(1,"zhangsan"));
        userList.add(new User(2, "lisi"));
        userList.add(new User(3, "wangwu"));
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("users"));

        // 序列化一个集合，这个集合对象中放了很多其他对象。
        oos.writeObject(userList);

        oos.flush();
        oos.close();
    }
}

//反序列化

public class ObjectInputStreamTest01 {
    public static void main(String[] args) throws Exception{
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("students"));
        // 开始反序列化，读
        Object obj = ois.readObject();
        // 反序列化回来是一个学生对象，所以会调用学生对象的toString方法。
        System.out.println(obj);
        ois.close();
    }
}

/*
反序列化集合
 */
public class ObjectInputStreamTest02 {
    public static void main(String[] args) throws Exception{
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("users"));
        //Object obj = ois.readObject();
        //System.out.println(obj instanceof List);
        List<User> userList = (List<User>)ois.readObject();
        for(User user : userList){
            System.out.println(user);
        }
        ois.close();
    }
}


```

transient 关键字，指定的变量不参加序列化

### IO + properties 联合使用

IO+Properties的联合应用。

非常好的一个设计理念：
- 以后经常改变的数据，可以单独写到一个文件中，使用程序动态读取。将来只需要修改这个文件的内容，java代码不需要改动，不需要重新编译，服务器也不需要重启。就可以拿到动态的信息。

- 类似于以上机制的这种文件被称为配置文件。并且当配置文件中的内容格式是： key=value 的时候，我们把这种配置文件叫做属性配置文件。

java规范中有要求：
- 属性配置文件建议以.properties结尾，但这不是必须的。
- 这种以.properties结尾的文件在java中被称为：属性配置文件。
- 其中Properties是专门存放属性配置文件内容的一个类。
- 最好不要有空格
- 在属性配置文件中， # 为注释，重复的值会覆盖

```java
public class IoPropertiesTest01 {
    public static void main(String[] args) throws Exception{
        /*
        Properties是一个Map集合，key和value都是String类型。
        想将userinfo文件中的数据加载到Properties对象当中。
         */
        // 新建一个输入流对象
        FileReader reader = new FileReader("chapter23/userinfo.properties");

        // 新建一个Map集合
        Properties pro = new Properties();

        // 调用Properties对象的load方法将文件中的数据加载到Map集合中。
        pro.load(reader); // 文件中的数据顺着管道加载到Map集合中，其中等号=左边做key，右边做value

        // 通过key来获取value呢？
        String username = pro.getProperty("username");
        System.out.println(username);
    }
}
```


### 文件复制

#### FileInputStream + FileOutputStream

- 使用FileInputStream + FileOutputStream完成文件的拷贝。
- 拷贝的过程应该是一边读，一边写。
- 使用以上的字节流拷贝文件的时候，文件类型随意，万能的。**什么样的文件都能拷贝。**

```java
public class Copy01 {
    public static void main(String[] args) {
        FileInputStream fis = null;
        FileOutputStream fos = null;
        try {
            // 创建一个输入流对象
            fis = new FileInputStream("D:\\course\\02-JavaSE\\video\\chapter01\\动力节点-JavaSE-杜聚宾-001-文件扩展名的显示.avi");
            // 创建一个输出流对象
            fos = new FileOutputStream("C:\\动力节点-JavaSE-杜聚宾-001-文件扩展名的显示.avi");

            // 最核心的：一边读，一边写
            byte[] bytes = new byte[1024 * 1024]; // 1MB（一次最多拷贝1MB。）
            int readCount = 0;
            while((readCount = fis.read(bytes)) != -1) {
                fos.write(bytes, 0, readCount);
            }

            // 刷新，输出流最后要刷新
            fos.flush();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            // 分开try，不要一起try。
            // 一起try的时候，其中一个出现异常，可能会影响到另一个流的关闭。
            if (fos != null) {
                try {
                    fos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (fis != null) {
                try {
                    fis.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

#### FileReader + FileWriter

```java
public class Copy02 {
    public static void main(String[] args) {
        FileReader in = null;
        FileWriter out = null;
        try {
            // 读
            in = new FileReader("chapter23/src/com/bjpowernode/java/io/Copy02.java");
            // 写
            out = new FileWriter("Copy02.java");

            // 一边读一边写：
            char[] chars = new char[1024 * 512]; // 1MB
            int readCount = 0;
            while((readCount = in.read(chars)) != -1){
                out.write(chars, 0, readCount);
            }

            // 刷新
            out.flush();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (in != null) {
                try {
                    in.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (out != null) {
                try {
                    out.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

    }
}
```

#### 目录拷贝

```java
/*
拷贝目录
 */
public class CopyAll {
    public static void main(String[] args) {
        // 拷贝源
        File srcFile = new File("D:\\course\\02-JavaSE\\document");
        // 拷贝目标
        File destFile = new File("C:\\a\\b\\c");
        // 调用方法拷贝
        copyDir(srcFile, destFile);
    }

    /**
     * 拷贝目录
     * @param srcFile 拷贝源
     * @param destFile 拷贝目标
     */
    private static void copyDir(File srcFile, File destFile) {
        if(srcFile.isFile()) {
            // srcFile如果是一个文件的话，递归结束。
            // 是文件的时候需要拷贝。
            // ....一边读一边写。
            FileInputStream in = null;
            FileOutputStream out = null;
            try {
                // 读这个文件
                // D:\course\02-JavaSE\document\JavaSE进阶讲义\JavaSE进阶-01-面向对象.pdf
                in = new FileInputStream(srcFile);
                // 写到这个文件中
                // C:\course\02-JavaSE\document\JavaSE进阶讲义\JavaSE进阶-01-面向对象.pdf
                String path = (destFile.getAbsolutePath().endsWith("\\") ? destFile.getAbsolutePath() : destFile.getAbsolutePath() + "\\")  + srcFile.getAbsolutePath().substring(3);
                out = new FileOutputStream(path);
                // 一边读一边写
                byte[] bytes = new byte[1024 * 1024]; // 一次复制1MB
                int readCount = 0;
                while((readCount = in.read(bytes)) != -1){
                    out.write(bytes, 0, readCount);
                }
                out.flush();
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                if (out != null) {
                    try {
                        out.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
                if (in != null) {
                    try {
                        in.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
            return;
        }
        // 获取源下面的子目录
        File[] files = srcFile.listFiles();
        for(File file : files){
            // 获取所有文件的（包括目录和文件）绝对路径
            //System.out.println(file.getAbsolutePath());
            if(file.isDirectory()){
                // 新建对应的目录
                //System.out.println(file.getAbsolutePath());
                //D:\course\02-JavaSE\document\JavaSE进阶讲义       源目录
                //C:\course\02-JavaSE\document\JavaSE进阶讲义       目标目录
                String srcDir = file.getAbsolutePath();
                String destDir = (destFile.getAbsolutePath().endsWith("\\") ? destFile.getAbsolutePath() : destFile.getAbsolutePath() + "\\")  + srcDir.substring(3);
                File newFile = new File(destDir);
                if(!newFile.exists()){
                    newFile.mkdirs();
                }
            }
            // 递归调用
            copyDir(file, destFile);
        }
    }
}
```

### File类

File类和四大家族没有关系，所以File类不能完成文件的读和写。
File对象代表什么？

	- 文件和目录路径名的抽象表示形式。
	- C:\Drivers 这是一个File对象
	- C:\Drivers\Lan\Realtek\Readme.txt 也是File对象。
	- 一个File对象有可能对应的是目录，也可能是文件。
	- File只是一个路径名的抽象表示形式。


```java
public class FileTest01 {
    public static void main(String[] args) throws Exception {
        // 创建一个File对象
        File f1 = new File("D:\\file");

        // 判断是否存在！
        System.out.println(f1.exists());

        // 如果D:\file不存在，则以文件的形式创建出来
        if(!f1.exists()) {
            // 以文件形式新建
            f1.createNewFile();
        }

        // 如果D:\file不存在，则以目录的形式创建出来
        if(!f1.exists()) {
            // 以目录的形式新建。
            f1.mkdir();
        }

        // 可以创建多重目录吗？
        File f2 = new File("D:/a/b/c/d/e/f");
        if(!f2.exists()) {
            // 多重目录的形式新建。
            f2.mkdirs();
        }

        File f3 = new File("D:\\course\\01-开课\\学习方法.txt");
        // 获取文件的父路径
        String parentPath = f3.getParent();
        System.out.println(parentPath); //D:\course\01-开课
        File parentFile = f3.getParentFile();
        System.out.println("获取绝对路径：" + parentFile.getAbsolutePath());

        File f4 = new File("copy");
        System.out.println("绝对路径：" + f4.getAbsolutePath()); // C:\Users\Administrator\IdeaProjects\javase\copy

    }
}

public class FileTest02 {
    public static void main(String[] args) {

        File f1 = new File("D:\\course\\01-开课\\开学典礼.ppt");
        // 获取文件名
        System.out.println("文件名：" + f1.getName());

        // 判断是否是一个目录
        System.out.println(f1.isDirectory()); // false

        // 判断是否是一个文件
        System.out.println(f1.isFile()); // true

        // 获取文件最后一次修改时间
        long haoMiao = f1.lastModified(); // 这个毫秒是从1970年到现在的总毫秒数。
        // 将总毫秒数转换成日期?????
        Date time = new Date(haoMiao);
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss SSS");
        String strTime = sdf.format(time);
        System.out.println(strTime);

        // 获取文件大小
        System.out.println(f1.length()); //216064字节。
    }
}


/*
File中的listFiles方法。
 */
public class FileTest03 {
    public static void main(String[] args) {
        // File[] listFiles()
        // 获取当前目录下所有的子文件。
        File f = new File("D:\\course\\01-开课");
        File[] files = f.listFiles();
        // foreach
        for(File file : files){
            //System.out.println(file.getAbsolutePath());
            System.out.println(file.getName());
        }
    }
}
```

## 多线程

什么是进程？什么是线程？
- 进程是一个应用程序（1个进程是一个软件）。
- 线程是一个进程中的执行场景/执行单元。
- 一个进程可以启动多个线程。

对于java程序来说，当在DOS命令窗口中输入：java HelloWorld 回车之后。会先启动JVM，而JVM就是一个进程。JVM再启动一个主线程调用main方法。同时再启动一个垃圾回收线程负责看护，回收垃圾。最起码，现在的java程序中至少有两个线程并发，一个是垃圾回收线程，一个是执行main方法的主线程。

进程和线程是什么关系？举个例子
- 阿里巴巴：进程
	- 马云：阿里巴巴的一个线程
	- 童文红:阿里巴巴的一个线程
- 京东：进程
	+ 强东：京东的一个线程
	+ 妹妹：京东的一个线程
- 进程可以看做是现实生活当中的公司。
- 线程可以看做是公司当中的某个员工。

注意：

- 进程A和进程B的内存独立不共享。（阿里巴巴和京东资源不会共享的！）
- 魔兽游戏是一个进程
- 酷狗音乐是一个进程
- 这两个进程是独立的，不共享资源。

线程A和线程B呢？
在java语言中：线程A和线程B，**堆内存和方法区内存**共享。但是**栈内存**独立，一个线程一个栈。
假设启动10个线程，会有10个栈空间，每个栈和每个栈之间，互不干扰，各自执行各自的，这就是多线程并发。

火车站，可以看做是一个进程。火车站中的每一个售票窗口可以看做是一个线程。我在窗口1购票，你可以在窗口2购票，你不需要等我，我也不需要等你。所以多线程并发可以提高效率。

- java中之所以有多线程机制，目的就是为了提高程序的处理效率。

- 使用了多线程机制之后，main方法结束，是不是有可能程序也不会结束。main方法结束只是主线程结束了，主栈空了，其它的栈(线程)可能还在压栈弹栈。

对于多核的CPU电脑来说，真正的多线程并发是没问题的。4核CPU表示同一个时间点上，可以真正的有4个进程并发执行。

分析一个问题：对于单核的CPU来说，真的可以做到真正的多线程并发吗？

什么是真正的多线程并发？t1线程执行t1的。t2线程执行t2的。t1不会影响t2，t2也不会影响t1。这叫做真正的多线程并发。

单核的CPU表示只有一个大脑：
**不能**够做到真正的多线程并发，但是可以做到给人一种“多线程并发”的感觉。对于单核的CPU来说，在某一个时间点上实际上只能处理一件事情，但是由于CPU的处理速度极快，多个线程之间频繁切换执行，跟人来的感觉是：多个事情同时在做！
线程A：播放音乐
线程B：运行魔兽游戏
线程A和线程B频繁切换执行，人类会感觉音乐一直在播放，游戏一直在运行，给我们的感觉是同时并发的。

电影院采用胶卷播放电影，一个胶卷一个胶卷播放速度达到一定程度之后，人类的眼睛产生了错觉，感觉是动画的。这说明人类的反应速度很慢，就像一根钢针扎到手上，到最终感觉到疼，这个过程是需要“很长的”时间的，在这个期间计算机可以进行亿万次的循环。所以计算机的执行速度很快。

### 实现多线程的两种方式

#### 第一种方式

实现线程的第一种方式：编写一个类，直接继承java.lang.Thread，重写run方法。

- 怎么创建线程对象？ new就行了。
- 怎么启动线程呢？ 调用线程对象的start()方法。
- 注意：亘古不变的道理：方法体当中的代码永远都是自上而下的顺序依次逐行执行的。
- 以下程序的输出结果有这样的特点：有先有后。有多有少。这是咋回事？
```java
public class ThreadTest02 {
    public static void main(String[] args) {
        // 这里是main方法，这里的代码属于主线程，在主栈中运行。
        // 新建一个分支线程对象
        MyThread t = new MyThread();
        // 启动线程
        //t.run(); // 直接调用run方法不会启动另一个线程，不会分配新的分支栈。（这种方式就是单线程。）

        // start()方法的作用是：启动一个分支线程，在JVM中开辟一个新的栈空间，这段代码任务完成之后，瞬间就结束了。这段代码的任务只是为了开启一个新的栈空间，只要新的栈空间开出来，start()方法就结束了。线程就启动成功了。 启动成功的线程会自动调用run方法，并且run方法在分支栈的栈底部（压栈）。
        // run方法在分支栈的栈底部，main方法在主栈的栈底部。run和main是平级的。
        t.start();
        // 这里的代码还是运行在主线程中。
        for(int i = 0; i < 100; i++){
            System.out.println("主线程--->" + i);
        }
    }
}
class MyThread extends Thread {
    @Override
    public void run() {
        // 编写程序，这段程序运行在分支线程中（分支栈）。
        for(int i = 0; i < 100; i++){
            System.out.println("分支线程--->" + i);
        }
    }
}
```

#### 第二种方式

实现线程的第二种方式，编写一个类实现java.lang.Runnable接口。

```java
public class ThreadTest03 {
    public static void main(String[] args) {
        // 创建一个可运行的对象
        // 将可运行的对象封装成一个线程对象
        Thread t = new Thread(new MyRunnable()); // 合并代码
        // 启动线程
        t.start();
        for(int i = 0; i < 100; i++)
            System.out.println("主线程--->" + i);
    }
}

// 这并不是一个线程类，是一个可运行的类。它还不是一个线程。
class MyRunnable implements Runnable {
    @Override
    public void run() {
        for(int i = 0; i < 100; i++){
            System.out.println("分支线程--->" + i);
        }
    }
}
```



匿名内部类

```java
public class ThreadTest04 {
    public static void main(String[] args) {
        // 创建线程对象，采用匿名内部类方式。
        // 这是通过一个没有名字的类，new出来的对象。
        Thread t = new Thread(new Runnable(){
            @Override
            public void run() {
                for(int i = 0; i < 100; i++){
                    System.out.println("t线程---> " + i);
                }
            }
        });

        // 启动线程
        t.start();

        for(int i = 0; i < 100; i++){
            System.out.println("main线程---> " + i);
        }
    }
}
```

#### 第三种方式


实现线程的第三种方式：实现Callable接口。（JDK8新特性。）
这种方式实现的线程可以获取线程的返回值。
之前讲解的那两种方式是无法获取线程返回值的，因为run方法返回void。

思考：
系统委派一个线程去执行一个任务，该线程执行完任务之后，可能
会有一个执行结果，我们怎么能拿到这个执行结果呢？
使用第三种方式：实现Callable接口方式。

实现线程的第三种方式：
- 实现Callable接口
- 这种方式的优点：可以获取到线程的执行结果。
- 这种方式的缺点：效率比较低，在获取t线程执行结果的时候，当前线程受阻塞，效率较低。

 ```java
public class ThreadTest15 {
    public static void main(String[] args) throws Exception {

        // 第一步：创建一个“未来任务类”对象。
        // 参数非常重要，需要给一个Callable接口实现类对象。
        FutureTask task = new FutureTask(new Callable() {
            @Override
            public Object call() throws Exception { // call()方法就相当于run方法。只不过这个有返回值
                // 线程执行一个任务，执行之后可能会有一个执行结果
                // 模拟执行
                System.out.println("call method begin");
                Thread.sleep(1000 * 10);
                System.out.println("call method end!");
                int a = 100;
                int b = 200;
                return a + b; //自动装箱(300结果变成Integer)
            }
        });

        // 创建线程对象
        Thread t = new Thread(task);

        // 启动线程
        t.start();

        // 这里是main方法，这是在主线程中。
        // 在主线程中，怎么获取t线程的返回结果？
        // get()方法的执行会导致“当前线程阻塞”
        // main方法这里的程序要想执行必须等待get()方法的结束
        // 而get()方法可能需要很久。因为get()方法是为了拿另一个线程的执行结果
        // 另一个线程执行是需要时间的。
        Object obj = task.get();
        System.out.println("线程执行结果:" + obj);
    }
}
 ```

怎么获取当前线程对象？
- Thread t = Thread.currentThread();
- 返回值t就是当前线程，这个代码出现在main中，当前线程就是主线程

获取线程对象的名字
- String name = 线程对象.getName();

修改线程对象的名字
- 线程对象.setName("线程名字");

当线程没有设置名字的时候，默认的名字有什么规律？main/Thread-0/Thread-1/Thread-2/Thread-3/.....

### 睡眠与终止

#### sleep

关于线程的sleep方法： static void sleep(long millis)

1、静态方法：Thread.sleep(1000);
2、参数是毫秒
3、作用：让当前线程进入休眠，进入“阻塞状态”，放弃占有CPU时间片，让给其它线程使用。
4、Thread.sleep()方法，可以做到这种效果：间隔特定的时间，去执行一段特定的代码，每隔多久执行一次。

```java
public class ThreadTest06 {
    public static void main(String[] args) {

        for(int i = 0; i < 10; i++){
            System.out.println(Thread.currentThread().getName() + "--->" + i);

            // 睡眠1秒
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

sleep睡眠太久了，如果希望半道上醒来，你应该怎么办？也就是说怎么叫醒一个正在睡眠的线程？？
注意：这个不是终断线程的执行，是终止线程的睡眠。

```java
public class ThreadTest08 {
    public static void main(String[] args) {
        Thread t = new Thread(new MyRunnable2());
        t.setName("t");
        t.start();

        // 希望5秒之后，t线程醒来（5秒之后主线程手里的活儿干完了。）
        try {
            Thread.sleep(1000 * 5);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // 终断t线程的睡眠（这种终断睡眠的方式依靠了java的异常处理机制。）
        // 所以线程中必须对异常进行捕捉
        t.interrupt(); // 干扰，一盆冷水过去！
    }
}
```

#### 终止

不建议使用：线程名称.stop();  已过时，不建议使用，容易丢失数据！

合理方式：

打标记/改标记。

```java
public class ThreadTest10 {
    public static void main(String[] args) {
        MyRunable4 r = new MyRunable4();
        Thread t = new Thread(r);
        t.setName("t");
        t.start();

        // 模拟5秒
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // 终止线程
        // 你想要什么时候终止t的执行，那么你把标记修改为false，就结束了。
        r.run = false;
    }
}

class MyRunable4 implements Runnable {
    // 打一个布尔标记
    boolean run = true;
    @Override
    public void run() {
        for (int i = 0; i < 10; i++){
            if(run){
                System.out.println(Thread.currentThread().getName() + "--->" + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }else{
                // return就结束了，你在结束之前还有什么没保存的。
                // 在这里可以保存。
                //save....
                //终止当前线程
                return;
            }
        }
    }
}
```

### 调度/优先级/让位/合并

常见的线程调度模型有哪些？

- 抢占式调度模型：那个线程的优先级比较高，抢到的CPU时间片的概率就高一些/多一些。java采用的就是抢占式调度模型。
- 均分式调度模型：平均分配CPU时间片。每个线程占有的CPU时间片时间长度一样。平均分配，一切平等。有一些编程语言，线程调度模型采用的是这种方式。

#### 优先级：

实例方法：

- void setPriority(int newPriority) 设置线程的优先级
- int getPriority() 获取线程优先级
- 最低优先级1
- 默认优先级是5
- 最高优先级10
- 优先级比较高的获取CPU时间片可能会多一些。（但也不完全是，大概率是多的。）

main线程的默认优先级是：5

- 优先级较高的，只是抢到的CPU时间片相对多一些。
- 大概率方向更偏向于优先级比较高的。

#### 让位

静态方法：
- static void yield()  让位方法
- Thread.yield(); 让位，当前线程暂停，回到就绪状态，让给其它线程。
- 暂停当前正在执行的线程对象，并执行其他线程
- yield()方法不是阻塞方法。让当前线程让位，让给其它线程使用。yield()方法的执行会让当前线程从“运行状态”回到“就绪状态”。注意：在回到就绪之后，有可能还会再次抢到。

#### 合并

```java
public class ThreadTest13 {
    public static void main(String[] args) {
        System.out.println("main begin");
        Thread t = new Thread(new MyRunnable7());
        t.setName("t");
        t.start();
        //合并线程
        try {
            t.join(); // t合并到当前线程中，当前线程受阻塞，t线程执行直到结束。
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("main over");
    }
}

class MyRunnable7 implements Runnable {

    @Override
    public void run() {
        for(int i = 0; i < 10000; i++){
            System.out.println(Thread.currentThread().getName() + "--->" + i);
        }
    }
}
```

### synchronized

#### 线程安全

为什么这个是重点？
- 以后在开发中，我们的项目都是运行在服务器当中，而服务器已经将线程的定义，线程对象的创建，线程的启动等，都已经实现完了。这些代码我们都不需要编写。

最重要的是
- 你要知道，你编写的程序需要放到一个多线程的环境下运行，你更需要关注的是这些数据在多线程并发的环境下是否是安全的。（重点）

什么时候数据在多线程并发的环境下会存在安全问题呢？

- 条件1：多线程并发。
- 条件2：有共享数据。
- 条件3：共享数据有修改的行为。
- 满足以上3个条件之后，就会存在线程安全问题。


当多线程并发的环境下，有共享数据，并且这个数据还会被修改，此时就存在线程安全问题，怎么解决这个问题？
- 线程排队执行。（不能并发）。
- 用排队执行解决线程安全问题。
- 这种机制被称为：线程同步机制。
- 专业术语叫做：线程同步，实际上就是线程不能并发了，线程必须排队执行。

怎么解决线程安全问题？ 使用“线程同步机制”。

线程同步就是线程排队了，线程排队了就会牺牲一部分效率，没办法，数据安全第一位，只有数据安全了，我们才可以谈效率。数据不安全，没有效率的事儿。

说到线程同步这块，涉及到这两个专业术语：

- 异步编程模型：
	- 线程t1和线程t2，各自执行各自的，t1不管t2，t2不管t1，谁也不需要等谁，这种编程模型叫做：异步编程模型。其实就是：多线程并发（效率较高。）
	- 异步就是并发。

- 同步编程模型：
	- 线程t1和线程t2，在线程t1执行的时候，必须等待t2线程执行结束，或者说在t2线程执行的时候，必须等待t1线程执行结束，两个线程之间发生了等待关系，这就是同步编程模型。
效率较低。线程排队执行。
	- 同步就是排队。


实例变量：在堆中。
静态变量：在方法区。
局部变量：在栈中。

以上三大变量中：
局部变量永远都不会存在线程安全问题。因为局部变量不共享。（一个线程一个栈。）局部变量在栈中。所以局部变量永远都不会共享。

实例变量在堆中，堆只有1个。静态变量在方法区中，方法区只有1个。堆和方法区都是多线程共享的，所以可能存在线程安全问题。

局部变量+常量：不会有线程安全问题。
成员变量：可能会有线程安全问题。

如果使用局部变量的话：建议使用：StringBuilder。因为局部变量不存在线程安全问题。选择StringBuilder。StringBuffer效率比较低。

- ArrayList是非线程安全的。
- Vector是线程安全的。
- HashMap HashSet是非线程安全的。
- Hashtable是线程安全的。

#### 银行取钱模拟

存在问题的：

```java
public class Test{
    public static void main(String[] args) {
        //创建账户对象，只建一个
        Account act = new Account("act-001", 10000);
        //创建两个线程
        Thread t1 = new AccountThread(act);
        Thread t2 = new AccountThread(act);
        //设置name
        t1.setName("t1");
        t2.setName("t2");
        //启动线程取款
        t1.start();
        t2.start();
    }
}

class Account {
    private String actno; //账号
    private double balance; //余额

    public Account(String actno, double balance) {
        this.actno = actno;
        this.balance = balance;
    }

    public String getActno() {
        return actno;
    }

    public void setActno(String actno) {
        this.actno = actno;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void withdraw(double money){
        //取款之前的余额
        double before = this.getBalance();
        //取款之后的余额
        double after = before - money;

        // 在这里模拟一下网络延迟，一定会出问题-》两次的余额都是 5000
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        //更新余额
        //t1执行到了这里，但是还没有来得及只从这行代码，t2线程进来withdraw方法了，此时一定出问题
        this.setBalance(after);
    }
}

class AccountThread extends Thread{
    //两个线程必须共享同一个账户对象
    private Account act;
    //通过构造方法传递过来账户对象
    public AccountThread(Account act){
        this.act = act;
    }
    //run 方法的执行标识取款操作
    public void run(){
        //取5000
        double money = 5000;
        act.withdraw(money);
        System.out.println( Thread.currentThread().getName() + "账户" + act.getActno() + "取款" + money + "成功， 余额为" + act.getBalance());
    }
}
```

使用了线程同步机制解决问题：

```java
public class Test{
    public static void main(String[] args) {
        //创建账户对象，只建一个
        Account act = new Account("act-001", 10000);
        //创建两个线程
        Thread t1 = new AccountThread(act);
        Thread t2 = new AccountThread(act);
        //设置name
        t1.setName("t1");
        t2.setName("t2");
        //启动线程取款
        t1.start();
        t2.start();
    }
}

class Account {
    private String actno; //账号
    private double balance; //余额

    public Account(String actno, double balance) {
        this.actno = actno;
        this.balance = balance;
    }

    public String getActno() {
        return actno;
    }

    public void setActno(String actno) {
        this.actno = actno;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void withdraw(double money){
        //以下这几行代码必须时县城排队的，不能并发
        //一个线程把这里的代码全部执行结束之后，另一个线程才能进来
        /*
        线程同步机制的语法：
        synchronized () {
            //线程同步代码块
        }
        synchronized 后面小括号中的数据时相当关键的，这个数据必须是多线程共享的数据才能达到多线程排队。
        ()中写什么，要看你想让哪些线程同步
            假设t1、t2、t3、t4、t5，有5个线程，你只希望t1 t2 t3排队，t4 t5不需要排队。怎么办？你一定要在()中写一个t1 t2 t3共享的对象。而这个对象对于t4 t5来说不是共享的。

            这里的共享对象是：账户对象。
            账户对象是共享的，那么this就是账户对象吧！！！
            不一定是this，这里只要是多线程共享的那个对象就行。

            在java语言中，任何一个对象都有“一把锁”，其实这把锁就是标记。（只是把它叫做锁。）
            100个对象，100把锁。1个对象1把锁。

            以下代码的执行原理？
                1、假设t1和t2线程并发，开始执行以下代码的时候，肯定有一个先一个后。
                2、假设t1先执行了，遇到了synchronized，这个时候自动找“后面共享对象”的对象锁，
                找到之后，并占有这把锁，然后执行同步代码块中的程序，在程序执行过程中一直都是
                占有这把锁的。直到同步代码块代码结束，这把锁才会释放。
                3、假设t1已经占有这把锁，此时t2也遇到synchronized关键字，也会去占有后面
                共享对象的这把锁，结果这把锁被t1占有，t2只能在同步代码块外面等待t1的结束，
                直到t1把同步代码块执行结束了，t1会归还这把锁，此时t2终于等到这把锁，然后
                t2占有这把锁之后，进入同步代码块执行程序。

                这样就达到了线程排队执行。
                这里需要注意的是：这个共享对象一定要选好了。这个共享对象一定是你需要排队执行的这些线程对象所共享的。

         */
        //synchronized (this){ //正确
        //synchronized (obj) { // 实例变量，只有一个，正确
        //synchronized ("abc") { // "abc"在字符串常量池当中。->所有线程都会同步，所以不行
        //synchronized (null) { // 报错：空指针。
        //synchronized (obj2) { // 这样编写就不安全了。因为obj2不是共享对象。是局部变量，不对

        synchronized (this) {
            double before = this.getBalance();
            double after = before - money;
            try { //模拟网络延迟
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        //更新余额
        //t1执行到了这里，但是还没有来得及只从这行代码，t2线程进来withdraw方法了，此时一定出问题
        this.setBalance(after);
        }
    }
}

class AccountThread extends Thread{
    //两个线程必须共享同一个账户对象
    private Account act;
    //通过构造方法传递过来账户对象
    public AccountThread(Account act){
        this.act = act;
    }
    //run 方法的执行标识取款操作
    public void run(){
        //取5000
        double money = 5000;
        act.withdraw(money);
        System.out.println( Thread.currentThread().getName() + "账户" + act.getActno() + "取款" + money + "成功， 余额为" + act.getBalance());
    }
}
```

- synchronized可以写在实例方法上，如果出现在实例方法上，一定锁的是this，不能有其他对象了，不灵活
- 另外还有一个缺点：它出现在实例方法上的时候表示整个方法体都要同步，可能会无故扩大同步的范围，导致程序的执行效率变低，所以这种方式不常用。
- 写在实例方法上有什么优点：代码下的少了，节俭了。
- 如果共享的对象就是this，并且需要同步的代码块是整个方法体，建议使用这种方式。
- 同步代码块越小，效率越高
- 第一种：同步代码块 灵活 synchronized(线程共享对象){同步代码块;}
- 第二种：在实例方法上使用synchronized表示共享对象一定是this并且同步代码块是整个方法体。
- 第三种：在静态方法上使用synchronized表示找类锁。类锁永远只有1把。就算创建了100个对象，那类锁也只有一把。
- 对象锁：1个对象1把锁，100个对象100把锁。类锁：100个对象，也可能只是1把类锁。


#### 面试题

##### 一

面试题：doOther方法执行的时候需要等待doSome方法的结束吗？

```java
public class Exam01 {
    public static void main(String[] args) throws InterruptedException {
        MyClass mc = new MyClass();

        Thread t1 = new MyThread(mc);
        Thread t2 = new MyThread(mc);

        t1.setName("t1");
        t2.setName("t2");

        t1.start();
        Thread.sleep(1000); //这个睡眠的作用是：为了保证t1线程先执行。
        t2.start();
    }
}

class MyThread extends Thread {
    private MyClass mc;
    public MyThread(MyClass mc){
        this.mc = mc;
    }
    public void run(){
        if(Thread.currentThread().getName().equals("t1")){
            mc.doSome();
        }
        if(Thread.currentThread().getName().equals("t2")){
            mc.doOther();
        }
    }
}

class MyClass {
    public synchronized void doSome(){
        System.out.println("doSome begin");
        try {
            Thread.sleep(1000 * 10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("doSome over");
    }
    public void doOther(){
        System.out.println("doOther begin");
        System.out.println("doOther over");
    }
}

```

不需要，因为doOther()方法没有synchronized

##### 二

面试题：doOther方法执行的时候需要等待doSome方法的结束吗？

```java
public class Exam01 {
    public static void main(String[] args) throws InterruptedException {
        MyClass mc = new MyClass();

        Thread t1 = new MyThread(mc);
        Thread t2 = new MyThread(mc);

        t1.setName("t1");
        t2.setName("t2");

        t1.start();
        Thread.sleep(1000); //这个睡眠的作用是：为了保证t1线程先执行。
        t2.start();
    }
}

class MyThread extends Thread {
    private MyClass mc;
    public MyThread(MyClass mc){
        this.mc = mc;
    }
    public void run(){
        if(Thread.currentThread().getName().equals("t1")){
            mc.doSome();
        }
        if(Thread.currentThread().getName().equals("t2")){
            mc.doOther();
        }
    }
}

class MyClass {
    public synchronized void doSome(){
        System.out.println("doSome begin");
        try {
            Thread.sleep(1000 * 10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("doSome over");
    }
    public synchronized void doOther(){
        System.out.println("doOther begin");
        System.out.println("doOther over");
    }
}

```

需要，因为doOther()方法有synchronized了

##### 三

面试题：doOther方法执行的时候需要等待doSome方法的结束吗？

```java
public class Exam01 {
    public static void main(String[] args) throws InterruptedException {
        MyClass mc1 = new MyClass();
        MyClass mc2 = new MyClass();

        Thread t1 = new MyThread(mc1);
        Thread t2 = new MyThread(mc2);

        t1.setName("t1");
        t2.setName("t2");

        t1.start();
        Thread.sleep(1000); //这个睡眠的作用是：为了保证t1线程先执行。
        t2.start();
    }
}

class MyThread extends Thread {
    private MyClass mc;
    public MyThread(MyClass mc){
        this.mc = mc;
    }
    public void run(){
        if(Thread.currentThread().getName().equals("t1")){
            mc.doSome();
        }
        if(Thread.currentThread().getName().equals("t2")){
            mc.doOther();
        }
    }
}

class MyClass {
    public synchronized void doSome(){
        System.out.println("doSome begin");
        try {
            Thread.sleep(1000 * 10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("doSome over");
    }
    public synchronized void doOther(){
        System.out.println("doOther begin");
        System.out.println("doOther over");
    }
}
```

不需要，因为MyClass对象是两个，两把锁。

##### 四

面试题：doOther方法执行的时候需要等待doSome方法的结束吗？

```java
public class Exam01 {
    public static void main(String[] args) throws InterruptedException {
        MyClass mc1 = new MyClass();
        MyClass mc2 = new MyClass();

        Thread t1 = new MyThread(mc1);
        Thread t2 = new MyThread(mc2);

        t1.setName("t1");
        t2.setName("t2");

        t1.start();
        Thread.sleep(1000); //这个睡眠的作用是：为了保证t1线程先执行。
        t2.start();
    }
}

class MyThread extends Thread {
    private MyClass mc;
    public MyThread(MyClass mc){
        this.mc = mc;
    }
    public void run(){
        if(Thread.currentThread().getName().equals("t1")){
            mc.doSome();
        }
        if(Thread.currentThread().getName().equals("t2")){
            mc.doOther();
        }
    }
}

class MyClass {
    public synchronized static void doSome(){
        System.out.println("doSome begin");
        try {
            Thread.sleep(1000 * 10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("doSome over");
    }
    public synchronized static void doOther(){
        System.out.println("doOther begin");
        System.out.println("doOther over");
    }
}
```
synchronized出现在静态方法上是找类锁。

需要，因为静态方法是类锁，不管创建了几个对象，类锁只有1把。

#### 死锁


死锁代码要会写。
一般面试官要求你会写。
只有会写的，才会在以后的开发中注意这个事儿。
因为死锁很难调试。

```java

public class DeadLock {
    public static void main(String[] args) {
        Object o1 = new Object();
        Object o2 = new Object();

        // t1和t2两个线程共享o1,o2
        Thread t1 = new MyThread1(o1,o2);
        Thread t2 = new MyThread2(o1,o2);

        t1.start();
        t2.start();
    }
}

class MyThread1 extends Thread{
    Object o1;
    Object o2;
    public MyThread1(Object o1,Object o2){
        this.o1 = o1;
        this.o2 = o2;
    }
    public void run(){
        synchronized (o1){
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            synchronized (o2){

            }
        }
    }
}

class MyThread2 extends Thread {
    Object o1;
    Object o2;
    public MyThread2(Object o1,Object o2){
        this.o1 = o1;
        this.o2 = o2;
    }
    public void run(){
        synchronized (o2){
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            synchronized (o1){

            }
        }
    }
}
```

synchronized 在开发过程中最好不要嵌套使用


#### 怎么解决线程安全问题

是一上来就选择线程同步吗？synchronized
不是，synchronized会让程序的执行效率降低，用户体验不好。系统的用户吞吐量降低。用户体验差。在不得已的情况下再选择线程同步机制。

第一种方案：尽量使用局部变量代替“实例变量和静态变量”。

第二种方案：如果必须是实例变量，那么可以考虑创建多个对象，这样实例变量的内存就不共享了。（一个线程对应1个对象，100个线程对应100个对象，对象不共享，就没有数据安全问题了。）

第三种方案：如果不能使用局部变量，对象也不能创建多个，这个时候就只能选择synchronized了。线程同步机制。


### 守护线程/定时器

#### 守护线程

java语言中线程分为两大类：
一类是：用户线程
一类是：守护线程（后台线程）
其中具有代表性的就是：垃圾回收线程（守护线程）。

守护线程的特点：
一般守护线程是一个死循环，所有的用户线程只要结束，守护线程自动结束。

注意：主线程main方法是一个用户线程。

守护线程用在什么地方呢？
每天00:00的时候系统数据自动备份。这个需要使用到定时器，并且我们可以将定时器设置为守护线程。一直在那里看着，每到00:00的时候就备份一次。所有的用户线程如果结束了，守护线程自动退出，没有必要进行数据备份了。

设置为守护线程 t.setDaemon(true);

```java
public class ThreadTest14 {
    public static void main(String[] args) {
        Thread t = new BakDataThread();
        t.setName("备份数据的线程");

        // 启动线程之前，将线程设置为守护线程
        t.setDaemon(true);
        t.start();

        // 主线程：主线程是用户线程
        for(int i = 0; i < 10; i++){
            System.out.println(Thread.currentThread().getName() + "--->" + i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class BakDataThread extends Thread {
    public void run(){
        int i = 0;
        // 即使是死循环，但由于该线程是守护者，当用户线程结束，守护线程自动终止。
        while(true){
            System.out.println(Thread.currentThread().getName() + "--->" + (++i));
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

#### 定时器

定时器的作用：间隔特定的时间，执行特定的程序。

每周要进行银行账户的总账操作。每天要进行数据的备份操作。

在实际的开发中，每隔多久执行一段特定的程序，这种需求是很常见的，那么在java中其实可以采用多种方式实现：可以使用sleep方法，睡眠，设置睡眠时间，没到这个时间点醒来，执行任务。这种方式是最原始的定时器。（比较low）

在java的类库中已经写好了一个定时器：java.util.Timer，可以直接拿来用。不过，这种方式在目前的开发中也很少用，因为现在有很多高级框架都是支持定时任务的。

在实际的开发中，目前使用较多的是Spring框架中提供的SpringTask框架，这个框架只要进行简单的配置，就可以完成定时器的任务。

```java
/*
使用定时器指定定时任务。
 */
public class TimerTest {
    public static void main(String[] args) throws Exception {

        // 创建定时器对象
        Timer timer = new Timer();
        //Timer timer = new Timer(true); //守护线程的方式

        // 指定定时任务
        //timer.schedule(定时任务, 第一次执行时间, 间隔多久执行一次);
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date firstTime = sdf.parse("2020-03-14 09:34:30");
        //timer.schedule(new LogTimerTask() , firstTime, 1000 * 10);
        // 每年执行一次。
        //timer.schedule(new LogTimerTask() , firstTime, 1000 * 60 * 60 * 24 * 365);

        //匿名内部类方式
        timer.schedule(new TimerTask(){
            @Override
            public void run() {
                // code....
            }
        } , firstTime, 1000 * 10);

    }
}

// 编写一个定时任务类
// 假设这是一个记录日志的定时任务
class LogTimerTask extends TimerTask {

    @Override
    public void run() {
        // 编写你需要执行的任务就行了。
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String strTime = sdf.format(new Date());
        System.out.println(strTime + ":成功完成了一次数据备份！");
    }
}
```

### 生产者和消费者模式

关于Object类中的wait和notify方法

- 第一：wait和notify方法不是线程对象的方法，是java中任何一个java对象都有的方法，因为这两个方式是Object类中自带的。wait方法和notify方法不是通过线程对象调用，不是这样的：t.wait()，也不是这样的：t.notify()..不对。
- 第二：wait()方法作用？Object o = new Object();o.wait();
	- 表示：让正在o对象上活动的线程进入等待状态，无期限等待，直到被唤醒为止。o.wait();方法的调用，会让“当前线程（正在o对象上活动的线程）”进入等待状态。
- 第三：notify()方法作用？Object o = new Object(); o.notify();
	+ 表示：唤醒正在o对象上等待的线程。
	+ 还有一个notifyAll()方法：这个方法是唤醒o对象上处于等待的所有线程。

#### 实现

使用wait方法和notify方法实现“生产者和消费者模式”

什么是“生产者和消费者模式”？
- 生产线程负责生产，消费线程负责消费。
- 生产线程和消费线程要达到均衡。
- 这是一种特殊的业务需求，在这种特殊的情况下需要使用wait方法和notify方法。

- wait和notify方法不是线程对象的方法，是普通java对象都有的方法。
- wait方法和notify方法建立在线程同步的基础之上。因为多线程要同时操作一个仓库。有线程安全问题。
- wait方法作用：o.wait()让正在o对象上活动的线程t进入等待状态，并且释放掉t线程之前占有的o对象的锁。
- notify方法作用：o.notify()让正在o对象上等待的线程唤醒，只是通知，不会释放o对象上之前占有的锁。


模拟这样一个需求：

- 仓库我们采用List集合。List集合中假设只能存储1个元素。1个元素就表示仓库满了。如果List集合中元素个数是0，就表示仓库空了。保证List集合中永远都是最多存储1个元素。必须做到这种效果：生产1个消费1个。

```java
public class ThreadTest16 {
    public static void main(String[] args) {
        // 创建1个仓库对象，共享的。
        List list = new ArrayList();
        // 创建两个线程对象
        // 生产者线程
        Thread t1 = new Thread(new Producer(list));
        // 消费者线程
        Thread t2 = new Thread(new Consumer(list));

        t1.setName("生产者线程");
        t2.setName("消费者线程");

        t1.start();
        t2.start();
    }
}

// 生产线程
class Producer implements Runnable {
    // 仓库
    private List list;

    public Producer(List list) {
        this.list = list;
    }
    @Override
    public void run() {
        // 一直生产（使用死循环来模拟一直生产）
        while(true){
            // 给仓库对象list加锁。
            synchronized (list){
                if(list.size() > 0){ // 大于0，说明仓库中已经有1个元素了。
                    try {
                        // 当前线程进入等待状态，并且释放Producer之前占有的list集合的锁。
                        list.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                // 程序能够执行到这里说明仓库是空的，可以生产
                Object obj = new Object();
                list.add(obj);
                System.out.println(Thread.currentThread().getName() + "--->" + obj);
                // 唤醒消费者进行消费
                list.notifyAll();
            }
        }
    }
}

// 消费线程
class Consumer implements Runnable {
    // 仓库
    private List list;

    public Consumer(List list) {
        this.list = list;
    }

    @Override
    public void run() {
        // 一直消费
        while(true){
            synchronized (list) {
                if(list.size() == 0){
                    try {
                        // 仓库已经空了。
                        // 消费者线程等待，释放掉list集合的锁
                        list.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                // 程序能够执行到此处说明仓库中有数据，进行消费。
                Object obj = list.remove(0);
                System.out.println(Thread.currentThread().getName() + "--->" + obj);
                // 唤醒生产者生产。
                list.notifyAll();
            }
        }
    }
}
```




### 面试题

#### sleep

```java
/*
关于Thread.sleep()方法的一个面试题：
 */
public class ThreadTest07 {
    public static void main(String[] args) {
        // 创建线程对象
        Thread t = new MyThread3();
        t.setName("t");
        t.start();

        // 调用sleep方法
        try {
            // 问题：这行代码会让线程t进入休眠状态吗？
            t.sleep(1000 * 5);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // 5秒之后这里才会执行。
        System.out.println("hello World!");
    }
}

class MyThread3 extends Thread {
    public void run(){
        for(int i = 0; i < 10000; i++){
            System.out.println(Thread.currentThread().getName() + "--->" + i);
        }
    }
}

```
答案：

- 在执行的时候还是会转换成：Thread.sleep(1000 * 5);
- 这行代码的作用是：让当前线程进入休眠，也就是说main线程进入休眠。
- 这样代码出现在main方法中，main线程睡眠。

## 反射机制

反射机制（比较简单，因为只要会查帮助文档，就可以了。）

反射机制有什么用？
- 通过java语言中的反射机制可以操作字节码文件。
- 类似于黑客。（可以读和修改字节码文件。）
- 通过反射机制可以操作代码片段。（class文件。）

- java.lang.reflect.*;

反射机制相关的重要的类有哪些？

- java.lang.Class：代表整个字节码，代表一个类型，代表整个类。
- java.lang.reflect.Method：代表字节码中的方法字节码。代表类中的方法。
- java.lang.reflect.Constructor：代表字节码中的构造方法字节码。代表类中的构造方法
- java.lang.reflect.Field：代表字节码中的属性字节码。代表类中的成员变量（静态变量+实例变量）。

### 获取一个类的字节码

三种方式

- 第一种：Class c = Class.forName("完整类名带包名");
- 第二种：Class c = 对象.getClass();
- 第三种：Class c = 任何类型.class;

```java
public class ReflectTest01 {
    public static void main(String[] args) {
        /*
        Class.forName()
            1、静态方法
            2、方法的参数是一个字符串。
            3、字符串需要的是一个完整类名。
            4、完整类名必须带有包名。java.lang包也不能省略。
         */
        Class c1 = null;
        Class c2 = null;
        try {
            c1 = Class.forName("java.lang.String"); // c1代表String.class文件，或者说c1代表String类型。
            c2 = Class.forName("java.util.Date"); // c2代表Date类型
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        //第二种方式 java中任何一个对象都有一个方法：getClass()
        String s = "abc";
        Class x = s.getClass(); // x代表String.class字节码文件，x代表String类型。

        // 第三种方式，java语言中任何一种类型，包括基本数据类型，它都有.class属性。
        Class z = String.class; // z代表String类型
        Class e = double.class; // e代表double类型
    }
}
```







3、关于JDK中自带的类加载器：（聊一聊，不需要掌握，知道当然最好！）
3.1、什么是类加载器？
专门负责加载类的命令/工具。
ClassLoader

3.2、JDK中自带了3个类加载器
启动类加载器:rt.jar
扩展类加载器:ext/*.jar
应用类加载器:classpath

3.3、假设有这样一段代码：
String s = "abc";

代码在开始执行之前，会将所需要类全部加载到JVM当中。
通过类加载器加载，看到以上代码类加载器会找String.class
文件，找到就加载，那么是怎么进行加载的呢？

首先通过“启动类加载器”加载。
注意：启动类加载器专门加载：C:\Program Files\Java\jdk1.8.0_101\jre\lib\rt.jar
rt.jar中都是JDK最核心的类库。

如果通过“启动类加载器”加载不到的时候，
会通过"扩展类加载器"加载。
注意：扩展类加载器专门加载：C:\Program Files\Java\jdk1.8.0_101\jre\lib\ext\*.jar


如果“扩展类加载器”没有加载到，那么
会通过“应用类加载器”加载。
注意：应用类加载器专门加载：classpath中的类。

3.4、java中为了保证类加载的安全，使用了双亲委派机制。
优先从启动类加载器中加载，这个称为“父”
“父”无法加载到，再从扩展类加载器中加载，
这个称为“母”。双亲委派。如果都加载不到，
才会考虑从应用类加载器中加载。直到加载
到为止。

1、回顾反射机制

1.1、什么是反射机制？反射机制有什么用？
反射机制：可以操作字节码文件
作用：可以让程序更加灵活。

1.2、反射机制相关的类在哪个包下？
java.lang.reflect.*;

1.3、反射机制相关的主要的类？
java.lang.Class
java.lang.reflect.Method;
java.lang.reflect.Constructor;
java.lang.reflect.Field;

1.4、在java中获取Class的三种方式？
第一种：
Class c = Class.forName("完整类名");
第二种：
Class c = 对象.getClass();
第三种：
Class c = int.class;
Class c = String.class;

1.5、获取了Class之后，可以调用无参数构造方法来实例化对象

//c代表的就是日期Date类型
Class c = Class.forName("java.util.Date");

//实例化一个Date日期类型的对象
Object obj = c.newInstance();

一定要注意：
newInstance()底层调用的是该类型的无参数构造方法。
如果没有这个无参数构造方法会出现"实例化"异常。

1.6、如果你只想让一个类的“静态代码块”执行的话，你可以怎么做？
Class.forName("该类的类名");
这样类就加载，类加载的时候，静态代码块执行！！！！
在这里，对该方法的返回值不感兴趣，主要是为了使用“类加载”这个动作。

1.7、关于路径问题？

String path = Thread.currentThread().getContextClassLoader()
  .getResource("写相对路径，但是这个相对路径从src出发开始找").getPath();

String path = Thread.currentThread().getContextClassLoader()
  .getResource("abc").getPath();//必须保证src下有abc文件。

String path = Thread.currentThread().getContextClassLoader()
  .getResource("a/db").getPath();//必须保证src下有a目录，a目录下有db文件。

String path = Thread.currentThread().getContextClassLoader()
  .getResource("com/bjpowernode/test.properties").getPath();
  //必须保证src下有com目录，com目录下有bjpowernode目录。
  //bjpowernode目录下有test.properties文件。

这种方式是为了获取一个文件的绝对路径。（通用方式，不会受到环境移植的影响。）
但是该文件要求放在类路径下，换句话说：也就是放到src下面。
src下是类的根路径。

直接以流的形式返回：
InputStream in = Thread.currentThread().getContextClassLoader()
.getResourceAsStream("com/bjpowernode/test.properties");

1.8、IO + Properties，怎么快速绑定属性资源文件？

//要求：第一这个文件必须在类路径下
//第二这个文件必须是以.properties结尾。
ResourceBundle bundle = ResourceBundle.getBundle("com/bjpowernode/test");
String value = bundle.getString(key);

2、今日反射机制的重点内容
2.1、通过反射机制访问对象的某个属性。
2.2、通过反射机制调用对象的某个方法。
2.3、通过反射机制调用某个构造方法实例化对象。
2.4、通过反射机制获取父类以及父类型接口。

## 注解

Annotation
注解Annotation是一种引用数据类型。编译之后也是生成xxx.class文件。

怎么自定义注解呢？ [修饰符列表] @interface 注解类型名{ }

注解使用时的语法格式是：@注解类型名

注解可以出现在类上、属性上、方法上、变量上等....注解还可以出现在注解类型上。默认情况下，注解可以出现在任意位置。

### 内置注解

#### Override

关于JDK lang包下的Override注解
源代码：public @interface Override {}

- 标识性注解，给编译器做参考的。编译器看到方法上有这个注解的时候，编译器会自动检查该方法是否重写了父类的方法。如果没有重写，报错。
- 这个注解只是在编译阶段起作用，和运行期无关！
- @Override这个注解只能注解方法。
- @Override这个注解是给编译器参考的，和运行阶段没有关系。

凡是java中的方法带有这个注解的，编译器都会进行编译检查，如果这个方法不是重写父类的方法，编译器报错。
Override 表示一个方法声明打算重写超类中的另一个方法声明。

#### Deprecated

作用：告诉其他程序员这个标记的元素已经过时了。

注释的程序元素，不鼓励程序员使用这样的元素，通常是因为它很危险或存在更好的选择。

### 元注解

什么是元注解？用来标注“注解类型”的“注解”，称为元注解。

常见的元注解有哪些？Target/Retention

关于Target注解：这是一个元注解，用来标注“注解类型”的“注解”这个Target注解用来标注“被标注的注解”可以出现在哪些位置上。

@Target(ElementType.METHOD)：表示“被标注的注解”只能出现在方法上。
@Target(value={CONSTRUCTOR, FIELD, LOCAL_VARIABLE, METHOD, PACKAGE, MODULE, PARAMETER, TYPE})
表示该注解可以出现在：构造方法上/字段上/局部变量上/方法上/类上...


关于Retention注解：这是一个元注解，用来标注“注解类型”的“注解”这个Retention注解用来标注“被标注的注解”最终保存在哪里。

@Retention(RetentionPolicy.SOURCE)：表示该注解只被保留在java源文件中。
@Retention(RetentionPolicy.CLASS)：表示该注解被保存在class文件中。
@Retention(RetentionPolicy.RUNTIME)：表示该注解被保存在class文件中，并且可以被反射机制所读取。

### 注解中的属性

```java
public @interface MyAnnotation {
    /**
     * 我们通常在注解当中可以定义属性，以下这个是MyAnnotation的name属性。
     * 看着像1个方法，但实际上我们称之为属性name。
     * @return
     */
    String name();
    String color();
    int age() default 25; //属性指定默认值
}

public class MyAnnotationTest {
    //报错的原因：如果一个注解当中有属性，那么必须给属性赋值。（除非该属性使用default指定了默认值。）
    //@MyAnnotation(属性名=属性值,属性名=属性值,属性名=属性值)
    //指定name属性的值就好了。
    @MyAnnotation(name = "zhangsan", color = "红色")
    public void doSome(){
    }
}
```

```java
/*
如果一个注解的属性的名字是value(其他名字不行)，并且只有一个属性的话，在使用的时候，该属性名可以省略。
 */
public class MyAnnotationTest {

    // 报错原因：没有指定属性的值。
    /*@MyAnnotation
    public void doSome(){
    }*/

    @MyAnnotation(value = "hehe")
    public void doSome(){
    }

    @MyAnnotation("haha")
    public void doOther(){
    }
}
```

```java


```


需求：
假设有这样一个注解，叫做：@Id
这个注解只能出现在类上面，当这个类上有这个注解的时候，
要求这个类中必须有一个int类型的id属性。如果没有这个属性
就报异常。如果有这个属性则正常执行！