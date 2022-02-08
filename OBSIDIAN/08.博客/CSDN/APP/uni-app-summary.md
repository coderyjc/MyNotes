# uni-app知识点总结

> 来源：[bilibili-Uni-App从入门到实战-黑马程序员杭州校区出品](https://www.bilibili.com/video/BV1BJ411W7pX)
>
> 官方文档：[uni-app官网](https://uniapp.dcloud.io/)

## 配置文件

`pages.json` 对 uni-app 进行全局配置，页面文件的路径、窗口样式、原生的导航栏、底部的原生tabbar 等

- 配置pages和globalStyle字段
  - navigationBarBackgroundColor  导航栏背景颜色（同状态栏背景色）
  - navigationBarTitleText 导航栏标题文字内容
  - enablePullDownRefresh 是否开启下拉刷新，详见[页面生命周期](https://uniapp.dcloud.io/use?id=%e9%a1%b5%e9%9d%a2%e7%94%9f%e5%91%bd%e5%91%a8%e6%9c%9f)。
  - onReachBottomDistance 页面上拉触底事件触发时距页面底部距离
  - ...
- tabBar字段
  - iconPath 图片路径
  - selectedIconPath  选中的图片路径
  - ...

`manifest.json` 文件是应用的配置文件，用于指定应用的名称、图标、权限等。

`App.vue`是我们的跟组件，所有页面都是在`App.vue`下进行切换的，是页面入口文件，可以调用应用的生命周期函数。

`main.js`是项目入口文件，主要作用是初始化`vue`实例并使用需要的插件。

`uni.scss`文件的用途是为了方便整体控制应用的风格。比如按钮颜色、边框风格，`uni.scss`文件里预置了一批scss全局变量预置。

```pages``` 所有的页面存放目录

```static``` 静态资源目录，例如图片等

```components``` 组件存放目录

## 组件

### text

属性

- selectable 文本是否可选
- space 是否显示连续空格
- decode 是否解码 

`text` 组件相当于行内标签、在同一行显示，除了文本节点以外的其他节点都无法长按选中

### view

类似于 div

其他属性见官方文档

### image

- src 地址
- mode 裁剪方式

页面结构复杂，css样式太多的情况，使用 image 可能导致样式生效较慢，出现 “闪一下” 的情况，此时设置 `image{will-change: transform}` ,可优化此问题。

## 样式、数据绑定

+ rpx 即响应式px，一种根据屏幕宽度自适应的动态单位。以750宽的屏幕为基准，750rpx恰好为屏幕宽度。屏幕变宽，rpx 实际显示效果会等比放大。

+ 使用`@import`语句可以导入外联样式表，`@import`后跟需要导入的外联样式表的相对路径，用`;`表示语句结束

+ 支持基本常用的选择器class、id、element等,在 `uni-app` 中不能使用 `*` 选择器。

+ `page` 相当于 `body` 节点

+ 定义在 App.vue 中的样式为全局样式，作用于每一个页面。在 pages 目录下 的 vue 文件中定义的样式为局部样式，只作用在对应的页面，并会覆盖 App.vue 中相同的选择器。

+ `uni-app` 支持使用字体图标，使用方式与普通 `web` 项目相同，需要注意以下几点：

  - 字体文件小于 40kb，`uni-app` 会自动将其转化为 base64 格式；

  - 字体文件大于等于 40kb， 需开发者自己转换，否则使用将不生效；

  - 字体文件的引用路径推荐使用以 ~@ 开头的绝对路径。


`~@/static/iconfont.ttf`

直接在data的return中定义数据即可，和vue一样

插值表达式也和vue一样，同样也可以进行基本运算和三元运算

也可以进行动态渲染和事件传参

## 上拉加载、下拉刷新

+ 需要在 `pages.json` 里，找到的当前页面的pages节点，并在 `style` 选项中开启 `enablePullDownRefresh`
+ 通过调用uni.startPullDownRefresh方法来开启下拉刷新

```js
	export default {
		data () {
			return {
				arr: ['前端','java','ui','大数据']
			}
		},
		methods: {
			startPull () {
				uni.startPullDownRefresh()
			}
		},
		
		onPullDownRefresh () { // 下拉刷新
			this.arr = []
			setTimeout(()=> {
				this.arr = ['前端','java','ui','大数据']
				uni.stopPullDownRefresh()
			}, 1000);
		},
        	onReachBottom () {  // 上拉加载
			console.log('触底了')
		}
	}
```

### 利用编程式导航进行跳转

[导航跳转文档]( [uni.navigateTo](https://uniapp.dcloud.io/api/router?id=navigateto))

#### **利用navigateTo进行导航跳转**

保留当前页面，跳转到应用内的某个页面，使用`uni.navigateBack`可以返回到原页面。

```html
<button type="primary" @click="goAbout">跳转到关于页面</button>
```

通过navigateTo方法进行跳转到普通页面

```js
goAbout () {
  uni.navigateTo({
    url: '/pages/about/about',
  })
}
```

#### **通过switchTab跳转到tabbar页面**

跳转到tabbar页面

```html
<button type="primary" @click="goMessage">跳转到message页面</button>
```

通过switchTab方法进行跳转

```js
goMessage () {
  uni.switchTab({
    url: '/pages/message/message'
  })
}
```

#### **redirectTo进行跳转** 

关闭当前页面，跳转到应用内的某个页面。

```html
<!-- template -->
<button type="primary" @click="goMessage">跳转到message页面</button>
<!-- js -->
goMessage () {
  uni.switchTab({
    url: '/pages/message/message'
  })
}
```

通过onUnload测试当前组件确实卸载

```js
onUnload () {
  console.log('组件卸载了')
}
```

### 导航跳转传递参数

在导航进行跳转到下一个页面的同时，可以给下一个页面传递相应的参数，接收参数的页面可以通过onLoad生命周期进行接收

传递参数的页面

```js
goAbout () {
  uni.navigateTo({
    url: '/pages/about/about?id=80',
  });
}
```

接收参数的页面

```js
<script>
	export default {
		onLoad (options) {
			console.log(options)
		}
	}
</script>
```

# uni-app项目总结

## 地图组件和拨打电话

```js
<view @click="makePhoneCall()">联系电话：000-0000-0000（ 点击拨打 ）</view>

<map class="map" :longitude="longitude" :latitude="latitude" :markers="markers"></map>
...
export default {
data() {
    return {
        longitude:116.088667,
        latitude:35.801418,
        markers:[ // 地图上的标记
            {
                longitude:116.088667,
                latitude:35.801418,
                iconPath: '../../static/image/marker.png',
                width: 15,
                height: 15
            }]
    }
},
    methods: {
        makePhoneCall(){
            // 拨打电话
            uni.makePhoneCall({
                phoneNumber:'0000000000'  // 电话
            })
        }
    }
}
```

## Swiper的使用

```js
<swiper class="swiper"
:indicator-dots="indicatorDots" 
:autoplay="autoplay" 
:interval="interval" 
:duration="duration">
    <swiper-item v-for="item in swipers">
        <image :src="item.url"></image>
</swiper-item>
</swiper>

data() {
    return {
        indicatorDots: true, // 显示当前是第几张图片的小点点
        autoplay: true,  // 自动播放
        interval: 2000, // 间隔
        duration: 500, // 持续时间
        swipers: [  // 图片
            {
                url:"../../static/image/goods-detail/1.png"
            },
            {
                url:"../../static/image/goods-detail/2.png"
            },
            {
                url:"../../static/image/goods-detail/3.png"
            },
            {
                url:"../../static/image/goods-detail/4.png"
            }
        ]
}
```

## 页面跳转

```js
<view class="good_list">
    <view class="goods_item" v-for="(item, index) in goods" @click="goodsDetail(index + 1)">
        <image :src="item.img"></image>
	<view class="price">
              <text>￥{{item.discount}}</text>
            <text>￥{{item.price}}</text>
	</view>
	<view class="name">商品{{index + 1}}</view>
	</view>
</view>
...
methods: {
    // 导航点击的处理函数
    navItemClick (path) {
        console.log(path)
        uni.navigateTo({
            // url 参数名称不一样的时候要指定，如果传过来的是参数名称是，url，就直接写 url，不用写 url:url
            url:path
        })
    },
        // 跳转到商品详情页
        goodsDetail(id){
            uni.navigateTo({
                url:'../goods-detail/goods-detail?id=' + id
            })
        }
}
```

## 过滤器的使用

```js
<view class="news_item" v-for="item in news" @click="goDetail(item.id)">
	<image :src="item.img"></image>
	<view class="right">
		<text class="title">{{item.title}}</text>
		<view class="info">
			<!-- 使用过滤器 fotmatDate -->
			<text>发表时间：{{item.date | formatDate}}</text> 
			<text>浏览：{{item.view}}次</text>
		</view>
	</view>
</view>
...
	export default {
		filters:{
			formatDate(date){
				return date.substr(0, 10)
			}
		},
		
		data() {
			return {
				news:[
					{
						id:1,
						img:'../../static/image/news/1.png',
						title:'Defender永久关闭W10杀毒',
						date:'2021-02-03 00:00:00',
						view:154
					}
				]
			}
		},
		methods: {
			goDetail(id){
				uni.navigateTo({
					url:'../news-detail/news-detail?id=' + id
				})
			}
		}
	}
```

## Scroll-View的使用

scroll-y 设置竖着滚动

前提是要设置页面长度为 100%

```js
<scroll-view class="left" scroll-y> 
	<view
		 :class="active === index ? 'active' : ''" 
		 v-for="(item, index) in options"
		 @click="leftClickHandler(index)"
	>
	 相册{{item}}
	 </view>
</scroll-view>
...
methods: {
	// 动态设置高亮
	leftClickHandler(index){
		this.active = index
	}
}
```

## 图片预览

```js
<view class="item" v-for="item in secondData" :key="item.id">
	<image :src="item.url" @click="previewImg(item.url)"></image>
	<text>{{item.title}}</text>
</view>

...

methods: {
	previewImg(current){
		// 用 secondData 中的每一个url组成一个列表
		const urls = this.secondData.map(item=>{
			return item.url;
		})
		// 图片预览
		uni.previewImage({
			current,
			urls
		})
	}
}
```

## 网络请求方法的封装和调用

```js
// 封装
const BASE_URL = 'http://localhost:8080'
export const myRequest = (options)=>{
	return new Promise((resolve, reject)={
		uni.request({
			url: BASE_URL+options.url,
			method: options.method || 'GET',
			data: options.data || {},
			success: (res)=>{
				if(res.data.status !== 0){
					return uni.showToast({
						title: '获取数据失败'
					})
				}
				resolve(res)
			},
			fail: (err)=>{
				uni.showToast({
					title:'请求接口失败'
				})
				reject(err)
			}
		})
	})
}

//调用
//相当于自己实现了一个ajax

import {myRequest} from './util/api.js'
Vue.prototype.$myRequest = myRequest

...

async function() {
    const res = await this.$myRequest({
        url: '/api/api',
        method: 'GET',
        data: [],
        success:{
            ...
        }
    })
}
```

