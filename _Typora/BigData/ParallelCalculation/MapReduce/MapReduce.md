# Hadoop-Mapreduce

> 来源 ：[bilibili-黑马程序员-MapReduce](https://www.bilibili.com/video/BV1kp4y1v7KE?)

## 1. MapReduce 介绍

MapReduce思想在生活中处处可见。或多或少都曾接触过这种思想。MapReduce的思想核心是“分而治之”，适用于大量复杂的任务处理场景（大规模数据处理场景）。

* Map负责“分”，即把复杂的任务分解为若干个“简单的任务”来并行处理。可以进行拆分的前提是这些小任务可以并行计算，彼此间几乎没有依赖关系。
* Reduce负责“合”，即对map阶段的结果进行全局汇总。
* MapReduce运行在yarn集群
  1. ResourceManager
  2. NodeManager

这两个阶段合起来正是MapReduce思想的体现。

![1565182220824](R:\GITHUB\MyNotes\_Typora\BigData\ParallelCalculation\MapReduce\MapReduce.imgs\1565182220824.png)

还有一个比较形象的语言解释MapReduce:

我们要数图书馆中的所有书。你数1号书架，我数2号书架。这就是“Map”。我们人越多，数书就更快。

现在我们到一起，把所有人的统计数加在一起。这就是“Reduce”。




### 1.1. MapReduce 设计构思

MapReduce是一个分布式运算程序的编程框架，核心功能是将用户编写的业务逻辑代码和自带默认组件整合成一个完整的分布式运算程序，并发运行在Hadoop集群上。

MapReduce设计并提供了统一的计算框架，为程序员隐藏了绝大多数系统层面的处理细节。为程序员提供一个抽象和高层的编程接口和框架。程序员仅需要关心其应用层的具体计算问题，仅需编写少量的处理应用本身计算问题的程序代码。如何具体完成这个并行计算任务所相关的诸多系统层细节被隐藏起来,交给计算框架去处理：

Map和Reduce为程序员提供了一个清晰的操作接口抽象描述。MapReduce中定义了如下的Map和Reduce两个抽象的编程接口，由用户去编程实现.Map和Reduce,MapReduce处理的数据类型是<key,value>键值对。

* Map: `(k1; v1) → [(k2; v2)]`

* Reduce: `(k2; [v2]) → [(k3; v3)]`


一个完整的mapreduce程序在分布式运行时有三类实例进程：

1. `MRAppMaster` 负责整个程序的过程调度及状态协调
2. `MapTask` 负责map阶段的整个数据处理流程
3. `ReduceTask` 负责reduce阶段的整个数据处理流程

​	![image-20210529214039773](R:\GITHUB\MyNotes\_Typora\BigData\ParallelCalculation\MapReduce\MapReduce.imgs\image-20210529214039773.png)	

## 2. MapReduce 编程规范

> MapReduce 的开发一共有八个步骤, 其中 Map 阶段分为 2 个步骤，Shuffle 阶段 4 个步骤，Reduce 阶段分为 2 个步骤

#####  Map 阶段 2 个步骤

1. 设置 InputFormat 类（决定文件读取方式）, 将数据切分为 Key-Value**(K1和V1)** 对, 输入到第二步
   1. k1 相对于文本的偏移量，v1 这一行的文本数据
2. 自定义 Map 逻辑（继承mapper类）, 将第一步的结果转换成另外的 Key-Value（**K2和V2**） 对, 输出结果

##### Shuffle 阶段 4 个步骤

3. 对输出的 Key-Value 对进行**分区**
4. 对不同分区的数据按照相同的 Key **排序**
5. (可选) 对分组过的数据初步**规约**, 降低数据的网络拷贝
6. 对数据进行**分组**, 相同 Key 的 Value 放入一个集合中

##### Reduce 阶段 2 个步骤

7. 对多个 Map 任务的结果进行排序以及合并, 编写 Reduce 函数实现自己的逻辑, 对输入的 Key-Value 进行处理, 转为新的 Key-Value（**K3和V3**）输出
8. 设置 OutputFormat 处理并保存 Reduce 输出的 Key-Value 数据

![image-20210529214216738](R:\GITHUB\MyNotes\_Typora\BigData\ParallelCalculation\MapReduce\MapReduce.imgs\image-20210529214216738.png)

![image-20210529214231869](R:\GITHUB\MyNotes\_Typora\BigData\ParallelCalculation\MapReduce\MapReduce.imgs\image-20210529214231869.png)

## 3. WordCount

> 需求: 在一堆给定的文本文件中统计输出每一个单词出现的总次数

##### Step 1. 数据格式准备

1. 创建一个新的文件

  ```shell
cd /export/servers
vim wordcount.txt
  ```

2. 向其中放入以下内容并保存

  ```text
hello,world,hadoop
hive,sqoop,flume,hello
kitty,tom,jerry,world
hadoop
  ```

3. 上传到 HDFS

  ```shell
hdfs dfs -mkdir /wordcount/
hdfs dfs -put wordcount.txt /wordcount/
  ```

##### Step 2. Mapper

```java
public class WordCountMapper extends Mapper<LongWritable,Text,Text,LongWritable> {
    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] split = line.split(",");
        for (String word : split) {
            context.write(new Text(word),new LongWritable(1));
        }
    }
}
```

##### Step 3. Reducer

```java
public class WordCountReducer extends Reducer<Text,LongWritable,Text,LongWritable> {
    /**
     * 自定义我们的reduce逻辑
     * 所有的key都是我们的单词，所有的values都是我们单词出现的次数
     * @param key
     * @param values
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
        long count = 0;
        for (LongWritable value : values) {
            count += value.get();
        }
        context.write(key,new LongWritable(count));
    }
}
```

##### Step 4. 定义主类, 描述 Job 并提交 Job

```java
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] args) throws Exception {
        Job job = Job.getInstance(super.getConf(), JobMain.class.getSimpleName());
        //打包到集群上面运行时候，必须要添加以下配置，指定程序的main函数
        job.setJarByClass(JobMain.class);
        //第一步：读取输入文件解析成key，value对
        //输入的文件夹应该存在，并且他会读取目标文件夹内的所有文件
        job.setInputFormatClass(TextInputFormat.class);
        TextInputFormat.addInputPath(job,new Path("hdfs://192.168.52.250:8020/wordcount"));

        //第二步：设置我们的mapper类
        job.setMapperClass(WordCountMapper.class);
        //设置我们map阶段完成之后的输出类型
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);
        //第三步，第四步，第五步，第六步，省略
        //第七步：设置我们的reduce类
        job.setReducerClass(WordCountReducer.class);
        //设置我们reduce阶段完成之后的输出类型
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);
        //第八步：设置输出类以及输出路径
        //输出的目标文件夹不用我们自己建立，不能存在，存在会报错
        //这时候我们库用加一步判断
        job.setOutputFormatClass(TextOutputFormat.class);
        //设置输出路径
        Path path = new Path("hdfs://输出路径");
        TextOutputFormat.setOutputPath(job, path);
        // 获取FileSystem
        FileSystem fileSystem = FileSystem.get(new URI("hdfs://输出路径"), super.getConf());
        // 如果存在就删除
        boolean bl = fileSystem.exists(path);
        if(bl){
            fileSystem.delete(path, true);
        }
        boolean b = job.waitForCompletion(true);
        return b?0:1;
    }

    /**
     * 程序main函数的入口类
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        Tool tool  =  new JobMain();
        int run = ToolRunner.run(configuration, tool, args);
        System.exit(run);
    }
}
```

##### 常见错误

如果遇到如下错误

```text
Caused by: org.apache.hadoop.ipc.RemoteException(org.apache.hadoop.security.AccessControlException): Permission denied: user=admin, access=WRITE, inode="/":root:supergroup:drwxr-xr-x
```

直接将hdfs-site.xml当中的权限关闭即可

```xml
<property>
  <name>dfs.permissions</name>
  <value>false</value>
</property>
```

最后重启一下 HDFS 集群

##### 小细节

本地运行完成之后，就可以打成jar包放到服务器上面去运行了，实际工作当中，都是将代码打成jar包，开发main方法作为程序的入口，然后放到集群上面去运行

## 4. MapReduce 运行模式

##### 本地运行模式

1. MapReduce 程序是被提交给 LocalJobRunner 在本地以单进程的形式运行
2. 处理的数据及输出结果可以在本地文件系统, 也可以在hdfs上
3. 怎样实现本地运行? 写一个程序, 不要带集群的配置文件, 本质是程序的 `conf` 中是否有 `mapreduce.framework.name=local` 以及 `yarn.resourcemanager.hostname=local` 参数
4. 本地模式非常便于进行业务逻辑的 `Debug`, 只要在 `Eclipse` 中打断点即可

```java
configuration.set("mapreduce.framework.name","local");
configuration.set(" yarn.resourcemanager.hostname","local");
TextInputFormat.addInputPath(job,new Path("file:///F:\\传智播客大数据离线阶段课程资料\\3、大数据离线第三天\\wordcount\\input"));
TextOutputFormat.setOutputPath(job,new Path("file:///F:\\传智播客大数据离线阶段课程资料\\3、大数据离线第三天\\wordcount\\output"));
```

##### 集群运行模式

1. 将 MapReduce 程序提交给 Yarn 集群, 分发到很多的节点上并发执行
2. 处理的数据和输出结果应该位于 HDFS 文件系统
3. 提交集群的实现步骤: 将程序打成JAR包，然后在集群的任意一个节点上用hadoop命令启动
4. hadoop jar jar包的名称 主类的全路径名

```shell
hadoop jar hadoop_hdfs_operate-1.0-SNAPSHOT.jar cn.itcast.hdfs.demo1.JobMain
```

## 5. MapReduce 分区

在 MapReduce 中, 通过我们指定分区, 会**将同一个分区的数据发送到同一个 Reduce 当中进行处理**

例如: 为了数据的统计, 可以把一批类似的数据发送到同一个 Reduce 当中, 在同一个 Reduce 当中统计相同类型的数据, 就可以实现类似的数据分区和统计等

其实就是相同类型的数据, 有共性的数据, 送到一起去处理

Reduce 当中默认的分区只有一个

![1565182340140](R:\GITHUB\MyNotes\_Typora\BigData\ParallelCalculation\MapReduce\MapReduce.imgs\1565182340140.png)	

##### Step 1. 定义 Mapper

这个 Mapper 程序不做任何逻辑, 也不对 Key-Value 做任何改变, 只是接收数据, 然后往下发送

```java
public class MyMapper extends Mapper<LongWritable,Text,Text,NullWritable>{
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        context.write(value,NullWritable.get());
    }
}
```

##### Step 2. 定义 Reducer 逻辑

这个 Reducer 也不做任何处理, 将数据原封不动的输出即可

```java
public class MyReducer extends Reducer<Text,NullWritable,Text,NullWritable> {
    @Override
    protected void reduce(Text key, Iterable<NullWritable> values, Context context) throws IOException, InterruptedException {
        context.write(key,NullWritable.get());
    }
}
```

##### Step 3. 自定义 Partitioner

主要的逻辑就在这里, 这也是这个案例的意义, 通过 Partitioner 将数据分发给不同的 Reducer

```java
public class PartitonerOwn extends Partitioner<Text,LongWritable> {
    @Override
    public int getPartition(Text text, LongWritable longWritable, int i) {
        if(text.toString().length() >= 5 ){
            return  0;
        }else{
            return 1;
        }
    }
}
```

##### Step 4. Main 入口

```java

public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] args) throws Exception {
        //1:创建job任务对象
        Job job = Job.getInstance(super.getConf(), "partition_maperduce");

        //2:对job任务进行配置(八个步骤)
            //第一步:设置输入类和输入的路径
            job.setInputFormatClass(TextInputFormat.class);
            //TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/input"));
            TextInputFormat.addInputPath(job, new Path("file:///D:\\input"));
            //第二步:设置Mapper类和数据类型（K2和V2）
            job.setMapperClass(PartitionMapper.class);
            job.setMapOutputKeyClass(Text.class);
            job.setMapOutputValueClass(NullWritable.class);

            //第三步，指定分区类
            job.setPartitionerClass(MyPartitioner.class);
            //第四, 五，六步
            //第七步:指定Reducer类和数据类型(K3和V3)
            job.setReducerClass(PartitionerReducer.class);
            job.setOutputValueClass(Text.class);
            job.setOutputValueClass(NullWritable.class);
            //设置ReduceTask的个数
            job.setNumReduceTasks(2);

            //第八步:指定输出类和输出路径
            job.setOutputFormatClass(TextOutputFormat.class);
            //TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/out/partition_out"));
            TextOutputFormat.setOutputPath(job, new Path("file:///D:\\out\\partition_out3"));

        //3:等待任务结束
        boolean bl = job.waitForCompletion(true);

        return bl?0:1;
    }

    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        //启动job任务
        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);
    }
}
```

## 6. MapReduce 排序和序列化

* 序列化 (Serialization) 是指把结构化对象转化为字节流

* 反序列化 (Deserialization) 是序列化的逆过程. 把字节流转为结构化对象. 当要在进程间传递对象或持久化对象的时候, 就需要序列化对象成字节流, 反之当要将接收到或从磁盘读取的字节流转换为对象, 就要进行反序列化

* Java 的序列化 (Serializable) 是一个重量级序列化框架, 一个对象被序列化后, 会附带很多额外的信息 (各种校验信息, header, 继承体系等）, 不便于在网络中高效传输. 所以, Hadoop 自己开发了一套序列化机制(Writable), 精简高效. 不用像 Java 对象类一样传输多层的父子关系, 需要哪个属性就传输哪个属性值, 大大的减少网络传输的开销

* Writable 是 Hadoop 的序列化格式, Hadoop 定义了这样一个 Writable 接口. 一个类要支持可序列化只需实现这个接口即可

* 另外 Writable 有一个子接口是 WritableComparable, WritableComparable 是既可实现序列化, 也可以对key进行比较, 我们这里可以通过自定义 Key 实现 WritableComparable 来实现我们的排序功能

数据格式如下

```text
a	1
a	9
b	3
a	7
b	8
b	10
a	5
```

要求:

* 第一列按照字典顺序进行排列
* 第一列相同的时候, 第二列按照升序进行排列

解决思路:

* 将 Map 端输出的 `<key,value>` 中的 key 和 value 组合成一个新的 key (newKey), value值不变
* 这里就变成 `<(key,value),value>`, 在针对 newKey 排序的时候, 如果 key 相同, 就再对value进行排序

##### Step 1. 自定义类型和比较器

```java
@Data
@AllArgsConstructor
@NoArgsConstructor
public class PairWritable implements WritableComparable<PairWritable> {
    // 组合key,第一部分是我们第一列，第二部分是我们第二列
    private String first;
    private int second;
    public PairWritable() {
    }
    public PairWritable(String first, int second) {
        this.set(first, second);
    }
    /**
     * 方便设置字段
     */
    public void set(String first, int second) {
        this.first = first;
        this.second = second;
    }
    /**
     * 反序列化
     */
    @Override
    public void readFields(DataInput input) throws IOException {
        this.first = input.readUTF();
        this.second = input.readInt();
    }
    /**
     * 序列化
     */
    @Override
    public void write(DataOutput output) throws IOException {
        output.writeUTF(first);
        output.writeInt(second);
    }
    /*
     * 重写比较器
     */
    public int compareTo(PairWritable o) {
        //每次比较都是调用该方法的对象与传递的参数进行比较，说白了就是第一行与第二行比较完了之后的结果与第三行比较，
        //得出来的结果再去与第四行比较，依次类推
        System.out.println(o.toString());
        System.out.println(this.toString());
        int comp = this.first.compareTo(o.first);
        if (comp != 0) {
            return comp;
        } else { // 若第一个字段相等，则比较第二个字段
            return Integer.valueOf(this.second).compareTo(
                    Integer.valueOf(o.getSecond()));
        }
    }

}
```

##### Step 2. Mapper

```java
public class SortMapper extends Mapper<LongWritable,Text,SortBean,NullWritable> {
    /*
      map方法将K1和V1转为K2和V2:

      K1            V1
      0            a  3
      5            b  7
      ----------------------
      K2                         V2
      SortBean(a  3)         NullWritable
      SortBean(b  7)         NullWritable
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        //1:将行文本数据(V1)拆分，并将数据封装到SortBean对象,就可以得到K2
        String[] split = value.toString().split("\t");

        SortBean sortBean = new SortBean();
        sortBean.setWord(split[0]);
        sortBean.setNum(Integer.parseInt(split[1]));

        //2:将K2和V2写入上下文中
        context.write(sortBean, NullWritable.get());
    }
}

```

##### Step 3. Reducer

```java
public class SortReducer extends Reducer<SortBean,NullWritable,SortBean,NullWritable> {

    //reduce方法将新的K2和V2转为K3和V3
    @Override
    protected void reduce(SortBean key, Iterable<NullWritable> values, Context context) throws IOException, InterruptedException {
       context.write(key, NullWritable.get());
    }
}
```

##### Step 4. Main 入口

```java
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] args) throws Exception {
        //1:创建job对象
        Job job = Job.getInstance(super.getConf(), "mapreduce_sort");

        //2:配置job任务(八个步骤)
            //第一步:设置输入类和输入的路径
            job.setInputFormatClass(TextInputFormat.class);
            ///TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/input/sort_input"));
            TextInputFormat.addInputPath(job, new Path("file:///D:\\input\\sort_input"));

            //第二步: 设置Mapper类和数据类型
            job.setMapperClass(SortMapper.class);
            job.setMapOutputKeyClass(SortBean.class);
            job.setMapOutputValueClass(NullWritable.class);
            //第三，四，五，六

            //第七步：设置Reducer类和类型
            job.setReducerClass(SortReducer.class);
            job.setOutputKeyClass(SortBean.class);
            job.setOutputValueClass(NullWritable.class);

            //第八步: 设置输出类和输出的路径
            job.setOutputFormatClass(TextOutputFormat.class);
            //TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/out/sort_out"));
            TextOutputFormat.setOutputPath(job, new Path("file:///D:\\out\\sort_out"));

        //3:等待任务结束
        boolean bl = job.waitForCompletion(true);

        return bl?0:1;
    }

    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();

        //启动job任务
        int run = ToolRunner.run(configuration, new JobMain(), args);

        System.exit(run);
    }
}

```

## 7. 规约Combiner

##### 概念

每一个 map 都可能会产生大量的本地输出，Combiner 的作用就是对 map 端的输出先做一次合并，以减少在 map 和 reduce 节点之间的数据传输量，以提高网络IO 性能，是 MapReduce 的一种优化手段之一

- combiner 是 MR 程序中 Mapper 和 Reducer 之外的一种组件
- combiner 组件的父类就是 Reducer
- combiner 和 reducer 的区别在于运行的位置
  - Combiner 是在每一个 maptask 所在的节点运行
  - Reducer 是接收全局所有 Mapper 的输出结果
- combiner 的意义就是对每一个 maptask 的输出进行局部汇总，以减小网络传输量

##### 实现步骤

1. 自定义一个 combiner 继承 Reducer，重写 reduce 方法
2. 在 job 中设置 `job.setCombinerClass(CustomCombiner.class)`

combiner 能够应用的前提是不能影响最终的业务逻辑，而且，combiner 的输出 kv 应该跟 reducer 的输入 kv 类型要对应起来



```java
/*
  四个泛型解释:
    KEYIN :K1的类型
    VALUEIN: V1的类型

    KEYOUT: K2的类型
    VALUEOUT: V2的类型
 */
public class WordCountMapper extends Mapper<LongWritable,Text, Text , LongWritable> {

    //map方法就是将K1和V1 转为 K2和V2
    /*
      参数:
         key    : K1   行偏移量
         value  : V1   每一行的文本数据
         context ：表示上下文对象
     */
    /*
      如何将K1和V1 转为 K2和V2
        K1         V1
        0   hello,world,hadoop
        15  hdfs,hive,hello
       ---------------------------

        K2            V2
        hello         1
        world         1
        hdfs          1
        hadoop        1
        hello         1
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        Text text = new Text();
        LongWritable longWritable = new LongWritable();
        //1:将一行的文本数据进行拆分
        String[] split = value.toString().split(",");

        //2:遍历数组，组装 K2 和 V2
        for (String word : split) {
            //3:将K2和V2写入上下文
            text.set(word);
            longWritable.set(1);
            context.write(text, longWritable);
        }

    }
}

```

```java
/*
  四个泛型解释:
    KEYIN:  K2类型
    VALULEIN: V2类型

    KEYOUT: K3类型
    VALUEOUT:V3类型
 */

public class WordCountReducer extends Reducer<Text,LongWritable,Text,LongWritable> {
    //reduce方法作用: 将新的K2和V2转为 K3和V3 ，将K3和V3写入上下文中
    /*
      参数:
        key ： 新K2
        values： 集合 新 V2
        context ：表示上下文对象

        ----------------------
        如何将新的K2和V2转为 K3和V3
        新  K2         V2
            hello      <1,1,1>
            world      <1,1>
            hadoop     <1>
        ------------------------
           K3        V3
           hello     3
           world     2
           hadoop    1
     */
    @Override
    protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
        long count = 0;
       //1:遍历集合，将集合中的数字相加，得到 V3
        for (LongWritable value : values) {
             count += value.get();
        }
        //2:将K3和V3写入上下文中
        context.write(key, new LongWritable(count));
    }
}
```

```java
public class MyCombiner extends Reducer<Text,LongWritable,Text,LongWritable> {

    /*
       key : hello
       values: <1,1,1,1>
     */
    @Override
    protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
        long count = 0;
        //1:遍历集合，将集合中的数字相加，得到 V3
        for (LongWritable value : values) {
            count += value.get();
        }
        //2:将K3和V3写入上下文中
        context.write(key, new LongWritable(count));
    }
}
```

```java
// JobMain.java

public class JobMain extends Configured implements Tool {

    @Override
    public int run(String[] strings) throws Exception {
        // 第一步，创造实例，创建输入流
        Job job = Job.getInstance(super.getConf(), "word_count_combiner_test");

        job.setInputFormatClass(TextInputFormat.class);
        TextInputFormat.addInputPath(job, new Path("hdfs://127.0.0.1"));

        // 第二步，设置map类和mapKV
        job.setMapperClass(WordCountCMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);

        // 第三四五六步，排序，规约，分组
        job.setCombinerClass(WordCountCombiner.class);
        // 其他使用默认配置

        // 第七步 设置reduce类和KV
        job.setReducerClass(WordCountCReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);

        // 第八步，设置输出类，等待任务执行结束
        job.setOutputFormatClass(TextOutputFormat.class);
        TextOutputFormat.setOutputPath(job, new Path("hdfs://127.0.0.1"));

        boolean b = job.waitForCompletion(true);
        return b ? 0 : 1;

    }

    public static void main(String[] args) throws Exception {
        int exeCode = ToolRunner.run(new Configuration(), new JobMain(), args);
        System.exit(exeCode);
    }
}
```

## 阶段练习-流量统计

### 需求一: 统计求和

统计每个手机号的上行数据包总和，下行数据包总和，上行总流量之和，下行总流量之和

分析：以手机号码作为key值，上行流量，下行流量，上行总流量，下行总流量四个字段作为value值，然后以这个key，和value作为map阶段的输出，reduce阶段的输入

##### Step 1: 自定义map的输出value对象FlowBean

```java
@Data
@AllArgsConstructor
@NoArgeConstructor
public class FlowBean implements Writable {
    private Integer upFlow;  //上行数据包数
    private Integer downFlow;  //下行数据包数
    private Integer upCountFlow; //上行流量总和
    private Integer downCountFlow;//下行流量总和

    @Override
    public String toString() {
        return  upFlow +
                "\t" + downFlow +
                "\t" + upCountFlow +
                "\t" + downCountFlow;
    }

    //序列化方法
    @Override
    public void write(DataOutput out) throws IOException {
        out.writeInt(upFlow);
        out.writeInt(downFlow);
        out.writeInt(upCountFlow);
        out.writeInt(downCountFlow);
    }

    //反序列化
    @Override
    public void readFields(DataInput in) throws IOException {
        this.upFlow = in.readInt();
        this.downFlow = in.readInt();
        this.upCountFlow = in.readInt();
        this.downCountFlow = in.readInt();
    }
}
```

##### Step 2: 定义FlowMapper类

```java
public class FlowCountMapper extends Mapper<LongWritable,Text,Text,FlowBean> {
    /*
      将K1和V1转为K2和V2:
      K1              V1
      0            1360021750219	128	1177	16852	200
     ------------------------------
      K2              V2
      13600217502     FlowBean(19	128	1177	16852)
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        //1:拆分行文本数据,得到手机号--->K2
        String[] split = value.toString().split("\t");
        String phoneNum = split[1];

        //2:创建FlowBean对象,并从行文本数据拆分出流量的四个四段,并将四个流量字段的值赋给FlowBean对象
        FlowBean flowBean = new FlowBean();

        flowBean.setUpFlow(Integer.parseInt(split[6]));
        flowBean.setDownFlow(Integer.parseInt(split[7]));
        flowBean.setUpCountFlow(Integer.parseInt(split[8]));
        flowBean.setDownCountFlow(Integer.parseInt(split[9]));

        //3:将K2和V2写入上下文中
        context.write(new Text(phoneNum), flowBean);

    }
}

```

##### Step 3: 定义FlowReducer类

```java
public class FlowCountReducer extends Reducer<Text,FlowBean,Text,FlowBean> {
    @Override
    protected void reduce(Text key, Iterable<FlowBean> values, Context context) throws IOException, InterruptedException {
        //1:遍历集合,并将集合中的对应的四个字段累计
         Integer upFlow = 0;  //上行数据包数
         Integer downFlow = 0;  //下行数据包数
         Integer upCountFlow = 0; //上行流量总和
         Integer downCountFlow = 0;//下行流量总和

        for (FlowBean value : values) {
            upFlow += value.getUpFlow();
            downFlow += value.getDownFlow();
            upCountFlow += value.getUpCountFlow();
            downCountFlow += value.getDownCountFlow();
        }

        //2:创建FlowBean对象,并给对象赋值  V3
        FlowBean flowBean = new FlowBean();
        flowBean.setUpFlow(upFlow);
        flowBean.setDownFlow(downFlow);
        flowBean.setUpCountFlow(upCountFlow);
        flowBean.setDownCountFlow(downCountFlow);

        //3:将K3和V3下入上下文中
        context.write(key, flowBean);
    }
}
```

##### Step 4: 程序main函数入口FlowMain

```java
public class JobMain extends Configured implements Tool {

    //该方法用于指定一个job任务
    @Override
        public int run(String[] args) throws Exception {
        //1:创建一个job任务对象
        Job job = Job.getInstance(super.getConf(), "mapreduce_flowcount");
        //如果打包运行出错，则需要加该配置
        job.setJarByClass(JobMain.class);
        //2:配置job任务对象(八个步骤)

        //第一步:指定文件的读取方式和读取路径
        job.setInputFormatClass(TextInputFormat.class);
        //TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/wordcount"));
        TextInputFormat.addInputPath(job, new Path("file:///D:\\input\\flowcount_input"));



        //第二步:指定Map阶段的处理方式和数据类型
         job.setMapperClass(FlowCountMapper.class);
         //设置Map阶段K2的类型
          job.setMapOutputKeyClass(Text.class);
        //设置Map阶段V2的类型
          job.setMapOutputValueClass(FlowBean.class);


          //第三（分区），四 （排序）
          //第五步: 规约(Combiner)
          //第六步 分组


          //第七步：指定Reduce阶段的处理方式和数据类型
          job.setReducerClass(FlowCountReducer.class);
          //设置K3的类型
           job.setOutputKeyClass(Text.class);
          //设置V3的类型
           job.setOutputValueClass(FlowBean.class);

           //第八步: 设置输出类型
           job.setOutputFormatClass(TextOutputFormat.class);
           //设置输出的路径
           TextOutputFormat.setOutputPath(job, new Path("file:///D:\\out\\flowcount_out"));



        //等待任务结束
           boolean bl = job.waitForCompletion(true);

           return bl ? 0:1;
    }

    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();

        //启动job任务
        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);

    }
}
```

### 需求二: 上行流量倒序排序（递减排序）

分析，以需求一的输出数据作为排序的输入数据，自定义FlowBean,以FlowBean为map输出的key，以手机号作为Map输出的value，因为MapReduce程序会对Map阶段输出的key进行排序

##### Step 1: 定义FlowBean实现WritableComparable实现比较排序

Java 的 compareTo 方法说明:

- compareTo 方法用于将当前对象与方法的参数进行比较。
- 如果指定的数与参数相等返回 0。
- 如果指定的数小于参数返回 -1。
- 如果指定的数大于参数返回 1。

例如：`o1.compareTo(o2);` 返回正数的话，当前对象（调用 compareTo 方法的对象 o1）要排在比较对象（compareTo 传参对象 o2）后面，返回负数的话，放在前面

~~~java
@Data
@AllArgsConstructor
@NoArgeConstructor
public class FlowBean implements WritableComparable<FlowBean> {
    private Integer upFlow;  //上行数据包数
    private Integer downFlow;  //下行数据包数
    private Integer upCountFlow; //上行流量总和
    private Integer downCountFlow;//下行流量总和

    @Override
    public String toString() {
        return  upFlow +
                "\t" + downFlow +
                "\t" + upCountFlow +
                "\t" + downCountFlow;
    }

    //序列化方法
    @Override
    public void write(DataOutput out) throws IOException {
        out.writeInt(upFlow);
        out.writeInt(downFlow);
        out.writeInt(upCountFlow);
        out.writeInt(downCountFlow);
    }

    //反序列化
    @Override
    public void readFields(DataInput in) throws IOException {
        this.upFlow = in.readInt();
        this.downFlow = in.readInt();
        this.upCountFlow = in.readInt();
        this.downCountFlow = in.readInt();
    }

    //指定排序的规则
    @Override
    public int compareTo(FlowBean flowBean) {
       // return this.upFlow.compareTo(flowBean.getUpFlow()) * -1;
       return  flowBean.upFlow - this.upFlow ;
    }
}
~~~

##### Step 2: 定义FlowMapper

```java
public class FlowSortMapper extends Mapper<LongWritable,Text,FlowBean,Text> {
    //map方法:将K1和V1转为K2和V2
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        //1:拆分行文本数据(V1),得到四个流量字段,并封装FlowBean对象---->K2
        String[] split = value.toString().split("\t");

        FlowBean flowBean = new FlowBean();

        flowBean.setUpFlow(Integer.parseInt(split[1]));
        flowBean.setDownFlow(Integer.parseInt(split[2]));
        flowBean.setUpCountFlow(Integer.parseInt(split[3]));
        flowBean.setDownCountFlow(Integer.parseInt(split[4]));

        //2:通过行文本数据,得到手机号--->V2
        String phoneNum = split[0];

        //3:将K2和V2下入上下文中
        context.write(flowBean, new Text(phoneNum));

    }
}
```

##### Step 3: 定义FlowReducer

```java
/*
  K2: FlowBean
  V2: Text  手机号

  K3: Text  手机号
  V3: FlowBean
 */

public class FlowSortReducer extends Reducer<FlowBean,Text,Text,FlowBean> {
    @Override
    protected void reduce(FlowBean key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        //1:遍历集合,取出 K3,并将K3和V3写入上下文中
        for (Text value : values) {
            context.write(value, key);
        }

    }
}

```

##### Step 4: 程序main函数入口

```java
public class JobMain extends Configured implements Tool {    //该方法用于指定一个job任务    @Override        public int run(String[] args) throws Exception {        //1:创建一个job任务对象        Job job = Job.getInstance(super.getConf(), "mapreduce_flowsort");        //2:配置job任务对象(八个步骤)        //第一步:指定文件的读取方式和读取路径        job.setInputFormatClass(TextInputFormat.class);        //TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/wordcount"));        TextInputFormat.addInputPath(job, new Path("file:///D:\\out\\flowcount_out"));        //第二步:指定Map阶段的处理方式和数据类型         job.setMapperClass(FlowSortMapper.class);         //设置Map阶段K2的类型          job.setMapOutputKeyClass(FlowBean.class);        //设置Map阶段V2的类型          job.setMapOutputValueClass(Text.class);          //第三（分区），四 （排序）          //第五步: 规约(Combiner)          //第六步 分组          //第七步：指定Reduce阶段的处理方式和数据类型          job.setReducerClass(FlowSortReducer.class);          //设置K3的类型           job.setOutputKeyClass(Text.class);          //设置V3的类型           job.setOutputValueClass(FlowBean.class);           //第八步: 设置输出类型           job.setOutputFormatClass(TextOutputFormat.class);           //设置输出的路径           TextOutputFormat.setOutputPath(job, new Path("file:///D:\\out\\flowsort_out"));        //等待任务结束           boolean bl = job.waitForCompletion(true);           return bl ? 0:1;    }    public static void main(String[] args) throws Exception {        Configuration configuration = new Configuration();        //启动job任务        int run = ToolRunner.run(configuration, new JobMain(), args);        System.exit(run);    }}
```

### 需求三: 手机号码分区

在需求一的基础上，继续完善，将不同的手机号分到不同的数据文件的当中去，需要自定义分区来实现，这里我们自定义来模拟分区，将以下数字开头的手机号进行分开

```text
135 开头数据到一个分区文件136 开头数据到一个分区文件137 开头数据到一个分区文件其他分区
```

##### 自定义分区

```java
public class FlowCountPartition extends Partitioner<Text,FlowBean> {    /*      该方法用来指定分区的规则:        135 开头数据到一个分区文件        136 开头数据到一个分区文件        137 开头数据到一个分区文件        其他分区       参数:         text : K2   手机号         flowBean: V2         i   : ReduceTask的个数     */    @Override    public int getPartition(Text text, FlowBean flowBean, int i) {        //1:获取手机号        String phoneNum = text.toString();        //2:判断手机号以什么开头,返回对应的分区编号(0-3)        if(phoneNum.startsWith("135")){            return  0;        }else  if(phoneNum.startsWith("136")){            return  1;        }else  if(phoneNum.startsWith("137")){            return  2;        }else{            return 3;        }    }}
```

##### 作业运行设置

```java
job.setPartitionerClass(FlowPartition.class);job.setNumReduceTasks(4);
```

##### 修改输入输出路径, 并运行

```java
TextInputFormat.addInputPath(job, new Path("file:///D:\\input\\flowpartition_input"));TextOutputFormat.setOutputPath(job, new Path("file:///D:\\out\\flowpartiton_out"));
```

## 1 .MapReduce的运行机制详解

### 1.1:MapTask 工作机制

![1561706243507](R:\GITHUB\MyNotes\_Typora\BigData\ParallelCalculation\MapReduce\MapReduce.imgs\1561706243507.png)	

![1561706253827](R:\GITHUB\MyNotes\_Typora\BigData\ParallelCalculation\MapReduce\MapReduce.imgs\1561706253827.png)	

整个Map阶段流程大体如上图所示。

简单概述：inputFile通过split被逻辑切分为多个split文件，通过Record按行读取内容给map（用户自己实现的）进行处理，数据被map处理结束之后交给OutputCollector收集器，对其结果key进行分区（默认使用hash分区），然后写入buffer，每个map task都有一个内存缓冲区，存储着map的输出结果，当缓冲区快满的时候需要将缓冲区的数据以一个临时文件的方式存放到磁盘，当整个map task结束后再对磁盘中这个map task产生的所有临时文件做合并，生成最终的正式输出文件，然后等待reduce task来拉数据

![image-20210601151228334](R:\GITHUB\MyNotes\_Typora\BigData\ParallelCalculation\MapReduce\MapReduce.imgs\image-20210601151228334.png)

![image-20210601151236611](R:\GITHUB\MyNotes\_Typora\BigData\ParallelCalculation\MapReduce\MapReduce.imgs\image-20210601151236611.png)

##### 详细步骤

1. 读取数据组件 **InputFormat** (默认 TextInputFormat) 会通过 `getSplits` 方法对输入目录中文件进行逻辑切片规划得到 `block`, 有多少个 `block`就对应启动多少个 `MapTask`. 

2. 将输入文件切分为 `block` 之后, 由 `RecordReader` 对象 (默认是LineRecordReader) 进行**读取**, 以 `\n` 作为分隔符, 读取一行数据, 返回 `<key，value>`. Key 表示每行首字符偏移值, Value 表示这一行文本内容

3. 读取 `block` 返回 `<key,value>`, **进入用户自己继承的 Mapper 类中**，执行用户重写的 map 函数, RecordReader 读取一行这里调用一次

4. Mapper 逻辑结束之后, 将 Mapper 的每条结果通过 `context.write` 进行collect数据收集. 在 collect 中, 会先对其进行分区处理，默认使用 **HashPartitioner**

   - > MapReduce 提供 `Partitioner` 接口, 它的作用就是根据 `Key` 或 `Value` 及 `Reducer` 的数量来决定当前的这对输出数据最终应该交由哪个 `Reduce task` 处理, 默认对 Key Hash 后再以 Reducer 数量取模. 默认的取模方式只是为了平均 Reducer 的处理能力, 如果用户自己对 Partitioner 有需求, 可以订制并设置到 Job 上

5. 接下来, 会将数据写入内存, 内存中这片区域叫做环形缓冲区, 缓冲区的作用是批量收集 Mapper 结果, 减少磁盘 IO 的影响. 我们的 **Key/Value 对以及 Partition 的结果都会被写入缓冲区**. 当然, 写入之前，Key 与 Value 值都会被序列化成字节数组

   - > 环形缓冲区其实是一个数组, 数组中存放着 Key, Value 的序列化数据和 Key, Value 的元数据信息, 包括 Partition, Key 的起始位置, Value 的起始位置以及 Value 的长度. 环形结构是一个抽象概念

   - > 缓冲区是有大小限制, 默认是 100MB. 当 Mapper 的输出结果很多时, 就可能会撑爆内存, 所以需要在一定条件下将缓冲区中的数据临时写入磁盘, 然后重新利用这块缓冲区. 这个从内存往磁盘写数据的过程被称为 Spill, 中文可译为溢写. 这个溢写是由单独线程来完成, 不影响往缓冲区写 Mapper 结果的线程. 溢写线程启动时不应该阻止 Mapper 的结果输出, 所以整个缓冲区有个溢写的比例 `spill.percent`. 这个比例默认是 0.8, 也就是当缓冲区的数据已经达到阈值 `buffer size * spill percent = 100MB * 0.8 = 80MB`, 溢写线程启动, 锁定这 80MB 的内存, 执行溢写过程. Mapper 的输出结果还可以往剩下的 20MB 内存中写, 互不影响

6. 当溢写线程启动后, 需要**对这 80MB 空间内的 Key 做排序 (Sort)**. 排序是 MapReduce 模型默认的行为, 这里的排序也是对序列化的字节做的排序

   - > 如果 Job 设置过 Combiner, 那么现在就是使用 Combiner 的时候了. 将有相同 Key 的 Key/Value 对的 Value 加起来, 减少溢写到磁盘的数据量. Combiner 会优化 MapReduce 的中间结果, 所以它在整个模型中会多次使用

   - > 那哪些场景才能使用 Combiner 呢? 从这里分析, Combiner 的输出是 Reducer 的输入, Combiner 绝不能改变最终的计算结果. Combiner 只应该用于那种 Reduce 的输入 Key/Value 与输出 Key/Value 类型完全一致, 且不影响最终结果的场景. 比如累加, 最大值等. Combiner 的使用一定得慎重, 如果用好, 它对 Job 执行效率有帮助, 反之会影响 Reducer 的最终结果

7. **合并溢写文件**, 每次溢写会在磁盘上生成一个临时文件 (写之前判断是否有 Combiner), 如果 Mapper 的输出结果真的很大, 有多次这样的溢写发生, 磁盘上相应的就会有多个临时文件存在. 当整个数据处理结束之后开始对磁盘中的临时文件进行 Merge 合并, 因为最终的文件只有一个, 写入磁盘, 并且为这个文件提供了一个索引文件, 以记录每个reduce对应数据的偏移量

##### 配置

| 配置                               | 默认值                           | 解释                       |
| ---------------------------------- | -------------------------------- | -------------------------- |
| `mapreduce.task.io.sort.mb`        | 100                              | 设置环型缓冲区的内存值大小 |
| `mapreduce.map.sort.spill.percent` | 0.8                              | 设置溢写的比例             |
| `mapreduce.cluster.local.dir`      | `${hadoop.tmp.dir}/mapred/local` | 溢写数据目录               |
| `mapreduce.task.io.sort.factor`    | 10                               | 设置一次合并多少个溢写文件 |

### 1.2 :ReduceTask 工作机制

![1561706287927](R:\GITHUB\MyNotes\_Typora\BigData\ParallelCalculation\MapReduce\MapReduce.imgs\1561706287927.png)	

Reduce 大致分为 copy、sort、reduce 三个阶段，重点在前两个阶段。copy 阶段包含一个 eventFetcher 来获取已完成的 map 列表，由 Fetcher 线程去 copy 数据，在此过程中会启动两个 merge 线程，分别为 inMemoryMerger 和 onDiskMerger，分别将内存中的数据 merge 到磁盘和将磁盘中的数据进行 merge。待数据 copy 完成之后，copy 阶段就完成了，开始进行 sort 阶段，sort 阶段主要是执行 finalMerge 操作，纯粹的 sort 阶段，完成之后就是 reduce 阶段，调用用户定义的 reduce 函数进行处理

##### 详细步骤

1. **`Copy阶段`**，简单地拉取数据。Reduce进程启动一些数据copy线程(Fetcher)，通过HTTP方式请求maptask获取属于自己的文件。
2. **`Merge阶段`**。这里的merge如map端的merge动作，只是数组中存放的是不同map端copy来的数值。Copy过来的数据会先放入内存缓冲区中，这里的缓冲区大小要比map端的更为灵活。merge有三种形式：内存到内存；内存到磁盘；磁盘到磁盘。默认情况下第一种形式不启用。当内存中的数据量到达一定阈值，就启动内存到磁盘的merge。与map 端类似，这也是溢写的过程，这个过程中如果你设置有Combiner，也是会启用的，然后在磁盘中生成了众多的溢写文件。第二种merge方式一直在运行，直到没有map端的数据时才结束，然后启动第三种磁盘到磁盘的merge方式生成最终的文件。
3. **`合并排序`**。把分散的数据合并成一个大的数据后，还会再对合并后的数据排序。
4. **`对排序后的键值对调用reduce方法`**，键相等的键值对调用一次reduce方法，每次调用会产生零个或者多个键值对，最后把这些输出的键值对写入到HDFS文件中。

### 1.3 Shuffle 过程

map 阶段处理的数据如何传递给 reduce 阶段，是 MapReduce 框架中最关键的一个流程，这个流程就叫 shuffle
shuffle: 洗牌、发牌 ——（核心机制：数据分区，排序，分组，规约，合并等过程）

![1561706306005](R:\GITHUB\MyNotes\_Typora\BigData\ParallelCalculation\MapReduce\MapReduce.imgs\1561706306005.png)	

shuffle 是 Mapreduce 的核心，它分布在 Mapreduce 的 map 阶段和 reduce 阶段。一般把从 Map 产生输出开始到 Reduce 取得数据作为输入之前的过程称作 shuffle。

1. **`Collect阶段`**：将 MapTask 的结果输出到默认大小为 100M 的环形缓冲区，保存的是 key/value，Partition 分区信息等。
2. **`Spill阶段`**：当内存中的数据量达到一定的阀值的时候，就会将数据写入本地磁盘，在将数据写入磁盘之前需要对数据进行一次排序的操作，如果配置了 combiner，还会将有相同分区号和 key 的数据进行排序。
3. **`Merge阶段`**：把所有溢出的临时文件进行一次合并操作，以确保一个 MapTask 最终只产生一个中间数据文件。
4. **`Copy阶段`**：ReduceTask 启动 Fetcher 线程到已经完成 MapTask 的节点上复制一份属于自己的数据，这些数据默认会保存在内存的缓冲区中，当内存的缓冲区达到一定的阀值的时候，就会将数据写到磁盘之上。
5. **`Merge阶段`**：在 ReduceTask 远程复制数据的同时，会在后台开启两个线程对内存到本地的数据文件进行合并操作。
6. **`Sort阶段`**：在对数据进行合并的同时，会进行排序操作，由于 MapTask 阶段已经对数据进行了局部的排序，ReduceTask 只需保证 Copy 的数据的最终整体有效性即可。
   Shuffle 中的缓冲区大小会影响到 mapreduce 程序的执行效率，原则上说，缓冲区越大，磁盘io的次数越少，执行速度就越快
   缓冲区的大小可以通过参数调整,  参数：mapreduce.task.io.sort.mb  默认100M

## 2. 案例: Reduce 端实现 JOIN

### 2.1. 需求

> 假如数据量巨大，两表的数据是以文件的形式存储在 HDFS 中, 需要用 MapReduce 程序来实现以下 SQL 查询运算
>
> ```sql
> select  a.id,a.date,b.name,b.category_id,b.price from t_order a left join t_product b on a.pid = b.id
> ```

##### 商品表

| id    | pname  | category_id | price |
| ----- | ------ | ----------- | ----- |
| P0001 | 小米5  | 1000        | 2000  |
| P0002 | 锤子T1 | 1000        | 3000  |

##### 订单数据表

| id   | date     | pid   | amount |
| ---- | -------- | ----- | ------ |
| 1001 | 20150710 | P0001 | 2      |
| 1002 | 20150710 | P0002 | 3      |

### 2.2 实现步骤

通过将关联的条件作为map输出的key，将两表满足join条件的数据并携带数据所来源的文件信息，发往同一个reduce task，在reduce中进行数据的串联

#### Step 1: 定义 Mapper

```java
public class ReduceJoinMapper extends Mapper<LongWritable,Text,Text,Text> {
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        //1:判断数据来自哪个文件
        FileSplit fileSplit = (FileSplit) context.getInputSplit();
        String fileName = fileSplit.getPath().getName();
        if(fileName.equals("product.txt")){
            //数据来自商品表
            //2:将K1和V1转为K2和V2,写入上下文中
            String[] split = value.toString().split(",");
            String productId = split[0];

            context.write(new Text(productId), value);

        }else{
            //数据来自订单表
            //2:将K1和V1转为K2和V2,写入上下文中
            String[] split = value.toString().split(",");
            String productId = split[2];

            context.write(new Text(productId), value);

        }

    }
}

```

#### Step 2: 定义 Reducer

```java
public class ReduceJoinMapper extends Mapper<LongWritable,Text,Text,Text> {
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        //1:判断数据来自哪个文件

        FileSplit fileSplit = (FileSplit) context.getInputSplit();
        String fileName = fileSplit.getPath().getName();
        if(fileName.equals("product.txt")){
            //数据来自商品表
            //2:将K1和V1转为K2和V2,写入上下文中
            String[] split = value.toString().split(",");
            String productId = split[0];

            context.write(new Text(productId), value);

        }else{
            //数据来自订单表
            //2:将K1和V1转为K2和V2,写入上下文中
            String[] split = value.toString().split(",");
            String productId = split[2];

            context.write(new Text(productId), value);

        }



    }
}
```



#### Step 3: 定义主类

```java
public class ReduceJoinReducer extends Reducer<Text,Text,Text,Text> {
    @Override
    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
       //1:遍历集合,获取V3 (first +second)
        String first = "";
        String second = "";
        for (Text value : values) {
            if(value.toString().startsWith("p")){
                first = value.toString();
            }else{
                second += value.toString();
            }

        }
        //2:将K3和V3写入上下文中
        context.write(key, new Text(first+"\t"+second));
    }
}
```

## 3. 案例: Map端实现 JOIN

#### 3.1 概述

​	适用于关联表中有小表的情形.

​	使用分布式缓存,可以将小表分发到所有的map节点，这样，map节点就可以在本地对自己所读到的大表数据进行join并输出最终结果，可以大大提高join操作的并发度，加快处理速度

#### 3.2 实现步骤

  先在mapper类中预先定义好小表，进行join

 引入实际场景中的解决方案：一次加载数据库或者用

##### Step 1：定义Mapper

~~~java
public class MapJoinMapper extends Mapper<LongWritable,Text,Text,Text>{
    private HashMap<String, String> map = new HashMap<>();

    //第一件事情:将分布式缓存的小表数据读取到本地Map集合(只需要做一次)

    @Override
    protected void setup(Context context) throws IOException, InterruptedException {
        //1:获取分布式缓存文件列表
        URI[] cacheFiles =  context.getCacheFiles();

        //2:获取指定的分布式缓存文件的文件系统(FileSystem)
        FileSystem fileSystem = FileSystem.get(cacheFiles[0], context.getConfiguration());

        //3:获取文件的输入流
        FSDataInputStream inputStream = fileSystem.open(new Path(cacheFiles[0]));

        //4:读取文件内容, 并将数据存入Map集合
           //4.1 将字节输入流转为字符缓冲流FSDataInputStream --->BufferedReader
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
           //4.2 读取小表文件内容,以行位单位,并将读取的数据存入map集合

        String line = null;
        while((line = bufferedReader.readLine()) != null){
            String[] split = line.split(",");

            map.put(split[0], line);

        }

        //5:关闭流
        bufferedReader.close();
        fileSystem.close();
    }

    //第二件事情:对大表的处理业务逻辑,而且要实现大表和小表的join操作

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            //1:从行文本数据中获取商品的id: p0001 , p0002  得到了K2
            String[] split = value.toString().split(",");
            String productId = split[2];  //K2

            //2:在Map集合中,将商品的id作为键,获取值(商品的行文本数据) ,将value和值拼接,得到V2
            String productLine = map.get(productId);
            String valueLine = productLine+"\t"+value.toString(); //V2
            //3:将K2和V2写入上下文中
            context.write(new Text(productId), new Text(valueLine));
    }
}

~~~

##### Step 2：定义主类

~~~java
public class JobMain  extends Configured implements Tool{
    @Override
    public int run(String[] args) throws Exception {
        //1:获取job对象
        Job job = Job.getInstance(super.getConf(), "map_join_job");

        //2:设置job对象(将小表放在分布式缓存中)
            //将小表放在分布式缓存中
           // DistributedCache.addCacheFile(new URI("hdfs://node01:8020/cache_file/product.txt"), super.getConf());
           job.addCacheFile(new URI("hdfs://node01:8020/cache_file/product.txt"));

           //第一步:设置输入类和输入的路径
            job.setInputFormatClass(TextInputFormat.class);
            TextInputFormat.addInputPath(job, new Path("file:///D:\\input\\map_join_input"));
            //第二步:设置Mapper类和数据类型
            job.setMapperClass(MapJoinMapper.class);
            job.setMapOutputKeyClass(Text.class);
            job.setMapOutputValueClass(Text.class);

            //第八步:设置输出类和输出路径
            job.setOutputFormatClass(TextOutputFormat.class);
            TextOutputFormat.setOutputPath(job, new Path("file:///D:\\out\\map_join_out"));


        //3:等待任务结束
        boolean bl = job.waitForCompletion(true);
        return bl ? 0 :1;
    }

    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        //启动job任务
        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);
    }
}
~~~

  

## 4. 案例:求共同好友

### 4.1 需求分析

以下是qq的好友列表数据，冒号前是一个用户，冒号后是该用户的所有好友（数据中的好友关系是单向的）

~~~java
A:B,C,D,F,E,O
B:A,C,E,K
C:A,B,D,E,I 
D:A,E,F,L
E:B,C,D,M,L
F:A,B,C,D,E,O,M
G:A,C,D,E,F
H:A,C,D,E,O
I:A,O
J:B,O
K:A,C,D
L:D,E,F
M:E,F,G
O:A,H,I,J
~~~

求出哪些人两两之间有共同好友，及他俩的共同好友都有谁？

### 4.2 实现步骤

##### 第一步：代码实现

**Mapper类**

~~~java
public class Step1Mapper extends Mapper<LongWritable,Text,Text,Text> {
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
         //1:以冒号拆分行文本数据: 冒号左边就是V2
        String[] split = value.toString().split(":");
        String userStr = split[0];

        //2:将冒号右边的字符串以逗号拆分,每个成员就是K2
        String[] split1 = split[1].split(",");
        for (String s : split1) {
            //3:将K2和v2写入上下文中
            context.write(new Text(s), new Text(userStr));
        }
    }
}
~~~

**Reducer类:**

~~~java
public class Step1Reducer extends Reducer<Text,Text,Text,Text> {    @Override    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {        //1:遍历集合,并将每一个元素拼接,得到K3        StringBuffer buffer = new StringBuffer();        for (Text value : values) {            buffer.append(value.toString()).append("-");        }        //2:K2就是V3        //3:将K3和V3写入上下文中        context.write(new Text(buffer.toString()), key);    }}
~~~

**JobMain:**

~~~java
public class JobMain extends Configured implements Tool {    @Override    public int run(String[] args) throws Exception {        //1:获取Job对象        Job job = Job.getInstance(super.getConf(), "common_friends_step1_job");        //2:设置job任务            //第一步:设置输入类和输入路径            job.setInputFormatClass(TextInputFormat.class);            TextInputFormat.addInputPath(job, new Path("file:///D:\\input\\common_friends_step1_input"));            //第二步:设置Mapper类和数据类型            job.setMapperClass(Step1Mapper.class);            job.setMapOutputKeyClass(Text.class);            job.setMapOutputValueClass(Text.class);            //第三,四,五,六            //第七步:设置Reducer类和数据类型            job.setReducerClass(Step1Reducer.class);            job.setOutputKeyClass(Text.class);            job.setOutputValueClass(Text.class);            //第八步:设置输出类和输出的路径            job.setOutputFormatClass(TextOutputFormat.class);            TextOutputFormat.setOutputPath(job, new Path("file:///D:\\out\\common_friends_step1_out"));        //3:等待job任务结束        boolean bl = job.waitForCompletion(true);        return bl ? 0: 1;    }    public static void main(String[] args) throws Exception {        Configuration configuration = new Configuration();        //启动job任务        int run = ToolRunner.run(configuration, new JobMain(), args);        System.exit(run);    }}
~~~

##### 第二步：代码实现

**Mapper类**

```java
public class Step2Mapper extends Mapper<LongWritable,Text,Text,Text> {    /*     K1           V1     0            A-F-C-J-E-	B    ----------------------------------     K2             V2     A-C            B     A-E            B     A-F            B     C-E            B     */    @Override    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {        //1:拆分行文本数据,结果的第二部分可以得到V2        String[] split = value.toString().split("\t");        String   friendStr =split[1];        //2:继续以'-'为分隔符拆分行文本数据第一部分,得到数组        String[] userArray = split[0].split("-");        //3:对数组做一个排序        Arrays.sort(userArray);        //4:对数组中的元素进行两两组合,得到K2        /*          A-E-C ----->  A  C  E          A  C  E            A  C  E         */        for (int i = 0; i <userArray.length -1 ; i++) {            for (int j = i+1; j  < userArray.length ; j++) {                //5:将K2和V2写入上下文中                context.write(new Text(userArray[i] +"-"+userArray[j]), new Text(friendStr));            }        }    }}
```

**Reducer类:**

```java
public class Step2Reducer extends Reducer<Text,Text,Text,Text> {    @Override    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {        //1:原来的K2就是K3        //2:将集合进行遍历,将集合中的元素拼接,得到V3        StringBuffer buffer = new StringBuffer();        for (Text value : values) {            buffer.append(value.toString()).append("-");                    }        //3:将K3和V3写入上下文中        context.write(key, new Text(buffer.toString()));    }}
```

**JobMain:**

```java
public class JobMain extends Configured implements Tool {    @Override    public int run(String[] args) throws Exception {        //1:获取Job对象        Job job = Job.getInstance(super.getConf(), "common_friends_step2_job");        //2:设置job任务            //第一步:设置输入类和输入路径            job.setInputFormatClass(TextInputFormat.class);            TextInputFormat.addInputPath(job, new Path("file:///D:\\out\\common_friends_step1_out"));            //第二步:设置Mapper类和数据类型            job.setMapperClass(Step2Mapper.class);            job.setMapOutputKeyClass(Text.class);            job.setMapOutputValueClass(Text.class);            //第三,四,五,六            //第七步:设置Reducer类和数据类型            job.setReducerClass(Step2Reducer.class);            job.setOutputKeyClass(Text.class);            job.setOutputValueClass(Text.class);            //第八步:设置输出类和输出的路径            job.setOutputFormatClass(TextOutputFormat.class);            TextOutputFormat.setOutputPath(job, new Path("file:///D:\\out\\common_friends_step2_out"));        //3:等待job任务结束        boolean bl = job.waitForCompletion(true);        return bl ? 0: 1;    }    public static void main(String[] args) throws Exception {        Configuration configuration = new Configuration();        //启动job任务        int run = ToolRunner.run(configuration, new JobMain(), args);        System.exit(run);    }}
```





