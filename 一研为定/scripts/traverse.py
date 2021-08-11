# -!- coding: utf-8 -!-


import requests
from lxml import etree

if __name__ == "__main__":
    # 设置UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    # 设置url
    url = "https://undermine.fandom.com/wiki/Potions"

    # 获取回应的数据
    response = requests.get(url=url, headers=headers).text
    # 将回应的数据转化为json格式
    ul_tree = etree.HTML(response)
    gallery = ul_tree.xpath('//div[@class="gallerytext"]/p/a/@href')
    # 数据的持久化存储
    base_url = 'https://undermine.fandom.com'
    i = 0
    for item in gallery:
        item_url = base_url + item
        response = requests.get(item_url, headers).text
        item_tree = etree.HTML(response)
        content = item_tree.xpath('//aside/section[2]/div/div/text()')
        title = item_tree.xpath('//aside/h2/text()')
        if len(content) == 2:
            print('\"' + title[0] + '\" ' + content[0] + ' ' + content[1])
        else:
            print(title[0] + ' ' + content[0])
