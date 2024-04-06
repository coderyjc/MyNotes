### Error processing request/Error reading request, ignored/Error running socket processor

```
简单来说就是spring-boot中tomcat版本是9.0.24或者9.0.25版本的，这两个版本有两个bug就是你的服务如果是https的时候，接受到http请求的时候就会报这个错，但是对业务无影响；

解决方案：

忽略对应错误或者升级tomcat版本到9.0.26及以上版本
```