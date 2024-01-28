---
tags:
  - 前端/hexo
---


安装hexo的搜索插件 

```bash
npm install hexo-generator-search --save
```

创建搜索页面

```bash
hexo new page search
```

修改搜索页面的frontmatter

```md
---
title: Search
type: search
---
```

在nav中添加路由

```yml
nav:
  search: /search/
```