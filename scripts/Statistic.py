import os
import markdown2
import re
from zhon import hanzi

def output_details(d):
    sorted_data = sorted(d.values(), key=lambda x: x['size'], reverse=True)
    print("| 文件类型 | 数量 | 大小 |")
    print("|----------|-------|------|")
    for item in sorted_data:
        print("| {} | {} | {:.2f} MBytes |".format(item['name'], item['count'], item['size']))

def output_overall(d):
    type_dict = {
        '笔记': {'name': '笔记', 'count': 0, 'size': 0},
        '书籍': {'name': '书籍', 'count': 0, 'size': 0},
        '图片': {'name': '图片', 'count': 0, 'size': 0},
        '插件相关': {'name': '插件相关', 'count': 0, 'size': 0},
        '其他': {'name': '其他', 'count': 0, 'size': 0}
    }

    file_types = {
        'md': '笔记', 'pdf': '书籍', 'png': '图片', 'jpg': '图片', 
        'jpeg': '图片', 'gif': '图片', 'drawio': '图片', 'webp': '图片', 'xmind': '图片',
        'js': '插件相关', 'css': '插件相关', 'scss': '插件相关', 'ts': '插件相关'
    }

    for key, value in d.items():
        file_type = file_types.get(key, '其他')
        type_dict[file_type]['count'] += value['count']
        type_dict[file_type]['size'] += value['size']

    sorted_data = sorted(type_dict.values(), key=lambda x: x['size'], reverse=True)
    print("| 文件类型 | 数量 | 大小 |")
    print("|----------|-------|------|")
    for item in sorted_data:
        print("| {} | {} | {:.2f} MBytes |".format(item['name'], item['count'], item['size']))


def count_words_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        # 统计中文字符数量
        chinese_characters = re.findall(f'[{hanzi.characters}]', content)
        # 统计英文单词数量
        english_words = re.findall(r'\b[A-Za-z]+\b', content)

        total_words = len(chinese_characters) + len(english_words)
        return total_words

def process_folder(folder_path):
    file_types_count = {}
    total_md_words = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 文件路径
            file_path = os.path.join(root, file)
            # 文件扩展名
            file_extension = file.split('.')[-1].lower()

            if file_extension not in file_types_count:
                file_types_count[file_extension] = {}
                file_types_count[file_extension]['name'] = file_extension
                file_types_count[file_extension]['count'] = 0
                file_types_count[file_extension]['size'] = 0

            # 按照文件扩展名统计
            file_types_count[file_extension]['count'] += 1
            file_types_count[file_extension]['size'] += round(os.path.getsize(file_path)/(1024*1024), 2)

            # 统计MD文件的字数
            if file_extension == 'md':
                total_md_words += count_words_md(file_path)

    return file_types_count, total_md_words

# 替换为你的笔记文件夹路径
note_folder_path = '../OBSIDIAN/'



file_types_count, total_md_words = process_folder(note_folder_path)

output_overall(file_types_count)

print("\n所有MD文件字数总和:")
print(f"{total_md_words} 个字")

