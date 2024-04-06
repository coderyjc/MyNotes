## MySQL-表的创建

### 创建表

建表语句的语法格式：

```sql
create table 表名(
    字段名1 数据类型,
    字段名2 数据类型,
    字段名3 数据类型,
    ....
);
```

关于MySQL当中字段的数据类型？以下只说常见的

- int 整数型(java中的int)
- bigint 长整型(java中的long)
- float 浮点型(java中的float double)
- char 定长字符串(String)
- varchar 可变长字符串(StringBuffer/StringBuilder) 理论上最大为65532字节
- date 日期类型 （对应Java中的java.sql.Date类型）
- BLOB 二进制大对象（存储图片、视频等流媒体信息） Binary Large OBject （对应java中的Object）
- CLOB 字符大对象（存储较大文本，比如，可以存储4G的字符串。） Character Large OBject（对应java中的Object）
- ......

**char和varchar怎么选择？**

- 在实际的开发中，当某个字段中的数据长度不发生改变的时候，是定长的，例如：性别、生日等都是采用char。
- 当一个字段的数据长度不确定，例如：简介、姓名等都是采用varchar。

建议：表名在数据库当中一般建议以：t_ 或者 tbl_ 开始

```sql

创建学生表：

学生信息包括：
    学号、姓名、性别、班级编号、生日
    学号：bigint
    姓名：varchar
    性别：char
    班级编号：int
    生日：char

create table t_student(
    no bigint,
    name varchar(255),
    sex char(1),
    classno varchar(255),
    birth char(10)
);

```

### 插入数据

语法格式：

```sql
insert into 表名(字段名1,字段名2,字段名3,....) values(值1,值2,值3,....)
```

- 要求：字段的数量和值的数量相同，并且数据类型要对应相同。

注意:

- 如果不指定值，则默认为NULL
- insert语句只要执行成功，数据库中必然多一条记录
- 即使多的这一行记录当中某些字段是NULL，后期也没有办法在执行
- insert语句插入数据了，只能使用update进行更新
- 字段可以省略不写，但是后面的value对数量和顺序都要按照表的创建顺序来写
- 也可以以此插入多行数据，`insert into <表名> (参数) value(值),(值)...`

表的复制和批量插入

将查询结果当做表创建出来。

```sql
create table 表名 as select语句;
```

将查询结果插入到一张表中

```sql
insert into <目标表名> select * from <查询表名>;
```

### 修改数据

语法格式：

```sql
update 表名 set 字段名1=值1,字段名2=值2... where 条件;
```

更新所有记录

```sql
update <表名> set 字段 = 值，字段 = 值, ... ;
```

注意：没有条件整张表数据全部更新。

案例：将部门10的LOC修改为SHANGHAI，将部门名称修改为RENSHIBU

```sql
update dept1 set loc = 'SHANGHAI', dname = 'RENSHIBU' where deptno = 10;
```

### 删除数据

delete删除之后还可以再回来，效率比较低，适合删小表
truncate删了之后回不来了，**删之前必须多次确认**，效率高，适合删大型表

语法格式：

```sql
delete from 表名 where 条件;
```

注意：没有条件全部删除。

删除10部门数据？

```sql
delete from dept1 where deptno = 10;
```

删除所有记录？

```sql
delete from dept1;
```

怎么删除大表？（重点）

```sql
truncate table 表名; // 表被截断，不可回滚。 永久丢失。
```

对于表结构的修改，这里不讲了，大家使用工具完成即可，因为在实际开发中表一旦设计好之后，对表结构的修改是很少的，修改表结构就是对之前的设计进行了否定，即使需要修改表结构，我们也可以直接使用工具操作。修改表结构的语句不会出现在Java代码当中。
出现在java代码当中的sql包括：insert delete update select（这些都是表中的数据操作。）

增删改查有一个术语：CRUD操作

Create（增） Retrieve（检索） Update（修改） Delete（删除）