# Axios

> Axios 官网 [https://github.com/axios/axios](https://github.com/axios/axios)

## get请求

基本语法：

`axios.get(地址？k1=v1&k2=vv2&k3=v3).then(function(reponse){},function(error){})`

示例：

```js
function(){
    axios.get("https://autumnfish.cn/api/joke/list?num=3").then(function(response){
        console.log(response);
    }, function(error){
        console.log(error)
    })
}
```

## post请求

`axios.post(地址,json对象).then(function(response){},function(error){})`

示例：

```javascript
function(){
    axios.post("https://automnfish.cn/api/user/reg", {
        username:"jack"
    }).then(function(response){
        console.log(response)
    }, function(error){
        console.log(error)
    })
}
```

## Vue+Axios

点击按钮之后随机获取一条笑话

```js
<body>
	<div id="app">
		<button type="button" @click="getJoke">点击按钮随机获取一条笑话</button> <br>
		{{msg}}
	</div>
	<script type="text/javascript">
		Vue = new Vue({
			el:"#app",
			data: {
				msg: ""
			},
			methods: {
				getJoke: function(){
                    	// 在匿名函数中this的指向改变了
                    	// 所以在这里先用that把this保存起来
					var that = this
					axios.get("https://autumnfish.cn/api/joke").then(function(response){
                        		// 在这里直接用that进行赋值
						that.msg = response.data
					}, function(error){
						console.log(error)
					})
				}
			}
		})
		
	</script>
</body>
```

