---
type: DeBug
skill: Uni-App
create_date: 2022-01-31
---

#前端/Vue #前端/UniApp #前端/前端框架 

# Uni-App 

>post接口后端获取不到参数

修改请求头Content-type

```jsx
header:{
	'Content-type':'application/x-www-form-urlencoded'
}
//或者：
header : {  
	'content-type': 'application/x-www-form-urlencoded;charset=utf-8'  
}
```

```jsx
// 发起注册或者登录的请求
this.$u.post('/user/login', {username: username, password: password }, {'Content-type':'application/x-www-form-urlencoded'}).then(res => {
    console.log(res)
    setTimeout(() => {
        uni.showToast({
            title:"登录成功"
        })
        // 跳转到个人中心
    }, 1000)
});
```

>[system] TypeError: _vm.typeList[_vm.index] is undefined

在data里面定义如下：

```jsx
data() {
		return {
			typeList: [],
			index: 0,
		}
	}
```

我想用http请求获取typelist之后填充到data中的typeList中，并没有说明typeList的内容。

我在下面的函数中引用了将要传过来的typeList中的对象typeList[0].typeName;然后报了 这个未定义错误。

解读：这个错误可以忽略不计，不影响程序运行。

解除这个警告：

方法一： 给要渲染的元素加上v-if 指令，判断这个数组中是否有内容，警告即可解除，因为我要渲染的span 包含在div中，所以我在div中加入判断指令

方法二：在使用之前先判断这个东西是否存在