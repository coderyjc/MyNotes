## 集合

什么是集合？有什么用？

- 数组其实就是一个集合。集合实际上就是一个容器。可以来容纳其它类型的数据。

集合为什么说在开发中使用较多？

- 集合是一个容器，是一个载体，可以一次容纳多个对象。在实际开发中，假设连接数据库，数据库当中有10条记录，那么假设把这10条记录查询出来，在java程序中会将10条数据封装成10个java对象，然后将10个java对象放到某一个集合当中，将集合传到前端，然后遍历集合，将一个数据一个数据展现出来。

注意：

- 集合不能直接存储基本数据类型，另外集合也不能直接存储java对象，集合当中存储的都是java对象的内存地址。（或者说集合中存储的是引用。）
- 集合在java中本身是一个容器，是一个对象。
- 集合中任何时候存储的都是“引用”。

在java中每一个不同的集合，底层会对应不同的数据结构。往不同的集合中存储元素，等于将数据放到了不同的数据结构当中。什么是数据结构？数据存储的结构就是数据结构。不同的数据结构，数据存储方式不同。例如：数组、二叉树、链表、哈希表...以上这些都是常见的数据结构。

new ArrayList(); 创建一个集合，底层是数组。
new LinkedList(); 创建一个集合对象，底层是链表。
new TreeSet(); 创建一个集合对象，底层是二叉树。
.....

集合在java JDK中哪个包下？

- java.util.*;所有的集合类和集合接口都在java.util包下。

为了让大家掌握集合这块的内容，最好能将集合的继承结构图背会！！！

在java中集合分为两大类：
- 一类是单个方式存储元素：单个方式存储元素，这一类集合中超级父接口：java.util.Collection;
- 一类是以键值对儿的方式存储元素以键值对的方式存储元素，这一类集合中超级父接口：java.util.Map;

![1595553406932](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1595553406932.png)

![1595553421651](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1595553421651.png)

重点：

- 第一个重点：把集合继承结构图背会。
- 第二个重点：把Collection接口中常用方法测试几遍。
- 第三个重点：把迭代器弄明白。
- 第四个重点：Collection接口中的remove方法和contains方法底层都会调用equals，
这个弄明白。

总结：所有实现类

- ArrayList 底层是数组
- LinkedList 底层是双向链表
- Vector 底层是数组，线程安全，效率比较低，使用较少
- HashSet 底层是HashMap，放在HashSet集合中的元素等同于放到HashMap集合key部分了
- TreeSet 底层是TreeMap，放在TreeSet集合中的元素等同于放到TreeMap集合的key部分了
- HashMap 底层是哈希表
- HashTable 底层也是哈希表，不过是线程安全的，效率较低，使用较少
- Properties 是线程安全的，并且k和v只能存储字符串String
- TreeMap 底层是二叉树。TreeMap集合的key可以自动按照大小顺序排序


List 集合存储元素特点

- 有序可重复
- 有序：存进去的顺序和取出得到顺序相同，每一个元素都有下标
- 可重复：存进去1， 可以再存储一个1

Set(Map) 集合存储元素特点

- 无序不可重复
- 无序：存进去的顺序和去除的顺序不一定相同，另外Set集合中没有下标
- 不可重复：存进去1，不能再存储1了

SortedSet（SortedMap） 集合存储元素特点

- 无序不可重复但是可以排序
- 可排序：可以按照大小顺序排列

Map集合的Key就是一个Set集合，往Set中放数据就相当于放到了map的key部分

### Collection

关于java.util.Collection接口中常用的方法。

Collection中能存放什么元素？
- 没有使用“泛型”之前，Collection中可以存储Object的所有子类型，且**可以不同**，因为存的是地址
- 使用了“泛型”之后，Collection中只能存储某个具体的类型。
- Collection中什么都能存只要是Object的子类型就行。
- 集合中不能直接存储基本数据类型,也不能存java对象，只是存储java对象的内存地址。

Collection中的常用方法

- boolean add(Object e) 向集合中添加元素(自动装箱)
- int size()  获取集合中元素的个数
- void clear() 清空集合
- boolean contains(Object o) 判断当前集合中是否包含元素o，包含返回true，不包含返回false
- boolean remove(Object o) 删除集合中的某个元素。
- boolean isEmpty()  判断该集合中元素的个数是否为0
- Object[] toArray()  调用这个方法可以把集合转换成数组。【作为了解，使用不多。】

#### 迭代器

```java
public class CollectionTest02 {
    public static void main(String[] args) {
        // 注意：以下讲解的遍历方式/迭代方式，是所有Collection通用的一种方式。
        // 在Map集合中不能用。在所有的Collection以及子类中使用。
        // 创建集合对象
        Collection c = new ArrayList(); // 后面的集合无所谓，主要是看前面的Collection接口，怎么遍历/迭代。
        // 添加元素
        c.add("abc");
        c.add(new Object());
        // 对集合Collection进行遍历/迭代
        // 第一步：获取集合对象的迭代器对象Iterator
        Iterator it = c.iterator();
        // 第二步：通过以上获取的迭代器对象开始迭代/遍历集合。
        /*
            以下两个方法是迭代器对象Iterator中的方法：
                boolean hasNext()如果仍有元素可以迭代，则返回 true。
                Object next() 返回迭代的下一个元素。
         */
        while(it.hasNext()){
            Object obj = it.next();
            System.out.println(obj);
        }
    //等价于：
		while(it2.hasNext()){
            System.out.println(it2.next());
        }
        // 一直取，不判断，会出现异常：java.util.NoSuchElementException
    }
}

```

#### contains

深入Collection集合的contains方法：

boolean contains(Object o)
判断集合中是否包含某个对象o
如果包含返回true， 如果不包含返回false。

contains方法是用来判断集合中是否包含某个元素的方法，那么它在底层是怎么判断集合中是否包含某个元素的呢？
调用了equals方法进行比对。equals方法返回true，就表示包含这个元素。

```java
public class CollectionTest04 {
    public static void main(String[] args) {
        // 创建集合对象
        Collection c = new ArrayList();

        // 向集合中存储元素
        String s1 = new String("abc"); // s1 = 0x1111
        c.add(s1); // 放进去了一个"abc"

        String s2 = new String("def"); // s2 = 0x2222
        c.add(s2);

        // 集合中元素的个数
        System.out.println("元素的个数是：" + c.size()); // 2

        // 新建的对象String
        String x = new String("abc"); // x = 0x5555
        // c集合中是否包含x？结果猜测一下是true还是false？
        System.out.println(c.contains(x));
    }
}

//包含，因为底层调用了String的equals方法，比较的是内容，内容一样所以是true
//和字符串常量值

```

结论：**放在集合中的元素一定要重写equals方法**

#### remove

- 当集合的结构发生改变时，迭代器必须重新获取，如果还是用以前老的迭代器，会出现异常：java.util.ConcurrentModificationException
- 在迭代集合元素的过程中，不能调用集合对象的remove方法，删除元素：c.remove(o); 迭代过程中不能这样。会出现：java.util.ConcurrentModificationException
- 在迭代元素的过程当中，一定要使用迭代器Iterator的remove方法，删除元素不要使用集合自带的remove方法删除元素。

```java
public class CollectionTest06 {
    public static void main(String[] args) {
        // 创建集合
        Collection c = new ArrayList();

        // 注意：此时获取的迭代器，指向的是那是集合中没有元素状态下的迭代器。
        // 一定要注意：集合结构只要发生改变，迭代器必须重新获取。
        // 当集合结构发生了改变，迭代器没有重新获取时，调用next()方法时：java.util.ConcurrentModificationException
        Iterator it = c.iterator();

        // 添加元素
        c.add(1); // Integer类型
        c.add(2);

        // 获取迭代器
        //Iterator it = c.iterator();
        /*while(it.hasNext()){
            // 编写代码时next()方法返回值类型必须是Object。
            // Integer i = it.next();
            Object obj = it.next();
            System.out.println(obj);
        }*/

        Collection c2 = new ArrayList();
        c2.add("abc");
        c2.add("def");
        c2.add("xyz");

        Iterator it2 = c2.iterator();
        while(it2.hasNext()){
            Object o = it2.next();
            // 删除元素
            // 删除元素之后，集合的结构发生了变化，应该重新去获取迭代器
            // 但是，循环下一次的时候并没有重新获取迭代器，所以会出现异常：java.util.ConcurrentModificationException
            // 出异常根本原因是：集合中元素删除了，但是没有更新迭代器（迭代器不知道集合变化了）
            //c2.remove(o); // 直接通过集合去删除元素，没有通知迭代器。（导致迭代器的快照和原集合状态不同。）
            // 使用迭代器来删除可以吗？
            // 迭代器去删除时，会自动更新迭代器，并且更新集合（删除集合中的元素）。
            it2.remove(); // 删除的一定是迭代器指向的当前元素。
            System.out.println(o);
        }

        System.out.println(c2.size()); //0
    }
}

```


### List

List集合存储元素特点：有序可重复

- 有序：List集合中的元素有下标。
- 从0开始，以1递增。
- 可重复：存储一个1，还可以再存储1.

List既然是Collection接口的子接口，那么肯定List接口有自己“特色”的方法：
以下只列出List接口特有的常用的方法：

- void add(int index, Object element)
- Object set(int index, Object element)
- Object get(int index)
- int indexOf(Object o)
- int lastIndexOf(Object o)
- Object remove(int index)

以上几个方法不需要死记硬背，可以自己编写代码测试一下，理解一下, 以后开发的时候，还是要翻阅帮助文档。

迭代器迭代元素的过程中不能使用集合对象的remove方法删除元素，要使用迭代器Iterator的remove方法来删除元素，防止出现异常： ConcurrentModificationException

怎么得到一个线程安全的List：
Collections.synchronizedList(list);


```java

public class ListTest01 {
    public static void main(String[] args) {
        // 创建List类型的集合。
        List myList = new ArrayList();

        // 添加元素
        myList.add("A"); // 默认都是向集合末尾添加元素。
        myList.add("B");

        //在列表的指定位置插入指定元素（第一个参数是下标）
        // 这个方法使用不多，因为对于ArrayList集合来说效率比较低。
        myList.add(1, "KING");

        // 迭代
        Iterator it = myList.iterator();
        while(it.hasNext()){
            Object elt = it.next();
            System.out.println(elt);
        }

        // 根据下标获取元素
        Object firstObj = myList.get(0);
        System.out.println(firstObj);

        // 因为有下标，所以List集合有自己比较特殊的遍历方式
        // 通过下标遍历。【List集合特有的方式，Set没有。】
        for(int i = 0; i < myList.size(); i++){
            Object obj = myList.get(i);
            System.out.println(obj);
        }

        // 获取指定对象第一次出现处的索引。
        System.out.println(myList.indexOf("C")); // 3

        // 获取指定对象最后一次出现处的索引。
        System.out.println(myList.lastIndexOf("C")); // 4

        // 删除下标为0的元素
        myList.remove(0);

        // 修改指定位置的元素
        myList.set(2, "Soft");

        // 遍历集合
        for(int i = 0; i < myList.size(); i++){
            Object obj = myList.get(i);
            System.out.println(obj);
        }
    }
}

```

#### ArrayList

- 默认初始化容量10（底层先创建了一个长度为0的数组，当添加第一个元素的时候，初始化容量10。）扩容为原容量1.5倍。
- 集合底层是一个Object[]数组。
- 构造方法：
	- new ArrayList();
	- new ArrayList(20);
- ArrayList集合的扩容：        增长到原容量的1.5倍。
- ArrayList集合底层是数组，怎么优化？
	- 尽可能少的扩容。因为数组扩容效率比较低，建议在使用ArrayList集合的时候预估计元素的个数，给定一个初始化容量。
- 数组优点：
	- 检索效率比较高。（每个元素占用空间大小相同，内存地址是连续的，知道首元素内存地址，知道下标，通过数学表达式计算出元素的内存地址，所以检索效率最高。）
- 数组缺点：
	- 随机增删元素效率比较低。
	- 另外数组无法存储大数据量。（很难找到一块非常巨大的连续的内存空间。）
- 向数组末尾添加元素，效率很高，不受影响。
- 面试官经常问的一个问题？ 这么多的集合中，你用哪个集合最多？
	- 答：ArrayList集合。因为往数组末尾添加元素，效率不受影响。另外，我们检索/查找某个元素的操作比较多。
- ArrayList集合是非线程安全的。（不是线程安全的集合。）
- ArrayList之所以检索效率比较高，不是单纯因为下标的原因。是因为底层数组发挥的作用。
- LinkedList集合照样有下标，但是检索/查找某个元素的时候效率比较低，因为只能从头节点开始一个一个遍历。

怎么将一个线程不安全的ArrayList集合转换成线程安全的呢？
使用集合工具类：java.util.Collections;

java.util.Collection 是集合接口。

java.util.Collections 是集合工具类。

#### LinkedList

链表的优点：
    由于链表上的元素在空间存储上内存地址不连续。所以随机增删元素的时候不会有大量元素位移，因此随机增删效率较高。在以后的开发中，如果遇到**随机增删集合中元素**的业务比较多时，建议使用LinkedList。

链表的缺点：
    不能通过数学表达式计算被查找元素的内存地址，每一次查找都是从头节点开始遍历，直到找到为止。所以LinkedList集合检索/查找的效率较低。

- LinkedList集合底层也是有下标的。
- LinkedList集合有初始化容量吗？没有。
- 最初这个链表中没有任何元素。first和last引用都是null。


ArrayList：把检索发挥到极致。（末尾添加元素效率还是很高的。）
LinkedList：把随机增删发挥到极致。
加元素都是往末尾添加，所以ArrayList用的比LinkedList多。

#### Vector

Vector初始化容量是10.

扩容为原容量的2倍。

底层是数组。

Vector底层是线程安全的。

Vector中所有的方法都是线程同步的，都带有synchronized关键字，是线程安全的。效率比较低，使用较少了。

### 泛型

#### 使用泛型

- JDK5.0之后推出的新特性：泛型
- 泛型这种语法机制，只在程序编译阶段起作用，只是给编译器参考的。（运行阶段泛型没用！）
- 使用了泛型好处是什么？
	- 第一：集合中存储的元素类型统一了。
	- 第二：从集合中取出的元素类型是泛型指定的类型，不需要进行大量的“向下转型”！
- 泛型的缺点是什么？
    - 导致集合中存储的元素缺乏多样性！
    - 大多数业务中，集合中元素的类型还是统一的。所以这种泛型特性被大家所认可。

 ```java
public class GenericTest01 {
    public static void main(String[] args) {

        // 使用泛型List<Animal>之后，表示List集合中只允许存储Animal类型的数据。
        // 用泛型来指定集合中存储的数据类型。
        List<Animal> myList = new ArrayList<Animal>();

        // 指定List集合中只能存储Animal，那么存储String就编译报错了。
        // 这样用了泛型之后，集合中元素的数据类型更加统一了。
        Cat c = new Cat(); Bird b = new Bird();
        myList.add(c); myList.add(b);

        // 获取迭代器
        // 这个表示迭代器迭代的是Animal类型。
        Iterator<Animal> it = myList.iterator();
        while(it.hasNext()){
            // 使用泛型之后，每一次迭代返回的数据都是Animal类型。
            //Animal a = it.next();
            // 这里不需要进行强制类型转换了。直接调用。
            //a.move();

            // 调用子类型特有的方法还是需要向下转换的！
            Animal a = it.next();
            if(a instanceof Cat) {
                Cat x = (Cat)a;
                x.catchMouse();
            }
            if(a instanceof Bird) {
                Bird y = (Bird)a;
                y.fly();
            }
        }
    }
}

class Animal {
    // 父类自带方法
    public void move(){
        System.out.println("动物在移动！");
    }
}

class Cat extends Animal {
    // 特有方法
    public void catchMouse(){
        System.out.println("猫抓老鼠！");
    }
}

class Bird extends Animal {
    // 特有方法
    public void fly(){
        System.out.println("鸟儿在飞翔！");
    }
}

 ```


#### 钻石表达式（自动类型推断）

```java

public class GenericTest02 {
    public static void main(String[] args) {

        // ArrayList<这里的类型会自动推断>()，前提是JDK8之后才允许。
        // 自动类型推断，钻石表达式！
        List<Animal> myList = new ArrayList<>();

        myList.add(new Animal());
        myList.add(new Cat());
        myList.add(new Bird());

        // 遍历
        Iterator<Animal> it = myList.iterator();
        while(it.hasNext()){
            Animal a = it.next();
            a.move();
            //调用子类中的方法还是要转型
        }

        List<String> strList = new ArrayList<>();

        // 遍历
        Iterator<String> it2 = strList.iterator();
        while(it2.hasNext()){
            // 直接通过迭代器获取了String类型的数据
            String s = it2.next();
            // 直接调用String类的substring方法截取字符串。
            String newString = s.substring(7);
            System.out.println(newString);
        }
    }
}

```

#### 自定义泛型

//不太明白这个

自定义泛型可以吗？可以

- 自定义泛型的时候，<> 尖括号中的是一个标识符，随便写。
- java源代码中经常出现的是： <E>和<T>
- E是Element单词首字母。
- T是Type单词首字母。

```java
public class GenericTest03<标识符随便写> {

    public void doSome(标识符随便写 o){
        System.out.println(o);
    }

    public static void main(String[] args) {

        // new对象的时候指定了泛型是：String类型
        GenericTest03<String> gt = new GenericTest03<>();

        gt.doSome("abc");

        // =============================================================
        GenericTest03<Integer> gt2 = new GenericTest03<>();
        gt2.doSome(100);

        // 类型不匹配
        //gt2.doSome("abc");

        MyIterator<String> mi = new MyIterator<>();
        String s1 = mi.get();

        MyIterator<Animal> mi2 = new MyIterator<>();
        Animal a = mi2.get();

        // 不用泛型就是Object类型。
        /*GenericTest03 gt3 = new GenericTest03();
        gt3.doSome(new Object());*/
    }
}

class MyIterator<T> {
    public T get(){
        return null;
    }
}
```

### Map

- Map和Collection没有继承关系。
- Map集合以key和value的方式存储数据：键值对
	+ key和value都是引用数据类型。
	+ key和value都是存储对象的内存地址。
	+ key起到主导的地位，value是key的一个附属品。
- Map接口中常用方法：
	+ V put(K key, V value) 向Map集合中添加键值对
	+ V get(Object key) 通过key获取value
	+ void clear()    清空Map集合
	+ boolean containsKey(Object key) 判断Map中是否包含某个key
	+ boolean containsValue(Object value) 判断Map中是否包含某个value
	+ boolean isEmpty()   判断Map集合中元素个数是否为0
	+ V remove(Object key) 通过key删除键值对
	+ int size() 获取Map集合中键值对的个数。
	+ Collection<V> values() 获取Map集合中所有的value，返回一个Collection
	+ Set<K> keySet() 获取Map集合所有的key（所有的键是一个set集合）
	+ Set<Map.Entry<K,V>> entrySet()  将Map集合转换成Set集合

	假设现在有一个Map集合，如下所示：
    map1集合对象
    key             value
    ----------------------------
    1               zhangsan
    2               lisi
    3               wangwu
    4               zhaoliu

Set set = map1.entrySet();
set集合对象
1=zhangsan 【注意：Map集合通过entrySet()方法转换成的这个Set集合，Set集合中元素的类型是 Map.Entry<K,V>】
2=lisi【Map.Entry和String一样，都是一种类型的名字，只不过：Map.Entry是静态内部类，是Map中的静态内部类】
3=wangwu
4=zhaoliu ---> 这个东西是个什么？ Map.Entry

#### 使用方式：

```java
public class MapTest01 {
    public static void main(String[] args) {
        // 创建Map集合对象
        Map<Integer, String> map = new HashMap<>();
        // 向Map集合中添加键值对
        map.put(1, "zhangsan"); // 1在这里进行了自动装箱。
        map.put(2, "lisi");
        map.put(3, "wangwu");
        // 通过key获取value
        String value = map.get(2);
        System.out.println(value);
        // 获取键值对的数量
        System.out.println("键值对的数量：" + map.size());
        // 通过key删除key-value
        map.remove(2);
        // 判断是否包含某个key
        // contains方法底层调用的都是equals进行比对的，所以自定义的类型需要重写equals方法。
        System.out.println(map.containsKey(new Integer(4))); // true
        // 判断是否包含某个value
        System.out.println(map.containsValue(new String("wangwu"))); // true

        // 获取所有的value
        Collection<String> values = map.values();
        // foreach
        for(String s : values){
            System.out.println(s);
        }

        // 清空map集合
        map.clear();
        System.out.println("键值对的数量：" + map.size());
        // 判断是否为空
        System.out.println(map.isEmpty()); // true
    }
}

```

#### 遍历方式

```java
public class MapTest02 {
    public static void main(String[] args) {

        // 第一种方式：获取所有的key，通过遍历key，来遍历value
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "zhangsan");
        map.put(2, "lisi");
        map.put(3, "wangwu");
        map.put(4, "zhaoliu");
        // 遍历Map集合
        // 获取所有的key，所有的key是一个Set集合
        Set<Integer> keys = map.keySet();
        // 遍历key，通过key获取value
        // 迭代器可以
        /*Iterator<Integer> it = keys.iterator();
        while(it.hasNext()){
            // 取出其中一个key
            Integer key = it.next();
            // 通过key获取value
            String value = map.get(key);
            System.out.println(key + "=" + value);
        }*/
        // foreach也可以
        for(Integer key : keys){
            System.out.println(key + "=" + map.get(key));
        }

        // 第二种方式：Set<Map.Entry<K,V>> entrySet()
        // 以上这个方法是把Map集合直接全部转换成Set集合。
        // Set集合中元素的类型是：Map.Entry
        Set<Map.Entry<Integer,String>> set = map.entrySet();
        // 遍历Set集合，每一次取出一个Node
        // 迭代器
        /*Iterator<Map.Entry<Integer,String>> it2 = set.iterator();
        while(it2.hasNext()){
            Map.Entry<Integer,String> node = it2.next();
            Integer key = node.getKey();
            String value = node.getValue();
            System.out.println(key + "=" + value);
        }*/

        // foreach
        // 这种方式效率比较高，因为获取key和value都是直接从node对象中获取的属性值。
        // 这种方式比较适合于大数据量。
        for(Map.Entry<Integer,String> node : set){
            System.out.println(node.getKey() + "--->" + node.getValue());
        }
    }
}
```

### 哈希表（散列表）

HashMap集合：
- HashMap集合底层是哈希表/散列表的数据结构。
- 哈希表是一个怎样的数据结构呢？
    - 哈希表是一个数组和单向链表的结合体。
    - 数组：在查询方面效率很高，随机增删方面效率很低。
    - 单向链表：在随机增删方面效率较高，在查询方面效率很低。
    - 哈希表将以上的两种数据结构融合在一起，充分发挥它们各自的优点。"中庸"
- HashMap集合底层的源代码：
    ```java
        public class HashMap{
            // HashMap底层实际上就是一个数组。（一维数组）
            Node<K,V>[] table;
            // 静态的内部类HashMap.Node
            static class Node<K,V> {
                final int hash; // 哈希值（哈希值是key的hashCode()方法的执行结果。hash值通过哈希函数/算法，可以转换存储成数组的下标。）
                final K key; // 存储到Map集合中的那个key
                V value; // 存储到Map集合中的那个value
                Node<K,V> next; // 下一个节点的内存地址。
            }
        }
    ```
- 哈希表/散列表：一维数组，这个数组中每一个元素是一个单向链表。（数组和链表的结合体。）
- 最主要掌握的是：
    - map.put(k,v)
    - v = map.get(k)
    - 以上这两个方法的实现原理，是必须掌握的。
- HashMap集合的key部分特点：
    - 无序，不可重复。
    - 为什么无序？ 因为不一定挂到哪个单向链表上。
    - 不可重复是怎么保证的？ equals方法来保证HashMap集合的key不可重复。如果key重复了，value会覆盖。
    - 放在HashMap集合key部分的元素其实就是放到HashSet集合中了。
    - 所以HashSet集合中的元素也需要同时重写hashCode()+equals()方法。
- 哈希表HashMap使用不当时无法发挥性能！
- 假设将所有的hashCode()方法返回值固定为某个值，那么会导致底层哈希表变成了纯单向链表。这种情况我们称为：散列分布不均匀。
	- 什么是散列分布均匀？
	- 假设有100个元素，10个单向链表，那么每个单向链表上有10个节点，这是最好的，是散列分布均匀的。
	- 假设将所有的hashCode()方法返回值都设定为不一样的值，可以吗，有什么问题？
	- 不行，因为这样的话导致底层哈希表就成为一维数组了，没有链表的概念了。也是散列分布不均匀。散列分布均匀需要你重写hashCode()方法时有一定的技巧。
- 重点：放在HashMap集合key部分的元素,以及放在HashSet集合中的元素,需要同时重写hashCode和equals方法.
- HashMap集合的默认初始化容量是16，默认加载因子是0.75, 这个默认加载因子是当HashMap集合底层数组的容量达到75%的时候，数组开始扩容。
- 重点，记住：HashMap集合初始化容量**必须是2的倍数**，这也是官方推荐的，这是因为达到散列均匀，为了提高HashMap集合的存取效率，所必须的。

这里有个图

测试:
```java
public class HashMapTest01 {
    public static void main(String[] args) {
        // 测试HashMap集合key部分的元素特点
        // Integer是key，它的hashCode和equals都重写了。
        Map<Integer,String> map = new HashMap<>();
        map.put(1111, "zhangsan");
        map.put(6666, "lisi");
        map.put(7777, "wangwu");
        map.put(2222, "zhaoliu");
        map.put(2222, "king"); //key重复的时候value会自动覆盖。

        System.out.println(map.size()); // 4

        // 遍历Map集合
        Set<Map.Entry<Integer,String>> set = map.entrySet();
        for(Map.Entry<Integer,String> entry : set){
            // 验证结果：HashMap集合key部分元素：无序不可重复。
            System.out.println(entry.getKey() + "=" + entry.getValue());
        }
    }
}
```

#### 必须重写hashcode和equals

- 向Map集合中存，以及从Map集合中取，都是先调用key的hashCode方法，然后再调用equals方法！
equals方法有可能调用，也有可能不调用。
    - 拿put(k,v)举例，什么时候equals不会调用？k.hashCode()方法返回哈希值，哈希值经过哈希算法转换成数组下标。数组下标位置上如果是null，equals不需要执行。
    - 拿get(k)举例，什么时候equals不会调用？k.hashCode()方法返回哈希值，哈希值经过哈希算法转换成数组下标。数组下标位置上如果是null，equals不需要执行。

- 注意：如果一个类的equals方法重写了，那么hashCode()方法必须重写。
    - 并且equals方法返回如果是true，hashCode()方法返回的值必须一样。equals方法返回true表示两个对象相同，在同一个单向链表上比较。那么对于同一个单向链表上的节点来说，他们的哈希值都是相同的。所以hashCode()方法的返回值也应该相同。
    
- hashCode()方法和equals()方法不用研究了，直接使用IDEA工具生成，但是这两个方法需要同时生成。

- 对于哈希表数据结构来说：如果o1和o2的hash值相同，一定是放到同一个单向链表上。 如果o1和o2的hash值不同，但由于哈希算法执行结束之后转换的数组下标可能相同，此时会发生“哈希碰撞”。

- HashMap集合key部分允许null吗？  允许  但是要注意：HashMap集合的key null值只能有一个。

- 终极结论：放在HashMap集合key部分的，以及放在HashSet集合中的元素，需要**同时重写hashCode方法和equals方法**。


#### HashMap和Hashtable的区别。

Hashtable和HashMap一样，底层都是哈希表数据结构。

HashMap：
- 初始化容量16，扩容2倍。非线程安全。key和value可以为null。
- HashMap集合的key和value都是可以为null的。

Hashtable：
- 初始化容量11，默认加载因子是：0.75f，扩容2倍+1。线程安全。key和value都不能是null。
- Hashtable的key和value都是不能为null的。

Hashtable方法都带有synchronized：线程安全的。线程安全有其它的方案，这个Hashtable对线程的处理导致效率较低，使用较少了。


### Properties

目前只需要掌握Properties属性类对象的相关方法即可。
Properties是一个Map集合，继承Hashtable，Properties的key和value都是String类型。
Properties被称为属性类对象。
Properties是线程安全的。

```java
public class PropertiesTest01 {
    public static void main(String[] args) {

        // 创建一个Properties对象
        Properties pro = new Properties();

        // 需要掌握Properties的两个方法，一个存，一个取。
        pro.setProperty("url", "jdbc:mysql://localhost:3306/bjpowernode");
        pro.setProperty("driver","com.mysql.jdbc.Driver");

        // 通过key获取value
        String url = pro.getProperty("url");
        String driver = pro.getProperty("driver");


        System.out.println(url);
        System.out.println(driver);

    }
}
```

### TreeMap/TreeSet


TreeSet集合存储元素特点：

- 无序不可重复的，但是存储的元素可以自动按照大小顺序排序！称为：可排序集合。
- 无序：这里的无序指的是存进去的顺序和取出来的顺序不同。并且没有下标。
- TreeSet集合底层实际上是一个TreeMap
- TreeMap集合底层是一个二叉树。
- 放到TreeSet集合中的元素，等同于放到TreeMap集合key部分了。
- 无法对自定义类型排序castException
- 可以不写equals方法，因为底层调用了comparable方法进行比较了

#### 自定义排序规则

TreeMap的key或者TreeSet集合中的元素要想排序，有两种实现方式：

- 第一种：实现java.lang.Comparable接口。
- 第二种：单独编写一个比较器Comparator接口。

##### 第一种

```java
public class TreeSetTest04 {
    public static void main(String[] args) {
        Customer c1 = new Customer(32);
        Customer c2 = new Customer(20);
        // 创建TreeSet集合
        TreeSet<Customer> customers = new TreeSet<>();
        // 添加元素
        customers.add(c1);
        customers.add(c2);
        // 遍历
        for (Customer c : customers){
            System.out.println(c);
        }
    }
}

// 放在TreeSet集合中的元素需要实现java.lang.Comparable接口。
// 并且实现compareTo方法。equals可以不写。
class Customer implements Comparable<Customer>{

    int age;
    public Customer(int age){
        this.age = age;
    }

    // 需要在这个方法中编写比较的逻辑，或者说比较的规则，按照什么进行比较！
    // k.compareTo(t.key)
    // 拿着参数k和集合中的每一个k进行比较，返回值可能是>0 <0 =0
    // 比较规则最终还是由程序员指定的：例如按照年龄升序。或者按照年龄降序。
    @Override
    public int compareTo(Customer c) { // c1.compareTo(c2);
        return c.age - this.age;
    }

    public String toString(){
        return "Customer[age="+age+"]";
    }
//----------------------------------------------------------------
 /*
先按照年龄升序，如果年龄一样的再按照姓名升序。
 */
    @Override
    public int compareTo(Vip v) {
        // 写排序规则，按照什么进行比较。
        if(this.age == v.age){
            // 年龄相同时按照名字排序。
            // 姓名是String类型，可以直接比。调用compareTo来完成比较。
            return this.name.compareTo(v.name);
        } else {
            // 年龄不一样
            return this.age - v.age;
        }
    }

}
```

##### 第二种

使用比较器的方式

最终的结论：放到TreeSet或者TreeMap集合key部分的元素要想做到排序,包括两种方式
	- 第一种：放在集合中的元素实现java.lang.Comparable接口。
	- 第二种：在构造TreeSet或者TreeMap集合的时候给它传一个比较器对象。

Comparable和Comparator怎么选择呢？
- 当比较规则不会发生改变的时候，或者说当比较规则只有1个的时候，建议实现Comparable接口。
- 如果比较规则有多个，并且需要多个比较规则之间频繁切换，建议使用Comparator接口。

- Comparator接口的设计符合OCP原则。


```java
public class TreeSetTest06 {
    public static void main(String[] args) {
        // 创建TreeSet集合的时候，需要使用这个比较器。
        // TreeSet<WuGui> wuGuis = new TreeSet<>();//这样不行，没有通过构造方法传递一个比较器进去。

        // 给构造方法传递一个比较器。
        //TreeSet<WuGui> wuGuis = new TreeSet<>(new WuGuiComparator());

        // 大家可以使用匿名内部类的方式（这个类没有名字。直接new接口。）
        TreeSet<WuGui> wuGuis = new TreeSet<>(new Comparator<WuGui>() {
            @Override
            public int compare(WuGui o1, WuGui o2) {
                return o1.age - o2.age;
            }
        });

        wuGuis.add(new WuGui(1000));
        wuGuis.add(new WuGui(800));
        wuGuis.add(new WuGui(810));

        for(WuGui wuGui : wuGuis){
            System.out.println(wuGui);
        }
    }
}

// 乌龟
class WuGui{

    int age;

    public WuGui(int age){
        this.age = age;
    }

    @Override
    public String toString() {
        return "小乌龟[" +
                "age=" + age +
                ']';
    }
}

// 单独在这里编写一个比较器
//比较器实现java.util.Comparator接口。（Comparable是java.lang包下的。Comparator是java.util包下的。）

class WuGuiComparator implements Comparator<WuGui> {

    @Override
    public int compare(WuGui o1, WuGui o2) {
        // 指定比较规则
        // 按照年龄排序
        return o1.age - o2.age;
    }
}

```


#### 自平衡二叉树



图片



### Collections工具类

synchronizedList方法

sort方法（要求集合中元素实现Comparable接口。）

```java

/*
java.util.Collection 集合接口
java.util.Collections 集合工具类，方便集合的操作。
 */
public class CollectionsTest {
    public static void main(String[] args) {

        // ArrayList集合不是线程安全的。
        List<String> list = new ArrayList<>();

        // 变成线程安全的
        Collections.synchronizedList(list);

        // 排序
        list.add("abf");
        list.add("abx");

        Collections.sort(list);
        for(String s : list){
            System.out.println(s);
        }

        List<WuGui2> wuGuis = new ArrayList<>();
        wuGuis.add(new WuGui2(1000));
        wuGuis.add(new WuGui2(8000));
        // 注意：对List集合中元素排序，需要保证List集合中的元素实现了：Comparable接口。
        Collections.sort(wuGuis);
        for(WuGui2 wg : wuGuis){
            System.out.println(wg);
        }

        // 对Set集合怎么排序呢？
        Set<String> set = new HashSet<>();
        set.add("king");
        set.add("kingsoft");
        // 将Set集合转换成List集合
        List<String> myList = new ArrayList<>(set);
        Collections.sort(myList);
        for(String s : myList) {
            System.out.println(s);
        }

        // 这种方式也可以排序。
        //Collections.sort(list集合, 比较器对象);
    }
}

class WuGui2 implements Comparable<WuGui2>{
    int age;
    public WuGui2(int age){
        this.age = age;
    }

    @Override
    public int compareTo(WuGui2 o) {
        return this.age - o.age;
    }

    @Override
    public String toString() {
        return "WuGui2{" +
                "age=" + age +
                '}';
    }
}

```