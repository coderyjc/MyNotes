# JDBC

## 介绍

JDBC是什么？
- Java Database Counnectivity（Java语言链接数据库）

本质是什么？
- SUN公司制定的一套接口（interface）
    + java.sql.* 这个包下的
- 接口都有调用者/实现者
- 面向接口调用/面向接口写实现类，都属于面向接口编程

为什么面向接口编程？
- 解耦合，降低程序的耦合度，提高程序的扩展力
- 多态就是非常典型的面向抽象编程（不要面向具体过程编程）

为什么制定这一套接口呢？
- 因为每一个数据可以的底层实现原理都不一样（oracle/mysql/ms sqlserver）
- 每一个数据库产品都有自己独特的实现原理。

开发的准备：如果是用文本编辑器开发，则需要配置classpath文件，用IDEA的时候，不需要

## API 主要成员变量



JDBC API 主要功能：三件事，具体是通过以下类/接口实现：

- DriverManager ： 管理jdbc驱动

- Connection： 连接（通过DriverManager产生）

- Statement（PreparedStatement） ：增删改查  （通过Connection产生 ）

- CallableStatement  ： 调用数据库中的 存储过程/存储函数  （通过Connection产生 ）

- Result ：返回的结果集  （上面的Statement等产生 ）



Connection产生操作数据库的对象：

- Connection产生Statement对象：createStatement()

- Connection产生PreparedStatement对象：prepareStatement()

- Connection产生CallableStatement对象：prepareCall();



Statement操作数据库：

- 增删改：executeUpdate()

- 查询：executeQuery();

- ResultSet：保存结果集 select * from xxx

- next():光标下移，判断是否有下一条数据；true/false

- previous():  true/false

- getXxx(字段名|位置):获取具体的字段值 



PreparedStatement操作数据库：

因为 public interface PreparedStatement extends Statement 

所以

- 增删改：executeUpdate()

- 查询：executeQuery();

- 赋值操作 setXxx();



PreparedStatement与Statement在使用时的区别：

1. Statement: sql executeUpdate(sql)
2. PreparedStatement: sql(可能存在占位符?) 在创建PreparedStatement 对象时，将sql预编译 prepareStatement(sql) executeUpdate() setXxx()替换占位符？



推荐使用PreparedStatement：原因如下：

1.编码更加简便（避免了字符串的拼接）

2.提高性能(因为 有预编译操作，预编译只需要执行一次)

3.安全（可以有效防止sql注入）



JDBC编程六步

1. 注册驱动（作用：告诉Java程序，即将链接的是哪个品牌的数据库）
2. 获取链接（表示JVM的进程和数据库进程之间的**通道打开**了，属于进程之间的通信，重量级的，使用完一定要关闭）
3. 获取数据库操作对象（专门执行sql语句的对象）
4. 执行SQL语句（DQL and DML）
5. 处理查询结果集（只有当4执行的是select语句的时候，才有这个处理查询结果集）
6. 释放资源（使用完资源之后一定要关闭资源）



---



## 普通数据增删改查实例

### 练习1

向dept中添加一个职位‘人事部’，no为50，地址为北京

```java
import java.sql.*;

public class Test{
    public static void main(String[] args){
        Statement stmt = null;
        Connection conn = null;
        try{
            //1.注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取链接
            String url = "jdbc:mysql://127.0.0.1:3306/mytest";
            String user = "root";
            String password = "333";
            conn = DriverManager.getConnection(url, user, password);
            //3.获取数据库操作对象
            stmt = conn.createStatement();
            //4.执行sql
            String sql = "insert into dept(deptno, dname, loc) value(60, 'renshi2', 'beijing1')";
            //专门执行DML语句的(insert delete update)
            //返回值是“影响数据库中的记录条数”
            int count = stmt.executeUpdate(sql);
            System.out.print(count == 1 ? "success" : "fail");
            //5.处理结果集
            //不是select语句，不需要处理
            //6.释放资源，为了保证资源一定释放，在finally中关闭资源
            //从小到大依次关闭，分别对其try/catch
        }catch(SQLException e){
            e.printStackTrace();
        }finally{
            // 关闭数据库连接，此处省略
        }
    }
}
```

### 练习2

删除一条数据

```java
import java.sql.*;
import java.util.*;
/*
    实际开发中不建议把数据库的信息写死到java程序中
*/
public class Test{
    public static void main(String[] args){
        Connection conn = null;
        Statement stmt = null;
        try{
        //1. 注册驱动， 通过反射机制，这种方式常用
        //因为参数是一个字符串，自负床可以写到.properties文件中
        //以下方法不接受返回值，因为我们只用它的加载动作
        Class.forName("com.mysql.jdbc.Driver");
        //2. 获取链接
        conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mytest", "root", "333");
        //3. 获取数据库操作对象
        stmt = conn.createStatement();
        //4. 执行SQL语句
        String sql = "delete from dept where deptno = 50";
        int count = stmt.executeUpdate(sql);
        if(count == 1)
            System.out.print("yes");
        //5. 未使select语句，所以不用处理查询结果集
        }catch(ClassNotFoundException e){
            e.printStackTrace();
        }catch(SQLException e){
            e.printStackTrace();
        }finally{
            //6. 释放资源
           // 关闭数据库连接，此处省略
        }
    }
}
```

### 将链接数据库的所有信息配置到信息文件中



```java
import java.sql.*;
import java.util.*;
/*
    实际开发中不建议把数据库的信息写死到java程序中
*/
public class Test{
    public static void main(String[] args){
        //使用资源绑定器
        ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
        //String driver = bundle.getString("Driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");
        Connection conn = null;
        Statement stmt = null;
        try{
        //1. 注册驱动， 通过反射机制，这种方式常用
        //因为参数是一个字符串，所以可以写到.properties文件中
        //以下方法不接受返回值，因为我们只用它的加载动作
        Class.forName("com.mysql.jdbc.Driver");
        //2. 获取链接
        conn = DriverManager.getConnection(url, user, password);
        //3. 获取数据库操作对象
        stmt = conn.createStatement();
        //4. 执行SQL语句
        String sql = "insert into dept(deptno, dname, loc) value(50,'HumanResource','Beijing')";
        int count = stmt.executeUpdate(sql);
        if(count == 1)
            System.out.print("yes");
        //5. 未使select语句，所以不用处理查询结果集
        }catch(ClassNotFoundException e){
            e.printStackTrace();
        }catch(SQLException e){
            e.printStackTrace();
        }finally{
            //6. 释放资源
   // 关闭数据库连接，此处省略
        }
    }
}
```

### 查询结果集的处理



```java
import java.sql.*;

public class Test{
    public static void main(String[] args){
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try{
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2. 获取链接
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mytest", "root", "333");
            //3. 获取数据库操作对象
            stmt = conn.createStatement();
            //4. 执行sql
            String sql = "select ename name ,sal s from emp";
            /*
                (int) executeUpdate(insert/delete/update), 返回执行成功的数量
                (ResultSet) executeQuery(select), 返回查询结果集
            */
            rs = stmt.executeQuery(sql); //专门处理DQL语句的方法
            //5. 处理查询结果集
            while(rs.next()){
                //光标指向的 行 有数据，取数据
                String ename = rs.getString("name"); //引号里面是列名字，也可以是第几列（从1开始）
                // 不管数据库中的数据类型是什么，都以String类型取出来
                //这里的列名是查询结果集中的列名，也就是重命名之后的列名
                //JDBC 中所有的数据从1开始而不是从0开始
                Double sal = rs.getDouble("s");
                System.out.println(ename + " " + sal);
                //除了以String类型去除之外，也可以用其他类型取出
            }
        }catch(Exception e){
            e.printStackTrace();
        }finally{
            // 6. 释放资源
           // 关闭数据库连接，此处省略
        }
    }
}
```

### 用户登录功能实现

可以对sql脚本进行编辑

```sql

drop table if exists t_user;
/*==============================================================*/
/* Table: t_user                                                */
/*==============================================================*/
create table t_user
(
   id                   bigint auto_increment,
   loginName            varchar(255),
   loginPwd             varchar(255),
   realName             varchar(255),
   primary key (id)

);
INSERT INTO t_user
(
 loginName, loginPwd, realName
)
VALUES
(
 'zhangsan', '123', '张三'
),
(
 'jack','123','杰克'
),
(
 'lisi','123','李四'
);

```

#### 问题代码

```java
import java.sql.*;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        //初始化界面
        Map<String,String> userLoginInfo = initUI();
        // 验证用户名和密码
        boolean loginRst = login(userLoginInfo);
        //输出结果
        System.out.println(loginRst ? "登录成功" : "登录失败");
    }

    /**
     *用户登录
     * @param userLoginInfo 用户登录信息
     * @return 用户登录的结果 false失败，true成功
     */
    private static boolean login(Map<String, String> userLoginInfo) {
        boolean loginSuccess = false; //打标记
        //JDBC代码
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            //1.注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取链接
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mytest", "root", "333");
            //3.获取数据操作对象
            stmt = conn.createStatement();
            //4.执行sql
            String sql = "select * from t_user where loginName = '" + userLoginInfo.get("loginName") + "' and loginPwd = '" + userLoginInfo.get("loginPwd") + "'";
            rs = stmt.executeQuery(sql);
            //5.处理结果集
            if(rs.next()){
                loginSuccess = true;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }finally{
        //6.释放资源
            try {
            if(rs != null) {
                rs.close();
            }
            } catch (SQLException s) {
                s.printStackTrace();
            }

            try{
                if(stmt != null){
                    stmt.close();
                }
            }catch (SQLException s){
                s.printStackTrace();
            }

            try{
                if(conn != null){
                    conn.close();
                }
            }catch(SQLException s){
                s.printStackTrace();
            }
        }
        return loginSuccess;
    }

    /**
     * 初始化用户界面
     * @return 用户输入的用户名和密码等信息
     */
    private static Map<String, String> initUI() {
        Scanner s = new Scanner(System.in);
        System.out.println("用户名：");
        String username = s.next();
        System.out.println("密码：");
        String password = s.next();
        Map<String, String> userLoginInfo = new HashMap<>();
        userLoginInfo.put("loginName", username);
        userLoginInfo.put("loginPwd", password);
        return userLoginInfo;
    }
}
```


#### SQL注入

用户名：asd

密码：asd'or'1' = '1

原因：用户输入的信息中含有sql语句的关键字，并且这些关键字参与sql语句的编译过程，导致sql的原意被扭曲。

解决：

只要用户提供的信息不参与SQL语句的编译过程，问题就解决了。即使用户提供的信息中含有SQL语句的关键字，但是没有参与编译，不起作用，要想用户信息不参与SQL语句的编译，那么必须使用java.sql.PreparedStatement.
这个接口继承了java.sql.Statement,是预编译的数据库操作对象，原理：预先对SQL语句的框架进行编译，然后再给SQL语句传值。

对比Statement和PerparedStatement：
- Statement存在SQL注入问题，preparedstatement解决了SQL注入问题。
- Statement是编译一次执行一次。preparedstatement是编译一次，可执行多次。
- PreparedStatement效率较高一些。
- PreparedStatement会在编译阶段做类型的安全检查。

综上所述：Preparedstatement使用较多。只有极少数的情况下需要使用statement

什么情况下必须使用statement呢？
- 业务方面要求必须支持SQL注入的时候。需要进行SQL语句的拼接的时候。
- Statement支持SQL注入，凡是业务方面要求是需要进行SQL语句拼接的，必须使用Statement


#### 最终版本

```java
import java.sql.*;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        //初始化界面
        Map<String,String> userLoginInfo = initUI();
        // 验证用户名和密码
        boolean loginRst = login(userLoginInfo);
        //输出结果
        System.out.println(loginRst ? "登录成功" : "登录失败");
    }

    /**
     *用户登录
     * @param userLoginInfo 用户登录信息
     * @return 用户登录的结果 false失败，true成功
     */
    private static boolean login(Map<String, String> userLoginInfo) {
        boolean loginSuccess = false; //打标记
        //JDBC代码
        Connection conn = null;
        PreparedStatement ps = null; //这里使用PS预编译的数据库操作对象
        ResultSet rs = null;
        try {
            //1.注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取链接
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mytest", "root", "333");
            //3.获取预编译的数据操作对象
            // ？ 不能用单引号括起来
            String sql = "select * from t_user where loginName = ? and loginPwd = ?"; // 先写上SQL语句的框架，其中一个？标识一个占位符
            //程序执行到这步，会发送SQL语句的框架给DBMS，然后DBMS进行sql语句的预编译
            ps = conn.prepareStatement(sql);//这里不用传入sql语句参数了
            // 给 ‘？’ 传值 第一个问号下标是1，第二个是2，JDBC所有下标从1开始
            ps.setString(1, userLoginInfo.get("loginName"));//自动添加上单引号
            ps.setString(2, userLoginInfo.get("loginPwd"));
            //4.执行ps对象的sql
            rs = ps.executeQuery(); //这里不用传入参数了
            //5.处理结果集
            if(rs.next()){
                loginSuccess = true; //登录成功
            }
        } catch (Exception e) {
            e.printStackTrace();
        }finally{
        //6.释放资源
            try {
            if(rs != null) {
                rs.close();
            }
            } catch (SQLException s) {
                s.printStackTrace();
            }

            try{
                if(ps != null){
                    ps.close();
                }
            }catch (SQLException s){
                s.printStackTrace();
            }

            try{
                if(conn != null){
                    conn.close();
                }
            }catch(SQLException s){
                s.printStackTrace();
            }
        }
        return loginSuccess;
    }

    /**
     * 初始化用户界面
     * @return 用户输入的用户名和密码等信息
     */
    private static Map<String, String> initUI() {
        Scanner s = new Scanner(System.in);
        System.out.println("用户名：");
        String username = s.next();
        System.out.println("密码：");
        String password = s.next();
        Map<String, String> userLoginInfo = new HashMap<>();
        userLoginInfo.put("loginName", username);
        userLoginInfo.put("loginPwd", password);
        return userLoginInfo;
    }
}
```

### PrepareStatement

```java
import java.sql.*;

public class Test{
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs =null;

        try {
            //1.注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取链接
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mytest", "root", "333");
            //3.获取预编译的数据操作对象
            String sql = "insert into dept(dname, loc, deptno) values(?, ?, ?)";
            ps = conn.prepareStatement(sql);
            ps.setString(1, "HR");
            ps.setString(2, "Shanghai");
            ps.setInt(3, 70);
            //4.执行ps对象的sql
            int count = ps.executeUpdate();
            System.out.println(count);
        } catch (Exception e) {
            e.printStackTrace();
        }finally {
            // 6.释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException throwables) {
                    throwables.printStackTrace();
                }
            }
            if (ps != null) {
                try {
                    ps.close();
                } catch (SQLException throwables) {
                    throwables.printStackTrace();
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException throwables) {
                    throwables.printStackTrace();
                }
            }
        }
    }
}
```

### 银行转账业务

JDBC事务默认自动提交，

关闭自动提交？  conn.setAutoCommit(false);

提交事务 conn.commit();

回滚事务 conn.rollback();

```java
import java.sql.*;

public class Test{
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs =null;
        try {
            //1.注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取链接
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mytest", "root", "333");
            //3.获取预编译的数据操作对象
            conn.setAutoCommit(false); //关闭自动提交
            String sql = "update t_account set balance = ? where act = ?";
            ps = conn.prepareStatement(sql);

            //4.执行ps对象的sql
            //给 ？ 传值
            ps.setDouble(1, 10000);
            ps.setString(2, "111");
            int count  = ps.executeUpdate();

            ps.setDouble(1, 10000);
            ps.setString(2, "222");
            count  += ps.executeUpdate();
            System.out.println(count == 2 ? "转账成功" : "转账失败");

            conn.commit(); //提交事务
        } catch (Exception e) {
            if(conn != null){
                try { //回滚事务
                    conn.rollback();
                } catch (SQLException throwables) {
                    throwables.printStackTrace();
                }
            }
            e.printStackTrace();
        }finally {
            // 6.释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException throwables) {
                    throwables.printStackTrace();
                }
            }
            if (ps != null) {
                try {
                    ps.close();
                } catch (SQLException throwables) {
                    throwables.printStackTrace();
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException throwables) {
                    throwables.printStackTrace();
                }
            }
        }
    }
}
```

### JDBC工具类的封装

```java
import java.sql.*;

public class DBUtil {
    /**
     * 工具类中的构造方法是私有的
     * 因为工具类中的方法都是静态的，不需要new对象，直接类名调用
     */
    private DBUtil(){}

    //静态代码块在类加载时执行，并且只执行一次
    static {
        try {
            Class.forName("com.mysql.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    /**
     * 获取链接对象
     * @return 链接对象
     * @throws SQLException 连接异常
     */
    public static Connection getConnection() throws SQLException{
        return DriverManager.getConnection("jdbc:mysql://localhost:3306/mytest", "root", "333");
    }

    /**
     * 释放资源
     * @param conn 链接对象
     * @param ps 操作对象
     * @param rs 查询结果集
     */
    public static void close(Connection conn, Statement ps, ResultSet rs){
        if(rs != null){
            try {
                rs.close();
            } catch (SQLException s) {
                s.printStackTrace();
            }
        }
        if(ps != null){
            try {
                ps.close();
            } catch (SQLException s) {
                s.printStackTrace();
            }
        }
        if(conn != null){
            try {
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}

```

### 基于工具类的模糊查询

查询员工中名字有A的

```java
import java.sql.*;

public class Test{
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs =null;
        try {
            //1.注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取链接
            conn = DBUtil.getConnection();
            //3.获取预编译的数据操作对象
            String sql = "select ename from emp where ename like ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, "_A%");
            //4.执行ps对象的sql
            rs = ps.executeQuery();
            while(rs.next()){
                System.out.println(rs.getString("ename"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }finally {
            DBUtil.close(conn, ps, rs);
        }
    }
}
```



## 存储过程与存储函数调用

CallableStatement:调用 存储过程、存储函数

connection.prepareCall(参数：存储过程或存储函数名)

参数格式：

存储过程（无返回值return，用out参数替代）：

​	{ call  存储过程名(参数列表) }

存储函数（有返回值return）：

​	{ ? = call  存储函数名(参数列表) }

```plsql
create or replace procedure addTwoNum ( num1  in number,num2  in number,result out number )  as
begin
	result := num1+num2 ;
end ;
```

强调：

如果通过sqlplus 访问数据库，只需要开启：OracleServiceSID

通过其他程序访问数据（sqldevelop、navicate、JDBC），需要开启：OracleServiceSID、XxxListener

JDBC调用存储过程的步骤：

a. 产生 调用存储过程的对象（CallableStatement） cstmt = 	connection.prepareCall(   "..." ) ;

b. 通过setXxx()处理 输出参数值 cstmt.setInt(1, 30);

c. 通过 registerOutParameter(...)处理输出参数类型

d.cstmt.execute()执行

e.接受 输出值（返回值）getXxx()

调存储函数：

```plsql
create or replace function addTwoNumfunction ( num1  in number,num2  in number)  -- 1 + 2 
return number
as
	result number ;	
begin
	result := num1+num2 ;
	return result ;
end ;
```

JDBC调用存储函数：与调存储过程的区别：
在调用时，注意参数："{? =  call addTwoNumfunction	(?,?) }"

### 存储过程

首先在数据库中创建存过程：

```sql
CREATE OR REPLACE PROCEDURE ADDNUM(num1 in number, num2 in number, rst out number) AS 
BEGIN -- 计算两个数的和，给第三个值
  rst := num1 + num2; 
END ADDNUM;
```

然后进行调用

```java
        // 数据库连接
        Connection conn = null;
        // 存储过程返回值的对象
        CallableStatement callableStatement = null;

        try {
            conn = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:ORCL", "c##libmanager", "333");
            callableStatement = conn.prepareCall("{call addNum(?, ?, ?)}");

            // 设置第一个和第二个数
            callableStatement.setInt(1, 13);
            callableStatement.setInt(2, 10);
            // 设置第三个参数的输出类型
            callableStatement.registerOutParameter(3, Types.INTEGER);

            // 调用存储过程， 执行的是num1 + num2
            // 这句话之前处理的是输入值， 这句话之后是输出值
            callableStatement.execute();
            // 获取返回值
            int rst =  callableStatement.getInt(3);
            // 输出计算结果
            System.out.println(rst);
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        
```

### 存储函数

在数据库中创建函数：

```sql
CREATE OR REPLACE FUNCTION addNum 
(
  NUM1 IN NUMBER  
, NUM2 IN NUMBER  
) RETURN NUMBER AS 
BEGIN
  RETURN num1 + num2;
END addNum;
```

```java
        // 数据库连接
        Connection conn = null;
        // 存储过程返回值的对象
        CallableStatement callableStatement = null;

        try {
            conn = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:ORCL", "c##libmanager", "333");
            callableStatement = conn.prepareCall("{? = call addNum(?, ?)}");

            // 设置第一个和第二个数
            callableStatement.setInt(2, 13);
            callableStatement.setInt(3, 10);
            // 设置第三个参数的输出类型
            callableStatement.registerOutParameter(1, Types.INTEGER);

            // 调用函数， 执行的是num1 + num2
            // 这句话之前处理的是输入值， 这句话之后是输出值
            callableStatement.execute();
            // 获取返回值
            int rst = callableStatement.getInt(1);
            // 输出计算结果
            System.out.println(rst);
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

```

## 大类型数据存储与读取实例

处理CLOB/BLOB类型 - 处理稍大型数据：

a.存储路径	E:\JDK_API_zh_CN.CHM	通过JDBC存储文件路径，然后 根据IO操作处理

例如：JDBC将 E:\JDK_API_zh_CN.CHM 文件 以字符串形式 “E:\JDK_API_zh_CN.CHM” 存储到数据库中

获取：1.获取该路径“E:\JDK_API_zh_CN.CHM”  2.IO	

b.

CLOB：大文本数据 （小说->数据）

BLOB：二进制

clob:大文本数据   字符流 Reader Writer



存:

1. 先通过pstmt 的? 代替小说内容 （占位符）

2. 再通过pstmt.setCharacterStream(2, reader,  (int)file.length());  将上一步的？替换为 小说流， 注意第三个参数需要是 Int类型

取：

1. 通过Reader reader = rs.getCharacterStream("NOVEL") ; 将cloc类型的数据  保存到Reader对象中
2. 将Reader通过Writer输出即可。

blob:二进制  字节流 InputStream OutputStream

与CLOB步骤基本一致，区别：setBinaryStream(...)  getBinaryStream(...)   

### 大文本存储

存储

```java
			String sql = "insert into mynovel values(?,?)";
			// c.发送sql，执行(增删改、查)
			pstmt = connection.prepareStatement(sql);
			pstmt.setInt(1, 1);
			File file = new File("E:\\all.txt");
			InputStream in = new FileInputStream( file) ;
			Reader reader = new InputStreamReader( in   ,"UTF-8") ;//转换流 可以设置编码
			pstmt.setCharacterStream(2, reader,  (int)file.length());
			int count =pstmt.executeUpdate() ;
			// d.处理结果
			if (count > 0) {  
				System.out.println("操作成功！");
			}
			
			reader.close();
```



读取

```java
			String sql = "select NOVEL from mynovel where id = ? ";
			// c.发送sql，执行(查)
			pstmt = connection.prepareStatement(sql);
			pstmt.setInt(1, 1);
			
			rs = pstmt.executeQuery() ;
			//setXxxx getXxxx      setInt  getInt
			if(rs.next())
			{
				Reader reader = rs.getCharacterStream("NOVEL") ;
				Writer writer = new FileWriter("src/小说.txt");
				
				char[] chs = new char[100] ;
				int len = -1;
				while(  (len = reader.read(chs)) !=-1 ) {
					writer.write( chs,0,len  );
				}
				writer.close();
				reader.close();
			}

```

### 音乐存储

存储

```java
			String sql = "insert into mymusic values(?,?)";
			// c.发送sql，执行(增删改、查)
			pstmt = connection.prepareStatement(sql);
			pstmt.setInt(1, 1);
			File file = new File("d:\\luna.mp3");
			
			InputStream in = new FileInputStream(file );
			pstmt.setBinaryStream(2,in ,(int)file.length()  );
			
			
			int count =pstmt.executeUpdate() ;
			// d.处理结果
			if (count > 0) {  
				System.out.println("操作成功！");
			}
			// 关闭流
			in.close();
```

读取：

```java
			String sql = "select music from mymusic where id = ? ";
			
			
			// c.发送sql，执行(查)
			pstmt = connection.prepareStatement(sql);
			pstmt.setInt(1, 1);
			
			rs = pstmt.executeQuery() ;
			if(rs.next())
			{
				InputStream in = rs.getBinaryStream("music") ;
				OutputStream out = new FileOutputStream("src/music.mp3") ;
				
				byte[] chs = new byte[100] ;
				int len = -1;
				while(  (len = in.read(chs)) !=-1 ) {
					out.write( chs,0,len  );
				}
				out.close();
				in.close();
			}
```

