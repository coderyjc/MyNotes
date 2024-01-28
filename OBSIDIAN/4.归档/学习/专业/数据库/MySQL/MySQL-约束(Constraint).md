## MySQL-约束(Constraint)

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