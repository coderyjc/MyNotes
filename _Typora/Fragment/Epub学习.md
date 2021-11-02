# Epub格式解析

Epub底层是zip压缩文件，把epub格式文件后缀名改为zip解压之后文件目录大致如下：

```
/images --书中的图片
/META-INF/container.xml -- 告诉阅读器，电子书的根文件（rootfile）的路径（红色部分）和打开放式
/text -- 文本
/content.opf -- epub电子书的核心文件，下面细说
/cover.jpeg  -- 封面
/mimetype -- 说明epub的文件格式
/page_style.css -- 打印属性
/stylesheet.css -- 浏览属性
/titlepage.xhtml -- 首页
/toc.ncx -- 文章目录
```



## /content.opf

1. < metadata >, 元数据信息，由两个子元素组成：
-  < dc-metadata >，其元素构成采用dubline core(DC)的15项核心元素，包括：
   - < title >:题名
   - < creator >：责任者
   - < subject >：主题词或关键词
   - < description >：内容描述
   - < contributor>：贡献者或其它次要责任者
   - < date>：日期
   - < type>：类型
   - < format>：格式
   - < identifier>：标识符
   - < source>：来源
   - < language>：语种
   - < relation>：相关信息
   - < coverage>：履盖范围
   - < rights>：权限描述

- < x-metadata>，即扩展元素。如果有些信息在上述元素中无法描述，则在此元素中进行扩展。



2. < menifest>，文件列表，由于列出OEBPS文档及相关的文档，有一个子元素构成，

- < item id="" href="" media-type="">,该元素由三个属性构成：
  - id:表示文件的ID号
  - href：文件的相对路径
  - media-type：文件的媒体类型
  - 例如：< item id="chap01" href="chap01.xhtml" media-type="application/xhtml+xml"/>



3. < spine toc="ncx">，脊骨，其主要功能是提供书籍的线性阅读次序。由一个子元素构成：

- < itemref idref="">,由一个属性构成：
- - idref:即参照menifest列出的ID
  - 例如：< itemref idref="chap01"/>



4. < guide>,指南,依次列出电子书的特定页面, 例如封面、目录、序言等, 属性值指向文件保存地址。一般情况下，epub电子书可以不用该元素。

5. < tour>,导读。可以根据不同的读者水平或者阅读目的, 按一定次序, 选择电子书中的部分页面组成导读。一般情况下，epub电子书可以不用该元素。







## /images

书籍的图片信息。



## /META-INF/container.xml

电子书的根文件（rootfile）的路径（media-type）和打开方式

**一般不需要改**

```xml
<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
   <rootfiles>
      <rootfile full-path="content.opf" media-type="application/oebps-package+xml"/>
      
   </rootfiles>
</container>
```



## /text

文章的文本。

html格式存放，可修改。





