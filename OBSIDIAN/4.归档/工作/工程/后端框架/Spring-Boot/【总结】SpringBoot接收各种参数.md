## 接收Map参数

```java
@RequestMapping(value = "/test", method = RequestMethod.POST)
public void receiveMap(@RequestParam Map<String, String> map){

}
```

![[assets/Pasted image 20230407144522.png]]

## 接收List参数

### 方法一，使用数组接收

这种方法应该把参数用逗号连接，url中只有两个参数

```java
@RequestMapping(value = "/test", method = RequestMethod.POST)
public void receiveMap(
		@RequestParam String[] list1,
		@RequestParam String[] list2
){
	System.out.println(Arrays.toString(list1));
	System.out.println(Arrays.toString(list2));
}
```

![[assets/Pasted image 20230407150709.png]]

### 方法二，使用List接收

同上

```java
@RequestMapping(value = "/test", method = RequestMethod.POST)
public void receiveMap(
		@RequestParam List<String> list1,
		@RequestParam List<String> list2
){
	System.out.println(list1);
	System.out.println(list2);
}
```

![[assets/Pasted image 20230407150840.png]]

### 使用Axios发送List的时候会拆分成数组的形式

如果显示中括号无法进行传输，参考：[[【Bug】SpringBoot-Bug#Invalid character found in the request target]]

形式如：`http://localhost:8080/writtenScore/test?exportColumn[]=姓名&exportId[]=5&exportId[]=6&exportId[]=22332`

这时候应该指定`RequestParam`的`value`为数组形式，也就是在字符串后面添加`[]`

```java
@RequestMapping(value = "/test", method = RequestMethod.POST)
public void receiveMap(
		@RequestParam(value = "exportColumn[]") String[] exportColumn,
		@RequestParam(value = "exportId[]") String[] exportId
		){
	System.out.println(Arrays.toString(exportColumn));
	System.out.println(Arrays.toString(exportId));
}
```

![[assets/Pasted image 20230407153342.png]]
