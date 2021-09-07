# YOLOv5s的模型训练与使用(纯小白入门)

[TOC]

## 概要

本文主要面向第一次使用yolov5，连参数都不会配置的纯小白，记录了我自己初次使用的过程。

从下载yolov5，安装依赖，到训练模型和进行识别。

## 下载yolov5与安装依赖

git方式：

`git clone https://github.com/ultralytics/yolov5.git `

从github直接下载zip并解压：

[https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)

使用pycharm直接把这个文件夹作为项目打开。

首次使用我们要使用两个文件，以后会接触其他文件：

- train.py 是我们进行训练的脚本
- detect.py 是进行检测的脚本

此时，`import torch` 会划线并报错，因为我的环境中并没有pytorch

安装 pytorch：

我是用的 Annaconda 3 (Python 3.8) 环境，自带了conda.exe 命令，所以用了如下命令

`conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch`

其他环境的安装方式参考pytorch官网：

[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

安装完毕之后，pycharm上的红线就没了，也就是说可以运行了。

> 按道理说这时候应该可以了，但是我出现了 “wandb 未注册异常” ： `wandb.errors.UsageError: api_key not configured (no-tty). call wandb.login(key=[your_api_key])` 
>
> 详情见踩坑记录

但是pycharm提示说有一些库没有安装，要自己装上

**没有安装的这些库最好用pip安装，pip安装的一般是最新的，我用的conda清华的镜像，下载之后报错 opencv-python>=4.1.2 not found ，conda下载的这个是旧版本的，我又用的pip下载，成功下载了最新版。**

`pip install opencv-python`	

没有的依赖以此类推，进行安装。

## 训练

我使用的是东北大学的钢材表面缺陷数据集，这几天外网进不去了，但是度盘可以：链接：https://pan.baidu.com/s/1NaSVKLEiM_XUHRAToWR38Q 提取码：tdrd 

训练数据要配置运行参数和进行数据集的规整，这里我们先从运行参数入手：

![image-20210903202804184](yolov5s模型的模型训练与使用(纯小白入门).imgs/image-20210903202804184.png)

这里我们配置了三个参数：

data: 数据配置文件的路径，在这个文件里我们要指定样本集和验证集数据的相关路径等东西，程序会从中获取数据集的路径

cfg: 模型配置文件的路径，这个不需要我们配置，这里不再展开

- 本次使用的是yolov5s模型，不同的模型有什么区别？
- s：small 小型的；l：large 大型的；x：extra large加大的
- 不同的模型的层数大小不同，生成的模型文件的大小不同，

batch-size : 每一次训练所选取的样本数，视情况而定

在 data.yaml 中我配置如下：

```yaml
train: ../NEU-DET/train/images
val: ../NEU-DET/valid/images

nc: 6 
names: ['crazing', 'inclusion', 'patches', 'pitted_surface', 'roll-in_scale', 'scratches']
```

从中可以看出，我的训练集和验证集相对于这个项目的根目录的路径、类别的数量和每一类的标签名称。这个名称和我们训练集、验证集的图像的前缀是一样的。

![image-20210903203941283](yolov5s模型的模型训练与使用(纯小白入门).imgs/image-20210903203941283.png)

我们配置了image目录，程序会自动在同级目录下寻找labels目录，从中读取标签。

这样我们的目录就配置完成了。

下面向里面复制数据。

image中存放图像数据，labels中存放候选框的方位，每一个图片对应一个同名标签（图片和标签只是后缀不一样，名字是一样的）

但是我们下载下来的文件中有一个annotations文件夹（存放标签），和一个images文件夹（存放图片数据）标签数据，标签数据是xml，我们需要转化成txt，在annotation同级目录下创建LABELS，并把下面这个脚本放在annotation同级目录下执行，即可转化标签为txt格式：

```python
# 来源：https://www.bilibili.com/video/BV1Bv411H7ER?p=5

import xml.etree.ElementTree as ET
from os import getcwd
import glob

classes = ['crazing', 'inclusion', 'patches', 'pitted_surface', 'rolled-in_scale', 'scratches']


def convert(size, box):
    delta_w = 1. / size[0]
    delta_h = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * delta_w
    w = w * delta_w
    y = y * delta_h
    h = h * delta_h
    return x, y, w, h


def convert_annotation(image_name):
    in_file = open('./ANNOTATIONS/' + image_name[:-3] + 'xml')
    out_file = open('./LABELS/' + image_name[:-3] + 'txt', 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            print(cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()

if __name__ == '__main__':
    for image_path in glob.glob('./ANNOTATIONS/*.xml'):
#       获取文件名
        image_name = image_path.split('\\')[-1]
# 		转换
		convert_annotation(image_name)

```

在图片中选取一部分作为验证集，放在 NEU-DET/valid/images中，同时把对应的标签放在NEU-DET/valid/labels中，其他的放在NEU-DET/train 中对应的 images和labels中。

这样我们的数据就做好了。目录总览：

![image-20210903210352315](yolov5s模型的模型训练与使用(纯小白入门).imgs/image-20210903210352315.png)

运行一下，如下说明成功：

![image-20210903205904997](yolov5s模型的模型训练与使用(纯小白入门).imgs/image-20210903205904997.png)

看白色字体：本次的日志保存在了runs\train\exp10文件夹

进入这个文件夹：

![image-20210903210206128](yolov5s模型的模型训练与使用(纯小白入门).imgs/image-20210903210206128.png)

weight中存放的是训练好的模型数据，一个是最好的(best.pt)，一个是最近的(last.pt)，我们在进行检测的时候会用到。

## 检测

### 检测图片

执行脚本detect.py 下面的运行参数：

```
--source ../NEU-DET/valid/images/scratches_1.jpg # 目标文件路径 
--weights ./runs/train/exp/weights/best.pt # 这个是权重文件，也就是我们训练的时候生成的
--conf 0.3 # 置信度
--output ../NEU-DET/output # 这个文件夹需要事先创建
--view-img # 识别的时候实时显示画面
```

直接运行即可

### 检测视频

执行脚本dectect.py 下面是运行参数

```
--source 0 # 0 代表本机摄像头
--weights ./runs/train/exp/weights/best.pt # 这个是权重文件，也就是我们训练的时候生成的
--conf 0.3 # 置信度
--view-img # 识别的时候实时显示画面
```

直接运行即可。



