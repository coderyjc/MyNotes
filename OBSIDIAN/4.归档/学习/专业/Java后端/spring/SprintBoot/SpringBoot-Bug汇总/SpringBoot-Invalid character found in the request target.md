---
type: DeBug
skill: SpringBoot
create_date: 2022-01-31
---

#后端/JavaWeb #Java后端/SpringBoot #后端/Spring


情景：

使用Vue-Cli工程构建博客系统，集成 [[tui.editor]] 在向后端传输md格式的文本的时候发生400错误，并后端报错：Invalid character found in the request target

```markdown
Invalid character found in the request target [/article/post?title=&type=&summary=&
comment=true&md=%27%23+Axios%0A%0A%3E+Axios+%E5%AE%98%E7%BD%91+[https:%2F%2Fgithub.
com%2Faxios%2Faxios](https://%2F%2Fgithub.com%2Faxios%2Faxios/)%0A%0A%23%23+get%E8%
F%B7%E6%B1%82%0A%0A%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95%EF%BC%9A%0A%0A%60axios.get(%
E5%9C%B0%E5%9D%80%EF%BC%9Fk1%3Dv1%26k2%3Dvv2%26k3%3Dv3).then(function(reponse)%7B%7D
,function(error)%7B%7D)%60%0A%0A%E7%A4%BA%E4%BE%8B%EF%BC%9A%0A%0A%60%60%60js%0Afunct
ion()%7B%0A++++axi
... ...
```

**原因：**

SpringBoot 2.0.0 以上都采用内置[[../../../基础/middleware/tomcat/Tomcat|Tomcat]]8.0以上版本，而tomcat8.0以上版本遵从RFC规范添加了对Url的特殊字符的限制，url中只允许包含英文字母(a-zA-Z)、数字(0-9)、-_.~四个特殊字符以及保留字符( ! * ’ ( ) ; : @ & = + $ , / ? # [ ] ) (262+10+4+18=84)这84个字符,请求中出现了{}大括号或者[],所以tomcat报错。设置RelaxedQueryChars允许此字符(建议)，设置requestTargetAllows选项(Tomcat 8.5中不推荐)。 根据Tomcat文档，下面提供一种方法来设置松弛的QueryChars属性* 

**解决方案：**

在启动类中添加如下函数：

```java
@Bean
public ConfigurableServletWebServerFactory webServerFactory() {
	TomcatServletWebServerFactory factory = new TomcatServletWebServerFactory();
	factory.addConnectorCustomizers(connector -> connector.setProperty("relaxedQueryChars", "|{}[]"));
	return factory;
}
```