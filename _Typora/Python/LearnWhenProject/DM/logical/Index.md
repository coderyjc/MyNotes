```python
qdarkstyle = abspath(dirname(abspath(__file__)) + "/..") + "/qrcs/qdarkstyle"

#语法
os.path.abspath(path)
#作用
#返回绝对路径
print(os.path.abspath("."))   #当前目录的绝对路径

#语法
os.path.dirname(path)
#作用
#去掉文件名，返回文件目录
print(os.path.dirname('W:\Python_File,py')) #结果  W:\
```

```python
sys.path.insert(0, ui)
#注：sys.path模块是动态的修改系统路径
""""
动态地在python的搜索路径中添加了一个"目录"，前提是此目录存在而且此前不在sys.path中。

sys.path是个列表，所以在末尾添加目录是很容易的，用sys.path.append就行了。当这个append执行完之后，新目录即时起效，以后的每次import操作都可能会检查这个目录。

也可以选择用sys.path.insert() 这样新添加的目录会优先于其他目录被import检查。

返回1表示成功，-1表示new_path不存在，0表示已经在sys.path中了

程序向sys.path添加的目录只会在此程序的生命周期之内有效，其他所有的对sys.path的动态操作也是如此。
重复添加目录不会出什么错，但是会耗费一定的系统资源，所以最好不这样。

"""
```

