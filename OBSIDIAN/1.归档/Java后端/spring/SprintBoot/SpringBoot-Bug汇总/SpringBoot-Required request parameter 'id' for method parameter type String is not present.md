---
type: DeBug
skill: SpringBoot
create_date: 2022-01-31
---

#后端/JavaWeb #Java后端/SpringBoot #后端/Spring

说我这个参数没有提供 ，我看了一下请求，确实没有提供。

异步函数，在值没有拿到的时候就使用了，导致找不到值。

await等待拿值的函数执行完成即可