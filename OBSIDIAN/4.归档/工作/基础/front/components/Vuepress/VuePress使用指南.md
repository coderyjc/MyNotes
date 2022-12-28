
> 学习技术最有效的方式是查看官方文档[https://www.vuepress.cn/](https://www.vuepress.cn/)
> 
> 本教程为本人的学习官方文档的记录.

#前端/Vuepress 

VuePress 是 Vue 驱动的静态网站生成器, 一般用来作为文档网站.

## 安装

安装

```bash
# 安装
npm install -g vuepress

# 开始写作
vuepress dev .
```

构建静态文件

```bash
# 构建静态文件
vuepress build .
```

目录结构: 

> 这是我修改版的目录结构, 官方完整版目录查看 [这里](https://www.vuepress.cn/guide/directory-structure.html#%E9%BB%98%E8%AE%A4%E7%9A%84%E9%A1%B5%E9%9D%A2%E8%B7%AF%E7%94%B1)

```
.
├── docs
│   ├── .vuepress (可选的) // 配置文件
│   │   ├── public (可选的) // 存放图片等
│   ├── README.md // 首页
│   └── doc // 文档, 网站的内容全都放在这个目录下面
│       └── README.md
│   
└── package.json
```


## 使用

### 首页

在根目录的READ.ME上添加如下文字作为文档头

```yaml
---
home: true
heroText: CoderYan's Doc
tagline: 在线文档
heroImage: /icon.png
actionText: 开始 (｡･ω･｡)ﾉ♡
actionLink: /docs/
features:
- title: 基础知识
  details: 不是调试和开发经验总结, 而是各种技术的基础知识和基本使用
- title: 实践为主
  details: 大多文档没有繁杂的理论, 偏向实用性, 大多代码复制修改便可使用.
- title: 无限进步
  details: 随着作者技术的进步, 本文档会不断更新.
footer: 鲁ICP备2022021779号
---
```

icon.png是一张空白的图片, 用来占用标题上方的位置, 以将标题挤下来, 使它位于中间.

actionLink是点击中间绿色按钮的跳转事件

![](assets/Pasted%20image%2020220907081920.png)

### 导航栏

> 配置写在  `.vuepress\config.js` 的 `themeConfig.nav` 列表中, 

代码总览

```js
module.exports = {
  title: 'CoderYan\'s Doc',
  themeConfig: {
    nav: [
      {
        // 带有分组的下拉列表
        text: '前端技术',
        items: [
          { 
            // 分组名字
            text: '前端基础', 
            // 分组项目
            items: [
              { text: 'HTML', link: '/docs' },
              { text: 'CSS', link: '/docs' },
              { text: 'JavaScript', link: '/docs' }
            ]
          },
        ]
      },
      // 下拉列表
      {
        text: 'Java后端',
        items: [
          { text: 'JavaSE', link: '/docs' },
          { text: 'JVM', link: '/docs' },
          { text: 'JUC', link: '/docs' }
        ]
      },
      // 普通的导航栏
      { text: 'Python', link: '/docs' },
      { text: '效率软件', link: '/docs' },
      { text: '部落格', link: 'http://blog.evilemperor.top/' },
      { text: 'Github', link: 'https://github.com/jancoyan/doc' },
    ]
  }
}
```

![](assets/Pasted%20image%2020220907083640.png)

![](assets/Pasted%20image%2020220907083740.png)

### 侧边栏

> 该配置写在  `.vuepress\config.js` 中







