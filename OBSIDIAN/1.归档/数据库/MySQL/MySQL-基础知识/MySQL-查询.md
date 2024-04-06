## MySQL-查询

### 简单的查询语句（DQL）

语法格式：

`select 字段名1，字段名2，字段名3，....from 表名；`

提示：

- 任何一条sql语句以；结尾
- 不区分大小写

去重：在字段前面加上distinct 关键字

distinct关键字如果出现在所有字段的最前方，则去除所有记录联合起来的重复元素

查找所有工作：

```sql
select distinct job from emp;
```

统计岗位的数量

```sql
select count(distinct job) from emp;
```

查询员工的年薪？

```sql
select ename，sal*12 from emp；
```

说明: 字段可以参与数学运算

给查询结果的列重命名：

```sql
select ename, sal*12 as yearsal from emp;
select ename, sal*12 yearsal from emp;
```

如果用中文的话，应该用单引号括起来 `select ename, sal*12 as '年薪' from emp;`

（mysql支持双引号，但是最好别用，因为标准的sql语句是单引号的）

查询所有字段：`select * from emp；` 平时可以用，实际开发中不能用（效率低）！

### 条件查询

语法格式：

```sql
select 字段，字段... from 表名 where 条件;
```

查询工资等于5000的员工姓名：

```sql
select ename from emp where **sal = 5000**；
```

查询史密斯的工资：

```sql
select sal from emp where **ename = 'smith'；**
```

查询工资不等于3000员工：

```sql
select ename,sal from emp where sal **<>** 3000;

select ename,sal from emp where sal **!>** 3000;
```

查询工资1000 - 3000之内的员工：

```sql
select ename,sal from emp where sal **between** 1000 **and** 3000;

select ename,sal from emp where sal >= 1000 and sal <= 3000;
```

- between and 使用的时候必须左小右大，否则会 empty set
- 还可以使用在字符方面` select ename,sal from emp where ename between 'A' and 'B'; `左闭右开

找出哪些人没有工资？

- 在数据库中NULL不是一个值，代表什么都没有，为空，空是一个值，不能用等号衡量，必须使用is null 或者 is not null

```sql
select ename,sal from emp where sal is null;

select ename,sal from emp where sal = null;
```

- 有工资：`select ename,sal from emp where sal is not null;`

找出工作岗位是salesman或manager的员工：

```sql
select ename,job from emp where job = 'manager' or job = 'salesman';
```

and和or联合起来用：找出薪资大于1000的并且部门编号是20或30部门的员工。

- 优先级：and > or
- 优先级不确定的时候加上小括号

```sql
select ename,sal from emp where sal > 3000 and （deptno = 20 or deptno = 30）;
```


in等同于or，查询工作岗位是manager和salesman 的员工：

```sql
select ename,job from emp where job = 'salesman' or job = 'manager';

select ename, job from emp where job in('salesman', 'manager');
```

- 注意：括号中的**不是区间**，而是具体的值

not in，不等于in中的值的，查询工资不是1000和5000的员工

```sql
select ename,sal from emp where sal not in(1000,5000)；
```

找出名字中含有A的（掌握两个符号：%：表示任意多个字符  __：表示任意一个字符）

```sql
select ename from emp where ename like '%A%';
```

找出名字第二个字母是A的：

```sql
select ename from emp where ename like '_A%';
```

找出名字中有下划线的（转义字符）：

```sql
select ename from emp where ename like '%\ _%';
```

### 排序

按照工资升序找出名字和薪资(order by)：

```sql
select ename,sal from emp order by sal;
```

- 默认升序-asc 升序；desc-降序

按照工资降序排列：

```sql
select ename,sal from emp order by sal desc;
```

按照工资降序，工资相同按照名字升序排列（多个字段排序，靠前的主导性大，前面相等才用到后面的）

```sql
select ename,sal from emp order by sal desc, ename asc;
```

按照第一列排序（不建议这样， 不健壮）：

```sql
select ename,sal from emp order by 1;（等于按照ename排序）
```

找出工作岗位是salesman的员工并且按照工资降序排列

```sql
select ename,sal,job from emp where job='salesman' order by sal desc;
```

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

```sql
select sum(sal) from emp;
```

找出总人数

```sql
select count(*) from emp;

count(*) 不是统计某个字段中数据的个数，而是统计总记录条数，与某个字段无关

count(comm) 统计comm字段中不对null的数据总量
```

计算每个员工的年薪（考虑到有null的情况）

- ifnull()空处理函数（单行处理函数）

```sql
select ename,(sal+ifnull(comm,0))*12 as yearsal from emp;
```

找出工资高于平均工资的员工

- SQL语句规则：分组函数不能直接使用在where子句中
- 理解：group by 在where 后面执行，执行where的时候还没有“组”呢，而分组函数的执行首先要有“组”

```sql
select ename,sal from emp where sal > (select avg(sal) from emp);
```

### 分组查询

#### group by

group by：按照某个字段或者某些字段进行分组

having : having是对分组之后的数据进行再次过滤。

案例：找出每个工作岗位的最高薪资。

```sql
select max（sal）from emp group by job；
```

注意：<u>当一条sql语句中有group by 的话，select字段中只能有分组函数和分组字段。</u>

 ~~select ename,job,max(sal) from emp group by job;~~这句话在Oracle中报错（因为语法比较严谨），但是在mysql中能执行，但是**毫无意义**！因为ename是随机选中的。

注意：

- 分组函数一般都会和group by联合使用，这也是为什么它被称为分组函数的原因。

- 并且任何一个分组函数（count sum avg maxmin）都是在group by语句执行结束之后才会执行的。

- 当一条sql语句没有group by的话，整张表的数据会自成一组。

找出每个岗位的平均工资

```sql
select job,avg(sal) from emp group by job;
```

找出每个部门不同工作岗位的最高薪资

```sql
select deptno,job,max(sal) from emp group by job,deptno order by deptno;
```

#### having

建议：能用where的用where，不能就用having

找出每个部门的最高薪资，要求显示薪资大于2900的数据

```sql
select deptno,max(sal) from emp group by deptno having max(sal) > 2900;
```

- 这种方式效率低，因为是都找出来之后，筛选大于2900的，不如在开始的时候就不对小于2900的进行筛选
- 即：`select deptno,max(sal) from emp where sal > 2900 group by deptno;`
- 能用where最好用where，不能的话用having

找出每个部门的平均薪资，要求显示薪资大于2000的数据

- 此时不能用where了就，因为是对分组函数的结果进行选择

```sql
select deptno,avg(sal) from emp group by deptno having avg(sal) > 2000;
```

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

```sql
select e.ename,d.dname from emp e,dept d;
```

表的别名有什么好处？

- 第一：执行效率高。
- 第二：可读性好。

注意：以后写sql语句的时候都要开始起别名了

笛卡尔积现象

案例：找出每一个员工的部门名称，要求显示员工名和部门名。

```sql
select ename,dname from emp,dept;
```

笛卡尔积现象：当两张表进行连接查询的时候，没有任何条件进行限制，最终的查询结果条数是两张表记录条数的

乘积。

怎样避免？加上条件进行过滤。

避免了笛卡尔积现象，会减少记录的匹配次数吗？ 不会，次数还是56次。只不过显示的是有效记录。

案例：找出每一个员工的部门名称，要求显示员工名和部门名。

```sql
select e.ename,d.dname from emp e , dept d  where e.deptno = d.deptno;
```

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

```sql
select
    ..(select).
from
    ..(select).
where
    ..(select).
```


案例：找出高于平均薪资的员工信息。

```sql
select * from emp where sal > (select avg(sal) from emp);
```

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

- 第一种：`select ename,job from emp where job = 'MANAGER' or job = 'SALESMAN';`

- 第二种：`select ename,job from emp where job in('MANAGER','SALESMAN');`

- 第三种：`union`

- 只要确定了两张表的查询结果一定不重复，就用UNION ALL， 因为查询效率高

```sql
select ename,job from emp where job = 'MANAGER'
union
select ename,job from emp where job = 'SALESMAN';
```

### limit（MySQL特有）

重点中的重点，以后分页查询全靠它了。

limit是mysql特有的，其他数据库中没有，不通用。（Oracle中有一个相同的机制，叫做rownum）

limit取结果集中的部分数据，这时它的作用。

语法机制：
    limit startIndex, length
        startIndex表示起始位置，从0开始，0表示第一条数据。
        length表示取几个

案例：取出工资前5名的员工（思路：降序取前5个）

```sql
select ename,sal from emp order by sal desc;
```

取前5个：

```sql
select ename,sal from emp order by sal desc limit 0, 5;
select ename,sal from emp order by sal desc limit 5;
```

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

```sql
select ename,sal from emp order by sal desc limit 3,6;
```

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