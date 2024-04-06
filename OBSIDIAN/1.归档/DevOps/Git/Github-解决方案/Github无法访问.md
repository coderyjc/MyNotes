#github

# Github



![image-20221226103720874](assets/image-20221226103720874.png)

## Github无法访问

设置DNS解析改变github的DNS路径

具体参考[github520项目](https://github.com/521xueweihan/GitHub520)

---

cannot access remote repository...

节点在国内的梯子是可以访问的，但是在国外的不行。

---

挂着Clash的时候github无法访问：

设置git全局代理

```bash
git config --global http.proxy 'http://127.0.0.1:10809' git config --global https.proxy 'http://127.0.0.1:10809' # OR git config --global http.proxy 'socks5://127.0.0.1:10808' git config --global https.proxy 'socks5://127.0.0.1:10808'
```

查看代理

```bash
git config --global http.proxy
git config --global https.proxy
```

取消代理

```bash
git config --global --unset http.proxy 
git config --global --unset https.proxy
```

