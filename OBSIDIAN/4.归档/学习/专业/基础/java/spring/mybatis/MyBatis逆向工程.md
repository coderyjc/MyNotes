#后端/MyBatis 

# MyBatis逆向工程 - MyBatis Generator的使用

> 官网 ： [http://mybatis.org/generator/](http://mybatis.org/generator/)

1. 添加依赖 、引入jar包

   ```xml
       <!-- pom.xml -->
   
   	<!-- MBG -->
       <!-- https://mvnrepository.com/artifact/org.mybatis.generator/mybatis-generator-core -->
       <dependency>
         <groupId>org.mybatis.generator</groupId>
         <artifactId>mybatis-generator-core</artifactId>
         <version>1.3.5</version>
       </dependency>
   ```

2. 在项目主目录下创建`mbg.xml` （也就是和pom.xml一个目录）

	> MyBatis Generator 官方给出了xml文件的示例 [http://mybatis.org/generator/configreference/xmlconfig.html](http://mybatis.org/generator/configreference/xmlconfig.html), 我们只需要在这基础上稍作修改。

   以下是我修改之后的配置文件：
   
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE generatorConfiguration
           PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
           "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">
   
   <generatorConfiguration>
   
       <context id="DB2Tables" targetRuntime="MyBatis3">
   
   <!--        设置不生成注释，可写，可不写-->
           <commentGenerator>
               <property name="suppressAllComments" value="true"/>
           </commentGenerator>
   
   <!--        配置数据库连接-->
           <jdbcConnection driverClass="com.mysql.jdbc.Driver"
                           connectionURL="jdbc:mysql://localhost:3306/ssm"
                           userId="root"
                           password="333">
           </jdbcConnection>
   
           <javaTypeResolver >
               <property name="forceBigDecimals" value="false" />
           </javaTypeResolver>
   
   <!--       JavaBean生成的位置-->
           <javaModelGenerator targetPackage="com.Jancoyan.domain"
                               targetProject="./src/main/java">
               <property name="enableSubPackages" value="true" />
               <property name="trimStrings" value="true" />
           </javaModelGenerator>
   
   <!--        mapper文件生成的位置-->
           <sqlMapGenerator targetPackage="mapper"
                            targetProject="./src/main/resources">
               <property name="enableSubPackages" value="true" />
           </sqlMapGenerator>
   
   <!--        DAO文件生成的位置-->
           <javaClientGenerator type="XMLMAPPER"
                                targetPackage="com.Jancoyan.dao"
                                targetProject="./src/main/java">
               <property name="enableSubPackages" value="true" />
           </javaClientGenerator>
   
   
   <!--        表相关数据-->
   <!--        tableName表示需要生成的表名字
                  domainObjectName 表示生成的类名-->
           <table tableName="tbl_dept" domainObjectName="Department" />
           <table tableName="tbl_emp" domainObjectName="Employee" />
   
       </context>
   </generatorConfiguration>
   ```
   
   
   
   相关标签解释：
   
   - jdbcConnection 配置数据库连接
   
     - 标签是自己的数据库配置信息
   
   - javaModelGenerator 指定JavaBean生成的位置
   
     - targetPackage: 需要生成的包
     - targetProject: 指定生成的位置
   
   - sqlMapGenerator 指定SQL映射文件生成位置
   
     - targetPackage: 需要生成的包
     - targetProject: 指定生成的位置
   
   - javaClientGenerator 指定DAO接口生成的位置
   
     - targetPackage: 需要生成的包
     - targetProject: 指定生成的位置
   
   - table 指定每个表的生成策略
   
       - tableName属性 需要逆向生成的表名
       - domainObjectName 生成的类名


3. 编写Java文件运行生成相关类

   ```java
   package com.Jancoyan.test;
   
   import org.mybatis.generator.api.MyBatisGenerator;
   import org.mybatis.generator.config.Configuration;
   import org.mybatis.generator.config.xml.ConfigurationParser;
   import org.mybatis.generator.internal.DefaultShellCallback;
   
   import java.io.File;
   import java.util.ArrayList;
   import java.util.List;
   
   public class MBGTest {
       public static void main(String[] args) throws Exception {
           List<String> warnings = new ArrayList<String>();
           boolean overwrite = true;
           File configFile = new File("mbg.xml"); // 自己的配置文件的名称
           ConfigurationParser cp = new ConfigurationParser(warnings);
           Configuration config = cp.parseConfiguration(configFile);
           DefaultShellCallback callback = new DefaultShellCallback(overwrite);
           MyBatisGenerator myBatisGenerator = new MyBatisGenerator(config, callback, warnings);
           myBatisGenerator.generate(null);
       }
   }
   ```
   
   运行成功之后就生成了相关类。

