
###  Invalid bound statement (not found)

原因是找不到可映射的xml文件，在`application.yml`中设置一下mp的xml文件所在目录即可

```yml
mybatis-plus:  
  mapper-locations: classpath:mapper/*.xml
```

此时的目录结构为：

![[assets/Pasted image 20230405180249.png]]

此时的 `pom.xml`中的build为：

```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
```

