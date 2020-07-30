# MySQL高级

## MySQL架构介绍

MySQL是一个关系型数据库管理系统，由瑞典MySQL AB公司开发，目前属于Oracle公司。 

MySQL是一种关联数据库管理系统，将数据保存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。

MySQL是开源的，所以你不需要支付额外的费用。

MySQL是可以定制的，采用了GPL协议，你可以修改源码来开发自己的MySQL系统。 

MySQL支持大型的数据库。可以处理拥有上千万条记录的大型数据库。

MySQL使用标准的SQL数据语言形式。

MySQL可以允许于多个系统上，并且支持多种语言。这些编程语言包括C、C++、Python、Java、Perl、PHP、Eiffel、Ruby和Tcl等。

MySQL支持大型数据库，支持5000万条记录的数据仓库（分库），单表最大容量大约为500万条数据（分表），32位系统表文件最大可支持4GB，64位系统支持最大的表文件为8TB。

### MySQL用户与权限管理

#### 用户管理

- 创建用户 create user zhang3 identified by '123123';
	
	- 表示创建名称为zhang3的用户，密码设为123123；
- 修改当前用户的密码:

  -  set password =password('123456'); flush privileges; 
- 修改某个用户的密码: 
	- update mysql.user set password=password('123456') where user='li4'; flush privileges; 

-  修改用户名：
	- update mysql.user set user='li4' where user='wang5'; flush privileges;

- 删除用户：
	- drop user li4 ; （不要通过delete from  user u where user='li4' 进行删除，系统会有残留信息保留。 ）
- <span style = "color:red">flush privileges;   所有通过user表的修改，必须用该命令才能生效。</span>

**user表：**

查看用户
select host,user,authentication_string,select_priv,insert_priv,drop_priv from mysql.user;

![查看用户](images\查看用户.bmp)

 **host** ：   表示连接类型

% 表示所有远程通过 TCP方式的连接

IP 地址 如 (192.168.1.2,127.0.0.1) 通过制定ip地址进行的TCP方式的连接

机器名   通过制定i网络中的机器名进行的TCP方式的连接

::1   IPv6的本地ip地址  等同于IPv4的 127.0.0.1

localhost 本地方式通过命令行方式的连接 ，比如mysql -u xxx -p 123xxx 方式的连接。

**User**:表示用户名

同一用户通过不同方式链接的权限是不一样的。

**password** ： 密码

所有密码串通过 password(明文字符串) 生成的密文字符串。加密算法为MYSQLSHA1 ，不可逆 。

mysql 5.7 的密码保存到 authentication_string 字段中，不再使用password 字段。

**select_priv , insert_priv**等为该用户所拥有的权限。

#### 权限管理

授予权限：

授权命令： grant 权限1,权限2,…权限n on 数据库名称.表名称 to 用户名@用户地址 identified by ‘连接口令’;
该权限如果发现没有该用户，则会直接新建一个用户。

grant select,insert,delete,drop on atguigudb.* to li4@localhost  ;
 #给li4用户用本地命令行方式下，授予atguigudb这个库下的所有表的插删改查的权限。

grant all privileges on *.* to joe@'%'  identified by '123'; 
#授予通过网络方式登录的的joe用户 ，对所有库所有表的全部权限，密码设为123.

收回权限：

查看当前用户权限 show grants;

收回权限命令： 
revoke  权限1,权限2,…权限n on 数据库名称.表名称  from  用户名@用户地址 ;

REVOKE ALL PRIVILEGES ON mysql.* FROM joe@localhost;
#收回全库全表的所有权限

REVOKE select,insert,update,delete ON mysql.* FROM joe@localhost;
#收回mysql库下的所有表的插删改查权限

<span style="color:red"> 必须用户重新登录后才能生效</span>

查看权限：

查看当前用户权限
show grants;

查看某用户的全局权限
select  * from user ;

查看某用户的某个表的权限
select * from tables_priv;

### 底层执行过程

![a、MySql架构1](images\a、MySql架构1.png)