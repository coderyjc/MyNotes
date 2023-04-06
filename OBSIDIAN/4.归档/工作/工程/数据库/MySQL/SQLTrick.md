### 根据身份证号设置性别

```sql
update tbl_written_score set gender = 1 where substr(identification_id, 17, 1) % 2 = 1;  
  
update tbl_written_score set gender = 0 where substr(identification_id, 17, 1) % 2 = 0;
```

也可以写`gender = '男'`什么的

