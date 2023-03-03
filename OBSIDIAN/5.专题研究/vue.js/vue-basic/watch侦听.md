## watch侦听

### watch入门

开发中我们在data返回的对象中定义了数据，这个数据通过插值语法等方式绑定到template中,当数据变化时，template会自动进行更新来显示最新的数据,但是在某些情况下，我们希望在代码逻辑中监听某个数据的变化，这个时候就需要用侦听器watch来完成了；

侦听器的用法如下：
- 选项：watch
- 类型：`{ [key: string]: string | Function | Object | Array}`