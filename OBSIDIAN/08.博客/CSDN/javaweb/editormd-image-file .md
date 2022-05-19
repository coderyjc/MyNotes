# Required request part 'editormd-image-file' is not present

我是用的SSM框架搭建的博客系统，使用editormd进行图片上传的时候遇到了问题：

后端报错`Required request part 'editormd-image-file' is not present`

前端报错`cannot parse json` // 具体错误记不清了，反正就是不能把一个对象转换为json格式

废话不多说，直接上解决方案。

[[SpringMVC]]处理MultipartFile的时候要进行两个地方的配置：

SpringMVC配置文件中添加

```xml
<!--dispatcherServlet-servlet.xml -->

<bean id="multipartResolver" class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
    <!-- 文件上传的最大值-->
    <property name="maxUploadSize" value="10485760"></property>
    <!-- 文件上传时写入内存的最大值，默认为10240 -->
    <property name="maxInMemorySize" value="4096"></property>
    <!-- 默认编码 -->
    <property name="defaultEncoding" value="UTF-8"></property>
</bean>
```

项目中引入依赖

```xml
<!--pom.xml-->
	<dependency>
      <groupId>commons-fileupload</groupId>
      <artifactId>commons-fileupload</artifactId>
      <version>1.2.2</version>
    </dependency>
    <dependency>
      <groupId>commons-io</groupId>
      <artifactId>commons-io</artifactId>
      <version>2.0.1</version>
    </dependency>
```

解决了这两个问题之后就好了。