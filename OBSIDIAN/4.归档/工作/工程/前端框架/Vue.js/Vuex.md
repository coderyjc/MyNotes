---
type: 学习总结
skill: Vuex
create_date: 2022-01-31
---

#前端框架 #前端 #组件 #前端/Vue

# Vuex

Mutition 函数中不能写异步的代码，比如 setTimeout ，要想写异步代码的函数，必须定义在 action中

在action中不能直接修改state中的数据，必须通过context.commit() 触发某个mutation才行