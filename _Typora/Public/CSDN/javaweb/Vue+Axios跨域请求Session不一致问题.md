# vue-element-admin+Axios跨域请求session不一致问题



### 场景复现

> 前端：Vue-Cli + Axios + ElementUI + Node.js + vue-element-admin
>
> 后端：Spring Boot
>
> 数据库：MySQL + Redis



在做用户注册的验证码功能的时候，前端发起请求，后端生成验证码图片发送到前端，并将验证码字符串存放到session中，但是在前端输入表单发送注册请求的时候，一直显示注册失败，通过调试发现两次请求的SessionID不同。



### 解决步骤

1. 设置proxy代理（根目录下 vue.config.js 文件，没有就新建一个）

   ```js
   module.exports = {
   　　　　devServer: {
   　　// 设置代理
   　　　　　　proxy: {
   　　　　　　　'/app': {
     　　　　　　　　// 目标 API 地址
   　　　　　　　　　target: 'http://localhost:8080/',
   　　　　　　　　　changeOrigin: true,
   　　　　　　　　　pathRewrite:{
   　　　　　　　　　　'^/app':""
   　　　　　　　　　　}
   　　　　　　　　}
   　　　　　}
   　　}
   }
   ```

   

2. main.js 中配置axios

   ```js
   // 在引入axios之后加入下面这句话
   Axios.defaults.withCredentials=true;
   ```



3. 后端过滤器加入两行代码

   ```java
   
   public class AllowOriginIntercepter implements HandlerInterceptor {
   
       @Override
       public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) {
           // 过滤器
         // 注释掉这一句
         // response.setHeader("Access-Control-Allow-Origin", "*");
         // 加入这两句
           response.setHeader("Access-Control-Allow-Origin", request.getHeader("Origin"));
           response.setHeader("Access-Control-Allow-Credentials", "true");
         
         // --------------无关代码-----------------------
           response.setHeader("Access-Control-Allow-Methods","GET, POST, OPTIONS");
           response.setHeader("Access-Control-Allow-Headers","Authorization, Content-Type, token");
           return true;
       }
   }
   
   ```

   

问题解决。



### 参考文章

https://www.cnblogs.com/guangixn/p/9843946.html

