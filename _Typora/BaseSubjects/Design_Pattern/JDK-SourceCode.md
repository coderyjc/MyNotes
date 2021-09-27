## 单例模式

### 4.1.4 JDK源码解析-Runtime类

Runtime类就是使用的单例设计模式。

1. 通过源代码查看使用的是哪儿种单例模式

   ```java
   public class Runtime {    private static Runtime currentRuntime = new Runtime();    /**     * Returns the runtime object associated with the current Java application.     * Most of the methods of class <code>Runtime</code> are instance     * methods and must be invoked with respect to the current runtime object.     *     * @return  the <code>Runtime</code> object associated with the current     *          Java application.     */    public static Runtime getRuntime() {        return currentRuntime;    }    /** Don't let anyone else instantiate this class */    private Runtime() {}    ...}
   ```

   从上面源代码中可以看出Runtime类使用的是恶汉式（静态属性）方式来实现单例模式的。

   

2. 使用Runtime类中的方法

   ```java
   public class RuntimeDemo {    public static void main(String[] args) throws IOException {        //获取Runtime类对象        Runtime runtime = Runtime.getRuntime();        //返回 Java 虚拟机中的内存总量。        System.out.println(runtime.totalMemory());        //返回 Java 虚拟机试图使用的最大内存量。        System.out.println(runtime.maxMemory());        //创建一个新的进程执行指定的字符串命令，返回进程对象        Process process = runtime.exec("ipconfig");        //获取命令执行后的结果，通过输入流获取        InputStream inputStream = process.getInputStream();        byte[] arr = new byte[1024 * 1024* 100];        int b = inputStream.read(arr);        System.out.println(new String(arr,0,b,"gbk"));    }}
   ```

   

## 抽象工厂模式

### 4.2.6 JDK源码解析-Collection.iterator方法

```java
public class Demo {    public static void main(String[] args) {        List<String> list = new ArrayList<>();        list.add("令狐冲");        list.add("风清扬");        list.add("任我行");        //获取迭代器对象        Iterator<String> it = list.iterator();        //使用迭代器遍历        while(it.hasNext()) {            String ele = it.next();            System.out.println(ele);        }    }}
```

对上面的代码大家应该很熟，使用迭代器遍历集合，获取集合中的元素。而单列集合获取迭代器的方法就使用到了工厂方法模式。我们看通过类图看看结构：

<img src="JDK-SourceCode.imgs/JDK源码解析.png" style="zoom:75%;" />

Collection接口是抽象工厂类，ArrayList是具体的工厂类；Iterator接口是抽象商品类，ArrayList类中的Iter内部类是具体的商品类。在具体的工厂类中iterator()方法创建具体的商品类的对象。

> 另：
>
> ​	1,DateForamt类中的getInstance()方法使用的是工厂模式；
>
> ​	2,Calendar类中的getInstance()方法使用的是工厂模式；

