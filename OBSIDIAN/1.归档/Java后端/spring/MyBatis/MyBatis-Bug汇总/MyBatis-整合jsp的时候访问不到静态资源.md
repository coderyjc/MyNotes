---
type: 学习总结
skill: MyBatis
create_date: 2022-01-31
---

#后端/JavaWeb #后端/MyBatis #后端/PageHelper

springboot 默认的静态资源的值有四个：

-   _classpath:/META-INF/resources/_
-   _classpath:/resources/_
-   _classpath:/static/_
-   _classpath:/public/_

如果你没有特别配置静态资源的位置，那么默认的静态资源的位置就是resource 下面的static文件夹，毕竟不用自己新建文件夹

那么你的页面引入的静态文件可以这么写：

`<script type="text/javascript" src="/js/jquery.min.js"></script>`

这样就需要在static下面创建js文件夹，将jqeruy.js放在这个js文件夹下面

![[assets/image-20220131015250.png]]

详解可以查看[[../../SprintBoot/SprintBoot-解决方案/【总结】SpringBoot路径访问]]
