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

