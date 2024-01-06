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

直接把一堆文件放root文件夹里。

```bash
git add .
git commit -m "init"
git push
```

## 在vercel中登录github，选择git仓库并选择仓库

```ad-note
Ref： https://zhuanlan.zhihu.com/p/347990778
```

![[assets/Pasted image 20230421144530.png]]

## 使用自定义域名

在项目设置中添加自定义域名

![[assets/Pasted image 20230421144944.png]]

会提示不正确的设置，不用管，直接在自己的域名管理上添加CNAME解析即可

![[assets/Pasted image 20230421145047.png]]

添加成功

![[assets/Pasted image 20230421145303.png]]

回到vercel，部署成功

![[assets/Pasted image 20230421145434.png]]

可以成功访问。

![[assets/Pasted image 20230421145546.png]]

这样，每次提交commit之后就能同步更新了。

---

```ad-attention
title: 注意
这里的 theme 从 git clone 下来之后由于自带`.git`文件，直接push到repo的时候会导致识别不出来，就是文件夹上有一个小箭头。
这时候build的时候会找不到相关的layout，因此要最好删除`.git`和`LICENSE`文件。之后把文件push to repo
```


```ad-attention
title: 注意
hexo theme下载之后需要保证`_config.yml`中`theme`标签和`themes/*`里面的文件夹名字相同，否则无法加载主题。
```
