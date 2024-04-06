C++面向对象的三大特性为：封装、继承、多态

C++认为万事万物都皆为对象，对象上有其属性和行为

## 面向对象之一  ====>   封装

封装是C++面向对象三大特性之一

封装的意义：
1. 将属性和行为作为一个整体，表现生活中的事物
2. 将属性和行为加以权限控制

成员私有化的优点：
1. 可以自己控制读写的权限
2. 对于写，可以检测数据的有效性（在函数接口里安排提示信息）
(通常在public里写函数（作为接口），来控制private里的对象是可读的还是读写的，方便修改或读取private里的对象)

### 构造和析构

 1. 构造函数
- 没有返回值
- 不用写void
- 函数名与类名相同
- 构造函数可以有参数，可以发生重载
- 创建对象的时候，构造函数会自动调用，而且只调用一次

2. 析构函数
- 进行清理的操作
- 没有返回值
- 不写void
- 函数名和类名相同
- 在名称前加~
- 析构函数不可以有参数的，不可以重载对象
- 在销毁前会自动调用析构函数，而且只会调用一次

```C++
#include<iostream>
#include<string>
using namespace std;
class Person {
public:
       //无参（默认）构造函数
       Person() {
              cout << "无参构造函数！" << endl;
       }
       //有参构造函数
       Person(int a) {
                     age = a;
                     cout << "有参构造函数！" << endl;
       }
       //拷贝构造函数
       Person(const Person& p){
       age = p.age;
       cout << "拷贝构造函数！" << endl;
       }
       //析构函数
       ~Person(){}
private:
       int age;
};

//2、构造函数的调用
void t01()
{
       Person p;     //调用无参构造函数
}
void t02()    //调用有参构造的函数
{
       //2.1 括号法，常用
       Person p1(10);
       //注意： 调用无参构造函数不能加口号，如果加了括号，编译器会认为这是一个函数声明
       //Person p2()
       //2.2 显示法
       Person p2 = Person(10);
       Person p3 = Person(p2);
       //Person(10)单独写就是匿名对象，当前行结束之后马上析构
       //2.3 隐式转换法
       Person p4 = 10;
       Person p5 = p4;
       //注意： 不能用拷贝构造函数初始化匿名对象，编译器认为是对象声明
       // Person p5(p4)
}
```

什么时候用拷贝构造？
- 使用一个已经创建完毕的对象来初始化一个新对象
- 值传递的方式给函数参数传值
- 以值方式返回局部对象

默认情况下，C++编译器至少给一个类添加3个函数
1. 默认构造函数（无参，函数体为空）
2. 默认析构函数（无参，函数体为空）
3. 默认拷贝构造函数，对属性进行值拷贝

构造函数调用规则如下：
- 如果用户定义有参构造函数，C++不在提供默认无参构造，但是会提供默认拷贝构造
- 如果用户定义拷贝构造函数，C++不会再提供其他构造函数

析构函数里用delete来清理内存

浅拷贝： 编译器给我们提供的等号赋值操作（带来的问题：同一块内存空间被释放两次，导致程序崩溃）
深拷贝：我们在堆区重新new一块内存（要在析构函数里释放）

```c++
Person(const Person& p) {
  cout << "拷贝构造函数" << endl;
  //如果不利用深拷贝，则会导致浅拷贝重复释放堆区内存的问题
  m_age = p.m_age;
  m_height = new int(*p.m_height);
}

~Person() {
  cout << "析构函数" << endl;
  if (m_height != NULL) {
	delete m_height;
}
```

初始化列表：

作用：用来初始化属性
语法：构造函数（）：属性1（值1），属性2（值2）...（）

```c++
class Person {
public:
       //初始化列表初始化属性
       Person(int a, int b, int c) :m_a(a), m_b(b), m_c(c) {
              //则在调用这个函数的时候，
              /*
                     m_a = a;
                     m_b = b;
                     m_c = c;
              */
              //(也可以给他传递参数)
       }
       int m_a;
       int m_b;
       int m_c;
};
```

类对象作为类的成员：

```c++
class Phone {
public:
   string brand;
   Phone(string p_brand) {
		  brand = p_brand;
   }
};

class Person {
public:
       string name;
       Phone phone;
Person(string name, string pbrand) :name(name), phone(pbrand) {}
};
//先构造 phone 类，也就是说 ： 当其他的类的对象作为本类的成员的时候，在构造的时候，先构造其他类，在构造自身
// 在析构的时候， 先析构本类（也就是大类）， 再析构小类（被包含的类）
//析构的顺序与构造相反
```

### static

```c++
#include<iostream>
#include<string>
using namespace std;
class Person {
public:
       static void func() {
              m_a = 100;//静态成员函数可以访问静态成员变量
              m_b = 100;//静态成员函数不可以访问费静态成员变量，无法区分是哪个对象的m_b
              cout << "static void func 调用" << endl;
       }
       static int m_a; //静态成员变量
       int m_b; //非静态成员变量
};
int main() {
       // 1、通过对象访问
       Person p;
       p.func();
       //2、通过类名访问
       Person::func;
       //类外不能访问私有静态成员函数
       return 0;
}
```

空 class 占用的空间为1，因为C++编译器会给每个空对象也分配1字节的空间，是为了区分空对象占内存的位置；每个空对象也应该有一个独一无二的内存地址

静态成员变量类内声明类外初始化

```c++
class Person {
public:
       int m_a; //非静态成员变量 属于类的对象上
       static int m_b; // 静态成员变量 不属于类的对象上
       
       void func(){} // 非静态成员函数 不属于类的对象上
       static void func2() {} // 静态成员函数 不属于类的对象上
};
```


### this指针

指向被调用的成员函数所属的对象

1. 形参和成员变量同名时，可以用this指针来区分

```c++
class Person {
public:
       Person(int age) {
              age = age;
       }
       int age;
};
void test01() {
       Person p1(18);
       cout << p1.age << endl;
}
// 这样输出的数值为一个随机值， 因为编译器认为class里的成员函数里的3个age是同一个age。

class Person {
public:
       Person(int age) {
              this->age = age; // 指向被调用的成员函数所属的对象
       }
       int age;
};
void test01() {
       Person p1(18);
       cout << p1.age << endl;
}
//这样输出的是 18

```

2. 在类的非静态成员函数中返回对象本身，可以return *this;

```c++

class Person {
public:
       int age;
       Person(int age) {
              this->age = age;
       }
       Person& add(Person& p) {
              this->age += p.age;
              return *this;
       }
       //为什么返回引用而不返回值？
       /*
              原理和拷贝构造一样
              链式调用的时候，是在另外一个内存空间创造出来另一个数，那个数是18+10
              返回的是指向那个新开辟出来的空间的引用，每一次都是这样。而如果返回
              的是值的话，则每一次返回的都是在原来的18的基础上加的10，都是28,。
              
       */
};
void test01() {
       Person p1(18);
       Person p2(10);
       //链式编程思想
       p1.add(p2);//输出 28
       p1.add(p2).add(p2).add(p2); //输出 48
       cout << endl;
}

```

### 空指针访问成员函数

```c++
class Person {
public:
       int age = 0;
       void out01() {
              cout << "this is out01" << endl;
       }
       void out02() {
              cout << "age = " << this->age << endl;
       }
};
void test01() {
       Person *p = NULL;
       p->out01(); // 正常输出
       p->out02(); // 报错：无效指针 ，因为p指针为空，所以this指针为空。没有有效的地址。
}

       //更正方式：
       void out02() {
              if (this == NULL)
                     return;
              cout << "age = " << this->age << endl;
       }
```

### const 修饰成员函数

常函数：
- 成员函数后加const后我们称为这个函数为常函数
- 常函数内不可以修改成员属性
- 成员属性声明时加关键字mutable后，在常函数中依然可以修改

```c++
class Person {
public:
       //this指针的本质 ： 是指针常量，指针的指向是不可以修改的
       //但是， 指针指向的 值 可以修改
       /*
              如果想让指针指向的值也可以修改的话， 则应该在成员函数的后面加上 const
       */
       int m_a;
       mutable int m_b; // 特殊变量， 即使在常函数中也可以修改
       void showperson() const {
              this->m_b = 100;
       }
};
```

常对象：
- 声明对象前加const称该对象为常对象
- 常对象只能调用常函数

### 友元（friend）

目的：让一个函数或者类访问另一个类中的private成员

三种实现方法：
- 全局函数做友元
- 类做友元
- 成员函数做友元

全局函数做友元：

```c++
class Building {
public:
       Building() {
              m_sittingRoom = "客厅";
              m_BedRoom = "卧室";
       }
       string m_sittingRoom; // 客厅
private:
       string m_BedRoom; // 卧室
};
//全局函数
void Goodgay(Building& building) {
       cout << "好基友的全局函数 正在访问 " << building.m_sittingRoom << endl; // 公共属性 可以 访问
       cout << "好基友的全局函数 正在访问 " << building.BedRoom << endl; // 私有的属性 不可以 访问
}

       // 解决方法 ： 在class里的开头加上 friend 函数头；
class Building {

       // 即：
       friend void Goodgay(Building& building);
public:
       Building() {
              m_sittingRoom = "客厅";
              m_BedRoom = "卧室";
       }
       string m_sittingRoom; // 客厅
private:
       string m_BedRoom; // 卧室
};
```

类作为友元（一个类能够访问另一个类中的私有成员）：

```c++
class Building {
       //  goodgay 是Building的好朋友 可以访问building里的类
       friend class goodgay;
public:
       Building();// 类外实现成员函数
public:
       string m_sittingRoom;
private:
       string m_bedRoom;
};
class goodgay {
public:
       Building* building = new Building;
       void visit() {
              cout << "正在访问:" << building->m_sittingRoom <<  endl;
              cout << "正在访问:" << building->bedRoom << endl; // 非友元不可以访问
       }
};
Building::Building() {
       // 类外实现Building 的初始化
       m_sittingRoom = "客厅";
       m_bedRoom = "卧室";
}

（*有不懂的）成员函数作为友元：

#include<iostream>
#include<string>
using namespace std;
class Building;
class GoodGay {
public:
       GoodGay();
       void visit(); // 可以访问building中的私有成员
       void visit2(); // 不可以访问...
       Building* building;
};
class Building {
       //告诉编译器 GoodGay 下的 visit2 函数是友元
       friend void GoodGay::visit2();
public:
       string m_SittingRoom;
private:
       string m_BedRoom;
public:
       Building();
};
Building::Building() {
       m_SittingRoom = "sitting";
       m_BedRoom = "bed";
}
GoodGay::GoodGay() {
       building = new Building;
}
void GoodGay::visit() {
       cout << "visit函数正在访问" << building->m_SittingRoom << endl;
//     cout << "visit函数正在访问" << building->m_BedRoom << endl;
}
void GoodGay::visit2() {
       cout << "visit2函数正在访问" << building->m_SittingRoom << endl;
       cout << "visit2函数正在访问" << building->m_BedRoom << endl;
}
int main() {
       GoodGay gg;
       gg.visit();
       gg.visit2();
       return 0;
}
```

### 运算符重载

运算符可以和函数一起重载

加号运算符

```c++
//加号运算符重载
class Person {
public:
       int m_a;
       int m_b;
       //成员函数实现重载
       Person operator+(Person &p) {
              Person temp;
              temp.m_a = this->m_a + p.m_a;
              temp.m_b = this->m_b + p.m_b;
              return temp;
       }
};
void test() {
       Person p1;
       p1.m_a = 10;
       p1.m_b = 10;
       Person p2;
       p2.m_a = 5;
       p2.m_b = 15;
       Person p3 = p1 + p2;
       cout << p3.m_a << endl << p3.m_b << endl;
}

//加号运算符重载
class Person {
public:
       int m_a;
       int m_b;
};
       //全局函数实现重载
       Person operator+(Person &p1, Person &p2) {
              Person temp;
              temp.m_a = p1.m_a + p2.m_a;
              temp.m_b = p1.m_b + p2.m_b;
              return temp;
       }
void test() {
       Person p1;
       p1.m_a = 10;
       p1.m_b = 10;
       Person p2;
       p2.m_a = 5;
       p2.m_b = 15;
       Person p3 = p1 + p2;
       cout << p3.m_a << endl << p3.m_b << endl;
}
```

总结：对于内置的数据类型的表达式的运算符是不能重载的
总结： 不能滥用运算符

左移运算符重载（只能用全局函数重载）

```c++
// << 运算符重载
class Person {
public:
       int m_a;
       int m_b;
};
/*
       不能使用 成员函数重载 ， 因为无法实现 cout 在左边
       只能使用全局函数重载 左移运算符
*/
ostream& operator<<(ostream& cout, Person p) {
       cout << "m_a = " << p.m_a << endl;
       cout << "m_b = " << p.m_b << endl;
       return cout; // 链式编程， 返回 cout 的引用
}
void test() {
       Person p;
       p.m_a = 10;
       p.m_b = 20;
       cout << p << endl;
}
```

重载运算符配合着友元可以输出自定义的数据类型

递增运算符重载

```c++
//自定义整型
class MyInteger {
       friend ostream& operator<<(ostream& cout, MyInteger p);
public:
       MyInteger() {
              m_Num = 0;
       }
       //重载前置 ++ 运算符 
       //返回 class 的引用类型 是为了一直对一个数据进行递增操作
       MyInteger& operator++() {
              //先进行 ++ 运算
              m_Num++;
              //再进行返回
              return *this;
       }
       //重载后置 ++ 运算符  不用引用
       MyInteger operator++(int) {
              //先 记录当时的结果
              MyInteger temp = *this;
              //后 递增
              m_Num++;
              //最后 将记录作为结果返回
              return temp;
       }
private:
       int m_Num;
};
ostream & operator<<(ostream& cout, MyInteger p) {
       cout << p.m_Num << endl;
       return cout;
}
void test01() {
       MyInteger myint; // 重载前置++的测试
       //cout << ++myint ;
}
void test02() {
       MyInteger myint; // 重载后置++的测试
       cout << myint++ ;
       cout << myint ;
}
int main() {
       test01();
       test02();
       return 0;
}
```


赋值运算符重载

C++编译器至少给一个类添加4个函数
1. 默认构造函数(无参 , 函数体为空)
2. 默认析构函数(无参 , 函数体为空)
3. 默认拷贝构造函数,对属性进行值拷贝
4. 赋值运算符 operator= 对属性进行拷贝

如果类中有属性指向堆区, 做赋值操作时也会出现深浅拷贝的问题

```c++
class Person {
public:
       Person(int age) {
              m_Age = new int(age);
       }
       int* m_Age;
       
       Person& operator=(Person& p) {
              //应该先判断是否有属性在堆区, 如过有,先释放干净,然后再深拷贝
              if (m_Age != NULL)
              {
                     delete m_Age;
                     m_Age = NULL;
              }
              // 深拷贝
              m_Age = new int(*p.m_Age);
              //返回对象本身并且返回 Person 的引用 目的是让其可以 "连等"
              return *this;
       }
};
void test01() {
       Person p1(18);
       Person p2(20);
       p2 = p1;  // 直接复制会造成浅拷贝问题,同一块内存空间被释放两次
}
```

关系运算符重载

让两个自定义数据类型进行比较

可以根据经验自己写出:

```c++
// 重载关系运算符
class Person {
public:
       string name;
       int age;
       Person(string name, int age) {
              this->name = name;
              this->age = age;
       }
       int operator>(Person& p) {
              if (this->age > p.age)
                     return 1;
              else return 0;
       }
};
```

函数调用运算符重载(简单了解)

函数调用运算 () 也可以重载
叫做仿函数
没有固定写法, 非常灵活

```c++
// 重载函数调用运算符
class Person {
public:
       int operator()(int num1, int num2) {
              return num1 + num2;
       }
};
void test01() {
       Person myadd;
       int ret = myadd(100, 100);
       cout << "ret = " << ret;
}

class Add {
public:
       int operator()(int num1, int num2) {
              return num1 + num2;
       }
};
void test01() {
       //以 匿名函数对象 的形式输出: 使用完之后立即释放
       cout << Add()(100, 100);
}
```

## 面向对象之二  ====>   继承

![[assets/Pasted image 20240202175017.png]]

在定义这有些类的时候, 下级别的成员除了有上一级的共性, 还有自己的特性.
这个时候可以考虑使用继承的方式,减少重复代码

基本语法:

普通方法(一定==不要用==,  十分麻烦!!!):

```c++
//普通实现
//java页面
class Java {
public:
       void header() {
              cout << "首页/公开课/登录等....(头部)" << endl;
       }
       void footer() {
              cout << "帮助中心/交流合作等(底部)" << endl;
       }
       void list() {
              cout << "java, python ...(列表)" << endl;
       }
       void content() {
              cout << "其他学科 (目录)" << endl;
       }
};
//C++页面
// 再写的时候就要把已经写好了的 java 的东西复制过来然后
// 把java都改为 C++
// Python 页面也是一样的

// 这样非常麻烦!!!
```

继承的方法:

```c++
//继承实现
// 公共类:
class BasePage {
public:
    void header() {
        cout << "首页/公开课/登录等....(头部)" << endl;
    }
    void footer() {
        cout << "帮助中心/交流合作等(底部)" << endl;
    }
    void list() {
        cout << "java, python ...(列表)" << endl;
    }
};
//java页面
class Java : public BasePage {
public:
    void content() {
        cout << "Java学科视频" << endl;
    }
};
//C++页面
class Cpp : public BasePage {
public:
    void content() {
        cout << "C++学科视频" << endl;
    }
};
```

继承的好处: 减少重复的代码.

语法: ==class 子类 : 继承方式 父类==

子类 也叫 派生类
父类 也叫 基类

派生类中的成员包含两大部分:
一类是从基类继承过来的(共性) , 一类是自己增加的成员(个性)

### 继承方式

![[assets/Pasted image 20240202175047.png]]

- 公共继承
- 保护继承
- 私有继承

子类无论以什么方式都访问不到父类中的私有内容.

```c++
//继承方式
//公共继承
class Base1 {
public:
       int m_a;
private:
       int m_b;
protected:
       int m_c;
};
class Son1 : public Base1 {
public:
       void fun1() {
              m_a = 10;
              //m_b = 10;  私有权限访问不到
              m_c = 10; // 继承之后的保护权限, 在类外依然访问不到
       }
};
//保护继承
class Base2 {
public:
       int m_a;
private:
       int m_b;
protected:
       int m_c;
};
class Son2 : protected Base2 {
public :
       void fun() {
              m_a = 10; // 父类中的公共成员, 到子类中变为了保护成员 , 类外不可以访问
       //     m_b = 10; // 父类中的私有成员访问不到
              m_c = 10; // 父类成员的私有成员, 到了子类中变为了保护成员 , 类外不可以访问
       }
};
// 私有继承
class Base3 {
public:
       int m_a;
private:
       int m_b;
protected:
       int m_c;
};
class Son3 : private Base3 {
public:
       void fun() {
              m_a = 10; // 变为了私有成员
              // m_b = 10; // 父类中的私有成员在子类中访问不到
              m_c = 10; // 变为了私有成员
       }
};

```

### 继承中的对象模型

父类中的所有成员都会传给子类
父类中私有的成员属性被编译器隐藏了, 访问不到, 但是确实被继承下去了

利用  开发人员命令提示工具查看类 的布局

命令: `cl /d1 reportSingleClassLayout+类名(前面无空格)+空格+.cpp文件`

![[assets/Pasted image 20240202175137.png]]

### 继承中的构造和析构顺序

父类和子类的构造和析构顺序:

父类先构造后释放,子类后构造先释放.
即:

父类构造
子类构造
子类释放
父类释放

### 继承中同名成员处理方式

访问子类同名成员 直接反问即可(直接 . )
访问父类同名成员 需要加作用域

```c++
class Base {
public:
       int m_A;
       Base() {
              m_A = 10;
       }
};
class Son : public Base {
public:
       int m_A;
       Son() {
              m_A = 15;
       }
};
void test01() {
       Son p;
       cout << "p.m_A = " << (p.m_A) << endl;
       cout << "p.Base::m_A = " << (p.Base::m_A) << endl;
}
```

如果子类中出现了和父类同名的成员函数,在调用父类传下来的成员函数的时候都应该加上作用域

### 继承同名静态成员的处理方式

问题：继承中同名的静态成员在子类对象上如何进行访问？

静态成员和非静态成员出现同名，处理方式一致
只不过有两种方法: 通过对象 和 通过类名

- 访问子类同名成员直接访问即可
·访问父类同名成员需要加作用域

### 静态成员属性:

编译阶段分配内存
所有对象共享同一份数据
类内声明类外初始化

### 多继承语法:

实际开发中并不建议用!

class 子类 : 继承方式 父类1, 继承方式 父类2, ......
`class Son : public Base, public Base2 {}`

父类中出现了同名成员的时候应该加上作用域区分

### 菱形继承

概念: 两个派生类继承同一个基类,又有一个类继承了两个派生类

![[assets/Pasted image 20240202175233.png]]

问题: 

1. 羊继承了动物的数据，驼同样继承了动物的数据，当草泥马使用数据时就会产生二义性。
2. 草泥马继承自动物的数据继承了两份，其实我们应该清楚，这份数据我们只需要一份就可以。

当菱形继承的时候, 两个父类有相同的数据, 需要用作用于加以区分
但是我们知道这个数据有一份就可以了,怎么办?

利用虚继承可以解决 可以解决此类问题, 在中间两个子类的继承之前加上 virtual 

最上方的类叫做虚基类, 虚继承之后, 数据会变为"只有一个"

```c++
//继承中同名成员的处理
class animal {
public :
       int m_Age = 18;
};
// 在两个子类继承方式之前加上 virtual
class sheep :virtual public animal{};
class camel :virtual  public animal {};
class sheepcamel :  public sheep, public camel {};
void test01() {
       sheepcamel p;
       p.sheep::m_Age = 10;
       p.camel::m_Age = 18;
       cout << p.m_Age << endl;
}

```

(继承了指针. 可以通过偏移量来找到那个主题)

## 面向对象之三  ====>  多态

多态分为两类
- 静态多态：函数重载和运算符重载属于静态多态，复用函数名
- 动态多态：派生类和虚函数实现运行时多态

静态多态和动态多态区别：
- 静态多态的函数地址早绑定, 编译阶段确定函数地址
- 动态多态的函数地址晚绑定, 运行阶段确定函数地址

### 动态多态的基本语法

```c++

//多态
//动物类
class Animal {
public :
       virtual void speak() {
              cout << "动物在说话" << endl;
       }
};
// 猫类
class Cat : public Animal {
public :
       void speak() {
              cout << "猫在说话" << endl;
       }
};
//执行说话函数
// 地址早绑定, 在编译阶段就已经确定了函数地址
//如果想执行让猫说话, 这个函数的地址就不能提前绑定,也就是地址晚绑定
//解决方法: 在父类的speak 函数之前加上 virtual , 使其变为虚函数
void doSpeak(Animal& animal) {
       animal.speak();
}
void test01() {
       Cat cat;
       doSpeak(cat);
}
int main() {
       test01();
       return 0;
}
```

动态多态的满足条件
1. 有继承关系
2. 子类应该重写(不是重载)父类的虚函数, 重写:函数的返回值类型,函数名称,参数列表要完全相同.  子类的函数前面可以不写 virtual

动态多态的使用
父类的指针或者引用来指向子类的对象

多态的优点
- 代码组织结构清晰
- 可读性强
- 利于前期和后期的扩展以及维护

真正的开发中提倡开闭原则:对扩展进行开放, 对修改进行关闭

### 纯虚函数和抽象类

在多态中，通常父类中虚函数的实现是毫无意义的，主要都是调用子类重写的内容

因此可以将虚函数改为纯虚函数

纯虚函数语法：
virtual 返回值类型 函数名（参数列表）= 0 ;

当类中只要有了一个纯虚函数，这个类也称为抽象类

抽象类特点：
无法实例化对象
子类必须重写抽象类中的纯虚函数，否则也属于抽象类

```c++

//纯虚函数和抽象类
class Base {
public:
       //纯虚函数
       //只要有一个纯虚函数,就是抽象类
       //1. 无法实例化对象 , 就是不能用他定义一个对象
       //2. 抽象类的子类必须重写父类中的虚函数, 否则也是抽象类
       virtual void func() = 0;
};
class Son : public Base {
public:
       void func() {
       }
 };
void test01() {
       Son p; // 子类不是抽象类,可以实例化对象
}
```

### 虚析构和纯虚析构

多态使用时，如果子类中有属性开辟到维区，那么父类指针在释放时无法润用到子类的析构代码

解决方式：将父类中的析构函数改为虚析构或者纯虚析构

虚析构和纯虚析构共性：
- 可以解决父类指针释放子类对象
- 都需要有具体的函数实现

虚析构和纯虚析构区别：
- 如果是纯虚析构，该类属于抽象类，无法实例化对象

```c++
 class Animal {
public:
       virtual void speak() = 0;
       virtual ~Animal() = 0;
};
 // 纯虚析构需要有声明和实现
 // 有了纯虚析构之后, 也属于抽象类. 无法实例化对象
Animal::~Animal() {
       cout << "Animal的纯虚析构调用" << endl;
}
class Cat : public Animal {
public:
       Cat(string  name) {
              m_Name = new string(name);
       }
       virtual void speak() {
              cout << *m_Name << "猫在说话" << endl;
       }
       string* m_Name;
       ~Cat() {
              if (m_Name != NULL)
                     delete m_Name;
       }
};
void test01() {
       Animal* animal = new Cat("Tom");
       animal->speak();
       //父类指针在析构的时候 不会调用子类中的析构函数 导致子类函数使用的内存在结束的时候无法释放
       // 方法: 将父类的析构函数改为 虚析构 virtual ~ |  或者纯虚析构(纯虚析构需要在类外实现)
       delete animal;
}
```
