### 2021.12.24

在读题和做题的时候一定要分清哪个数是什么类型的！！！！！（PTA-batsic-1088）


[[数据读取]]方面

- 多参数输入的情况下，使用cin可能会超时，这时候建议改成scanf（PTA-Basic-1066）


**C++[[位运算]]**

|符号|作用|
|----|----|
| & | 与|
| \| | 或 |
| ^ | 异或|
| ~ | 取反 |


**使用 bits/stdc++ 步骤**

1. 在 `VS2022\VC\Tools\MSVC\14.30.30705\include` 中新建文件夹 `bits`
2. 文件夹中新建文件 `stdc++.h`
3. 写入以下内容
4. 保存，完成

```c++
//c
#ifndef _GLIBCXX_NO_ASSERT
#include<cassert>
#endif
#include<cctype>
#include<cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
 
#if __cplusplus >= 201103L
#include <ccomplex>
#include <cfenv>
#include <cinttypes>
#include <cstdalign>
#include <cstdbool>
#include <cstdint>
#include <ctgmath>
#include <cwchar>
#include <cwctype>
#endif
 
// C++
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
 
#if __cplusplus >= 201103L
#include <array>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#endif
```




### 2021.12.23

1059题是看的大佬的题解，和我的思路完全相反，但是非常优秀。

让VS2022忽略scanf_s的相关提示：

在文件的开头加上 以下内容

```c++
#pragma warning(disable:4996)
```



### 2021.12.22

algorithm中sort函数的使用：

**默认升序**

```c++
  // int
    sort(a+1,a+9);    //可以指定任意合法的排序区间，不能越界

  // char
    sort(b,b+8);     //对整个b排序

	// vector<double>
    sort(v1.begin(),v1.end());

	// vector<string>
    sort(v2.begin(),v2.end());

//// 默认升序，降序要reverse一下

reverse(a+1,a+9); // int, char
reverse(v.begin(), v.end()); // vector<T>
```

**测试用例**

> 有一个坑点，输入本身是6174，应该输出7641 - 1467 = 6174，因此必须用do while循环，如果用while循环，此处直接就输出了，有一个case错误！
>
> ——**进行测试的时候的时候，先从题目中找敏感数字，特殊数字。**

[[格式化输入输出]]问题

C++中，cin不会读取空行，getline可以读取空行，因此如果题目中有空行的话，用getline

```c++
#include <string>
string str;
getline(cin, str);
```

### 2021.12.21

数组整体赋值：

> 使用方法：memset函数按字节对内存块进行初始化，所以不能用它将int数组初始化为0和-1之外的其他值（除非该值高字节和低字节相同）。

 ```c++
 #include<cstring>
 
 //（1）赋值为-1
 // 等价的，都是给q数组赋值-1.
 memset(q,-1,sizeof(q));
 memset(q,255,sizeof(q));
 memset(q,0xff,sizeof(q));
 
 
 //（2）赋值为0
 memset(q,0,sizeof(q))
 ```

### 2021.12.20

起初以为是负数的问题，结果是因为没有看明白题目要求，没有输出零多项式的情况。

读取不定长[[字符串相关]]的方法stringstream

```c
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {

	string line;
	getline(cin, line);
	stringstream ss(line);
	
	int up, down;
	
	while(ss >> down >> up){
		cout<< down << " " << up << endl;
	}

	return 0;

```
