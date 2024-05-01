---
alias: PyTorch安装与配置
tags: 
- Python/Annaconda
- Python/PyTorch
---


### 安装CUDA

使用命令 `nvidia-smi` 查看显卡信息

```text
(d2l) C:\Users\Administrator>nvidia-smi
Tue Apr 30 22:50:40 2024
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 531.61                 Driver Version: 531.61       CUDA Version: 12.1     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                      TCC/WDDM | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf            Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce GTX 1050       WDDM | 00000000:01:00.0  On |                  N/A |
| N/A   40C    P8               N/A /  N/A|    116MiB /  3072MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
+---------------------------------------------------------------------------------------+
```

上面显示了 CUDA Version: 12.1 ，因此我需要安装版本小于等于12.1的cuda

我安装了12.1： https://developer.nvidia.com/cuda-12-1-0-download-archive

### 安装PyTorch

《动手学深度学习》 https://zh-v2.d2l.ai/ 书中的安装部分给出的pytorch安装方式默认是CPU版本的。

以下是CPU版本的：

```bash
pip install torch==1.12.0
pip install torchvision==0.13.0
```

GPU版本需要自己指定，如下：

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

如果再次之前已经安装了cpu版本的，需要先卸载 `conda uninstall pytorch`

安装完成之后，使用如下代码判断是否成功

```sh
C:\Users\Administrator>conda activate d2l

(d2l) C:\Users\Administrator>python
Python 3.9.19 (main, Mar 21 2024, 17:21:27) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.__version__
'2.3.0'
>>> torch.cuda.is_available()
True
```

`torch.cuda.is_available()` 为True则安装成功。