# -*- encoding: utf-8 -*-
# @Time    :   2025/10/11 22:14:16
# @File    :   test_save_file.py
# @Author  :   ciaoyizhen
# @Contact :   yizhen.ciao@gmail.com
# @Function:   测试存储文件

import sys
import os
sys.path.append(".")

from src.caoyizhen_basetool.file import read_file, save_file

data = read_file("example/data/test_jsonl.jsonl")


os.makedirs("output", exist_ok=True)
save_file("output/test_jsonl.jsonl", data, file_type="jsonl")
save_file("output/test_json.json", data, file_type="json")
save_file("output/test_xlsx.xlsx", data, file_type="xlsx")
save_file("output/test_csv.csv", data, file_type="csv")

save_file("output/test_jsonl.jsonl", data)
save_file("output/test_json.json", data)
save_file("output/test_xlsx.xlsx", data)
save_file("output/test_csv.csv", data)

