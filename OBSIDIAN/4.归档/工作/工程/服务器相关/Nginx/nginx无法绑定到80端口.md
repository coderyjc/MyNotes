修改nginx.conf下的默认端口号

（1）用记事本打开nginx目录下的nginx.conf文件

（2）按键盘win+r,输入cmd,打开管理员界面，输入netstat -aon|findstr :预期端口号，查看自己的预期端口号是否被占用

（3）修改nginx.conf，后保存

![[assets/Pasted image 20230321095748.png]]

（4）在命令提示符下输入nginx -s reload即可（重要一步）

（5）然后命令提示符下输入start nginx

（6）在浏览器localhost:81，如果出现以下页面在修改成功

![[assets/Pasted image 20230321095842.png]]

