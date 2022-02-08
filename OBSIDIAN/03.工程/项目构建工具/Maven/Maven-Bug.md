---
type: Bug总结
skill: maven
create_date: 2022-01-30
---

#bug总结 #maven #后端

# maven_bugs

####  Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.22.2

pom.xml中加入以下代码

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>2.22.2</version>
            <configuration>
                <skipTests>true</skipTests>
            </configuration>
        </plugin>
    </plugins>
</build>
```

---
#### 在generator生成表之后，更改表名之后，显示找不到指定的文件R:\GITHUB\JancoBlog\JancoBlog-v3.0\src\main\java\com\jancoyan\jancoblog\pojo\User_login.java (系统找不到指定的文件。)

解决方案：

在保证了所有名字都改好了的情况下。

maven → clean → build 即可

要更改名字的地方包括但不限于：

-   POJO
-   Java文件的import 语句
-   POJO、Service、Controller、Mapper、Mapper.xml 中的所有的用到该POJO的泛型
-   Mapper.xml 中的引用