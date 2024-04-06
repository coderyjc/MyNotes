---
create_date: 2024-01-27 09:45
tags:
  - Annaconda
  - Miniconda
  - Miniconda/环境配置
---

# 准备环境

使用了Miniconda而不是Annaconda

```ad-info
title: Miniconda比Annaconda的优势在哪

Anaconda 是一个开源的 Python 发行版本，而 Miniconda 则是 Anaconda 的一个子集。它们之间的关系是，Anaconda 包含了 Python 解释器以及一大堆常用的数据科学包，而 Miniconda 只包含了 Python 解释器和 Conda 包管理工具。因此，Miniconda 与 Anaconda 相比更加轻量级。

优势在于：精简性、灵活性、自定义环境、更新和维护。
```

## Windows环境

直接在官网 [https://docs.conda.io/projects/miniconda/en/latest/](https://docs.conda.io/projects/miniconda/en/latest/) 下载安装即可。

安装完成之后需要配置，配置环境变量PATH和镜像源在[[Annaconda安装以及镜像源配置#配置Annaconda环境变量]]

## Linux环境

首先要做的是将 **Miniconda3** 下载到系统中。

```shell
cd ~/Downloads
wget https://repo.anaconda.com/miniconda/...
```

其中 wget 命令后的 URL 是 miniconda3 网页的 URL。对于 64 位 Linux 系统，编写本书时的 URL 是

```shell
https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

下载 miniconda3 后，可以运行以下命令：

```shell
sh Miniconda3-latest-Linux-x86_64.sh
```

接下来，请阅读并按照屏幕上的说明操作。如果安装正确，你应该可以通过在终端输入 conda init 来启动 conda 环境。我们将创建一个在本书中一直使用的 conda 环境。要创建 conda 环境，可以输入：

```shell
conda create -n environment_name python=3.7.6
```

此命令将创建名为 environment_name 的 conda 环境，可以使用：

```shell
conda activate environment_name
```

现在我们的环境已经搭建完毕。是时候安装一些我们会用到的软件包了。在 conda 环境中，安装软件包有两种不同的方式。 你可以从 conda 仓库或 PyPi 官方仓库安装软件包。

```shell
conda/pip install package_name
```

注意：某些软件包可能无法在 conda 软件仓库中找到。因此，在本书中，使用 pip 安装是最可取的方法。我已经创建了一个编写本书时使用的软件包列表，保存在 environment.yml 中。 你可以在我的 GitHub 仓库中的额外资料中找到它。你可以使用以下命令创建环境：

```shell
conda env create -f environment.yml
```

该命令将创建一个名为 ml 的环境。要激活该环境并开始使用，应运行：

```shell
conda activate ml
```

现在我们已经准备就绪，可以进行一些应用机器学习的工作了！在使用本书进行编码时，请始终记住要在 "ml "环境下进行。现在，让我们开始学习真正的第一章。
