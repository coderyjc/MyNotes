
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



### 运行方式


