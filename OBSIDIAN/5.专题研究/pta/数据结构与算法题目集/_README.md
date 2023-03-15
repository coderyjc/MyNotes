
```ad-note
https://pintia.cn/problem-sets/15/exam/problems/type/6
```


[[7-1 最大子列和问题]]

[[7-3 树的同构]]

[[7-5 堆中的路径]]

[[7-6 列出连通集]]

[[7-7 六度空间]]

[[7-8 哈利·波特的考试]]

[[7-9 旅游规划]]

[[7-10 公路村村通]]

[[7-12 排序]]

[[7-17 汉诺塔的非递归实现]]

[[7-18 银行业务队列简单模拟]]

[[7-23 还原二叉树]]

[[7-25 朋友圈]]

[[7-26 Windows消息队列]]

7-47 打印选课学生名单

一开始写的，过不去最后一个，把大部分IO改成scanf和printf才过去。



7-49 打印学生选课清单

以下报错:

```json
[{
	"resource": "/f:/env/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++/bits/predefined_ops.h",
	"owner": "cpptools",
	"severity": 8,
	"message": "no match for 'operator==' (operand types are 'std::pair<const std::__cxx11::basic_string<char>, std::vector<int> >' and 'const std::__cxx11::basic_string<char>')",
	"source": "gcc",
	"startLineNumber": 241,
	"startColumn": 17,
	"endLineNumber": 241,
	"endColumn": 17
}]
```

说明编译器不知道如何比较两个vector的大小，因为我在代码中使用了`map<string, vector<int> >`

解决方案在这里 [[../../../4.归档/工作/基础/algorithm/STL/map#创建以string为键的map]]，但是后来发现这个无所谓，没有也可以，我这个错是因为别的错误。

```cpp
  for (int i = 0; i < n; i++){
    cin >> classId >> classStudent;
    for (int j = 0; j < classStudent; j++) {
    // 不用判断m[temp]是否存在，不存在他会自动创建的。
      cin >> temp;
      m[temp].push_back(classId);
    }
  }
```


[[7-52 两个有序链表序列的交集]]

