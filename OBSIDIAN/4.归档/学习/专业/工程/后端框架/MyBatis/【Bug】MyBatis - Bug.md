---
type: DeBug
skill: MyBatis
create_date: 2022-01-31
---

#JavaWeb #MyBatis #Bug/MyBatis

# MyBatis

>MyBatis 中测试类 ...... Not Found TableInfoCache.

主测试类中应该手动注入mapper类

```java
package com.jancoyan.timemaster;

import com.jancoyan.timemaster.pojo.Record;
import org.junit.jupiter.api.Test;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Date;

@SpringBootTest
@MapperScan("com.jancoyan.timemaster.mapper")
class TimeMasterApplicationTests {
    @Test
    void contextLoads() {
    }
}
```

在使用别的测试类的时候应该继承这个类

```java
/**
 * @Author: Yan Jingcun
 * @Date: 2021/8/30
 * @Description:
 * @Version: 1.0
 */

package com.jancoyan.timemaster;

import com.jancoyan.timemaster.pojo.Record;
import org.junit.jupiter.api.Test;

import java.util.Date;

public class DataBaseTest extends TimeMasterApplicationTests {

    @Test
    public void insertTest(){
        Record record = new Record();
        record.setRecordType(1);
        record.setRecordContent("test");
        record.setStartTime(new Date());
        record.setEndTime(new Date());
        record.insert();
    }

}
```

>There is no getter for property named 'null' in 'xx'
>No Such Field in Class for null

Mybatis Plus 在使用AR的时候会先在POJO类中查找带有TableId注解的类作为主键，如果没有会报错

所以原因：

-   POJO类中没有主键声明 @TableId 或者 @TableId(value = "record_id", type = IdType.AUTO)

如果不是上面的原因，那就是主键有问题，从主键方面找问题就行。

>Cannot determine value type from string

将字段类型修改成String类型解决问题。

遇到类似报错的童靴，可以检查数据库字段与实体类字段类型是否匹配

## 快速使用

添加依赖

```xml
<!--        MybitsPlus插件-->
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.2.0</version>
</dependency>
<dependency>
    <groupId>org.apache.velocity</groupId>
    <artifactId>velocity-engine-core</artifactId>
    <version>2.3</version>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-autoconfigure</artifactId>
    <version>2.5.2</version>
</dependency>
```

测试类

![[assets/image-20220131015058.png]]

上面这个错误，占位符错了

```sql
<select id="listIndex" resultMap="BaseResultMap">
        select <include refid="Index_Column_List" />
        from v_website_index #{ew.customSqlSegment}
</select>
```

改成

```sql
<select id="listIndex" resultMap="BaseResultMap">
        select <include refid="Index_Column_List" />
        from v_website_index ${ew.customSqlSegment}
</select>
```

占位符的区别：

-   #{} 的参数替换是发生在 DBMS 中，符号存在预编译的过程，对问号赋值，防止 SQL 注入。它将传入的数据都当成一个字符串，会对自动传入的数据加一个双引号
-   ${} 则发生在动态解析过程中，没有预编译过程，将传入的数据直接显示生成 SQL 中

使用$可能会导致SQL注入攻击，能用#号就不用 $号