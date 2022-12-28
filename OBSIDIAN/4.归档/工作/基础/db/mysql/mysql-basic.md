# MySQL基础

## 准备工作

### 安装与登录

数据库登录：

- cmd 打开命令行之后 用 mysql -uroot -p密码（直接输）输入密码是明文
- 或者 mysql -uroot -p 回车，然后出来“enter password” 再输密码是密文***

数据库忘记密码怎么办？

方法1：用SET PASSWORD命令
首先登录MySQL
格式：mysql->set password for 用户名@localhost = password（'新密码1'）;
例子：mysql>set password for root@localhost = password（'1231'）；

方法2：用mysqladmin
格式：mysqladmin -u用户名 -p 旧密码 password 新密码
例子：mysqladmin-uroot-p123456 password 123

方法3：用UPDATE直接编辑user表
首先登录MySQL。
mysql> use mysql；
mysql> update user set password=password（'123'）where user= 'root' and host = 'localhost'；
mysql> flush privileges；

方法4：在忘记root密码的时候，可以这样

以windows为例：

1.关闭正在运行的MysqL服务。

2.打开Dos窗口，转到mysql\bin目录。

3.输入mysqld --skip-grant-tables 回车。--skip-grant-tables的意思是启动MysQL服务的时候跳过权限表认证。

4.再开一个Dos窗口（因为刚才那个Dos窗口已经不能动了），转到mysql\bin目录。

5.输入myscql回车，如果成功，将出现MySQL提示符>。

6.连接权限数据库：use mysql；

6.改密码：update user set password = password（"123"）where user="root"；（别忘了最后加分号）。

7.刷新权限（必须步骤）：flush privileges；

8.退出quit。

9.注销系统，再进入，使用用户名root和刚才设置的新密码123登录。

如何卸载？
- 在安装的时候，那个安装程序会有一个remove选项，先remove了
- 然后C盘下的program filesx86下面有一个mySQL文件夹，要强行删除
- 然后C盘的隐藏目录有一个programData，有个MySQL文件夹，删除了

### 认识MySQL

MySQL

1、sql、DB、DBMS分别是什么，他们之间的关系？

- DB：
  - DataBase（数据库，数据库实际上在硬盘上以文件的形式存在）

- DBMS：
  - DataBase Management System（数据库管理系统，常见的有：MysQL oracle DB2 Sybase sqlserver...）

- SQL：
  - 结构化查询语言，是一门标准通用的语言。标准的sql适合于所有的数据库产品。
  - SQL属于高级语言。只要能看懂英语单词的，写出来的sql语句，可以读懂什么意思。
  - SQL语句在执行的时候，实际上内部也会先进行编译，然后再执行sql。（sql语句的编译由DBMS完成。）DBMS负责执行sq1语句，通过执行sq1语句来操作DB当中的数据。
  - DBMS->（执行）->SQL-（操作）->DB

2、什么是表？

表：table

表：table是数据库的基本组成单元，所有的数据都以表格的形式组织，目的是可读性强。

一个表包括行和列：

- 行：被称为数据/记录（data）
- 列：被称为字段（column）

每一个字段应该包括哪些属性？

字段名、数据类型、相关的约束。

3、SQL语句怎么分类呢？

- DQL（数据查询语言）：查询语句，凡是select语句都是DQL。
- DML（数据操作语言）：insert delete update，对表当中的数据进行增删改。
- DDL（数据定义语言）：create drop alter，对表结构的增删改。
- TCIL（事务控制语言）：commit提交事务，rollback回滚事务。（rcL中的T是Transaction）
- DCL（数据控制语言）：grant授权、revoke撤销权限等。

4、导入数据（后期大家练习的时候使用这个演示的数据）

第一步：登录mysq1数据库管理系统
dos命令窗口：
	- mysql -uroot -p333

第二步：查看有哪些数据库
show databases；（这个不是sQu语句，属于MysQL的命令。）
+-----------------------------------+
| Database                        |
+---------------------------------+
| information_schema   |
| mysql                             |
| performance_schema |
| test                                  |
+----------------------------------+

第三步：创建属于我们自己的数据库
create database bjpowernode；（这个不是SQL语句，属于MysQL的命令。）

第四步：使用bjpowernode数据
use bjpowernode；（这个不是SQL语句，属于MysQL的命令。）

第五步：查看当前使用的数据库中有哪些表？
show tables；（这个不是SQL语句，属于MysQL的命令。）

第六步：初始化数据
mysq1>source 文件拖过来
注意：数据初始化完成之后，有三张表：
+-----------------------------—-+
l Tables in bjpowernode I
+—------------------------------+
I dept                                  I
|emp                                  I
|salgrade                            I
+—------------------------------+

5、bjpowernode.sql'，这个文件以sql结尾，这样的文件被称为sql脚本”。什么是sc1脚本呢？

当一个文件的扩展名是.sql，并且该文件中编写了大量的slq语句，我们称这样的文件为sql脚本。
注意：直接使用source命令可以执行sql脚本。

sq1脚本中的数据量太大的时候，无法打开，请使用source命令完成初始化。

6、删库跑路 drop database bipowernode;

7、查看表结构：desc 表名字；

drop table if exists <表名>; // 当这个表存在的话删除。
drop table <表名>; // 删除表

mysql> desc emp;

9、常用命令

select database(); 查看当前使用的是哪个数据库

select version(); 查看mysql的版本号

\c 命令，结束一条语句

exit; 退出mySQL

10、查看创建表的语句 show create table <表名称>；

## 查询

### 简单的查询语句（DQL）

语法格式：

select 字段名1，字段名2，字段名3，....from表名；

提示：

- 任何一条sql语句以；结尾
- 不区分大小写

去重：在字段前面加上distinct 关键字

distinct关键字如果出现在所有字段的最前方，则去除所有记录联合起来的重复元素

查找所有工作：

-  select distinct job from emp;

统计岗位的数量

-  select count(distinct job) from emp;

查询员工的年薪？

- select ename，sal*12 from emp；

说明: 字段可以参与数学运算

给查询结果的列重命名：

- select ename, sal*12 as yearsal from emp;
- select ename, sal*12 yearsal from emp;

如果用中文的话，应该用单引号括起来 select ename, sal*12 as '年薪' from emp;

（mysql支持双引号，但是最好别用，因为标准的sql语句是单引号的）



查询所有字段：select * from emp； 平时可以用，实际开发中不能用（效率低）！

### 条件查询

语法格式：

- select 字段，字段... from 表名 where 条件;

查询工资等于5000的员工姓名：

- select ename from emp where **sal = 5000**；

查询史密斯的工资：

-  select sal from emp where **ename = 'smith'；**

查询工资不等于3000员工：

- select ename,sal from emp where sal **<>** 3000;
- select ename,sal from emp where sal **!>** 3000;

查询工资1000 - 3000之内的员工：

- select ename,sal from emp where sal **between** 1000 **and** 3000;
- select ename,sal from emp where sal >= 1000 and sal <= 3000;

- between and 使用的时候必须左小右大，否则会 empty set
- 还可以使用在字符方面 select ename,sal from emp where ename between 'A' and 'B'; 左闭右开

找出哪些人没有工资？

- 在数据库中NULL不是一个值，代表什么都没有，为空，空是一个值，不能用等号衡量，必须使用is null 或者 is not null

-  select ename,sal from emp where sal is null;
- select ename,sal from emp where sal = null;
- 有工资：select ename,sal from emp where sal is not null;

找出工作岗位是salesman或manager的员工：

- select ename,job from emp where job = 'manager' or job = 'salesman';

and和or联合起来用：找出薪资大于1000的并且部门编号是20或30部门的员工。

- 优先级：and > or
- 优先级不确定的时候加上小括号
-  select ename,sal from emp where sal > 3000 and （deptno = 20 or deptno = 30）;

in等同于or，查询工作岗位是manager和salesman 的员工：

- select ename,job from emp where job = 'salesman' or job = 'manager';
- select ename, job from emp where job in('salesman', 'manager');
- 注意：括号中的**不是区间**，而是具体的值

not in，不等于in中的值的，查询工资不是1000和5000的员工

-  select ename,sal from emp where sal not in(1000,5000)；

找出名字中含有A的（掌握两个符号：%：表示任意多个字符  __：表示任意一个字符）

- select ename from emp where ename like '%A%';

找出名字第二个字母是A的：

- select ename from emp where ename like '_A%';

找出名字中有下划线的（转义字符）：

- select ename from emp where ename like '%\ _%';

### 排序

按照工资升序找出名字和薪资(order by)：

- select ename,sal from emp order by sal;
- 默认升序-asc 升序；desc-降序

按照工资降序排列：

-  select ename,sal from emp order by sal desc;

按照工资降序，工资相同按照名字升序排列（多个字段排序，靠前的主导性大，前面相等才用到后面的）

- select ename,sal from emp order by sal desc, ename asc;

按照第一列排序（不建议这样， 不健壮）：

- select ename,sal from emp order by 1;（等于按照ename排序）

找出工作岗位是salesman的员工并且按照工资降序排列

- select ename,sal,job from emp where job='salesman' order by sal desc;

- 执行顺序： table name -> condition -> select -> order by

### 分组函数

**规定：在所有数据库中，只要表达式中有null，表达式的结果就一定是null**

分组函数（对一组数据进行操作），有且仅有5个：

- count 计数

- sum 求和

- avg 求平均

- max 最大值

- min 最小值

属于多行处理函数：输入多行，最终得到一个结果

单行处理函数：输入一行，输出一行

注意：分组函数自动忽略null，不用添加isnull函数



找出工资总和

- select sum(sal) from emp;

找出总人数

- select count(*) from emp;
- count(*) 不是统计某个字段中数据的个数，而是统计总记录条数，与某个字段无关
- count(comm) 统计comm字段中不对null的数据总量

计算每个员工的年薪（考虑到有null的情况）

- ifnull()空处理函数（单行处理函数）

- select ename,(sal+ifnull(comm,0))*12 as yearsal from emp;

找出工资高于平均工资的员工

- SQL语句规则：分组函数不能直接使用在where子句中
- 理解：group by 在where 后面执行，执行where的时候还没有“组”呢，而分组函数的执行首先要有“组”
- select ename,sal from emp where sal > (select avg(sal) from emp);




### 分组查询

#### group by

group by：按照某个字段或者某些字段进行分组

having : having是对分组之后的数据进行再次过滤。



案例：找出每个工作岗位的最高薪资。
- select max（sal）from emp group by job；

注意：<u>当一条sql语句中有group by 的话，select字段中只能有分组函数和分组字段。</u>

 ~~select ename,job,max(sal) from emp group by job;~~这句话在Oracle中报错（因为语法比较严谨），但是在mysql中能执行，但是**毫无意义**！因为ename是随机选中的。



注意：

- 分组函数一般都会和group by联合使用，这也是为什么它被称为分组函数的原因。

- 并且任何一个分组函数（count sum avg maxmin）都是在group by语句执行结束之后才会执行的。

- 当一条sql语句没有group by的话，整张表的数据会自成一组。



找出每个岗位的平均工资

-  select job,avg(sal) from emp group by job;

找出每个部门不同工作岗位的最高薪资

-  select deptno,job,max(sal) from emp group by job,deptno order by deptno;

#### having

建议：能用where的用where，不能就用having



找出每个部门的最高薪资，要求显示薪资大于2900的数据

- select deptno,max(sal) from emp group by deptno having max(sal) > 2900;
- 这种方式效率低，因为是都找出来之后，筛选大于2900的，不如在开始的时候就不对小于2900的进行筛选
- 即：select deptno,max(sal) from emp where sal > 2900 group by deptno;
- 能用where最好用where，不能的话用having

找出每个部门的平均薪资，要求显示薪资大于2000的数据

- 此时不能用where了就，因为是对分组函数的结果进行选择
-  select deptno,avg(sal) from emp group by deptno having avg(sal) > 2000;



**一个完整的DQL语句：select...from...where...group by...having...order by...**



### 连接查询

什么是连接查询 ？

- 在实际开发中，大部分的情况下都不是从单表中查询数据，一般都是多张表联合查询取出最终的结果。	在实际开发中，一般一个业务都会对应多张表，比如：学生和班级，起码两张表。学生和班级信息存储到一张表中，结果就像上面一样，数据会存在大量的重复，导致数据的冗余。

分类？

- 根据语法出现的年代来划分的话，包括：
	- SQL92（一些老的DBA可能还在使用这种语法。DBA：DataBase Administrator，数据库管理员）
	- SQL99（比较新的语法）
- 根据表的连接方式来划分，包括：
	- 内连接：
	  - 等值连接
	  - 非等值连接
	  - 自连接
	- 外连接：
		- 左外连接（左连接）
		- 右外连接（右连接）
		- 全连接（这个不讲，很少用！）

关于表的别名：

select e.ename,d.dname from emp e,dept d;

表的别名有什么好处？

- 第一：执行效率高。
- 第二：可读性好。

注意：以后写sql语句的时候都要开始起别名了



笛卡尔积现象

案例：找出每一个员工的部门名称，要求显示员工名和部门名。

- select ename,dname from emp,dept;

笛卡尔积现象：当两张表进行连接查询的时候，没有任何条件进行限制，最终的查询结果条数是两张表记录条数的

乘积。

怎样避免？加上条件进行过滤。

避免了笛卡尔积现象，会减少记录的匹配次数吗？ 不会，次数还是56次。只不过显示的是有效记录。

案例：找出每一个员工的部门名称，要求显示员工名和部门名。

- select e.ename,d.dname from emp e , dept d  where e.deptno = d.deptno; //SQL92，以后不用这样写



#### 内连接之等值连接

最大特点是：条件是等量关系。

案例：查询每个员工的部门名称，要求显示员工名和部门名。

sql92版：select e.ename,d.dname from emp e , dept d  where e.deptno = d.deptno;

我们主要用的是sql98版，因为98的更好

为什么98的更好？

- 连接条件和where条件分离了，使得代码结构更清晰了

```sql
	select
		e.ename,d.dname
	from
		emp e
	join
		dept d
	on
		e.deptno = d.deptno;
```

或者：

```sql
	// inner可以省略的，带着inner目的是可读性好一些。
	select
		e.ename,d.dname
	from
		emp e
	inner join
		dept d
	on
		e.deptno = d.deptno;
```

语法：
	...		A	join		B	on		连接条件	where		...

#### 内连接之非等值连接

最大的特点是：连接条件中的关系是非等量关系。

案例：找出每个员工的工资等级，要求显示员工名、工资、工资等级。

```sql
mysql> select e.ename,e.sal,s.grade
    -> from
    -> emp e
    -> inner join salgrade s
    -> on
    -> e.sal between s.losal and s.hisal;
```

#### 内连接之自连接


自连接：最大的特点是：一张表看做两张表。自己连接自己。

案例：找出每个员工的上级领导，要求显示员工名和对应的领导名。

```sql
员工的领导编号 = 领导的员工编号

select
	a.ename as '员工名',b.ename as '领导名'
from
	emp a
inner join
	emp b
on
	a.mgr = b.empno;
```

#### 外连接

什么是外连接，和内连接有什么区别？

内连接：

假设A和B表进行连接，使用内连接的话，凡是A表和B表能够匹配上的记录查询出来，这就是内连接。AB两张表没有主副之分，两张表是平等的。

外连接：

内连接查询的时候，能匹配上的数据才能显示出来

假设A和B表进行连接，使用外连接的话，AB两张表中有一张表是主表，一张表是副表，主要查询主表中的数据，捎带着查询副表，当副表中的数据没有和主表中的数据匹配上，副表自动模拟出NULL与之匹配。

外连接的分类？

- 左外连接（左连接）：表示左边的这张表是主表。
- 右外连接（右连接）：表示右边的这张表是主表。

左连接有右连接的写法，右连接也会有对应的左连接的写法。


案例：找出每个员工的上级领导？（所有员工必须全部查询出来。）

```sql

左连接写法：

select a.ename 'yuangong', b.ename 'boss'
from emp a
left outer join emp b
on a.mgr = b.empno;

右连接写法：

select a.ename 'yuangong', b.ename 'boss'
from emp b
right outer join emp a
on a.mgr = b.empno;

outer 可以省略
```

案例：找出哪个部门没有员工？

```sql

法一：

select
    d.*
from
    emp e
right join
    dept d
on
    e.deptno = d.deptno
where
    e.empno is null;

法二：

select d.dname, e.deptno
from dept d
 left outer join emp e
on d.deptno = e.deptno
where e.deptno is null;

```

三张表怎么连接查询？

语法:

```sql
....
        A
    join
        B
    join
        C
    on
        ...
```

案例：找出每一个员工的部门名称以及工资等级。

```sql

    表示：A表和B表先进行表连接，连接之后A表继续和C表进行连接。

    select
        e.ename,d.dname,s.grade
    from
        emp e
    join
        dept d
    on
        e.deptno = d.deptno
    join
        salgrade s
    on
        e.sal between s.losal and s.hisal;

```

案例：找出每一个员工的部门名称、工资等级、以及上级领导。

```sql

    select
        e.ename '员工',d.dname,s.grade,e1.ename '领导'
    from
        emp e
    join
        dept d
    on
        e.deptno = d.deptno
    join
        salgrade s
    on
        e.sal between s.losal and s.hisal
    left join
        emp e1
    on
        e.mgr = e1.empno;

```

### 子查询

什么是子查询？

    select语句当中嵌套select语句，被嵌套的select语句是子查询。

子查询可以出现在哪里？

select
    ..(select).
from
    ..(select).
where
    ..(select).


案例：找出高于平均薪资的员工信息。

- select * from emp where sal > (select avg(sal) from emp);

案例：找出每个部门平均薪水的等级。

```sql

第一步：找出每个部门平均薪水（按照部门编号分组，求sal的平均值）

select deptno,avg(sal) as avgsal from emp group by deptno;

第二步：将以上的查询结果当做临时表t，让t表和salgrade s表连接，条件是：t.avgsal between s.losal and s.hisal

select
    t.*,s.grade
from
    (select deptno,avg(sal) as avgsal from emp group by deptno) t
join
    salgrade s
on
    t.avgsal between s.losal and s.hisal;
```

案例：找出每个部门平均的薪水等级。

不是所有查询的都必须用子查询

```sql

第一步：找出每个员工的薪水等级。

select e.ename,e.sal,e.deptno,s.grade from emp e join salgrade s on e.sal between s.losal and s.hisal;

第二步：基于以上结果，继续按照deptno分组，求grade平均值。

select
    e.deptno,avg(s.grade)
from
    emp e
join
    salgrade s
on
    e.sal between s.losal and s.hisal
group by
    e.deptno;

```

案例：找出每个员工所在的部门名称，要求显示员工名和部门名。

```sql

select
    e.ename,d.dname
from
    emp e
join
    dept d
on
    e.deptno = d.deptno;

// 下面这种方法比较少用

select
    e.ename,(select d.dname from dept d where e.deptno = d.deptno) as dname
from
    emp e;
```

union（可以将查询结果集相加）

前提：两张表的列数相等

案例：找出工作岗位是SALESMAN和MANAGER的员工？

- 第一种：select ename,job from emp where job = 'MANAGER' or job = 'SALESMAN';

- 第二种：select ename,job from emp where job in('MANAGER','SALESMAN');

- 第三种：union

- 只要确定了两张表的查询结果一定不重复，就用UNION ALL， 因为查询效率高

select ename,job from emp where job = 'MANAGER'
union
select ename,job from emp where job = 'SALESMAN';

### limit（MySQL特有）

重点中的重点，以后分页查询全靠它了。

limit是mysql特有的，其他数据库中没有，不通用。（Oracle中有一个相同的机制，叫做rownum）

limit取结果集中的部分数据，这时它的作用。

语法机制：
    limit startIndex, length
        startIndex表示起始位置，从0开始，0表示第一条数据。
        length表示取几个

案例：取出工资前5名的员工（思路：降序取前5个）

- select ename,sal from emp order by sal desc;

取前5个：

- select ename,sal from emp order by sal desc limit 0, 5;
- select ename,sal from emp order by sal desc limit 5;

limit是sql语句最后执行的一个环节：

```sql

    select      5
        ...
    from        1
        ...
    where       2
        ...
    group by    3
        ...
    having      4
        ...
    order by    6
        ...
    limit       7
        ...;
```

案例：找出工资排名在第4到第9名的员工？

- select ename,sal from emp order by sal desc limit 3,6;

通用的标准分页sql？

每页显示3条记录：

第1页：0, 3
第2页：3, 3
第3页：6, 3

每页显示pageSize条记录：

第pageNo页：(pageNo - 1) * pageSize, pageSize
pageSize是什么？是每页显示多少条记录
pageNo是什么？显示第几页

```java

java代码{

    int pageNo = 2; // 页码是2
    int pageSize = 10; // 每页显示10条

    limit (pageNo - 1) * pageSize, pageSize

}

```

## 表的创建

创建表：

建表语句的语法格式：

create table 表名(
    字段名1 数据类型,
    字段名2 数据类型,
    字段名3 数据类型,
    ....
);

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

char和varchar怎么选择？

- 在实际的开发中，当某个字段中的数据长度不发生改变的时候，是定长的，例如：性别、生日等都是采用char。

- 当一个字段的数据长度不确定，例如：简介、姓名等都是采用varchar。

**表名在数据库当中一般建议以：t_ 或者 tbl_ 开始**

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

插入数据：

语法格式：

- insert into 表名(字段名1,字段名2,字段名3,....) values(值1,值2,值3,....)
- 要求：字段的数量和值的数量相同，并且数据类型要对应相同。

注意:

- 如果不指定值，则默认为NULL
- insert语句只要执行成功，数据库中必然多一条记录
- 即使多的这一行记录当中某些字段是NULL，后期也没有办法在执行
- insert语句插入数据了，只能使用update进行更新
- 字段可以省略不写，但是后面的value对数量和顺序都要按照表的创建顺序来写
- 也可以以此插入多行数据，insert into <表名> (参数) value(值),(值)...

表的复制和批量插入

将查询结果当做表创建出来。

- create table 表名 as select语句;


将查询结果插入到一张表中

- insert into <目标表名> select * from <查询表名>;


修改数据

语法格式：

- update 表名 set 字段名1=值1,字段名2=值2... where 条件;

更新所有记录

- update <表名> set 字段 = 值，字段 = 值, ... ;

注意：没有条件整张表数据全部更新。

案例：将部门10的LOC修改为SHANGHAI，将部门名称修改为RENSHIBU

- update dept1 set loc = 'SHANGHAI', dname = 'RENSHIBU' where deptno = 10;


删除数据

delete删除之后还可以再回来，效率比较低，适合删小表
truncate删了之后回不来了，**删之前必须多次确认**，效率高，适合删大型表

语法格式：

- delete from 表名 where 条件;

注意：没有条件全部删除。

删除10部门数据？

- delete from dept1 where deptno = 10;

删除所有记录？

- delete from dept1;

怎么删除大表？（重点）

- truncate table 表名; // 表被截断，不可回滚。 永久丢失。

对于表结构的修改，这里不讲了，大家使用工具完成即可，因为在实际开发中表一旦设计好之后，对表结构的修改是很少的，修改表结构就是对之前的设计进行了否定，即使需要修改表结构，我们也可以直接使用工具操作。修改表结构的语句不会出现在Java代码当中。
出现在java代码当中的sql包括：insert delete update select（这些都是表中的数据操作。）

增删改查有一个术语：CRUD操作

Create（增） Retrieve（检索） Update（修改） Delete（删除）


## 约束(Constraint)

什么是约束？

- 在创建表的时候，可以给表的字段添加相应的约束，添加约束的目的是为了保证表中数据的合法性、有效性、完整性。

常见的约束有哪些呢？

- 非空约束(not null)：约束的字段不能为NULL
- 唯一约束(unique)：约束的字段不能重复
- 主键约束(primary key)：约束的字段既不能为NULL，也不能重复（简称PK）
- 外键约束(foreign key)：...（简称FK）
- 检查约束(check)：注意Oracle数据库有check约束，但是mysql没有，目前mysql不支持该约束。


### 非空约束 not null

只有列级约束，没有表级约束

```sql
    drop table if exists t_user;
    create table t_user(
        id int,
        username varchar(255) not null,
        password varchar(255)
    );
```

### 唯一性约束(unique)

- 唯一性约束修饰的字段具有唯一性，不能重复。但可以为null。

案例：给某一列添加unique

```sql
      drop table if exists t_user;
      create table t_user(
        id int,
    username varchar(255) unique  //列级约束
    );
```

案例：给两个列或者多个列添加unique

```sql
    drop table if exists t_user;
    create table t_user(
        id int,
        usercode varchar(255),
        username varchar(255),
        unique(usercode,username)  //多个字段联合起来添加一个约束unique 【表级约束】
      );
```

注意：not null约束只有列级约束，没有表级约束。


### 主键约束

主键相关的术语？

- 主键约束 ：primary key
- 主键字段 : id字段添加primary key之后，id叫做主键字段
- 主键值 ：id字段中的每一个值都是主键值。

- 根据主键字段的字段数量来划分：

    - 单一主键 (推荐的，常用的。)
    - 复合主键(多个字段联合起来添加一个主键约束) (复合主键不建议使用，因为复合主键违背三范式。)

- 根据主键性质来划分：

    - 自然主键 ：主键值最好就是一个和业务没有任何关系的自然数。(这种方式是推荐的)
    - 业务主键 : 主键值和系统的业务挂钩，例如：拿着银行卡的卡号做主键、拿着身份证号做为主键。(不推荐使用)最好不要拿着和业务挂钩的字段做为主键。因为以后的业务一旦发生改变的时候，主键也可能需要随着发生变化，但有的时候没有办法变化，因为变化可能会导致主键重复。

**一张表的主键约束只能有1个**


给一张表添加主键约束

```sql
    drop table if exists t_user;
    create table t_user(
        id int primary key,  //列级约束
        username varchar(255),
        email varchar(255)
    );
```

使用表级约束方式定义主键

```sql
drop table if exists t_user;
create table t_user(
    id int,
    username varchar(255),
    primary key(id)
);

```

mysql提供主键值自增(非常重要。)
```sql
    drop table if exists t_user;
    create table t_user(
        id int primary key auto_increment,  //id字段自动维护一个自增的数字，从1开始，以1递增。
        username varchar(255)
    );
```

提示：Oracle当中也提供了一个自增机制，叫做：序列(sequence)对象。


### 外键约束

关于外键约束的相关术语：

- 外键约束：foreign key
- 外键字段：添加有外键约束的字段
- 外键值：外键字段中的每一个值。

注意：

- 删除数据的时候，先删除子表，再删除父表。
- 添加数据的时候，先添加父表，再添加子表。
- 创建表的时候，先创建父表，再创建子表。
- 删除表的时候，先删除子表，再删除父表。

外键值可以为NULL？外键可以为null。

外键字段引用其他表的某个字段的时候，被引用的字段必须是主键吗？

- 注意：被引用的字段不一定是主键，但至少是具有unique约束，具有唯一性，不可重复！

```sql
create table t_class(
        cno int,
        cname varchar(255),
        primary key(cno)
     );

create table t_student(
        sno int,
        sname varchar(255),
        classno int,
        primary key(sno),
        foreign key(classno) references t_class(cno)
    );

tstudent中的classno字段引用tclass表中的cno字段，此时tstudent表叫做子表。tclass表叫做父表。

```


## 事务(Transaction)

什么是事务？ 一个事务是一个完整的业务逻辑单元，不可再分。

比如：银行账户，从A账户向B账户转账10000元，需要执行两条update语句。

`update t_act set balance = balance - 10000 where actno = 'act-001';`
`update t_act set balance = balance + 10000 where actno = 'act-002';`

以上两条DML语句必须同时成功，或者同时失败，不允许出现一条成功，一条失败。

想要保证以上的两条DML语句同时成功或者同时失败，那么就要使用数据库的"事务机制"。

和事务相关的语句只有：DML语句。(insert delete update)

为什么？因为他们这三个语句都是和数据库表当中的"数据"相关的。

事务的存在是为了保证数据的完整性，安全性。

假设所有的业务都能使用1条DML语句搞定，还需要事务机制吗？不需要事务机制。

但实际情况不是这样的，通常一个"事儿(事务【业务】)"需要多条DML语句共同联合完成。

事务的特性？事务包括四大特性：ACID

- A:原子性：事务是最小的工作单元，不可再分。
- B:一致性：事务必须保证多条DML语句同时成功或者同时失败。
- C:隔离性：事务A与事务B之间具有隔离。
- D:持久性：持久性说的是最终数据必须持久化到硬盘中，事务才算成功结束。

### 事务的隔离性

事务隔离性存在隔离级别，理论上隔离级别包括4个：

- 第一级别：读未提交(read uncommitted)
    - 对方事务还没有提交，我们当前事务可以读取到对方未提交的数据。
    - 读未提交存在脏读(Dirty Read) 现象：表示读到了脏数据。
- 第二级别：读已提交(read committed)
    - 对方事务提交之后的数据我方可以读取到。
    - 读已提交存在的问题是：不可重复读。
- 第三级别：可重复读(repeatable read)
    - 这种隔离级别解决了：不可重复读问题。
    - 这种隔离级别存在的问题是：读取到的数据是幻象。
- 第四级别：序列化读/串行化读
    - 解决了所有问题。
    - 效率低，需要事务排队。

Oracle数据库默认的隔离级别是：第二级别，读已提交。

mysql数据库默认的隔离级别是：第三级别，可重复读。


### 演示事务

mysql事务默认情况下是自动提交的。(什么是自动提交？只要执行任意一条DML语句则提交一次。)

怎么关闭默认提交？start transaction;

- rollback : 回滚。
- commit ： 提交。
- start transaction : 关闭自动提交机制。

演示两个事务，假如隔离级别：
- 演示第一级别：读未提交 set global transaction isolation level read uncommitted;
- 演示第二级别；读已提交 set global transaction isolation level read committed;
- 演示第三级别:可重复读 set global transaction isolation level repeatable read;

mysql远程登录：mysql -h192.168.151.18 -uroot -p444


## 索引

什么是索引？ 索引就相当于一本书的目录，通过目录可以快速的找到对应的资源。

在数据库方面，查询一张表的时候有两种检索方式：

- 第一种方式：全表扫描
- 第二种方式：根据索引检索(效率很高)

索引为什么可以提高检索效率呢？ 最根本的原理是缩小了扫描的范围。

- 索引虽然可以提高检索效率，但是不能随意的添加索引，因为索引也是数据库当中的对象，也需要数据库不断的维护。是有维护成本的。
- 比如：表中的数据经常被修改，这样就不适合添加索引，因为数据一旦修改，索引需要重新排序，进行维护。

- 添加索引是给某一个字段，或者说某些字段添加索引。

select ename,sal from emp where ename = 'SMITH';
当ename字段没有添加索引的时候，以上sql语句会进行全表扫描，扫描ename字段中所有的值。
当ename字段添加索引的时候，以上sql语句会根据索引扫描，快速定位。

怎么创建索引对象？怎么删除索引对象？

- 创建索引对象： create index 索引名称 on 表名(字段名);
- 删除索引对象： drop index 索引名称 on 表名;

什么时候考虑给字段添加索引？(满足什么条件)

- 数据量庞大。(根据客户的需求，根据线上的环境)
- 该字段很少的DML操作。(因为字段进行修改操作，索引也需要维护)
- 该字段经常出现在where子句中。(经常根据哪个字段维护)

注意：主键具有unique约束的字段会自动添加索引。根据主键查询效率较高，尽量根据主键检索。


查看sql语句的执行计划（只有MySQL才有）：
- explain select ename,sal from emp where sal = 5000;

给薪资sal字段添加索引：
- create index empindex on emp(sal);

mysql> explain select ename,sal from emp where sal = 5000;

rows检索次数减少了

索引的实现原理？

- 索引底层采用的数据结构是：B + Tree

- 通过B Tree缩小扫描范围，底层索引进行了排序，分区，索引会携带数据在表中的"物理地址"，最终通过索引检索到数据之后，获取到关联的物理地址，通过物理索引检索到数据之后，获取到关联的物理地址，通过物理地址定位表中的数据，效率是最高的。

select ename from emp where ename = 'SMITH';
通过索引转换为：
select ename from emp where  物理地址 = 0x123;

索引的分类？

- 单一索引：给单个字段添加索引
- 复合索引：给多个字段联合起来添加一个索引
- 主键索引：主键上会自动添加索引
- 唯一索引：有unique约束的字段会自动添加索引
- ......

索引什么时候失效？

- select ename from emp where ename like ' %A% ';
- 模糊查询的时候，第一个通配符使用的是%，这个时候索引是是失效的。

## 视图(view)

什么是视图？ 站在不同的角度去看到数据。(同一张表的数据，通过不同的角度去看待)

怎么创建视图？ create view myview as select empno, ename from emp;
怎么删除视图？ drop view myview;

注意：只有DQL语句才能以试图对象的方式创建出来。

对视图进行增删改查，会影响到原表数据。(通过视图影响原表数据，不是直接操作的原表)
可以对视图进行CRUD操作。

面向视图操作？

- select * from myview;
```sql
create table emp_bak as select * from emp;
create view myview1 as select empno,ename,sal from emp_bak;
update myview1 set ename = 'hehe',sal = 1 where empno 7369;  //通过视图修改原表数据。
delete from myview1 where empno = 7369;  //通过试图删除原表数据。
```

视图的作用？

- 视图可以隐藏表的实现细节。保密级别较高的系统，数据库只对外提供相关的视图，java程序员只对视图对象进行CRUD。

视图并不会提高检索效率


## 数据库设计三范式

什么是设计范式？ 设计表的依据。按照这三个范式设计的表不会出现数据冗余。

三范式都是哪些？

- 第一范式：任何一张表都应该有主键，并且每一个字段原子性不可再分。

- 第二范式：建立在第一范式的基础上，所有非主键字段完全依赖主键，不能产生部份依赖。
        多对多？三张表，关系表两个外键。

- 第三范式：建立在第二范式的基础上，所有非主键字段直接依赖主键，不能产生传递依赖。
        一对多？两张表，多的表加外键。

提醒：在实际的开发中，以满足客户需求为主，有的时候会拿冗余换执行速度。

一对一怎么设计？ 一对一设计有两种方案：主键共享/外键唯一

## 存储引擎（了解）

完整的建表语句
```sql
CREATE TABLE `t_x` (
      `id` int(11) DEFAULT NULL
     ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

**注意：在MySQL当中，凡是标识符使用飘号括起来的。最好别用，不通用。**

建表的时候可以指定存储引擎，也可以指定字符集。

mysql默认使用的存储引擎是InnoDB方式。默认采用的字符集是UTF-8。（开始的时候我们自己设置的）

什么是存储引擎?

- 存储引擎这个名字只有在mysql中存在。(Oracle中有对应的机制，但不叫做存储引擎。Oracle中没有特殊的名字，就是"表的存储方式")

mysql支持很多存储引擎，每个存储引擎都对应了一种不同的存储方式。
每一个存储引擎都有自己的优缺点，需要在合适的时机选择合适的存储引擎。

查看当前mysql支持的存储引擎？ show engines \G

mysql 5.5.36版本支持的光速引擎有9个


常见的存储引擎？
MyISAM
```sql
Engine: MyISAM
Support: YES
Comment: MyISAM storage engine
Transactions: NO
XA: NO
Savepoints: NO
```

MyISAM这种存储引擎不支持事务。

MyISAM是mysql最常用的存储引擎，但是这种存储引擎不是默认的。

MyISAM采用三个文件组织一个表

- xxx.frm(存储格式的文件)
- xxx.MYD(存储表中数据的文件)
- xxx.MYI(存储表中索引的文件)

优点：可被压缩，节省存储空间。并且可以转换为只读表，提高检索效率。

缺点: 不支持事务。

InnoDB
```sql
Engine: InnoDB
Support: DEFAULT
         Comment: Supports transactions, row-level locking, and foreign keys
    Transactions: YES
          XA: YES
      Savepoints: YES
```

优点：支持事务、行级锁、外键等。这种存储引擎数据的安全得到保障。

表的结构存储在xxx.frm文件中

数据存储在tablespace这样的表空间中(逻辑概念)，无法被压缩，无法转换成只读。

这种InnoDB存储引擎在MySQL数据库崩溃之后提供自动恢复机制。

InoDB支持级联删除和级联更新。

MEMORY
```sql
Engine: MEMORY
Support: YES
Comment: Hash based, stored in memory, useful for temporary tables
Transactions: NO
XA: NO
Savepoints: NO
```

缺点：不支持事务。数据容易丢失。因为所有数据和索引都是存储在内存当中的。

优点：查询速度最快。

以前叫做HEPA引擎。

## DBA命令（了解）

在数据库当中的数据导出

在windows的DOS命令窗口中执行： (导出整个库)

- mysqldump bjpowernode>D:\bjpowernode.sql -uroot -p999

在windows的dos命令窗口中执行：(导出数据库中指定的表)

- mysqldump bjpowernode emp>D:\bjpowernode.sql -uroot -p999

导入数据

- create database bjpowernode;
- use bjpowernode;
- source D:\bjpowernode.sql
