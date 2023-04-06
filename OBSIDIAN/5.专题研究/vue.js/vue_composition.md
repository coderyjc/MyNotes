## 认识Composition API

### ref和reactive

在setup中定义的数据提供响应式的特性。

我们可以使用reactive的函数，但是reactive是提供的复杂数据类型的响应式，其参数只能是对象或者数组类型，而简单类型（String，Number，Boolean等）应该使用ref函数（ref也可以定义复杂数据）。

那么这两个函数应该分别在什么地方使用呢？

首先，实际上用ref是比reactive多的。

reactive 的一般应用场景：

1. 条件一: reactive应用于本地的数据
2. 条件二: 多个数据之间是有关系/联系(聚合的数据, 组织在一起会有特定的作用)，比如username 和 password

ref 的应用场景：

1. 所有场景都适合，不用reactive的时候就用ref
```js
  const username = ref("coderwhy")
  const password = ref("123456")
```

2. 定义简单数据
```js
  const message = ref("Hello World")
  const counter = ref(0)
  const name = ref("why")
  const age = ref(18)
```

*3. 定义从服务器拿到的数据（先定义一个空数组，然后再请求。）*
```js
  const musics = ref([])
  onMounted(() => {
	const serverMusics = ["海阔天空", "小苹果", "野狼"]
	musics.value = serverMusics
  })
```






## Setup()


