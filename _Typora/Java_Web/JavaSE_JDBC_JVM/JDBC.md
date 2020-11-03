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

## JDBC编程六步（背下来）

1. 注册驱动（作用：告诉Java程序，即将链接的是哪个品牌的数据库）
2. 获取链接（表示JVM的进程和数据库进程之间的**通道打开**了，属于进程之间的通信，重量级的，使用完一定要关闭）
3. 获取数据库操作对象（专门执行sql语句的对象）
4. 执行SQL语句（DQL and DML）
5. 处理查询结果集（只有当4执行的是select语句的时候，才有这个处理查询结果集）
6. 释放资源（使用完资源之后一定要关闭资源）


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
            try{
                if(stmt != null){
                    stmt.close();
                }
            }catch(SQLException e){
                e.printStackTrace();
            }
            try{
            if(conn != null){
                conn.close();
            }
            }catch(SQLException e){
                e.printStackTrace();
            }

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
            try{
                if(stmt != null){
                    stmt.close();
                }
            }catch(SQLException e){
                e.printStackTrace();
            }
            try{
                if(conn != null){
                    conn.close();
                }
            }catch(SQLException e){
                e.printStackTrace();
            }

        }
    }
}
```


## 将链接数据库的所有信息配置到信息文件中

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
            try{
                if(stmt != null){
                    stmt.close();
                }
            }catch(SQLException e){
                e.printStackTrace();
            }
            try{
                if(conn != null){
                    conn.close();
                }
            }catch(SQLException e){
                e.printStackTrace();
            }

        }
    }
}
```

## 查询结果集的处理

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
            try{
                if(rs != null){
                    rs.close();
                }
            }catch(SQLException e){
                e.printStackTrace();
            }
            try{
                if(stmt != null){
                    stmt.close();
                }
            }catch(SQLException e){
                e.printStackTrace();
            }
            try{
                if(conn != null){
                    conn.close();
                }
            }catch(SQLException e){
                e.printStackTrace();
            }
        }
    }
}
```

## 用户登录功能实现

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

### 问题代码

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


### SQL注入


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


### 最终版本

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

## PrepareStatement

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

## 银行转账业务

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

## JDBC工具类的封装

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

## 基于工具类的模糊查询

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
