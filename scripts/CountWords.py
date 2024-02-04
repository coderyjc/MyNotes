import os
import markdown2
import re
from zhon import hanzi

def recursive_dict_print(d, indent=0):
    sorted_data = sorted(d.values(), key=lambda x: x['size'], reverse=True)
    print("| 文件类型 | 数量 | 大小 |")
    print("|----------|-------|------|")
    for item in sorted_data:
        print("| {} | {} | {:.2f} MB |".format(item['name'], item['count'], item['size']))



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
note_folder_path = '../OBSIDIAN'

file_types_count, total_md_words = process_folder(note_folder_path)


recursive_dict_print(file_types_count)

# print("文件类型统计:")
# for file_type, count in file_types_count.items():
#     print(f"{file_type}: {count} 个文件")

print("\n所有MD文件字数总和:")
print(f"{total_md_words} 个字")

