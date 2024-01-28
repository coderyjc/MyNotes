#Java/多线程基础

## 多线程

什么是进程？什么是线程？
- 进程是一个应用程序（1个进程是一个软件）。
- 线程是一个进程中的执行场景/执行单元。
- 一个进程可以启动多个线程。

对于java程序来说，当在DOS命令窗口中输入：java HelloWorld 回车之后。会先启动JVM，而JVM就是一个进程。JVM再启动一个主线程调用main方法。同时再启动一个垃圾回收线程负责看护，回收垃圾。最起码，现在的java程序中至少有两个线程并发，一个是垃圾回收线程，一个是执行main方法的主线程。

进程和线程是什么关系？举个例子
- 阿里巴巴：进程
	- 马云：阿里巴巴的一个线程
	- 童文红:阿里巴巴的一个线程
- 京东：进程
	+ 强东：京东的一个线程
	+ 妹妹：京东的一个线程
- 进程可以看做是现实生活当中的公司。
- 线程可以看做是公司当中的某个员工。

注意：

- 进程A和进程B的内存独立不共享。（阿里巴巴和京东资源不会共享的！）
- 魔兽游戏是一个进程
- 酷狗音乐是一个进程
- 这两个进程是独立的，不共享资源。

线程A和线程B呢？
在java语言中：线程A和线程B，**堆内存和方法区内存**共享。但是**栈内存**独立，一个线程一个栈。
假设启动10个线程，会有10个栈空间，每个栈和每个栈之间，互不干扰，各自执行各自的，这就是多线程并发。

火车站，可以看做是一个进程。火车站中的每一个售票窗口可以看做是一个线程。我在窗口1购票，你可以在窗口2购票，你不需要等我，我也不需要等你。所以多线程并发可以提高效率。

- java中之所以有多线程机制，目的就是为了提高程序的处理效率。

- 使用了多线程机制之后，main方法结束，是不是有可能程序也不会结束。main方法结束只是主线程结束了，主栈空了，其它的栈(线程)可能还在压栈弹栈。

对于多核的CPU电脑来说，真正的多线程并发是没问题的。4核CPU表示同一个时间点上，可以真正的有4个进程并发执行。

分析一个问题：对于单核的CPU来说，真的可以做到真正的多线程并发吗？

什么是真正的多线程并发？t1线程执行t1的。t2线程执行t2的。t1不会影响t2，t2也不会影响t1。这叫做真正的多线程并发。

单核的CPU表示只有一个大脑：
**不能**够做到真正的多线程并发，但是可以做到给人一种“多线程并发”的感觉。对于单核的CPU来说，在某一个时间点上实际上只能处理一件事情，但是由于CPU的处理速度极快，多个线程之间频繁切换执行，跟人来的感觉是：多个事情同时在做！
线程A：播放音乐
线程B：运行魔兽游戏
线程A和线程B频繁切换执行，人类会感觉音乐一直在播放，游戏一直在运行，给我们的感觉是同时并发的。

电影院采用胶卷播放电影，一个胶卷一个胶卷播放速度达到一定程度之后，人类的眼睛产生了错觉，感觉是动画的。这说明人类的反应速度很慢，就像一根钢针扎到手上，到最终感觉到疼，这个过程是需要“很长的”时间的，在这个期间计算机可以进行亿万次的循环。所以计算机的执行速度很快。

### 实现多线程的两种方式

#### 第一种方式

实现线程的第一种方式：编写一个类，直接继承java.lang.Thread，重写run方法。

- 怎么创建线程对象？ new就行了。
- 怎么启动线程呢？ 调用线程对象的start()方法。
- 注意：亘古不变的道理：方法体当中的代码永远都是自上而下的顺序依次逐行执行的。
- 以下程序的输出结果有这样的特点：有先有后。有多有少。这是咋回事？
```java
public class ThreadTest02 {
    public static void main(String[] args) {
        // 这里是main方法，这里的代码属于主线程，在主栈中运行。
        // 新建一个分支线程对象
        MyThread t = new MyThread();
        // 启动线程
        //t.run(); // 直接调用run方法不会启动另一个线程，不会分配新的分支栈。（这种方式就是单线程。）

        // start()方法的作用是：启动一个分支线程，在JVM中开辟一个新的栈空间，这段代码任务完成之后，瞬间就结束了。这段代码的任务只是为了开启一个新的栈空间，只要新的栈空间开出来，start()方法就结束了。线程就启动成功了。 启动成功的线程会自动调用run方法，并且run方法在分支栈的栈底部（压栈）。
        // run方法在分支栈的栈底部，main方法在主栈的栈底部。run和main是平级的。
        t.start();
        // 这里的代码还是运行在主线程中。
        for(int i = 0; i < 100; i++){
            System.out.println("主线程--->" + i);
        }
    }
}
class MyThread extends Thread {
    @Override
    public void run() {
        // 编写程序，这段程序运行在分支线程中（分支栈）。
        for(int i = 0; i < 100; i++){
            System.out.println("分支线程--->" + i);
        }
    }
}
```

#### 第二种方式

实现线程的第二种方式，编写一个类实现java.lang.Runnable接口。

```java
public class ThreadTest03 {
    public static void main(String[] args) {
        // 创建一个可运行的对象
        // 将可运行的对象封装成一个线程对象
        Thread t = new Thread(new MyRunnable()); // 合并代码
        // 启动线程
        t.start();
        for(int i = 0; i < 100; i++)
            System.out.println("主线程--->" + i);
    }
}

// 这并不是一个线程类，是一个可运行的类。它还不是一个线程。
class MyRunnable implements Runnable {
    @Override
    public void run() {
        for(int i = 0; i < 100; i++){
            System.out.println("分支线程--->" + i);
        }
    }
}
```



匿名内部类

```java
public class ThreadTest04 {
    public static void main(String[] args) {
        // 创建线程对象，采用匿名内部类方式。
        // 这是通过一个没有名字的类，new出来的对象。
        Thread t = new Thread(new Runnable(){
            @Override
            public void run() {
                for(int i = 0; i < 100; i++){
                    System.out.println("t线程---> " + i);
                }
            }
        });

        // 启动线程
        t.start();

        for(int i = 0; i < 100; i++){
            System.out.println("main线程---> " + i);
        }
    }
}
```

#### 第三种方式


实现线程的第三种方式：实现Callable接口。（JDK8新特性。）
这种方式实现的线程可以获取线程的返回值。
之前讲解的那两种方式是无法获取线程返回值的，因为run方法返回void。

思考：
系统委派一个线程去执行一个任务，该线程执行完任务之后，可能
会有一个执行结果，我们怎么能拿到这个执行结果呢？
使用第三种方式：实现Callable接口方式。

实现线程的第三种方式：
- 实现Callable接口
- 这种方式的优点：可以获取到线程的执行结果。
- 这种方式的缺点：效率比较低，在获取t线程执行结果的时候，当前线程受阻塞，效率较低。

 ```java
public class ThreadTest15 {
    public static void main(String[] args) throws Exception {

        // 第一步：创建一个“未来任务类”对象。
        // 参数非常重要，需要给一个Callable接口实现类对象。
        FutureTask task = new FutureTask(new Callable() {
            @Override
            public Object call() throws Exception { // call()方法就相当于run方法。只不过这个有返回值
                // 线程执行一个任务，执行之后可能会有一个执行结果
                // 模拟执行
                System.out.println("call method begin");
                Thread.sleep(1000 * 10);
                System.out.println("call method end!");
                int a = 100;
                int b = 200;
                return a + b; //自动装箱(300结果变成Integer)
            }
        });

        // 创建线程对象
        Thread t = new Thread(task);

        // 启动线程
        t.start();

        // 这里是main方法，这是在主线程中。
        // 在主线程中，怎么获取t线程的返回结果？
        // get()方法的执行会导致“当前线程阻塞”
        // main方法这里的程序要想执行必须等待get()方法的结束
        // 而get()方法可能需要很久。因为get()方法是为了拿另一个线程的执行结果
        // 另一个线程执行是需要时间的。
        Object obj = task.get();
        System.out.println("线程执行结果:" + obj);
    }
}
 ```

怎么获取当前线程对象？
- Thread t = Thread.currentThread();
- 返回值t就是当前线程，这个代码出现在main中，当前线程就是主线程

获取线程对象的名字
- String name = 线程对象.getName();

修改线程对象的名字
- 线程对象.setName("线程名字");

当线程没有设置名字的时候，默认的名字有什么规律？main/Thread-0/Thread-1/Thread-2/Thread-3/.....

### 睡眠与终止

#### sleep

关于线程的sleep方法： static void sleep(long millis)

1、静态方法：Thread.sleep(1000);
2、参数是毫秒
3、作用：让当前线程进入休眠，进入“阻塞状态”，放弃占有CPU时间片，让给其它线程使用。
4、Thread.sleep()方法，可以做到这种效果：间隔特定的时间，去执行一段特定的代码，每隔多久执行一次。

```java
public class ThreadTest06 {
    public static void main(String[] args) {

        for(int i = 0; i < 10; i++){
            System.out.println(Thread.currentThread().getName() + "--->" + i);

            // 睡眠1秒
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

sleep睡眠太久了，如果希望半道上醒来，你应该怎么办？也就是说怎么叫醒一个正在睡眠的线程？？
注意：这个不是终断线程的执行，是终止线程的睡眠。

```java
public class ThreadTest08 {
    public static void main(String[] args) {
        Thread t = new Thread(new MyRunnable2());
        t.setName("t");
        t.start();

        // 希望5秒之后，t线程醒来（5秒之后主线程手里的活儿干完了。）
        try {
            Thread.sleep(1000 * 5);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // 终断t线程的睡眠（这种终断睡眠的方式依靠了java的异常处理机制。）
        // 所以线程中必须对异常进行捕捉
        t.interrupt(); // 干扰，一盆冷水过去！
    }
}
```

#### 终止

不建议使用：线程名称.stop();  已过时，不建议使用，容易丢失数据！

合理方式：

打标记/改标记。

```java
public class ThreadTest10 {
    public static void main(String[] args) {
        MyRunable4 r = new MyRunable4();
        Thread t = new Thread(r);
        t.setName("t");
        t.start();

        // 模拟5秒
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // 终止线程
        // 你想要什么时候终止t的执行，那么你把标记修改为false，就结束了。
        r.run = false;
    }
}

class MyRunable4 implements Runnable {
    // 打一个布尔标记
    boolean run = true;
    @Override
    public void run() {
        for (int i = 0; i < 10; i++){
            if(run){
                System.out.println(Thread.currentThread().getName() + "--->" + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }else{
                // return就结束了，你在结束之前还有什么没保存的。
                // 在这里可以保存。
                //save....
                //终止当前线程
                return;
            }
        }
    }
}
```

### 调度/优先级/让位/合并

常见的线程调度模型有哪些？

- 抢占式调度模型：那个线程的优先级比较高，抢到的CPU时间片的概率就高一些/多一些。java采用的就是抢占式调度模型。
- 均分式调度模型：平均分配CPU时间片。每个线程占有的CPU时间片时间长度一样。平均分配，一切平等。有一些编程语言，线程调度模型采用的是这种方式。

#### 优先级：

实例方法：

- void setPriority(int newPriority) 设置线程的优先级
- int getPriority() 获取线程优先级
- 最低优先级1
- 默认优先级是5
- 最高优先级10
- 优先级比较高的获取CPU时间片可能会多一些。（但也不完全是，大概率是多的。）

main线程的默认优先级是：5

- 优先级较高的，只是抢到的CPU时间片相对多一些。
- 大概率方向更偏向于优先级比较高的。

#### 让位

静态方法：
- static void yield()  让位方法
- Thread.yield(); 让位，当前线程暂停，回到就绪状态，让给其它线程。
- 暂停当前正在执行的线程对象，并执行其他线程
- yield()方法不是阻塞方法。让当前线程让位，让给其它线程使用。yield()方法的执行会让当前线程从“运行状态”回到“就绪状态”。注意：在回到就绪之后，有可能还会再次抢到。

#### 合并

```java
public class ThreadTest13 {
    public static void main(String[] args) {
        System.out.println("main begin");
        Thread t = new Thread(new MyRunnable7());
        t.setName("t");
        t.start();
        //合并线程
        try {
            t.join(); // t合并到当前线程中，当前线程受阻塞，t线程执行直到结束。
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("main over");
    }
}

class MyRunnable7 implements Runnable {

    @Override
    public void run() {
        for(int i = 0; i < 10000; i++){
            System.out.println(Thread.currentThread().getName() + "--->" + i);
        }
    }
}
```

### synchronized

#### 线程安全

为什么这个是重点？
- 以后在开发中，我们的项目都是运行在服务器当中，而服务器已经将线程的定义，线程对象的创建，线程的启动等，都已经实现完了。这些代码我们都不需要编写。

最重要的是
- 你要知道，你编写的程序需要放到一个多线程的环境下运行，你更需要关注的是这些数据在多线程并发的环境下是否是安全的。（重点）

什么时候数据在多线程并发的环境下会存在安全问题呢？

- 条件1：多线程并发。
- 条件2：有共享数据。
- 条件3：共享数据有修改的行为。
- 满足以上3个条件之后，就会存在线程安全问题。


当多线程并发的环境下，有共享数据，并且这个数据还会被修改，此时就存在线程安全问题，怎么解决这个问题？
- 线程排队执行。（不能并发）。
- 用排队执行解决线程安全问题。
- 这种机制被称为：线程同步机制。
- 专业术语叫做：线程同步，实际上就是线程不能并发了，线程必须排队执行。

怎么解决线程安全问题？ 使用“线程同步机制”。

线程同步就是线程排队了，线程排队了就会牺牲一部分效率，没办法，数据安全第一位，只有数据安全了，我们才可以谈效率。数据不安全，没有效率的事儿。

说到线程同步这块，涉及到这两个专业术语：

- 异步编程模型：
	- 线程t1和线程t2，各自执行各自的，t1不管t2，t2不管t1，谁也不需要等谁，这种编程模型叫做：异步编程模型。其实就是：多线程并发（效率较高。）
	- 异步就是并发。

- 同步编程模型：
	- 线程t1和线程t2，在线程t1执行的时候，必须等待t2线程执行结束，或者说在t2线程执行的时候，必须等待t1线程执行结束，两个线程之间发生了等待关系，这就是同步编程模型。
	效率较低。线程排队执行。
	- 同步就是排队。


实例变量：在堆中。
静态变量：在方法区。
局部变量：在栈中。

以上三大变量中：
局部变量永远都不会存在线程安全问题。因为局部变量不共享。（一个线程一个栈。）局部变量在栈中。所以局部变量永远都不会共享。

实例变量在堆中，堆只有1个。静态变量在方法区中，方法区只有1个。堆和方法区都是多线程共享的，所以可能存在线程安全问题。

局部变量+常量：不会有线程安全问题。
成员变量：可能会有线程安全问题。

如果使用局部变量的话：建议使用：StringBuilder。因为局部变量不存在线程安全问题。选择StringBuilder。StringBuffer效率比较低。

- ArrayList是非线程安全的。
- Vector是线程安全的。
- HashMap HashSet是非线程安全的。
- Hashtable是线程安全的。

#### 银行取钱模拟

存在问题的：

```java
public class Test{
    public static void main(String[] args) {
        //创建账户对象，只建一个
        Account act = new Account("act-001", 10000);
        //创建两个线程
        Thread t1 = new AccountThread(act);
        Thread t2 = new AccountThread(act);
        //设置name
        t1.setName("t1");
        t2.setName("t2");
        //启动线程取款
        t1.start();
        t2.start();
    }
}

class Account {
    private String actno; //账号
    private double balance; //余额

    public Account(String actno, double balance) {
        this.actno = actno;
        this.balance = balance;
    }

    public String getActno() {
        return actno;
    }

    public void setActno(String actno) {
        this.actno = actno;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void withdraw(double money){
        //取款之前的余额
        double before = this.getBalance();
        //取款之后的余额
        double after = before - money;

        // 在这里模拟一下网络延迟，一定会出问题-》两次的余额都是 5000
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        //更新余额
        //t1执行到了这里，但是还没有来得及只从这行代码，t2线程进来withdraw方法了，此时一定出问题
        this.setBalance(after);
    }
}

class AccountThread extends Thread{
    //两个线程必须共享同一个账户对象
    private Account act;
    //通过构造方法传递过来账户对象
    public AccountThread(Account act){
        this.act = act;
    }
    //run 方法的执行标识取款操作
    public void run(){
        //取5000
        double money = 5000;
        act.withdraw(money);
        System.out.println( Thread.currentThread().getName() + "账户" + act.getActno() + "取款" + money + "成功， 余额为" + act.getBalance());
    }
}
```

使用了线程同步机制解决问题：

```java
public class Test{
    public static void main(String[] args) {
        //创建账户对象，只建一个
        Account act = new Account("act-001", 10000);
        //创建两个线程
        Thread t1 = new AccountThread(act);
        Thread t2 = new AccountThread(act);
        //设置name
        t1.setName("t1");
        t2.setName("t2");
        //启动线程取款
        t1.start();
        t2.start();
    }
}

class Account {
    private String actno; //账号
    private double balance; //余额

    public Account(String actno, double balance) {
        this.actno = actno;
        this.balance = balance;
    }

    public String getActno() {
        return actno;
    }

    public void setActno(String actno) {
        this.actno = actno;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public void withdraw(double money){
        //以下这几行代码必须时县城排队的，不能并发
        //一个线程把这里的代码全部执行结束之后，另一个线程才能进来
        /*
        线程同步机制的语法：
        synchronized () {
            //线程同步代码块
        }
        synchronized 后面小括号中的数据时相当关键的，这个数据必须是多线程共享的数据才能达到多线程排队。
        ()中写什么，要看你想让哪些线程同步
            假设t1、t2、t3、t4、t5，有5个线程，你只希望t1 t2 t3排队，t4 t5不需要排队。怎么办？你一定要在()中写一个t1 t2 t3共享的对象。而这个对象对于t4 t5来说不是共享的。

            这里的共享对象是：账户对象。
            账户对象是共享的，那么this就是账户对象吧！！！
            不一定是this，这里只要是多线程共享的那个对象就行。

            在java语言中，任何一个对象都有“一把锁”，其实这把锁就是标记。（只是把它叫做锁。）
            100个对象，100把锁。1个对象1把锁。

            以下代码的执行原理？
                1、假设t1和t2线程并发，开始执行以下代码的时候，肯定有一个先一个后。
                2、假设t1先执行了，遇到了synchronized，这个时候自动找“后面共享对象”的对象锁，
                找到之后，并占有这把锁，然后执行同步代码块中的程序，在程序执行过程中一直都是
                占有这把锁的。直到同步代码块代码结束，这把锁才会释放。
                3、假设t1已经占有这把锁，此时t2也遇到synchronized关键字，也会去占有后面
                共享对象的这把锁，结果这把锁被t1占有，t2只能在同步代码块外面等待t1的结束，
                直到t1把同步代码块执行结束了，t1会归还这把锁，此时t2终于等到这把锁，然后
                t2占有这把锁之后，进入同步代码块执行程序。

                这样就达到了线程排队执行。
                这里需要注意的是：这个共享对象一定要选好了。这个共享对象一定是你需要排队执行的这些线程对象所共享的。

         */
        //synchronized (this){ //正确
        //synchronized (obj) { // 实例变量，只有一个，正确
        //synchronized ("abc") { // "abc"在字符串常量池当中。->所有线程都会同步，所以不行
        //synchronized (null) { // 报错：空指针。
        //synchronized (obj2) { // 这样编写就不安全了。因为obj2不是共享对象。是局部变量，不对

        synchronized (this) {
            double before = this.getBalance();
            double after = before - money;
            try { //模拟网络延迟
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        //更新余额
        //t1执行到了这里，但是还没有来得及只从这行代码，t2线程进来withdraw方法了，此时一定出问题
        this.setBalance(after);
        }
    }
}

class AccountThread extends Thread{
    //两个线程必须共享同一个账户对象
    private Account act;
    //通过构造方法传递过来账户对象
    public AccountThread(Account act){
        this.act = act;
    }
    //run 方法的执行标识取款操作
    public void run(){
        //取5000
        double money = 5000;
        act.withdraw(money);
        System.out.println( Thread.currentThread().getName() + "账户" + act.getActno() + "取款" + money + "成功， 余额为" + act.getBalance());
    }
}
```

- synchronized可以写在实例方法上，如果出现在实例方法上，一定锁的是this，不能有其他对象了，不灵活
- 另外还有一个缺点：它出现在实例方法上的时候表示整个方法体都要同步，可能会无故扩大同步的范围，导致程序的执行效率变低，所以这种方式不常用。
- 写在实例方法上有什么优点：代码下的少了，节俭了。
- 如果共享的对象就是this，并且需要同步的代码块是整个方法体，建议使用这种方式。
- 同步代码块越小，效率越高
- 第一种：同步代码块 灵活 synchronized(线程共享对象){同步代码块;}
- 第二种：在实例方法上使用synchronized表示共享对象一定是this并且同步代码块是整个方法体。
- 第三种：在静态方法上使用synchronized表示找类锁。类锁永远只有1把。就算创建了100个对象，那类锁也只有一把。
- 对象锁：1个对象1把锁，100个对象100把锁。类锁：100个对象，也可能只是1把类锁。


#### 面试题

##### 一

面试题：doOther方法执行的时候需要等待doSome方法的结束吗？

```java
public class Exam01 {
    public static void main(String[] args) throws InterruptedException {
        MyClass mc = new MyClass();

        Thread t1 = new MyThread(mc);
        Thread t2 = new MyThread(mc);

        t1.setName("t1");
        t2.setName("t2");

        t1.start();
        Thread.sleep(1000); //这个睡眠的作用是：为了保证t1线程先执行。
        t2.start();
    }
}

class MyThread extends Thread {
    private MyClass mc;
    public MyThread(MyClass mc){
        this.mc = mc;
    }
    public void run(){
        if(Thread.currentThread().getName().equals("t1")){
            mc.doSome();
        }
        if(Thread.currentThread().getName().equals("t2")){
            mc.doOther();
        }
    }
}

class MyClass {
    public synchronized void doSome(){
        System.out.println("doSome begin");
        try {
            Thread.sleep(1000 * 10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("doSome over");
    }
    public void doOther(){
        System.out.println("doOther begin");
        System.out.println("doOther over");
    }
}

```

不需要，因为doOther()方法没有synchronized

##### 二

面试题：doOther方法执行的时候需要等待doSome方法的结束吗？

```java
public class Exam01 {
    public static void main(String[] args) throws InterruptedException {
        MyClass mc = new MyClass();

        Thread t1 = new MyThread(mc);
        Thread t2 = new MyThread(mc);

        t1.setName("t1");
        t2.setName("t2");

        t1.start();
        Thread.sleep(1000); //这个睡眠的作用是：为了保证t1线程先执行。
        t2.start();
    }
}

class MyThread extends Thread {
    private MyClass mc;
    public MyThread(MyClass mc){
        this.mc = mc;
    }
    public void run(){
        if(Thread.currentThread().getName().equals("t1")){
            mc.doSome();
        }
        if(Thread.currentThread().getName().equals("t2")){
            mc.doOther();
        }
    }
}

class MyClass {
    public synchronized void doSome(){
        System.out.println("doSome begin");
        try {
            Thread.sleep(1000 * 10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("doSome over");
    }
    public synchronized void doOther(){
        System.out.println("doOther begin");
        System.out.println("doOther over");
    }
}

```

需要，因为doOther()方法有synchronized了

##### 三

面试题：doOther方法执行的时候需要等待doSome方法的结束吗？

```java
public class Exam01 {
    public static void main(String[] args) throws InterruptedException {
        MyClass mc1 = new MyClass();
        MyClass mc2 = new MyClass();

        Thread t1 = new MyThread(mc1);
        Thread t2 = new MyThread(mc2);

        t1.setName("t1");
        t2.setName("t2");

        t1.start();
        Thread.sleep(1000); //这个睡眠的作用是：为了保证t1线程先执行。
        t2.start();
    }
}

class MyThread extends Thread {
    private MyClass mc;
    public MyThread(MyClass mc){
        this.mc = mc;
    }
    public void run(){
        if(Thread.currentThread().getName().equals("t1")){
            mc.doSome();
        }
        if(Thread.currentThread().getName().equals("t2")){
            mc.doOther();
        }
    }
}

class MyClass {
    public synchronized void doSome(){
        System.out.println("doSome begin");
        try {
            Thread.sleep(1000 * 10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("doSome over");
    }
    public synchronized void doOther(){
        System.out.println("doOther begin");
        System.out.println("doOther over");
    }
}
```

不需要，因为MyClass对象是两个，两把锁。

##### 四

面试题：doOther方法执行的时候需要等待doSome方法的结束吗？

```java
public class Exam01 {
    public static void main(String[] args) throws InterruptedException {
        MyClass mc1 = new MyClass();
        MyClass mc2 = new MyClass();

        Thread t1 = new MyThread(mc1);
        Thread t2 = new MyThread(mc2);

        t1.setName("t1");
        t2.setName("t2");

        t1.start();
        Thread.sleep(1000); //这个睡眠的作用是：为了保证t1线程先执行。
        t2.start();
    }
}

class MyThread extends Thread {
    private MyClass mc;
    public MyThread(MyClass mc){
        this.mc = mc;
    }
    public void run(){
        if(Thread.currentThread().getName().equals("t1")){
            mc.doSome();
        }
        if(Thread.currentThread().getName().equals("t2")){
            mc.doOther();
        }
    }
}

class MyClass {
    public synchronized static void doSome(){
        System.out.println("doSome begin");
        try {
            Thread.sleep(1000 * 10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("doSome over");
    }
    public synchronized static void doOther(){
        System.out.println("doOther begin");
        System.out.println("doOther over");
    }
}
```
synchronized出现在静态方法上是找类锁。

需要，因为静态方法是类锁，不管创建了几个对象，类锁只有1把。

#### 死锁


死锁代码要会写。
一般面试官要求你会写。
只有会写的，才会在以后的开发中注意这个事儿。
因为死锁很难调试。

```java

public class DeadLock {
    public static void main(String[] args) {
        Object o1 = new Object();
        Object o2 = new Object();

        // t1和t2两个线程共享o1,o2
        Thread t1 = new MyThread1(o1,o2);
        Thread t2 = new MyThread2(o1,o2);

        t1.start();
        t2.start();
    }
}

class MyThread1 extends Thread{
    Object o1;
    Object o2;
    public MyThread1(Object o1,Object o2){
        this.o1 = o1;
        this.o2 = o2;
    }
    public void run(){
        synchronized (o1){
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            synchronized (o2){

            }
        }
    }
}

class MyThread2 extends Thread {
    Object o1;
    Object o2;
    public MyThread2(Object o1,Object o2){
        this.o1 = o1;
        this.o2 = o2;
    }
    public void run(){
        synchronized (o2){
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            synchronized (o1){

            }
        }
    }
}
```

synchronized 在开发过程中最好不要嵌套使用


#### 怎么解决线程安全问题

是一上来就选择线程同步吗？synchronized
不是，synchronized会让程序的执行效率降低，用户体验不好。系统的用户吞吐量降低。用户体验差。在不得已的情况下再选择线程同步机制。

第一种方案：尽量使用局部变量代替“实例变量和静态变量”。

第二种方案：如果必须是实例变量，那么可以考虑创建多个对象，这样实例变量的内存就不共享了。（一个线程对应1个对象，100个线程对应100个对象，对象不共享，就没有数据安全问题了。）

第三种方案：如果不能使用局部变量，对象也不能创建多个，这个时候就只能选择synchronized了。线程同步机制。


### 守护线程/定时器

#### 守护线程

java语言中线程分为两大类：
一类是：用户线程
一类是：守护线程（后台线程）
其中具有代表性的就是：垃圾回收线程（守护线程）。

守护线程的特点：
一般守护线程是一个死循环，所有的用户线程只要结束，守护线程自动结束。

注意：主线程main方法是一个用户线程。

守护线程用在什么地方呢？
每天00:00的时候系统数据自动备份。这个需要使用到定时器，并且我们可以将定时器设置为守护线程。一直在那里看着，每到00:00的时候就备份一次。所有的用户线程如果结束了，守护线程自动退出，没有必要进行数据备份了。

设置为守护线程 t.setDaemon(true);

```java
public class ThreadTest14 {
    public static void main(String[] args) {
        Thread t = new BakDataThread();
        t.setName("备份数据的线程");

        // 启动线程之前，将线程设置为守护线程
        t.setDaemon(true);
        t.start();

        // 主线程：主线程是用户线程
        for(int i = 0; i < 10; i++){
            System.out.println(Thread.currentThread().getName() + "--->" + i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class BakDataThread extends Thread {
    public void run(){
        int i = 0;
        // 即使是死循环，但由于该线程是守护者，当用户线程结束，守护线程自动终止。
        while(true){
            System.out.println(Thread.currentThread().getName() + "--->" + (++i));
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

#### 定时器

定时器的作用：间隔特定的时间，执行特定的程序。

每周要进行银行账户的总账操作。每天要进行数据的备份操作。

在实际的开发中，每隔多久执行一段特定的程序，这种需求是很常见的，那么在java中其实可以采用多种方式实现：可以使用sleep方法，睡眠，设置睡眠时间，没到这个时间点醒来，执行任务。这种方式是最原始的定时器。（比较low）

在java的类库中已经写好了一个定时器：java.util.Timer，可以直接拿来用。不过，这种方式在目前的开发中也很少用，因为现在有很多高级框架都是支持定时任务的。

在实际的开发中，目前使用较多的是Spring框架中提供的SpringTask框架，这个框架只要进行简单的配置，就可以完成定时器的任务。

```java
/*
使用定时器指定定时任务。
 */
public class TimerTest {
    public static void main(String[] args) throws Exception {

        // 创建定时器对象
        Timer timer = new Timer();
        //Timer timer = new Timer(true); //守护线程的方式

        // 指定定时任务
        //timer.schedule(定时任务, 第一次执行时间, 间隔多久执行一次);
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date firstTime = sdf.parse("2020-03-14 09:34:30");
        //timer.schedule(new LogTimerTask() , firstTime, 1000 * 10);
        // 每年执行一次。
        //timer.schedule(new LogTimerTask() , firstTime, 1000 * 60 * 60 * 24 * 365);

        //匿名内部类方式
        timer.schedule(new TimerTask(){
            @Override
            public void run() {
                // code....
            }
        } , firstTime, 1000 * 10);

    }
}

// 编写一个定时任务类
// 假设这是一个记录日志的定时任务
class LogTimerTask extends TimerTask {

    @Override
    public void run() {
        // 编写你需要执行的任务就行了。
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String strTime = sdf.format(new Date());
        System.out.println(strTime + ":成功完成了一次数据备份！");
    }
}
```

### 生产者和消费者模式

关于Object类中的wait和notify方法

- 第一：wait和notify方法不是线程对象的方法，是java中任何一个java对象都有的方法，因为这两个方式是Object类中自带的。wait方法和notify方法不是通过线程对象调用，不是这样的：t.wait()，也不是这样的：t.notify()..不对。
- 第二：wait()方法作用？Object o = new Object();o.wait();
	- 表示：让正在o对象上活动的线程进入等待状态，无期限等待，直到被唤醒为止。o.wait();方法的调用，会让“当前线程（正在o对象上活动的线程）”进入等待状态。
- 第三：notify()方法作用？Object o = new Object(); o.notify();
	+ 表示：唤醒正在o对象上等待的线程。
	+ 还有一个notifyAll()方法：这个方法是唤醒o对象上处于等待的所有线程。

#### 实现

使用wait方法和notify方法实现“生产者和消费者模式”

什么是“生产者和消费者模式”？
- 生产线程负责生产，消费线程负责消费。
- 生产线程和消费线程要达到均衡。
- 这是一种特殊的业务需求，在这种特殊的情况下需要使用wait方法和notify方法。

- wait和notify方法不是线程对象的方法，是普通java对象都有的方法。
- wait方法和notify方法建立在线程同步的基础之上。因为多线程要同时操作一个仓库。有线程安全问题。
- wait方法作用：o.wait()让正在o对象上活动的线程t进入等待状态，并且释放掉t线程之前占有的o对象的锁。
- notify方法作用：o.notify()让正在o对象上等待的线程唤醒，只是通知，不会释放o对象上之前占有的锁。


模拟这样一个需求：

- 仓库我们采用List集合。List集合中假设只能存储1个元素。1个元素就表示仓库满了。如果List集合中元素个数是0，就表示仓库空了。保证List集合中永远都是最多存储1个元素。必须做到这种效果：生产1个消费1个。

```java
public class ThreadTest16 {
    public static void main(String[] args) {
        // 创建1个仓库对象，共享的。
        List list = new ArrayList();
        // 创建两个线程对象
        // 生产者线程
        Thread t1 = new Thread(new Producer(list));
        // 消费者线程
        Thread t2 = new Thread(new Consumer(list));

        t1.setName("生产者线程");
        t2.setName("消费者线程");

        t1.start();
        t2.start();
    }
}

// 生产线程
class Producer implements Runnable {
    // 仓库
    private List list;

    public Producer(List list) {
        this.list = list;
    }
    @Override
    public void run() {
        // 一直生产（使用死循环来模拟一直生产）
        while(true){
            // 给仓库对象list加锁。
            synchronized (list){
                if(list.size() > 0){ // 大于0，说明仓库中已经有1个元素了。
                    try {
                        // 当前线程进入等待状态，并且释放Producer之前占有的list集合的锁。
                        list.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                // 程序能够执行到这里说明仓库是空的，可以生产
                Object obj = new Object();
                list.add(obj);
                System.out.println(Thread.currentThread().getName() + "--->" + obj);
                // 唤醒消费者进行消费
                list.notifyAll();
            }
        }
    }
}

// 消费线程
class Consumer implements Runnable {
    // 仓库
    private List list;

    public Consumer(List list) {
        this.list = list;
    }

    @Override
    public void run() {
        // 一直消费
        while(true){
            synchronized (list) {
                if(list.size() == 0){
                    try {
                        // 仓库已经空了。
                        // 消费者线程等待，释放掉list集合的锁
                        list.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                // 程序能够执行到此处说明仓库中有数据，进行消费。
                Object obj = list.remove(0);
                System.out.println(Thread.currentThread().getName() + "--->" + obj);
                // 唤醒生产者生产。
                list.notifyAll();
            }
        }
    }
}
```




### 面试题

#### sleep

```java
/*
关于Thread.sleep()方法的一个面试题：
 */
public class ThreadTest07 {
    public static void main(String[] args) {
        // 创建线程对象
        Thread t = new MyThread3();
        t.setName("t");
        t.start();

        // 调用sleep方法
        try {
            // 问题：这行代码会让线程t进入休眠状态吗？
            t.sleep(1000 * 5);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // 5秒之后这里才会执行。
        System.out.println("hello World!");
    }
}

class MyThread3 extends Thread {
    public void run(){
        for(int i = 0; i < 10000; i++){
            System.out.println(Thread.currentThread().getName() + "--->" + i);
        }
    }
}

```
答案：

- 在执行的时候还是会转换成：Thread.sleep(1000 * 5);
- 这行代码的作用是：让当前线程进入休眠，也就是说main线程进入休眠。
- 这样代码出现在main方法中，main线程睡眠。