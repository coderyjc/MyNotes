## 接收Map参数

```java
@RequestMapping(value = "/test", method = RequestMethod.POST)
public void receiveMap(@RequestParam Map<String, String> map){

}
```

![[assets/Pasted image 20230407144522.png]]

## 接收List参数

如果显示中括号无法进行传输，参考：[[【Bug】SpringBoot-Bug#Invalid character found in the request target]]

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

