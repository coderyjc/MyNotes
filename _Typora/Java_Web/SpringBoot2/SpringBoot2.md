## 第一个SpringBoot程序

核心原理：自动装配

### IDEA创建SpringBoot项目

建立新项目

<img src="R:\GITHUB\MyNotes\_Typora\Java_Web\SpringBoot2\SpringBoot2.imgs\image-20210424181919285.png" alt="image-20210424181919285" style="zoom:67%;" />

选择依赖

<img src="R:\GITHUB\MyNotes\_Typora\Java_Web\SpringBoot2\SpringBoot2.imgs\image-20210424182057332.png" alt="image-20210424182057332" style="zoom:67%;" />



在com.Jancoyan.helloSpringboot.Application.java的同级目录下面写项目，也就是如图所示：

<img src="R:\GITHUB\MyNotes\_Typora\Java_Web\SpringBoot2\SpringBoot2.imgs\image-20210421204104107.png" alt="image-20210421204104107" style="zoom:67%;" />

在Controller中新建一个controller

```java
// HelloController

@RestController
public class HelloController {
    //http://localhost:8080/hello 直接就能用了
    @RequestMapping("/hello")
    public String Hello(){
        // 调用业务接受前端参数
        return "hello world";
    }
}
```

运行项目，输入网址http://localhost:8080/hello

<img src="R:\GITHUB\MyNotes\_Typora\Java_Web\SpringBoot2\SpringBoot2.imgs\image-20210424183023654.png" alt="image-20210424183023654" style="zoom:67%;" />

运行成功。

## 自动装配原理

