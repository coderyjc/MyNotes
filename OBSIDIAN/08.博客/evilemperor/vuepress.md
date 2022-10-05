### 提示vue和vue-template-compiler版本不一致问题

可能是自己安装了一些东西, 卸载自己安装的东西之后, `npm install request` 重新安装一下依赖即可

另外, 安装新组件的时候新开一个cmd窗口安装有时候不会导致这种问题

### 多个侧边栏但是在页面中不显示多个侧边栏

> 官方教程: 多个侧边栏的使用 https://www.vuepress.cn/zh/theme/default-theme-config.html#%E5%A4%9A%E4%B8%AA%E4%BE%A7%E8%BE%B9%E6%A0%8F

在`config.js`中配置了多个侧边栏之后, **不能在单个的md文档中配置 sidebar:auto** , 否则会导致多侧边栏加载失败

文件目录结构

```
docs/java/javase
├── README.md   
└── java-basic
    ├── java-annotation.md
    ├── java-basic-basic.md
    ├── java-basic-jdbc.md
    ├── java-basic-oop.md
    ├── java-exception.md
    └── java-reflection.md
```

多侧边栏配置

```json
    sidebar: {
      '/docs/java/java-basic/': [
        '',
        'java-basic-basic',
        'java-basic-oop',
        'java-basic-jdbc',
        'java-exception',
        'java-annotation',
        'java-reflection',
      ]
    },
```

![](assets/Pasted%20image%2020221005231739.png)

注意: 在这里在`config.js`中配置了 sidebar 的 `/docs/java/java-basic/`, 因此访问的url定位到 `java-basic/` 的时候, 会默认显示`Java基础知识`处于激活状态, 这一点要注意, 在进行`侧边栏分组+多个侧边栏结合`的时候, 还会进行进一步说明.

**注意**: 配置之后就不能在这里面的文档中配置

```yaml
---
sidebar: auto
---
```

否则会导致加载侧边栏失败.

### 侧边栏分组+多个侧边栏结合

文档结构：

```text
docs/java/javase
├── README.md   
├── java-basic
│   ├── java-annotation.md
│   ├── java-basic-basic.md
│   ├── java-basic-jdbc.md
│   ├── java-basic-oop.md
│   ├── java-exception.md
│   └── java-reflection.md
└── java-collection
    ├── java-collection-src-arraylist.md
    ├── java-collection-src-hashset-hashmap.md
    ├── java-collection-src-linkedhashmap-set.md
    ├── java-collection-src-linkedlist.md
    ├── java-collection-src-priorityqueue.md
    ├── java-collection-src-stack-queue.md
    └── java-collection-src-treeset-treemap.md
```

应该进行的配置:

```json
sidebar: {
      '/docs/java/javase/': [
        {
          title: 'Java基础知识',
          collapsable: false,
          // path: '/docs/java/javase/',
          sidebarDepth: 1,
          children: [
            ['java-basic/java-basic-basic', 'Java-基础知识'],
            ['java-basic/java-basic-oop', 'Java-面向对象'],
            ['java-basic/java-exception', 'Java-异常处理'],
            ['java-basic/java-annotation', 'Java-注解'],
            ['java-basic/java-reflection', 'Java-反射机制'],
            ['java-basic/java-basic-jdbc', 'Java-JDBC'],
          ]
        },
        {
          title: 'Java集合详解',
          // path: '/docs/java/javase/',
          collapsable: false,
          sidebarDepth: 1,
          children: [
            ['java-collection/java-collection-src-arraylist', 'ArrayList源码解析'],
            ['java-collection/java-collection-src-linkedlist', 'LinkedList源码解析'],
            ['java-collection/java-collection-src-stack-queue', 'Stack&Queue源码解析'],
            ['java-collection/java-collection-src-priorityqueue', 'PriorityQueue源码解析'],
            ['java-collection/java-collection-src-hashset-hashmap', 'HashSet&HashMap源码解析'],
            ['java-collection/java-collection-src-linkedhashmap-set', 'LinkedHashMap&Set源码解析'],
            ['java-collection/java-collection-src-treeset-treemap', 'TreeSet&Map源码解析'],
          ]
        },

      ],
    },
 
```

**注意**: 这里的 path 被注释掉了, 不能加, 加了之后会出现如下情况, 当访问根目录的时候, 这两个分类会同时被激活, 而且鼠标指针是pointer, 不加的时候就没事.

![](assets/Pasted%20image%2020221005233521.png)


