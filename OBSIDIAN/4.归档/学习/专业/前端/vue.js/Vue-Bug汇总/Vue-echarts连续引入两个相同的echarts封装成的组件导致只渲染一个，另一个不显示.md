
封装echarts图标到组件中时指定了固定的id，在父组件中引入的时候相当于在一个页面中引入了两个id相同的echarts组件，因此会只显示一个。

解决方案：手动传入组件id，将id改为组件的一个prop