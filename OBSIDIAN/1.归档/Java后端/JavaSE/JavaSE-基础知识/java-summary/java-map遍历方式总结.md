```ad-note
参考：https://blog.csdn.net/tjcyjd/article/details/11111401
```

## foreach中使用entries遍历

```java
Map<Integer, Integer> map = new HashMap<Integer, Integer>();
 
for (Map.Entry<Integer, Integer> entry : map.entrySet()) { 
    System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
}
```


## foreach中遍历keys或者values

==此方法比entrySet快了大约10%==

```java
Map<Integer, Integer> map = new HashMap<Integer, Integer>();
 
//遍历map中的键
for (Integer key : map.keySet()) {
    System.out.println("Key = " + key);
}
 
//遍历map中的值
for (Integer value : map.values()) {
    System.out.println("Value = " + value);
}
```

## 使用迭代器进行遍历

在老版本java中这是惟一遍历map的方式。另一个好处是，你可以在遍历时调用iterator.remove()来删除entries，另两个方法则不能。

使用泛型。

```java
Map<Integer, Integer> map = new HashMap<Integer, Integer>();
 
Iterator<Map.Entry<Integer, Integer>> entries = map.entrySet().iterator();
 
while (entries.hasNext()) {
 
    Map.Entry<Integer, Integer> entry = entries.next();
 
    System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
 
}
```


不使用泛型。

```java
Map map = new HashMap();
Iterator entries = map.entrySet().iterator();
 
while (entries.hasNext()) {
    Map.Entry entry = (Map.Entry) entries.next();
    Integer key = (Integer)entry.getKey();
    Integer value = (Integer)entry.getValue();
    System.out.println("Key = " + key + ", Value = " + value);
}
```


## 不推荐使用


```java
Map<Integer, Integer> map = new HashMap<Integer, Integer>();
 
for (Integer key : map.keySet()) {
 
    Integer value = map.get(key);
 
    System.out.println("Key = " + key + ", Value = " + value);
 
}
```