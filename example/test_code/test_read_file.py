# -*- encoding: utf-8 -*-
# @Time    :   2025/10/11 21:18:39
# @File    :   test_read_file.py
# @Author  :   ciaoyizhen
# @Contact :   yizhen.ciao@gmail.com
# @Function:   测试读取file模块

import sys
sys.path.append(".")

from src.caoyizhen_basetool.file import read_file

data = read_file("example/data/test_jsonl.jsonl")
print(data)

data = read_file("example/data/test_jsonl.jsonl", output_type="dict", main_key_column="age")
print(data)

data = read_file("example/data/test_json.json", output_type="dict", main_key_column="age")
print(data)

data = read_file("example/data/test_json.json", output_type="list", main_key_column="age")
print(data)


data = read_file("example/data/test_xlsx.xlsx", output_type="list", main_key_column="age")
print(data)

data = read_file("example/data/test_xlsx.xlsx", output_type="dict", main_key_column="age")
print(data)

data = read_file("example/data/test_csv.csv", output_type="list", main_key_column="age")
print(data)

data = read_file("example/data/test_csv.csv", output_type="dict", main_key_column="age")
print(data)