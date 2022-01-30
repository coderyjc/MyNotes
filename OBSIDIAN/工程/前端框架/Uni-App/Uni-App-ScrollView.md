---
type: 学习总结
skill: Uni-App
create_date: 2022-01-31
---

#前端框架  #Vue 


# 下拉刷新无法正常恢复的问题

关于scroll-view组件的下拉刷新，无论是uni-app还是微信小程序，官方都说得不是很明白，有一个非常关键的关键规则没说清楚，组件属性例子：

refresher-triggered="triggered" @refresherrefresh="onRefresh" @refresherrestore="onRestore" scrolltolower="loadMore"

1.**通过程序将triggered设为true时**，将触发onRefresh；

2.**不管triggered为何值，在界面中下拉**，也会触发onRefresh，但不会自动改变triggered值(不能双向绑定，这是问题的根本原因)；

3.onRefresh执行完毕，**不会自动触发onRestore**（这是问题的表现），使得刷新图标一直显示，**必须是triggered由true变为false**，才会触发onRestore并隐藏刷新图标；如果triggered一直为false，或一直为true，都不会触发。

解决办法：

1.在进入onRefresh后，**如果triggered为false，则将它置为true**，当执行完你的刷新操作（通常是获取新的数据）后，**将triggered置为false**。

2.由于上一步中将triggered置为true，会再次触发onRefresh，故需再增加一个_freshing，表示是否正在执行刷新操作，在onRefresh中做判断，如_freshing为true，不执行刷新操作直接返回。

如果scroll-view有多个，要每个用自己的 triggered和refreshing来控制。

```html
<template>
	<view>
		<view class="wrap">
			<view class="u-tabs-box">
				<u-tabs-swiper 
					activeColor="#5098ff" 
					ref="tabs"
					:list="typeList" 
					:current="current"
					 name="typeName"
					@change="change" 
					:is-scroll="false" 
					swiperWidth="750"></u-tabs-swiper>
			</view>
			<u-top-tips ref="uTips"></u-top-tips>
			<swiper class="swiper-box" 
				:current="swiperCurrent" 
				@transition="transition" 
				@animationfinish="animationfinish">
				<swiper-item class="swiper-item" v-for="(comments,index) in commentList">
					<scroll-view 
					scroll-y
					refresher-enabled="true"
					refresher-background="#5098ff"
					:refresher-triggered="triggered"
					@refresherrefresh="onRefresh" 
					@refresherrestore="onRestore" 
					@scrolltolower="reachBottom">
						<u-card v-for="(item,index) in comments" :show-head="false">
							<view class="" slot="body">
								{{item.commentContent}}
							</view>
							<view class="info" slot="foot">
								<view class="author"> {{item.userName}} </view>
								<view class="date"> {{item.postDate}} </view>
								<!-- <view class="like"> 点赞 </view> -->
								<!-- <view class="collect"> 收藏 </view> -->
							</view>
						</u-card>
						<u-loadmore :status="loadStatus[0]"  bgColor="#f2f2f2" :load-text="loadText"></u-loadmore>
					</scroll-view>
				</swiper-item>
			</swiper>
		</view>
		
		<u-tabbar :list="tabbar" :mid-button="true" active-color=#5098FF></u-tabbar>
	</view>
</template>

<script>
export default {
	data() {
		return {
			triggered: true,
			// 默认是 false
			_freshing: false,
			
	},
	onLoad() {
		// 获取所有分类和每一个页面的数据
		this.getTypeList();
		// 必须在这初始化
		this._freshing = false
		this.triggered = true
	},
	onReachBottom() {
		this.reachBottom();
	},
	methods: {
		onRefresh() {
			this.debug("in Onrefresh")
			if (this._freshing) return
			if(!this.triggered) this.triggered = true
			this._freshing = true
			this.currentPage[this.current] = 1
			this.maxPage[this.current] = 1
			this.getCommentList(0, this.tabAndType[this.current], this.current)
			setTimeout(() => {
				this.triggered = false;
				this._freshing = false;
				this.$refs.uTips.show({
					title: '已刷新 o(〃\\'▽\\'〃)o',
					type: 'success',
					duration: '1000'
				})
			}, 1000)
		},
		onRestore() {
			this.debug("restore")
			this.triggered = false // 需要重置
			this._freshing = false // 需要重置
		},
};
</script>
```

uni-app 解决scroll-view下拉刷新无法正常恢复的问题

# Scroll-View 无法下滑问题

给 Scroll-view 一个高度即可

在scroll-view的属性中加上这样一行代码：

```jsx
style="height: calc(100vh - var(--window-top) - var(--window-bottom))"
```