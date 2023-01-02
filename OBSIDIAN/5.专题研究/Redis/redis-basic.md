#数据库/Redis

## NoSQL

### 结构化与非结构化

传统关系型数据库是结构化数据，每一张表都有严格的约束信息：字段名.字段数据类型.字段约束等等信息，插入的数据必须遵守这些约束。

![[assets/Pasted image 20230102094733.png]]

而NoSql则对数据库格式没有严格约束，往往形式松散，自由。可以是键值型、也可以是文档型、甚至可以是图格式

![[assets/Pasted image 20230102094800.png]]

![[assets/Pasted image 20230102094809.png]]

![[assets/Pasted image 20230102094815.png]]

### 关联和非关联

传统数据库的表与表之间往往存在关联，例如外键

![[assets/Pasted image 20230102094833.png]]

非关系型数据库不存在关联关系，要维护关系要么靠**代码中的业务逻辑**，要么靠**数据之间的耦合**

### 查询方式

传统关系型数据库会基于Sql语句做查询，语法有统一标准

而不同的非关系数据库查询语法差异极大，五花八门各种各样

![[assets/Pasted image 20230102094950.png]]

### 事务

传统关系型数据库能满足事务ACID的原则，而非关系型数据库往往不支持事务，或者不能严格保证ACID的特性，只能实现基本的一致性。

![[assets/Pasted image 20230102095054.png]]

- 存储方式
  - 关系型数据库基于磁盘进行存储，会有大量的磁盘IO，对性能有一定影响
  - 非关系型数据库，他们的操作更多的是依赖于内存来操作，内存的读写速度会非常快，性能自然会好一些
- 扩展性
  - 关系型数据库集群模式一般是主从，主从数据一致，起到数据备份的作用，称为垂直扩展。
  - 非关系型数据库可以将数据拆分，存储在不同机器上，可以保存海量数据，解决内存大小有限的问题。称为水平扩展。
  - 关系型数据库因为表之间存在关联关系，如果做水平扩展会给数据查询带来很多麻烦

## 概述

### 认识Redis

Redis诞生于2009年全称是**Re**mote **D**ictionary **S**erver 远程词典服务器，是一个基于内存的键值型NoSQL数据库。

**特征**：

- 键值（key-value）型，value支持多种不同数据结构，功能丰富
- 单线程，每个命令具备原子性
- 低延迟，速度快（基于内存.IO多路复用.良好的编码）。
- 支持数据持久化
- 支持主从集群.分片集群
- 支持多语言客户端

**作者**：Antirez

Redis的官方网站地址：<https://redis.io/>

## 安装

[[redis-install]]

## 常用命令

常见命令可以在[官网](https://redis.io/commands)查询

![[assets/Pasted image 20230102153939.png]]

也可以在终端使用help命令进行查询

```bash
127.0.0.1:6379> help
redis-cli 6.2.6
To get help about Redis commands type:
      "help @<group>" to get a list of commands in <group>
      "help <command>" for help on <command>
      "help <tab>" to get a list of possible help topics
      "quit" to exit

To set redis-cli preferences:
      ":set hints" enable online hints
      ":set nohints" disable online hints
Set your preferences in ~/.redisclirc
```

### 通用命令

通用指令是部分数据类型的，都可以使用的指令，常见的有：

- KEYS：查看符合模板的所有key
- DEL：删除一个指定的key
- EXISTS：判断key是否存在
- EXPIRE：给一个key设置有效期，有效期到期时该key会被自动删除
- TTL：查看一个KEY的剩余有效期

### String命令

String类型，也就是字符串类型，是Redis中最简单的存储类型。

其value是字符串，不过根据字符串的格式不同，又可以分为3类：

- string：普通字符串
- int：整数类型，可以做自增.自减操作
- float：浮点类型，可以做自增.自减操作

String的常见命令有：

- SET：添加或者修改已经存在的一个String类型的键值对
- GET：根据key获取String类型的value
- MSET：批量添加多个String类型的键值对
- MGET：根据多个key获取多个String类型的value
- INCR：让一个整型的key自增1
- INCRBY:让一个整型的key自增并指定步长，例如：incrby num 2 让num值自增2
- INCRBYFLOAT：让一个浮点类型的数字自增并指定步长
- SETNX：添加一个String类型的键值对，前提是这个key不存在，否则不执行
- SETEX：添加一个String类型的键值对，并且指定有效期

> [!note]
> 以上命令除了INCRBYFLOAT 都是常用命令


---

- SET 和GET: 如果key不存在则是新增，如果存在则是修改

```bash
127.0.0.1:6379> set name jancoyan // 原来不存在就是添加
OK
127.0.0.1:6379> get name
"jancoyan"
127.0.0.1:6379> set name janco // 原来存在就是修改
OK
127.0.0.1:6379> get name
"janco"
```

- MSET MGET

```bash
127.0.0.1:6379> mset k1 v1 k2 v2 k3 v3 // 批量设置
OK
127.0.0.1:6379> mget name k1 k2 k3 // 批量获取
1) "janco"
2) "v1"
3) "v2"
4) "v3"
```

-   INCR和INCRBY和DECY

```bash
127.0.0.1:6379> get age 
"10"
127.0.0.1:6379> incr age //增加1
(integer) 11
127.0.0.1:6379> get age //获得age
"11"
127.0.0.1:6379> incrby age 2 //一次增加2
(integer) 13 //返回目前的age的值
127.0.0.1:6379> incrby age 2
(integer) 15
127.0.0.1:6379> incrby age -1 //也可以增加负数，相当于减
(integer) 14
127.0.0.1:6379> incrby age -2 //一次减少2个
(integer) 12
127.0.0.1:6379> DECR age //相当于 incr 负数，减少正常用法
(integer) 11
127.0.0.1:6379> get age 
"11"
```

-   SETNX

```bash
127.0.0.1:6379> help setnx

  SETNX key value
  summary: Set the value of a key, only if the key does not exist
  since: 1.0.0
  group: string

127.0.0.1:6379> set name Jack  //设置名称
OK
127.0.0.1:6379> setnx name lisi //如果key不存在，则添加成功
(integer) 0
127.0.0.1:6379> get name //由于name已经存在，所以lisi的操作失败
"Jack"
127.0.0.1:6379> setnx name2 lisi //name2 不存在，所以操作成功
(integer) 1
127.0.0.1:6379> get name2 
"lisi"
```

-   SETEX

```bash
127.0.0.1:6379> setex name 10 jack
OK
127.0.0.1:6379> ttl name
(integer) 8
127.0.0.1:6379> ttl name
(integer) 7
127.0.0.1:6379> ttl name
(integer) 5
```

### Key的层级结构

Redis没有类似MySQL中的Table的概念，我们该如何区分不同类型的key呢？

例如，需要存储用户.商品信息到redis，有一个用户id是1，有一个商品id恰好也是1，此时如果使用id作为key，那就会冲突了，该怎么办？

我们可以通过给key添加前缀加以区分，不过这个前缀不是随便加的，有一定的规范：

Redis的key允许有多个单词形成层级结构，多个单词之间用':'隔开，格式如下：

```
项目名：业务名：类型：id
```
这个格式并非固定，也可以根据自己的需求来删除或添加词条。

例如我们的项目名称叫 heima，有user和product两种不同类型的数据，我们可以这样定义key：

-   user相关的key：**heima:user:1**
-   product相关的key：**heima:product:1**

如果Value是一个Java对象，例如一个User对象，则可以将对象序列化为JSON字符串后存储：

| **KEY**         | **VALUE**                                 |
| --------------- | ----------------------------------------- |
| heima:user:1    | {"id":1, "name": "Jack", "age": 21}       |
| heima:product:1 | {"id":1, "name": "小米11", "price": 4999} |

一旦我们向redis采用这样的方式存储，那么在可视化界面中，redis会以层级结构来进行存储，形成类似于这样的结构，更加方便Redis获取数据

![[assets/Pasted image 20230102155543.png]]

### Hash命令






### List命令



### Set命令



### SortedSet类型



## Java客户端-Jedis



##

