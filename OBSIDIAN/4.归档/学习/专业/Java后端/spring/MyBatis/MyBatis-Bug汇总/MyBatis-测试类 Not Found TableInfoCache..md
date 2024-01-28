---
type: DeBug
skill: MyBatis
create_date: 2022-01-31
---

#后端/JavaWeb #后端/MyBatis #后端/MyBatis

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
