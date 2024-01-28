## Nginx 通过不同的端口部署多个项目

#后端/nginx

在 `/www/server/nginx/conf/vhost` 添加项目的配置文件

假设是`manage.conf`

```
  1 server {
  2     listen 9091; # 监听9091 端口
  3     server_name 域名或者ip; # 服务器名称
  4     location / {
  5         root /www/wwwroot/manage/; # 所在文件夹
  6         index index.html; # 根目录
  7     }
  8 }
```

在nginx主文件中添加配置项的包含`include /www/server/nginx/conf/vhost/*.conf;`

![[Nginx-解决方案/assets/Pasted image 20220504145804.png]]

使用命令检查nginx服务是否正确 `nginx -t`

![[Nginx-解决方案/assets/Pasted image 20220504145951.png]]

重启服务器 `nginx -s reload`

> 在此之前， 记得把防火墙和安全组的端口开放。

