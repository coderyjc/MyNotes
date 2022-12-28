

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

