## IDEA的乱码问题

1. 更改File Encoding

   在Setting中搜索FileEncodings

![image-20210303075900840](R:\GITHUB\MyNotes\_Typora\Java_Web\_Docs\一些bug和解决方法.imgs\image-20210303075900840.png)

2. 修改虚拟机参数vmoptions

   修改这两个文件，在文件末尾的追加 `-Dfile.encoding=UTF-8`

<img src="R:\GITHUB\MyNotes\_Typora\Java_Web\_Docs\一些bug和解决方法.imgs\image-20210303080042805.png" alt="image-20210303080042805" style="zoom:80%;" />

3. 添加运行配置中的虚拟机参数

<img src="R:\GITHUB\MyNotes\_Typora\Java_Web\_Docs\一些bug和解决方法.imgs\image-20210303080406433.png" alt="image-20210303080406433" style="zoom:67%;" />

