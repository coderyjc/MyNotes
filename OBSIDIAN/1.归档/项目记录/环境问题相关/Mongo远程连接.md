## 通过 navicat连接docker中的mongo

连接之后发现

![[../前端项目总结/03.50Projects50Days/assets/Pasted image 20220623143453.png]]



```bash
#  这步开始刚刚安装好mongodb,没有进行什么操作
use admin

# 创建管理员账户（不能创建数据库）
db.createUser({ user: "admin", pwd: "123456", roles: [{ role: "userAdminAnyDatabase", db: "admin" }] })

# 创建超级管理员（可以创建数据库）
db.createUser({user:"root",pwd:"123456",roles:[{role: 'root', db: 'admin'}]})

# 创建test数据库
use test;

# 查看是否有test数据库，结果是没有的
show dbs

# 需要往里面添加数据，test才会生成
db.createCollection("list")

# 查看是否有test数据库，结果是有的
show dbs
```

![[../前端项目总结/03.50Projects50Days/assets/Pasted image 20220623144750.png]]


```bash
# 进入 test
use test;

# 创建test数据库的管理员
db.createUser({user: "dreamer", pwd: "sleep", roles:["dbOwner"]})

# 此时就可以连接成功
```

![[../前端项目总结/03.50Projects50Days/assets/Pasted image 20220623144831.png]]