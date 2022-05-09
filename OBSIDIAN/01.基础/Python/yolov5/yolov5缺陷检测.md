# yolov5缺陷检测

#深度学习

> https://www.bilibili.com/video/BV1yv411p7kv

步骤：

1. 下载数据集和yolo框架

   > 数据集 http://faculty.neu.edu.cn/yunhyan/NEU_surface_defect_database.html
   >
   > 框架 https://github.com/ultralytics/yolov5

2. 规整目录结构


3. 将数据标签转换为yolo所需要的格式

   ```python
   # -!- coding: utf-8 -!-
   
   """
   @Author: Jingcun Yan
   @Date: 2021/8/10
   @Time: 上午9:10
   @Description: 
   """
   
   import xml.etree.ElementTree as ET
   from os import getcwd
   import glob
   
   classes = ['crazing', 'inclusion', 'patches', 'pitted_surface', 'rolled-in_scale', 'scratches']
   
   
   def convert(size, box):
       dw = 1. / size[0]
       dh = 1. / size[1]
       x = (box[0] + box[1]) / 2.0
       y = (box[2] + box[3]) / 2.0
       w = box[1] - box[0]
       h = box[3] - box[2]
       x = x * dw
       w = w * dw
       y = y * dh
       h = h * dh
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
                float(xmlbox.find('ymin').text))
           bb = convert((w, h), b)
           out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
   
   
   wd = getcwd()
   
   if __name__ == '__main__':
   
       for image_path in glob.glob('./IMAGES/*.jpg'):
           img_name = image_path.split('/')[-1]
           convert_annotation(img_name)
   ```

4. 使用 train.py 训练数据

   配置运行参数

   ```
   --data ../NEU-DET/data.yaml
   --cfg models/yolo5s.yaml
   --batch-size 8
   ```

   

