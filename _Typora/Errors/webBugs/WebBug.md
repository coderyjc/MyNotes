## ajax 请求中无法给全局变量赋值

原因： $.ajax 默认是异步的， 异步回调在js主线程执行结束后才会被执行。所以先执行console.log(该变量)，再执行ajax中的回调函数。所以后面的console.log执行时，该变量还没有被ajax赋值，所以是undefind。

解决方案：如果确实需要获取ajax的结果赋值给该变量，那么可以ajax多加一个参数:async=false，就会同步执行。