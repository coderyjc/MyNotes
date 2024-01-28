---
type: 学习总结
skill: Uni-App
create_date: 2022-01-31
---

#前端/前端框架/Uni-App 

# Scroll-View 无法下滑问题

给 Scroll-view 一个高度即可

在scroll-view的属性中加上这样一行代码：

```jsx
style="height: calc(100vh - var(--window-top) - var(--window-bottom))"
```