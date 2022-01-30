---
type: DeBug
skill: MySQL
create_date: 2022-01-31
---

#数据库 #Debug 

# MySQL Debug

>MySQL创建触发器的时候报1419错误( 1419 - You do not have the SUPER privilege and binary logging is enabled )

解决方法：

第一步，用root用户登录：mysql -u root -p

第二步，设置参数log_bin_trust_function_creators为1：

```sql
set global log_bin_trust_function_creators = 1;
```

![[Pasted image 20220131010332.png]]

成功

![[Pasted image 20220131010344.png]]

宝塔Linux会把数据库root用户的密码给改了，登录的时候要在

![[Pasted image 20220131010359.png]]

>[21S01][1136] Column count doesn't match value count at row 1

在执行插入的时候会执行触发器中的内容

这个报错可能不是原有插入语句中的错误，

可能是触发器中有错误。

导出数据库中的表名和字段名为表格

```sql
SELECT
    COLUMN_NAME 列名,
    COLUMN_TYPE 数据类型,
    DATA_TYPE 字段类型,
    CHARACTER_MAXIMUM_LENGTH 长度,
    IS_NULLABLE 是否为空,
    COLUMN_DEFAULT 默认值,
    COLUMN_COMMENT 备注
FROM
    INFORMATION_SCHEMA.COLUMNS
where
-- jancoblog，到时候只需要修改成你要导出表结构的数据库即可
        table_schema ='jancoblog'
  AND
-- tbl_article为表名，到时候换成你要导出的表的名称
-- 如果不写的话，默认会查询出所有表中的数据，这样可能就分不清到底哪些字段是哪张表中的了，所以还是建议写上要导出的名名称
        table_name  = 'tbl_article'
```

即可生成数据表格：

![[Pasted image 20220131010429.png]]

