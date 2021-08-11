# -!- coding: utf-8 -!-

"""
@Author: Jingcun Yan
@Date: 2021/7/28
@Time: 21:18
@Desctiption: 
"""

import os

count = 0

root = 'F:\Books\大合集\pkgs\Part 856-920【解压码：love】\Part 856-920'
parts = os.listdir(root)
fp = open('index.txt', 'w+', encoding='utf-8')
for part in parts:
    fp.write(part + ':')
    part = root + '\\' + part
    books = os.listdir(part)
    for book in books:
        if book.endswith('.png'):
            os.remove(part + '\\' + book)
        else:
            fp.write('《' + book + '》')
            fp.write(' ')
            count += 1
    fp.write('\n\n')
fp.close()
print(count)