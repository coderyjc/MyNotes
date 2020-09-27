

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


