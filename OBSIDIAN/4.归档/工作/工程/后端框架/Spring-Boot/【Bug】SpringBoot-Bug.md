---
type: DeBug
skill: SpringBoot
create_date: 2022-01-31
---

#后端 #JavaWeb #SpringBoot #后端/Spring


## 网络请求相关

> Invalid character found in the request target

情景：

使用[[../../前端框架/Vue.js/Vue-Cli]]工程构建博客系统，集成 [[tui.editor]] 在向后端传输md格式的文本的时候发生400错误，并后端报错：Invalid character found in the request target

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

SpringBoot 2.0.0 以上都采用内置[[../../../基础/middleware/tomcat/Tomcat]]8.0以上版本，而tomcat8.0以上版本遵从RFC规范添加了对Url的特殊字符的限制，url中只允许包含英文字母(a-zA-Z)、数字(0-9)、-_.~四个特殊字符以及保留字符( ! * ’ ( ) ; : @ & = + $ , / ? # [ ] ) (262+10+4+18=84)这84个字符,请求中出现了{}大括号或者[],所以tomcat报错。设置RelaxedQueryChars允许此字符(建议)，设置requestTargetAllows选项(Tomcat 8.5中不推荐)。 根据Tomcat文档，下面提供一种方法来设置松弛的QueryChars属性* ———————————————— 版权声明：本文为CSDN博主「崔雨田」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。 原文链接：[](https://blog.csdn.net/qq_41291945/article/details/105126610)[https://blog.csdn.net/qq_41291945/article/details/105126610](https://blog.csdn.net/qq_41291945/article/details/105126610)

**解决方案：**

在启动类中添加如下函数：

```java
@Bean
public ConfigurableServletWebServerFactory webServerFactory() {
    TomcatServletWebServerFactory factory = new TomcatServletWebServerFactory();
    factory.addConnectorCustomizers(new TomcatConnectorCustomizer() {
        @Override
        public void customize(Connector connector) {
            connector.setProperty("relaxedQueryChars", "|{}[]");
        }
    });
    return factory;
}
```

>400 Bad Request "org.springframework.web.bind.MissingServletRequestParameterException: **Required request parameter 'id' for method parameter type String is not present**

说我这个参数没有提供 ，我看了一下请求，确实没有提供。

异步函数，在值没有拿到的时候就使用了，导致找不到值。

await等待拿值的函数执行完成即可

> Spring Boot Request header is too large

application.yml 配置文件中设置最大请求头大小

```yaml
server:
  max-http-header-size: 128KB
```

> 后台接受图片文件

后端接受 MultipartFile 类型的文件

前端使用XMLHttpRequest和formData 的时候不用自己指定contentType，而是可以让formdata封装好（会自动添加boundary）

这样后端就不会报错“is not multipart file ” 和 " boundary not found "

后端：

```java
/**
     * 更换头像
     * @return
     */
    @RequestMapping(value = "/upload/avatar", method = RequestMethod.POST)
    public Msg uploadAvatar(
            @RequestParam(value = "file") MultipartFile file,
            HttpServletRequest request
    ){
        // 登录状态
        String token = request.getHeader("token");
        if (null == token){
            return Msg.fail();
        }
        // 获取用户
        User user = (User) redisUtil.get(token);
        if (null == user){
            return Msg.expire();
        }
        // 文件判定
        if (null == file) {
            return Msg.fail().add("msg", "请选择要上传的图片");
        }
        if (file.getSize() > 1024 * 1024 * 10) {
            return Msg.fail().add("msg", "文件大小不能大于10M");
        }
        //获取文件后缀
        String suffix = Objects.requireNonNull(file.getOriginalFilename()).substring(file.getOriginalFilename().lastIndexOf(".") + 1);
        if (!"jpg,jpeg,gif,png".toUpperCase().contains(suffix.toUpperCase())) {
            return Msg.fail().add("msg", "请选择jpg,jpeg,gif,png格式的图片");
        }
        String savePath = null;
        try {
            savePath = new File(".").getCanonicalPath() + "\\\\target\\\\classes\\\\static\\\\avatar\\\\";
        } catch (IOException e) {
            e.printStackTrace();
        }

        File savePathFile = new File(savePath);
        if (!savePathFile.exists()) {
            //若不存在该目录，则创建目录
            savePathFile.mkdir();
        }

        //用户头像名称就是用户的id
        String filename = user.getUserId() + "." + suffix;

        try {
            //将文件保存指定目录
            file.transferTo(new File(savePath + filename));
        } catch (Exception e) {
            e.printStackTrace();
            return Msg.fail().add("msg", "保存文件异常");
        }

//        //返回文件名称
        return Msg.success().add("suc", true);
    }
```

前端

```jsx
uploadImg(type) {
      let _this = this
      if (type === 'blob') {
        //获取截图的blob数据
        this.$refs.cropper.getCropBlob(async (data) => {
          let formData = new FormData()
          formData.append('file', data, 'file.png')
          //调用接口上传
          const ajax = new XMLHttpRequest()
          ajax.open('POST', '<http://localhost:8080/user/upload/avatar>', true)
          ajax.setRequestHeader("token", getToken())
          ajax.send(formData)
          ajax.onreadystatechange = function () {

          }
        })
      }
    },
```


## 配置文件相关

> MalformedInputException: Input length = 1

是因为yml配置文件中有中文，删掉中文即可。