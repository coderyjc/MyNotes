## DBA命令（了解）

在数据库当中的数据导出

在windows的DOS命令窗口中执行： (导出整个库)

- mysqldump bjpowernode>D:\bjpowernode.sql -uroot -p999

在windows的dos命令窗口中执行：(导出数据库中指定的表)

- mysqldump bjpowernode emp>D:\bjpowernode.sql -uroot -p999

导入数据

- create database bjpowernode;
- use bjpowernode;
- source D:\bjpowernode.sql