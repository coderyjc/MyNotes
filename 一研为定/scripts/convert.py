# -!- coding: utf-8 -!-

"""
@Author: Jingcun Yan
@Date: 2021/7/26
@Time: 16:06
@Desctiption: 
"""
import json

import pandas as pd

if __name__ == '__main__':
    with open('data.json', 'w', encoding='utf8') as fp:
        data = pd.read_table("学科评估.csv", sep=",")
        t_dict = data.to_dict('records')
        print(t_dict[:10])
        json.dump(t_dict, fp, ensure_ascii=False)
