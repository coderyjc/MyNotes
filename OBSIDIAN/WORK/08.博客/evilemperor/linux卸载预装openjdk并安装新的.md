**1.卸载openjdk**

```bash
sudo apt-get remove openjdk-11-jdk
```

**2.卸载jre**

```bash
sudo apt-get remove openjdk-11-jre-headless 
```

### 3.安装并配置java 环境

1).进入/usr/lib/目录创建jvm文件夹

```bash
sudo mkdir /usr/libjvm
```

2).解压jdk安装包到/usr/lib/jvm目录下

```bash
tar -xzvf jdk-17_linux-x64_bin.tar.gz -C /usr/lib/jvm
```

**3).配置环境变量**

**修改/etc/profile文件**

```bash
 sudo vim /etc/profile
```

在文件首部或末尾添加如下信息：

```bash
export JAVA_HOME=/usr/lib/jvm/jdk-17.0.3.1
export PATH=${JAVA_HOME}/bin:${PATH}
```

保存并退出。

**4).使Java环境生效**

```bash
source /etc/profile
```
