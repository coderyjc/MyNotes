

## ORACLE的安装

![image-20200922185157628](ORCL.assets\image-20200922185157628.png)

![image-20200922185409683](ORCL.assets\image-20200922185409683.png)

### 主目录下的文件体系及其用途

- admin：存放创建数据库的脚本。

- audit：审计记录，用于监视用户所执行的数据库操作。

- cfgtoollogs：分别存放当运行 dbca，dbua，emca，netca 等图形化配置程序时的 log。

- checkpoints：检查点目录。

- diag：所有组件需要被用来诊断的 log 文件都存放在这个目录下。

- oradata：存放数据文件。

- product：Oracle RDBMS 的软件存放目录。

### ORACLE安装后的相关服务

- OracleJobSchedulerORCL：Oracle 作业调度（定时器）服务，ORCL 是Oracle 实例标识。（非必须启动）

- OracleOraDB12Home1MTSRecoveryService：服务端控制。该服务允许数据库充当一个微软事务服务器 MTS、COM/COM+对象和分布式环境下的事务的资源管理器。（非必须启动）

- OracleOraDB12Home1TNSListener：监听器服务，服务只有在数据库需要远程访问的时候才需要。需要客户端连接数据库的时候必须启动（必须启动）。

- OracleRemExecServiceV2：只是被 OUI 暂时性的使用，当 OUI 完成它的工作后，该服务会被 remove 掉。因此，在 reboot 之前，该服务的值为disabled。

- OracleServiceORCL：数据库服务(数据库实例)，是 Oracle 核心服务，该服务是数据库启动的基础， 只有该服务启动，Oracle 数据库才能正常启动。(必须启动)

- OracleVssWriterORCL：Oracle卷映射拷贝写入服务，VSS（Volume ShadowCopy Service）能够让存储基础设备（比如磁盘，阵列等）创建高保真的时间点映像，即映射拷贝（shadow copy）。它可以在多卷或者单个卷上创建映射拷贝，同时不会影响到系统的系统能。（非必须启动）


## ORALCE体系结构

### 作业

#### 1.了解以下 Oracle 初始参数的含义

|初始参数|说明|
|--------|-----|
|sga_target|指定所有SGA组成部分的全部大小，该参数自动确定DB_CACHE_SIZE,SHARED_POOL_SIZE,LARGE_POOL_SIZE,STREAMS_POOL_SIZE和JAVA_POOL_SIZE|
|processes|可同时链接到Oracle的最大操作系统进程数量，SESSIONS 和 RTRANSACTIONS 从这个值中派生|
|db_domain|数据库驻留在分布式数据库系统中的逻辑域名（如 us.oracle.com）|
|db_name|最多8个字符的数据库标识符。放置在DB_DOMAIN值的前面，形成完全限定的名称（marketing.us.com）|
|db_block_size|指定Oracle块的大小。这种块大小用于创建数据库时的SYSTEM\SYSAUX和临时表空间|
|compatible|允许安装新的数据库版本，同时确保与该参数指定的版本兼容|
|db_recovery_file_dest|恢复区域的默认设置，必须和db_recovery_file_dest_size一起设置|
|db_recovery_file_dest_size|以字节为单位的文件最大尺寸，该文件用于在恢复区域位置的恢复|
|control_files|指定该实例的控制文件的位置|

#### 了解 Oracle 内置数据类型

![image-20200929225629938](ORCL.assets\image-20200929225629938.png)

![image-20200929225715792](ORCL.assets\image-20200929225715792.png)

![image-20200929225748644](ORCL.assets\image-20200929225748644.png)

![image-20200929225816503](ORCL.assets\image-20200929225816503.png)

## ORACLE基本操作

