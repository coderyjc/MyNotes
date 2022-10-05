## json格式的书签转化为markdown文档

使用时修改`JSON_FILE_PATH` 和 `SAVE_FILE_PATH` 即可

json文件的格式

```json
{
  "name": "分类名称",
  "children": [
    {
      "name": "分类名称",
      "children": [
        {
          "name": "分类名称",
          "children": [],
          "web": [
            {
              "url": "网址",
              "title": "网址标题"
            },
            {
              "url": "...",
              "title": "..."
            }
        }
    }
}
```

python代码

```python
"""
Author: Yan Jingcun
Date: 2022-09-20
Time: 12:06:04
Description: 将chrome书签的json文件转换为python文件
"""

import json


# 书签文件路径
JSON_FILE_PATH = './convertchrome2json/rst.json'
# 保存文件路径
SAVE_FILE_PATH = './convertchrome2json/test.md'

content = ''

def convert(dic, layer):
  global content

  # name 分类
  line = str('#' * layer) + ' ' + dic['name'] + '\n'
  content += line
  
  # web 网站
  if dic['web'] != []:
    for web in dic['web']:
      line = '- [%s](%s)\n' % (web['title'], web['url'])
      content += line
  
  # childern 子分类
  if dic['children'] != []:
    for item in dic['children']:
      convert(item, layer + 1)

  print(dic['name'] + '----> 已完成')

def saveFile(path):
  open(path, 'w', encoding='utf-8').write(content)


if __name__ == '__main__':
# 字典数据
  data = json.loads(open(JSON_FILE_PATH, encoding='utf-8').read())

# 转换
  for folders in data:
    convert(folders, 1)

# 保存
  saveFile(SAVE_FILE_PATH)
```

