## ERRORS



## WARNINGS





Typo: In word 'qdarkstyle' 

<img src="ERRORs.assets\image-20201024122507562.png" alt="image-20201024122507562" style="zoom:50%;" />


- 变量命名方式不规范
- 变量命名方式改为驼峰命名法即可





PEP8：E402 module level import not at top of file

<img src="ERRORs.assets\image-20201024122602333.png" alt="image-20201024122602333" style="zoom:50%;" />

- import不在文件的最上面，可能引用之前还有代码
- 把import引用放到文件的最上部就可以消除警告了。



```
PEP 8: module level import not at top of file
解决：import不在文件的最上面，可能引用之前还有代码，把import引用放到文件的最上部就可以消除警告了。
PEP 8: expected 2 blank lines，found 0
解决：期望上面有2个空白行，发现0个，添加两个空白行就可以了。
function name should be lowercase
解决：函数名改成小写。
PEP 8: indentation contains tabs 或者 Inconsistent use of tabs and spaces in indentation
解决：缩进中有tab空格，推荐用四个空格缩进。
Indent expected
解决：意思是没有缩进，解析器报错了，添加缩进就可以了。
Unexpected indent
解决：不期望的缩进，重新添加符合规范的缩进或者Alt+Enter快捷键会提示你转化成规范的缩进。
PEP 8: missing whitespace around operator
解决：意思是操作符（‘=’，‘<’等）前后丢失了空格，举个例子a=b会报警告，a = b正常。
PEP 8: no newline at end of file
解决：文件尾部没有新起一行，光标移到最后回车即可。
PEP 8: blank line at end of file
解决：文件最后多了一个空白行，只要有一个即可，删掉一个。
Shadows name ‘xxx’ from outer scope
解决：意思是‘xxx’在外部已经定义了，修改一下‘xxx’-> ‘uuu’或者其他符合要求的修改都可。
PEP 8: block comment should start with ‘# ’
解决：说的很清楚要以#加一个空格开始
PEP 8: inline comment should start with ‘# ’
解决：注释信息单独放一行
PEP 8: multiple statements on one line (colon)
解决：多行语句写到一行了，Python3.0好像不允许写到一行了，例如if x == 2: print(something)这样写就会有警告，必须要分两行。像下面这样
if x == 2:
print(something)
Symplify chained comparision
解决：警告的意思是可简化连锁比较，下面举个例子
if a > 0 and a < 9 可修改为 if
```

---

non-UTF-8 Code Starting With '\xc8' in File xxxx.py

解决办法：在文件第一行，加上下面的代码：

```python
# -!- coding: utf-8 -!-
```

---

