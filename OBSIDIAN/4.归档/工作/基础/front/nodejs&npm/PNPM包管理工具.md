performant npm 高性能NPM

原来的工具（npm、cnpm、yarn等）存在的问题：
- 依赖重复下载
- 占用磁盘空间大
- 小文件非常多，难以删除


认知：硬连接和软连接

![[assets/Pasted image 20230227153604.png]]

## PNPM做了什么？

当使用 npm 或 Yarn 时，如果你有 100 个项目，并且所有项目都有一个相同的依赖包，那么， 你在硬盘上就需要保存 100 份该相同依赖包的副本。

如果是使用 pnpm，依赖包将被存放在一个**统一的位置**，因此：
- 如果你对同一依赖包使用相同的版本，那么磁盘上只有这个依赖包的一份文件；
-  如果你对同一依赖包需要使用不同的版本，则仅有版本之间不同的文件会被存储起来；
-  所有文件都保存在硬盘上的统一的位置：
- 当安装软件包时，其包含的所有文件都会硬链接到此位置，而不会占用额外的硬盘空间；这让你可以在项目之间方便地共享相同版本的依赖包；

![[assets/Pasted image 20230227153750.png]]

## 创建非扁平的node_modules目录

其结果是，源码可以访问 本不属于当前项目所设定的依赖包。

当使用 npm 或 Yarn Classic 安装依赖包时，所有软件包都将被提升到 node_modules 的 根目录下。

![[assets/Pasted image 20230227153834.png]]

安装pnpm

```bash
npm install -g pnpm
```

![[assets/Pasted image 20230227154845.png]]

更多命令和用法可以参考pnpm的官网 https://pnpm.io/zh/

## store存储位置

在pnpm7.0之前，统一的存储位置是 ~/.pnpm-score中的；

在pnpm7.0之后，统一的存储位置进行了更改：`<pnpm home directory>/store`

在 Linux 上，默认是 ~/.local/share/pnpm/store
在 Windows 上： %LOCALAPPDATA%/pnpm/store
在 macOS 上： ~/Library/pnpm/store

我们可以通过一些终端命令获取这个目录：获取当前活跃的store目录

```bash
pnpm store path
```

另外一个非常重要的store命令是prune（修剪）：从store中删除当前未被引用的包来释放store的空间

```bash
pnpm store prune
```

