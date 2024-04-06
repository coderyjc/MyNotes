---
type: 学习总结
skill: 
create_date: 2022-02-08
---


###  延时
```js
	setTimeout(function(){
		uni.switchTab({
			url: '/pages/index/index'
		})
		
//		跳转到tab不能用这个
//      uni.navigateTo({
//			url: '/pages/index/index'
//		})
	}, 1000)
```


