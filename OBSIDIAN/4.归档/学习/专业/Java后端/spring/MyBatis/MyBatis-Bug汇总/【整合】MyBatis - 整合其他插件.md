---
type: 学习总结
skill: MyBatis
create_date: 2022-01-31
---

#后端/JavaWeb #后端/MyBatis #后端/PageHelper

### 整合pagehelper和mybatis-plus


在SSM中整合pagehelper只需要导入一个依赖，但是Springboot中需要导入三个依赖

```xml
<dependency>
    <groupId>com.github.pagehelper</groupId>
    <artifactId>pagehelper</artifactId>
    <version>5.1.4</version>
</dependency>
<dependency>
    <groupId>com.github.pagehelper</groupId>
    <artifactId>pagehelper-spring-boot-starter</artifactId>
    <version>1.2.5</version>
</dependency>
<dependency>
    <groupId>com.github.pagehelper</groupId>
    <artifactId>pagehelper-spring-boot-autoconfigure</artifactId>
    <version>1.2.5</version>
</dependency>
```

并且如果要用Mybatis-plus进行分页，还要写一个过滤器

```java
/**
 * @Author: Yan Jingcun
 * @Date: 2021/6/28
 * @Description:
 * @Version: 1.0
 */

package com.jancoyan.commentset.config;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.transaction.annotation.EnableTransactionManagement;

@EnableTransactionManagement
@Configuration
@MapperScan("com.jancoyan.commentset.mapper")
public class MybatisPlusConfig {
    // 分页拦截器对象，目前分页不支持表连接，只能单表查询
    @Bean
    public MybatisPlusInterceptor mybatisPlusInterceptor() {
        MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();
        interceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
        return interceptor;
    }
}
```

### 整合jsp的时候访问不到静态资源

springboot 默认的静态资源的值有四个：

-   _classpath:/META-INF/resources/_
-   _classpath:/resources/_
-   _classpath:/static/_
-   _classpath:/public/_

如果你没有特别配置静态资源的位置，那么默认的静态资源的位置就是resource 下面的static文件夹，毕竟不用自己新建文件夹

那么你的页面引入的静态文件可以这么写：

`<script type="text/javascript" src="/js/jquery.min.js"></script>`

这样就需要在static下面创建js文件夹，将jqeruy.js放在这个js文件夹下面

![[assets/image-20220131015250.png]]

详解可以查看[[../../SprintBoot/SpringBoot-Bug汇总/【总结】SpringBoot路径访问]]
