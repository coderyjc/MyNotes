```ad-note
使用vercel，使用hexo模版进行部署
```


## 购买域名并进行实名认证

在百度智能云中购买了域名

```ad-warning
注意：只是使用域名，不使用服务器空间的话，只需要实名认证，**不需要进行备案**。
此时还是可以进行解析的。可以创建CNAME域名
```

![[assets/Pasted image 20230421142747.png]]

## 创建git repo并使用hexo模版进行部署

> hexo官方文档：https://hexo.io/zh-cn/docs/

创建空的git repo `vercel`

克隆repo到本地，此时是一个空的repo。

安装hexo `npm install -g hexo-cli`

文件夹中执行 `hexo init <folder>`

直接把一堆文件放文件夹里。


