## MySQL-视图(view)

什么是视图？ 站在不同的角度去看到数据。(同一张表的数据，通过不同的角度去看待)

怎么创建视图？ `create view myview as select empno, ename from emp;`
怎么删除视图？ `drop view myview;`

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