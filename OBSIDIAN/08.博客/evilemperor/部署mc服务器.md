

> 本文参考了  https://www.bilibili.com/read/cv16106328/ 作者：爷真可爱qwqwq 出处：bilibili 

## 客户端服务器搭建

下载 1.19.0 服务端文件, 并上传到服务器

地址:  https://bmclapi2.bangbang93.com/version/1.19/server

> 注意: MC1.19.0需要Java版本>= 17.0.3, 版本过低会导致运行失败

```bash
➜  mc java -Xms1G -Xmx2G -jar server.jar
```

运行之后命令行最后出现: 

```
[20:08:40] [ServerMain/INFO]: Building unoptimized datafixer
[20:08:41] [ServerMain/ERROR]: Failed to load properties from file: server.properties
[20:08:41] [ServerMain/WARN]: Failed to load eula.txt
[20:08:41] [ServerMain/INFO]: You need to agree to the EULA in order to run the server. Go to eula.txt for more info.
```

他告诉我们需要同意EULA来运行服务器

这时候的文件夹结构

```
➜  mc ll    
total 44M
-rw-rw-r-- 1 jancoyan jancoyan  158 Jul 19 20:08 eula.txt
drwxrwxr-x 8 jancoyan jancoyan 4.0K Jul 19 20:08 libraries
drwxrwxr-x 2 jancoyan jancoyan 4.0K Jul 19 20:08 logs
-rwxr-xr-x 1 www      www       44M Jul 19 18:55 server.jar
-rw-rw-r-- 1 jancoyan jancoyan 1.3K Jul 19 20:08 server.properties
drwxrwxr-x 3 jancoyan jancoyan 4.0K Jul 19 20:08 versions
```

编辑`Eula.txt` , 把里面的false改成true即可

改完之后的文件夹结构: 

```bash
  1 #By changing the setting below to TRUE you are indicating your agreement to our EULA (https://aka.ms/MinecraftEULA).
  2 #Tue Jul 19 20:08:41 CST 2022
  3 eula=true 
```

这时候再次运行java服务到后台

```bash
sudo nohup java -Xms1G -Xmx2G -jar server.jar > log.txt & 
```

如果你无法加入说明使用的不是正版，打开server.properties文件把online-mode改为false即可

![[Pasted image 20220719205849.png]]


这个时候的文件夹结构: 

```
total 44M
-rw-rw-r--  1 jancoyan jancoyan    2 Jul 19 20:52 banned-ips.json # 禁止加入的ip
-rw-rw-r--  1 jancoyan jancoyan    2 Jul 19 20:52 banned-players.json # 禁止加入的玩家
-rw-rw-r--  1 jancoyan jancoyan  157 Jul 19 20:14 eula.txt # 用户协议
drwxrwxr-x  8 jancoyan jancoyan 4.0K Jul 19 20:08 libraries
drwxrwxr-x  2 jancoyan jancoyan 4.0K Jul 19 20:52 logs # 日志文件
-rw-rw-r--  1 jancoyan jancoyan    0 Jul 19 20:20 log.txt # server启动的日志
-rw-rw-r--  1 jancoyan jancoyan    2 Jul 19 20:52 ops.json # 服务器管理员
-rwxr-xr-x  1 www      www       44M Jul 19 18:55 server.jar# 服务器程序
-rw-rw-r--  1 jancoyan jancoyan 1.3K Jul 19 20:52 server.properties # 服务器程序配置文件
-rw-rw-r--  1 jancoyan jancoyan  102 Jul 19 20:54 usercache.json # 缓存, 无意义
drwxrwxr-x  3 jancoyan jancoyan 4.0K Jul 19 20:08 versions
-rw-rw-r--  1 jancoyan jancoyan    2 Jul 19 20:15 whitelist.json # 白名单
drwxrwxr-x 12 jancoyan jancoyan 4.0K Jul 19 20:53 world # 世界
```

---

以下内容完全为引用 作者：爷真可爱qwqwq https://www.bilibili.com/read/cv16106328/ 出处：bilibili

服务器配置如下
```
#Minecraft server properties
#Sun Apr 10 15:32:09 CST 2022
spawn-protection=16 # 出生点保护 世界出生点一定范围内不可破坏或放置方块，设为0可以停用
max-tick-time=60000 # 一个tick跑多少ms以上之后会关闭服务器 不建议修改
query.port=25565
generator-settings= # 世界生成设置 一般没用
sync-chunk-writes=true # 启用同步区块写入 不建议修改
force-gamemode=false # 是否强制游戏模式，如果你想让整个服保持一个游戏模式可以设置为true
allow-nether=true # 是否启用下界 设为false则传送门不会生效
enforce-whitelist=false # 执行白名单 设置为true后会在reload白名单文件后踢出不在白名单里的在线玩家
gamemode=survival # 默认游戏模式，还可改为creative，adventure或spectator
broadcast-console-to-ops=true # 是否把在控制台使用的命令发给所有管理员
enable-query=false
player-idle-timeout=0 # 如果不是0，将会把挂机若干分钟的玩家踢出
text-filtering-config=
difficulty=easy # 游戏难度，还可改成peaceful，normal和hard
spawn-monsters=true # 是否生成怪物
broadcast-rcon-to-ops=true # 把远程控制的命令发送给所有在线管理员
op-permission-level=4 #默认管理员权限等级
pvp=true # 玩家互相伤害
entity-broadcast-range-percentage=100
snooper-enabled=true
level-type=default # 世界类型
hardcore=false # 极限 死去的玩家会自动被服务器ban掉
enable-status=true
enable-command-block=false # 是否启用命令方块
max-players=20 # 最大玩家数
network-compression-threshold=256
resource-pack-sha1= # 资源包的sha1哈希
max-world-size=29999984 # 最大世界大小（单位）取决于worldbounder位置，设置为1000允许玩家在2000*2000范围内
function-permission-level=2 # 数据包函数权限等级
rcon.port=25575 # 远程连接所用端口
server-port=25565 # 服务器绑定端口
server-ip=
spawn-npcs=true
allow-flight=false # 是否允许生存模式飞行
level-name=world # 世界名字
view-distance=10 # 视距 建议调大一点
resource-pack= # 资源包
spawn-animals=true # 是否生成动物
white-list=false # 是否开启白名单
rcon.password= # 远程控制的密码
generate-structures=true # 是否生成结构 如下界要塞等
max-build-height=256 # 最高建筑上限 修改了可能出现问题
online-mode=true # 是否启用正版验证 调为false允许非正版玩家进入 你进不了服务器的罪魁祸首（
level-seed= # 世界种子
use-native-transport=true
prevent-proxy-connections=false # 是否阻止玩家使用v*n或代理
enable-jmx-monitoring=false
enable-rcon=false # 启用远程控制
rate-limit=0
motd=A Minecraft Server # 服务器介绍，中文可能会乱码
```

最后可以在控制台里输入stop指令来停止服务器

请注意所有加入服务器的玩家都默认不为管理员（不能使用大部分指令），哪怕你是第一个进服的也一样

可以通过执行op 玩家名 的指令来让某位玩家成为管理员（拥有命令使用权）

控制台使用命令不需要打斜杠

平时需要用到的服务器指令：

```
令一位玩家成为管理员			op <player name>
剥夺玩家的管理员身份			deop <player name>
显示所有的管理员				ops
停止/关不服务器				stop
重新加载（配方和数据包		reload
将服务器存至硬盘				save-all
启用自动保存					save-on
禁用自动保存					save-off
踢出玩家						kick <player name>
禁止玩家进入服务器			ban <player name>
禁止玩家的ip加入服务器		ban-ip <player name>
解除玩家的封禁				pardon <player name>
解除玩家的ip的封禁			pardon-ip <player name>
```

