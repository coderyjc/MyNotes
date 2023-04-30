---
url: https://www.jianshu.com/p/be1af489551c
title: SpringBoot实现文件的上传和下载 - 简书
date: 2023-04-20 14:57:00
tag: 
summary: 前言 不关是用Java开发什么程序，或多或少都会使用到文件的上传和下载啊。比如图片文件，excel文件，错误文件是什么的。所以，能简单，快捷的实现对文件的上传和下载，或者有一...
---

- [ ] 已整理

---
### 前言

不关是用 Java 开发什么程序，或多或少都会使用到文件的上传和下载啊。比如图片文件，excel 文件，错误文件是什么的。所以，能简单，快捷的实现对文件的上传和下载，或者有一个自己的模板，用到的时候来取，是一件很方便的事情。今天小编就带领大家使用 springboot 来搭建文件的上传和下载的模板。

### 一，搭建一个 springboot 的开发环境

以下是 springboot 的 pow.xml 依赖

```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.wyl</groupId>
  <artifactId>SpringBootFile</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>SpringBootFile</name>
  <url>http://maven.apache.org</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
      <java.version>1.7</java.version>
  </properties>
  
  <parent>
      <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>1.5.3.RELEASE</version>
  </parent>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
    
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    
    <!-- thymeleaf模板插件 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-thymeleaf</artifactId>
    </dependency>
    
    
  </dependencies>
</project>
```

### 2、application.properties 文件中取消模板文件缓存

```
spring.thymeleaf.cache=false
```

### 3、编写模板文件

```
file.html

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:th="http://www.thymeleaf.org" xmlns:sec="http://www.thymeleaf.org/thymeleaf-extras-springsecurity3">
<head>
<meta charset="UTF-8" />
<title>Insert title here</title>
</head>
<body>
    <h1 th:inlines="text">文件上传</h1>
    <form action="fileUpload" method="post" enctype="multipart/form-data">
        <p>选择文件: <input type="file" name="fileName"/></p>
        <p><input type="submit" value="提交"/></p>
    </form>
</body>
</html>

multifile.html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:th="http://www.thymeleaf.org"  
      xmlns:sec="http://www.thymeleaf.org/thymeleaf-extras-springsecurity3">
<head>
<meta charset="UTF-8" />
<title>Insert title here</title>
</head>
<body>
    <h1 th:inlines="text">文件上传</h1>
    <form action="multifileUpload" method="post" enctype="multipart/form-data" >
        <p>选择文件1: <input type="file" name="fileName"/></p>
        <p>选择文件2: <input type="file" name="fileName"/></p>
        <p>选择文件3: <input type="file" name="fileName"/></p>
        <p><input type="submit" value="提交"/></p>
    </form>
</body>
</html>
```

### 4、编写 Controller

```
@Controller
public class FileUploadController {

    /*
     * 获取file.html页面
     */
    @RequestMapping("file")
    public String file(){
        return "/file";
    }
    
    /**
     * 实现文件上传
     * */
    @RequestMapping("fileUpload")
    @ResponseBody 
    public String fileUpload(@RequestParam("fileName") MultipartFile file){
        if(file.isEmpty()){
            return "false";
        }
        String fileName = file.getOriginalFilename();
        int size = (int) file.getSize();
        System.out.println(fileName + "-->" + size);
        
        String path = "F:/test" ;
        File dest = new File(path + "/" + fileName);
        if(!dest.getParentFile().exists()){ //判断文件父目录是否存在
            dest.getParentFile().mkdir();
        }
        try {
            file.transferTo(dest); //保存文件
            return "true";
        } catch (IllegalStateException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            return "false";
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            return "false";
        }
    }

　　/*
     * 获取multifile.html页面
     */
    @RequestMapping("multifile")
    public String multifile(){
        return "/multifile";
    }
    
    /**
     * 实现多文件上传
     * */
    @RequestMapping(value="multifileUpload",method=RequestMethod.POST) 
　　/**public @ResponseBody String multifileUpload(@RequestParam("fileName")List<MultipartFile> files) */
    public @ResponseBody String multifileUpload(HttpServletRequest request){
        
        List<MultipartFile> files = ((MultipartHttpServletRequest)request).getFiles("fileName");
        
        if(files.isEmpty()){
            return "false";
        }

        String path = "F:/test" ;
        
        for(MultipartFile file:files){
            String fileName = file.getOriginalFilename();
            int size = (int) file.getSize();
            System.out.println(fileName + "-->" + size);
            
            if(file.isEmpty()){
                return "false";
            }else{        
                File dest = new File(path + "/" + fileName);
                if(!dest.getParentFile().exists()){ //判断文件父目录是否存在
                    dest.getParentFile().mkdir();
                }
                try {
                    file.transferTo(dest);
                }catch (Exception e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                    return "false";
                } 
            }
        }
        return "true";
    }
}
```

### 五 遇见的问题

可能你再上传文件的时候遇见一个问题，就是我们上传的文件被限制了文件的大小。

```
org.apache.tomcat.util.http.fileupload.FileUploadBase$FileSizeLimitExceededException: 
The field fileName exceeds its maximum permitted size of 1048576 bytes.
```

SpringBoot 的默认上传文件的大小是 2m 如果你上传的文件超过了 2m 就会出现这样的错误。  
这个时候我们可以再 application.properties 里面进行修改

```
# Single file max size 
multipart.maxFileSize=50Mb
# All files max size 
multipart.maxRequestSize=50Mb
```

但是，这样有可能解决不了问题。  
这个是时候我们需要在配置文件里面修改下配置文件。

新建一个类，加上 @Configuration 文件进行说明，这是一个配置类。  
然后在类里面加上

```
@Bean
    public MultipartConfigElement multipartConfigElement() {
        MultipartConfigFactory factory = new MultipartConfigFactory();

        //factory.setMaxFileSize(1024);
        //单个文件最大
        factory.setMaxFileSize("10240KB"); //KB,MB
        /// 设置总上传数据总大小
        factory.setMaxRequestSize("102400KB");
        return factory.createMultipartConfig();
    }
```

@Bean 这个注解会把 return 的那个类装到 spring 的 bean 工厂里面，这样 springboot 在启动的时候，扫描到这个类就会进行相应配置的修改。

### 6 文件的下载

```
@RequestMapping("/download")
    public String downLoad(HttpServletResponse response) throws UnsupportedEncodingException {
        String filename="2.xlsx";
        String filePath = "D:/download" ;
        File file = new File(filePath + "/" + filename);
        if(file.exists()){ //判断文件父目录是否存在
            response.setContentType("application/vnd.ms-excel;charset=UTF-8");
            response.setCharacterEncoding("UTF-8");
           // response.setContentType("application/force-download");
            response.setHeader("Content-Disposition", "attachment;fileName=" +   java.net.URLEncoder.encode(filename,"UTF-8"));
            byte[] buffer = new byte[1024];
            FileInputStream fis = null; //文件输入流
            BufferedInputStream bis = null;

            OutputStream os = null; //输出流
            try {
                os = response.getOutputStream();
                fis = new FileInputStream(file);
                bis = new BufferedInputStream(fis);
                int i = bis.read(buffer);
                while(i != -1){
                    os.write(buffer);
                    i = bis.read(buffer);
                }

            } catch (Exception e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            System.out.println("----------file download---" + filename);
            try {
                bis.close();
                fis.close();
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }
        return null;
    }
```

[个人 GitHub 项目，记录学习 Java 知识的过程 欢迎 star](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Flikeaxa%2FJavaStudy)  

![](http://upload-images.jianshu.io/upload_images/10280355-506e9aa14313b513.png)

image.png