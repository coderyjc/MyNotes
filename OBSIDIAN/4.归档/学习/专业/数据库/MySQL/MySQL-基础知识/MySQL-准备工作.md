## MySQL-准备工作

### 安装与登录

数据库登录：

- cmd 打开命令行之后 用 `mysql -uroot -p密码（直接输）`输入密码是明文
- 或者 `mysql -uroot -p` 回车，然后出来“enter password” 再输密码是密文***

数据库忘记密码怎么办？

方法1：用SET PASSWORD命令
首先登录MySQL
格式：`mysql->set password for 用户名@localhost = password（'新密码1'）;`
例子：`mysql>set password for root@localhost = password（'1231'）；`

方法2：用mysqladmin
格式：`mysqladmin -u用户名 -p旧密码 password 新密码`
例子：`mysqladmin -uroot -p123456 password 123`

方法3：用UPDATE直接编辑user表
首先登录MySQL。

```bash
mysql> use mysql；
mysql> update user set password=password('333') where user= 'root' and host = 'localhost'；
mysql> flush privileges；
```

方法4：在忘记root密码的时候，可以这样

以windows为例：

1. 关闭正在运行的MysqL服务。
2. 打开Dos窗口，转到mysql\bin目录。
3. 输入`mysqld --skip-grant-tables 回车`。--skip-grant-tables的意思是启动MysQL服务的时候跳过权限表认证。
4. 再开一个Dos窗口（因为刚才那个Dos窗口已经不能动了），转到mysql\bin目录。
5. 输入myscql回车，如果成功，将出现MySQL提示符>。
6. 连接权限数据库：`use mysql；`
7. 改密码：`update user set password = password（"123"）where user="root"；`（别忘了最后加分号）。
8. 刷新权限（必须步骤）：`flush privileges；`
9. 退出quit。
10. 注销系统，再进入，使用用户名root和刚才设置的新密码123登录。

如何卸载？
- 在安装的时候，那个安装程序会有一个remove选项，先remove了
- 然后C盘下的program filesx86下面有一个mySQL文件夹，要强行删除
- 然后C盘的隐藏目录有一个programData，有个MySQL文件夹，删除了

### 认识MySQL

## sql、DB、DBMS分别是什么，他们之间的关系？

- DB：
  - DataBase（数据库，数据库实际上在硬盘上以文件的形式存在）

- DBMS：
  - DataBase Management System（数据库管理系统，常见的有：MysQL oracle DB2 Sybase sqlserver...）

- SQL：
  - 结构化查询语言，是一门标准通用的语言。标准的sql适合于所有的数据库产品。
  - SQL属于高级语言。只要能看懂英语单词的，写出来的sql语句，可以读懂什么意思。
  - SQL语句在执行的时候，实际上内部也会先进行编译，然后再执行sql。（sql语句的编译由DBMS完成。）DBMS负责执行sq1语句，通过执行sq1语句来操作DB当中的数据。
  - DBMS->（执行）->SQL-（操作）->DB

### 什么是表？

表：table

表：table是数据库的基本组成单元，所有的数据都以表格的形式组织，目的是可读性强。

一个表包括行和列：

- 行：被称为数据/记录（data）
- 列：被称为字段（column）

每一个字段应该包括哪些属性？

字段名、数据类型、相关的约束。

### SQL语句怎么分类

- DQL（数据查询语言）：查询语句，凡是select语句都是DQL。
- DML（数据操作语言）：insert delete update，对表当中的数据进行增删改。
- DDL（数据定义语言）：create drop alter，对表结构的增删改。
- TCIL（事务控制语言）：commit提交事务，rollback回滚事务。（rcL中的T是Transaction）
- DCL（数据控制语言）：grant授权、revoke撤销权限等。

### 导入数据

第一步：登录mysq1数据库管理系统
dos命令窗口：`mysql -uroot -p333`

第二步：查看有哪些数据库
`show databases；`（这个不是SQL语句，属于MysQL的命令。）
```text
+-----------------------------------+
| Database                        |
+---------------------------------+
| information_schema   |
| mysql                             |
| performance_schema |
| test                                  |
+----------------------------------+
```

第三步：创建属于我们自己的数据库
`create database bjpowernode；`（这个不是SQL语句，属于MysQL的命令。）

第四步：使用bjpowernode数据
`use bjpowernode；`（这个不是SQL语句，属于MysQL的命令。）

第五步：查看当前使用的数据库中有哪些表？
`show tables；`（这个不是SQL语句，属于MysQL的命令。）

第六步：初始化数据
`mysq1>source 文件拖过来`

注意：数据初始化完成之后，有三张表：
```text
+-----------------------------—-+
l Tables in bjpowernode I
+—------------------------------+
I dept                                  I
|emp                                  I
|salgrade                            I
+—------------------------------+
```

### 什么是sql脚本

当一个文件的扩展名是.sql，并且该文件中编写了大量的slq语句，我们称这样的文件为sql脚本。
注意：直接使用source命令可以执行sql脚本。

sq1脚本中的数据量太大的时候，无法打开，请使用source命令完成初始化。

### 删库跑路

`drop database bipowernode;`

### 查看表结构：

`desc 表名字；`

`drop table if exists <表名>;` // 当这个表存在的话删除。

`drop table <表名>;` // 删除表

`mysql> desc emp;`

### 常用命令

`select database();` 查看当前使用的是哪个数据库

`select version();` 查看mysql的版本号

`\c` 命令，结束一条语句

`exit;` 退出mySQL

### 查看创建表的语句

`show create table <表名称>；`