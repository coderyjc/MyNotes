# HadoopROOT安装







升级命令与安装vim编辑器

```shell
sudo apt-get update
sudo apt install vim
```

直接拿到root权限

```shell
sudo su
```

配置ssh，中间按3次回车

```shell
ssh-keygen -t rsa
```

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\Hadoop.imgs\image-20210323152137207.png" alt="image-20210323152137207" style="zoom: 67%;" />



确认SSH生成完毕, 第二行是两个小写字母 L

```shell
cd ~/.ssh 
ll
```

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\Hadoop.imgs\image-20210323152330890.png" alt="image-20210323152330890" style="zoom:67%;" />



创建一个空文本，名为authorized_keys，将存储公钥文件的id_rsa.pub里的内容，追加到authorized_keys中

```shell
touch ~/.ssh/authorized_keys 
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 
```

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\Hadoop.imgs\image-20210323152636538.png" alt="image-20210323152636538" style="zoom:67%;" />

安装服务并测试ssh，然后退出


```shell
apt-get install openssh-server
ssh localhost
exit
```

中间要输入一次yes

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323153036605.png" alt="image-20210323153036605" style="zoom:67%;" />

创建目录存放数据

```shell
mkdir /apps
mkdir /data
```



下载jdk和hadoop，地址默认在 /home/用户名/Downloads

解压这两个文件到/apps下面

```shell
tar -xzvf /home/hadoop/Downloads/jdk-8u281-linux-x64.tar.gz -C /apps/
tar -xzvf /home/hadoop/Downloads/hadoop-3.2.2.tar.gz -C /apps/
```

重命名这两个文件

```shell
mv /apps/jdk1.8.0_281/ /apps/java 
mv /apps/hadoop-3.2.2/ /apps/hadoop
```

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323154634188.png" alt="image-20210323154634188" style="zoom:67%;" />

配置jdk环境变量

```shell
sudo vim ~/.bashrc
```

将以下内容写入：

```bash
#java  
export JAVA_HOME=/apps/java  
export PATH=$JAVA_HOME/bin:$PATH 
```

使其生效，并测试java

```shell
source ~/.bashrc 
java -version
```

出现以下内容表示成功

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323155326656.png" alt="image-20210323155326656" style="zoom:67%;" />



配置hadoop环境变量


```shell
sudo vim ~/.bashrc
```

将以下内容写入：

```shell
#hadoop  
export HADOOP_HOME=/apps/hadoop 
export PATH=$HADOOP_HOME/bin:$PATH 
```

使其生效，并测试hadoop

```shell
source ~/.bashrc 
hadoop version
```

出现以下内容表示成功

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323155555660.png" alt="image-20210323155555660" style="zoom:67%;" />

修改hadoop本身相关的配置。


```shell
cd /apps/hadoop/etc/hadoop
vim /apps/hadoop/etc/hadoop/hadoop-env.sh
```

追加以下内容：


```bash
export JAVA_HOME=/apps/java
```

修改core-site.xml配置文件


```shell
vim /apps/hadoop/etc/hadoop/core-site.xml
```

添加下面配置到< configuration >与< /configuration >标签之间


```xml
  <property>  
      <name>hadoop.tmp.dir</name>  
      <value>/data/tmp/hadoop/tmp</value>  
  </property>  
  <property>  
      <name>fs.defaultFS</name>  
      <value>hdfs://localhost:9000</value>  
  </property>  
```

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323160526294.png" alt="image-20210323160526294" style="zoom:67%;" />

创建文件夹


```shell
mkdir -p /data/tmp/hadoop/tmp
```

配置hdfs-site.xml配置文件


```shell
vim /apps/hadoop/etc/hadoop/hdfs-site.xml 
```

添加下面配置到< configuration >与< /configuration >标签之间


```xml
 <property>  
     <name>dfs.namenode.name.dir</name>  
     <value>/data/tmp/hadoop/hdfs/name</value>  
 </property>  
  <property>  
      <name>dfs.datanode.data.dir</name>  
      <value>/data/tmp/hadoop/hdfs/data</value>  
  </property>  
  <property>  
      <name>dfs.replication</name>  
      <value>1</value>  
  </property>  
  <property>  
      <name>dfs.permissions.enabled</name>  
      <value>false</value>  
  </property>  
```

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323160812688.png" alt="image-20210323160812688" style="zoom:67%;" />

创建文件夹


```shell
mkdir -p /data/tmp/hadoop/hdfs 
```

配置slavs文件

```shell
vim /apps/hadoop/etc/hadoop/slaves  
```

追加以下内容：

```text
localhost
```

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323160958848.png" alt="image-20210323160958848" style="zoom:67%;" />

格式化HDFS文件系统, 启动hdfs相关进程，并用查看

```shell
hadoop namenode -format  
cd /apps/hadoop/sbin/
./start-dfs.sh
```

<font style="color:red; font-size:30px">如果出现 ： ...but there is no HDFS_NAMENODE_USER defined... 错误</font>，则在`/apps/hadoop/etc/hadoop/hadoop-env.sh`追加以下内容。

```bash
export HDFS_NAMENODE_USER=root
export HDFS_DATANODE_USER=root
export HDFS_SECONDARYNAMENODE_USER=root
export YARN_RESOURCEMANAGER_USER=root
export YARN_NODEMANAGER_USER=root
```

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323161513964.png" alt="image-20210323161513964" style="zoom:67%;" />

<font style="color:red; font-size:30px">如果没出错</font>，就直接执行下面这一句

```
jps
```

出现以下内容表示成功：

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323161725862.png" alt="image-20210323161725862" style="zoom:67%;" />



配置mapred-site.xml

```shell
vim /apps/hadoop/etc/hadoop/mapred-site.xml
```

将mapreduce相关配置，添加到< configuration >标签之间

```xml
  <property>  
      <name>mapreduce.framework.name</name>  
      <value>yarn</value>  
  </property> 
```

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323162647797.png" alt="image-20210323162647797" style="zoom:67%;" />

配置yarn-size.xml

```shell
vim /apps/hadoop/etc/hadoop/yarn-site.xml
```

将yarn相关配置，添加到< configuration >标签之间

```xml
 <property>  
     <name>yarn.nodemanager.aux-services</name>  
     <value>mapreduce_shuffle</value>  
 </property>
```

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323162730535.png" alt="image-20210323162730535" style="zoom:67%;" />

启动进程,并查看

```shell
cd /apps/hadoop/sbin/
./start-yarn.sh
jps
```

出现以下内容表示成功

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323162819886.png" alt="image-20210323162819886" style="zoom:67%;" />

hadoop计算测试：

切换目录，跑一个测试程序

```shell
cd /apps/hadoop/share/hadoop/mapreduce  
hadoop jar hadoop-mapreduce-examples-3.2.2.jar pi 3 3
```

<img src="R:\GITHUB\MyNotes\_Typora\BigData\Hadoop\ROOT安装.imgs\image-20210323165644018.png" alt="image-20210323165644018" style="zoom:67%;" />

成功。

---

如果在最后一步出错，则：

在命令行执行，复制信息。

```shell
hadoop classpath
```

编辑yarn-site.xml，添加信息：

```xml
<configuration>
  <property>
    <name>yarn.application.classpath</name>
    <value>复制的Hadoop classpath信息</value>
  </property>
</configuration>
```

在所有的Master和Slave节点进行如上设置，设置完毕后重启Hadoop集群，重新运行刚才的MapReduce程序，成功运行。