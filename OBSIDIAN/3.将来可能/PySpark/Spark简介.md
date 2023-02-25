
```ad-summary
【了解】Spark诞生背景
【了解】Spark的应用场景
```

## Spark是什么

定义：Apache Spark是用于 大规模数据（large-scala data ）处理的统一（unified ）分析引擎。其特点就是对任意类型的数据进行自定义计算。

![[assets/Pasted image 20230223204913.png]]

有点类似于mr

## 发展历程

Spark的发展历史，经历过几大重要阶段，如下图所示：

![[assets/Pasted image 20230223205501.png]]

Stack Overflow的数据可以看出，2015年开始Spark每月的问题提交数量已经超越Hadoop，而2018年Spark Python版本的API PySpark每月的问题提交数量也已超过Hadoop。2019年排名Spark第一，PySpark第二；而十年的累计排名是Spark第一，PySpark第三。

按照这个趋势发展下去，Spark和PySpark在未来很长一段时间内应该还会处于垄断地位。

![[assets/Pasted image 20230223205124.png]]

从图中可以看到，Spark如日中天，PySpark也在持续发力，并且在3.2.0中， PySpark增加了对Pandas的支持。

## Spark V.S. MapReduce

![[assets/Pasted image 20230223205305.png]]

- 从类型来说：Hadoop的计算来自于MR，存储来自于HDFS，调度来自于Yarn；SPark是纯计算工具
- 从场景来说，Hadoop是数据批处理框架，Spark是流-批一体的计算框架，除此之外，Spark还支持内存迭代计算和交互式计算。
- 价格如图
- 编程范式方面，Hadoop只有两个算子，Map和Reduce，适用面比较窄；而Spark RDD基于DAG，算子丰富，便于使用

尽管Spark相对于Hadoop而言具有较大优势，但Spark并不能完全替代Hadoop

- 在计算层面，Spark相比较MR（MapReduce）有巨大的性能优势，但至今仍有许多计算工具基于MR构架，比如非常成熟的Hive

- park仅做计算，而Hadoop生态圈不仅有计算（MR）也有存储（HDFS）和资源管理调度（YARN），HDFS和YARN仍是许多大数据体系的核心架构。

融合，而不是替代，只是替代了Hadoop的MR

## Spark四大特点

速度快、易于使用、通用性强、运行方式多样

![[assets/Pasted image 20230223210548.png]]

### 速度快

由于Apache Spark支持内存计算，并且通过DAG（有向无环图）执行引擎支持无环数据流，所以官方宣称其在内存中的运算速度要比Hadoop的MapReduce快100倍，在硬盘中要快10倍。

![[assets/Pasted image 20230223210909.png]]

Spark处理数据与MapReduce处理数据相比，有如下两个不同点：
- 其一、Spark处理数据时，可以将中间处理结果数据存储到内存中；
- 其二、Spark 提供了非常丰富的算子(API), 可以做到复杂任务在一个Spark 程序中完成

### 易于使用

Spark 的版本已经更新到 Spark 3.2.0（截止日期2021.10.13），支持了包括 Java、Scala、Python 、R和SQL语言在内的多种语言。

### 通用性强

在 Spark 的基础上，Spark 还提供了包括Spark SQL、Spark Streaming、MLib 及GraphX在内的多个工具库，我们可以在一个应用中无缝地使用这些工具库。

![[assets/Pasted image 20230223211012.png]]

### 运行方式

Spark 支持多种运行方式，包括在 Hadoop 和 Mesos 上，也支持 Standalone的独立运行模式，同时也可以运行在云Kubernetes（Spark2.3开始支持）上。

i、文件系统：LocalFS、HDFS、Hive、text、parquet、orc、json、csv
ii、数据库RDBMs： mysql、Oracle、mssql
iii、NOSQL数据库：HBase、ES、Redis
iv、消息对象：Kafka

对于数据源而言，Spark 支持从HDFS、HBase、Cassandra 及 Kafka 等多种途径获取数据。

## Spark框架模块

整个Spark 框架模块包含：Spark Core、 Spark SQL、 Spark Streaming、 Spark GraphX、 Spark MLlib，而后四项的能力都是建立在核心引擎之上

![[assets/Pasted image 20230223211158.png]]

Spark Core：Spark的核心，Spark核心功能均由Spark Core模块提供，是Spark运行的基础。Spark Core以RDD为数据抽象，提供Python、Java、Scala、R语言的API，可以编程进行海量离线数据批处理计算。

SparkSQL：基于SparkCore之上，提供结构化数据的处理模块。SparkSQL支持以SQL语言对数据进行处理，SparkSQL本身针对离线计算场景。同时基于SparkSQL，Spark提供了StructuredStreaming模块，可以以SparkSQL为基础，进行数据的流式计算。

SparkStreaming：以SparkCore为基础，提供数据的流式计算功能。

MLlib：以SparkCore为基础，进行机器学习计算，内置了大量的机器学习库和API算法等。方便用户以分布式计算的模式进行机器学习计算。

GraphX：以SparkCore为基础，进行图计算，提供了大量的图计算API，方便用于以分布式计算模式进行图计算。

## 运行模式

Spark提供多种运行模式，包括：

Local模式（单机）
- 本地模式就是以一个独立的进程，通过其内部的多个线程来模拟整个Spark运行时环境

Standalone模式（集群）
- Spark中的各个角色以独立进程的形式存在，并组成Spark集群环境

Hadoop YARN模式（集群）
- Spark中的各个角色运行在YARN的容器内部，并组成Spark集群环境

Kubernetes模式（容器集群）
- Spark中的各个角色运行在Kubernetes的容器内部，并组成Spark集群环境

云服务模式（运行在云平台上）


## 架构角色

### YARN角色回顾

YARN主要有4类角色，从2个层面去看：

资源管理层面
- 集群资源管理者（Master）：ResourceManager
- 单机资源管理者（Worker）：NodeManager

任务计算层面
- 单任务管理者（Master）：ApplicationMaster
- 单任务执行者（Worker）：Task（容器内计算框架的工作角色）

![[assets/Pasted image 20230223212601.png]]

### Spark运行角色

![[assets/Pasted image 20230223212702.png]]

![[assets/Pasted image 20230223212725.png]]


