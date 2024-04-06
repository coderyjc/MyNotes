程序运行时产生的数据都属于临时数据，程序一旦运行结束都会被释放

通过文件可以将数据持久化

C++中对文件操作需要包含头文件`<fstream>`

文件类型分为两种：
1. 文本文件-文件以文本的ASCll码形式存储在计算机中
2. 二进制文件-文件以文本的二进制形式存储在计算机中，用户一般不能直接读懂它们

操作文件的三大类：
1. ofstream：写操作
2. ifstream：读操作
3. fstream：读写操作

## 写文本文件

写文件步骤如下：

1.包含头文件
`#include <fstream>`

2.创建流对象
`ofstream ofs；`

3.打开文件
`ofs.open（"文件路径”, 打开方式）；`

4.写数据
`ofs<<“写入的数据"；`

5.关闭文件
`ofs.close()；`

```c++
#include<iostream>
#include<fstream>
using namespace std;
void test01() {
       // 1. 包含头文件
       // 2. 创建流对象
       ofstream ofs;
       // 3. 指定打开方式
       ofs.open("test.txt", ios::out);
       // 4. 写内容
       ofs << "这是一个测试文件" << endl;
       ofs << "用来测试一下这个文件是否有写入成功" << endl;
       ofs << "如果写成功了, 你就会看见这几行字" << endl;
       ofs << "好运~ " << endl;
       // 5. 关闭文件
       ofs.close();
}
int main() {
       test01();
       cout << "写入成功!" << endl;
       return 0;
}
```

## 读文本文件

读文件步骤如下：

1. 包含头文件
`#include<fstream>`

2. 创建流对象
`ifstream ifs；`

3. 打开文件并判断文件是否打开成功
`ifs.open（“文件路径”, 打开方式）;`

4. 读数据
四种方式读取

5. 关闭文件
`ifs.close()；`

```c++

#include<iostream>
#include<fstream>
#include<string>
using namespace std;
void test01() {
       // 1. 包含头文件
       // 2. 创建流对象
       ifstream ifs;
       // 3. 打开文件并且判断是否打开成功了
       ifs.open("test.txt", ios::in);
       // 4. 读数据
       if (!ifs.is_open()) {
              cout << "文件打开失败!" << endl;
              return;
       }
       //第一种读取方式:
       char buf[1024] = {0};
       while (ifs >> buf)
       {
              cout << buf << endl;
       }
       //第二种读取方式
       char buf[1024] = {0};
       while ( ifs.getline(buf, sizeof(buf)) )
       {
              cout << buf << endl;
       }
       //第三种读取方式
       string buf;
       while (getline(ifs, buf)){  // 注意包含头文件 string
              cout << buf << endl;
       }
       //第四种(不推荐用)
       char c;
       while ( (c = ifs.get()) != EOF) {
              cout << c << endl;
       }
       // 5. 关闭文件
       ifs.close();
}
int main() {
       test01();
       cout << "文件打开成功!" << endl;
       return 0;
}
```

在对文件进行写入的时候, 对于字符串文件最好用 char 字符串的方式来定义,  因为用C++内置的 string 类型有时候会出现一些错误

## 写二进制文件

用二进制文件来写数据可以写入一些自定义数据类型

```c++
class Person {
public:
       char m_Name[60];
       int m_Age;
};
void test01() {
       Person p = {"zhangsan", 18};
       ofstream ofs;
       ofs.open("person.txt", ios::out | ios::binary);
       ofs.write((const char*)&p, sizeof(Person));
       ofs.close();
}

```

## 读二进制文件

```c++
class Person {
public:
       char m_Name[60];
       int m_Age;
};
void test01() {
       ifstream ifs;
       ifs.open("person.txt", ios::in | ios::binary);
       if (!(ifs.is_open())) {
              cout << "文件打开失败!! " << endl;
              return;
       }
       Person p;
       ifs.read( (char*)&p, sizeof(Person));
       cout << "姓名 = " << p.m_Name << endl << "年龄 = " << p.m_Age << endl;
       ifs.close();
}
```