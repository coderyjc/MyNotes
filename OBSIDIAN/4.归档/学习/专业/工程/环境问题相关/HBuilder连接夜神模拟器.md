### 基础连接

设置

![[assets/Pasted image 20220429152732.png]]

![[assets/Pasted image 20220429152837.png]]

```
nox_adb connect 127.0.0.1:62001  
```

![[assets/Pasted image 20220429154304.png]]

### 由于目标计算机积极拒绝，无法连接

原因:
1. adb和nox_adb的版本不一致
2. 


1.  进入进Android SDK下的platform-tools目录

2.  将adb.exe拷贝至夜神bin目录下，粘贴两个，一个改成nox_adb.exe，把原来的nox_adb.exe删掉。

配置环境变量, 将夜神模拟器的bin目录添加到path目录下面

V:\IDE\Android-SDK\android-sdk-windows\platform-tools 添加到path目录下面

