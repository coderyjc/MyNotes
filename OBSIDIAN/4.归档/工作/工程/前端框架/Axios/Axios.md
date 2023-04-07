### Axios无法下载文件

```ad-attention
<font color="#ff0000">Axios是基于ajax的，ajax的设计初衷是传递json数据，而不是二进制数据！！！</font>
```

在传述文件的时候这里不能用axios传递参数到后端，因为axios主要运用ajax技术，ajax方式请求的数据只能存放在javascipt内存空间，可以通过javascript访问，但是无法保存到硬盘，因为javascript不能直接和硬盘交互，否则将是一个安全问题。

**Ajax无法下载文件的原因**

浏览器的GET(frame、a)和POST(form)请求具有如下特点：
1. response会交由浏览器处理
2. response内容可以为二进制文件、字符串等

Ajax请求具有如下特点：
1. response会交由Javascript处理
2. response内容仅可以为字符串 

Ajax本身设计的目标就是用来获取文本数据的，而不是用来传输二进制的。

如何解决这个问题：

1. 使用单独的Axios实例，而不是使用公共的（不推荐）
2. 后端，返回URL，前端进行重定向或者打开新标签页

