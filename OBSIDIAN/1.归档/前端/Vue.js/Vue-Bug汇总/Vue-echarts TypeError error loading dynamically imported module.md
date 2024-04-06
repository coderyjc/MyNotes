---
type: DeBug
skill: Vue.js
create_date: 2022-01-31
---

#前端/前端框架


![[assets/Pasted image 20230310084246.png]]

代码中的option应该提前声明

错误代码：

```js
option =  {
// .....
}
```

正确代码：

```js
const option = {
// .....
}
```