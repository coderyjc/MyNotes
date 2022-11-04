## Ubuntu20.10中连接mysql8.0时报错：Access denied for user 'root'@'localhost'（亲测有效）

关闭服务

```bash
service mysql stop
```

修改配置文件跳过grant-tables


```
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
---
在mysqld下面写 skip-grant-tables

[mysqld]
skip-grant-tables
```

启动服务登录

```
service mysql start
```

修改密码：

进入mysql数据库，查看user和host

```
mysql> use mysql;
mysql> select user,host from user;
+------------------+-----------+
| user             | host      |
+------------------+-----------+
| root             | %         |
| admin            | localhost |
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| zhangj           | localhost |
+------------------+-----------+
```

- 注意我的root，host是'%'，<font style="color:red">这个一定要对应起来</font>

这样改:

```
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123';
```

如果root对应的host为localhost，就要写成 `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123';`

如果报错，就刷新一下权限`flush privileges`, 然后再改。

改完之后退出

停掉服务

```
service mysql stop
```

删除 `/etc/mysql/mysql.conf.d/mysqld.cnf` 中的 skip-grant-tables

启动服务

```
service mysql start
```

重新用新的密码登陆，成功。
