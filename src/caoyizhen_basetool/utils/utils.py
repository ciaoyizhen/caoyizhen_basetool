# -*- encoding: utf-8 -*-
# @Time    :   2025/10/12 12:48:14
# @File    :   utils.py
# @Author  :   ciaoyizhen
# @Contact :   yizhen.ciao@gmail.com
# @Function:   通用工具
import json
from functools import wraps
from threading import Lock

def singleton(cls):
    """线程安全的单例模式装饰器"""
    instances = {}
    lock = Lock()

    @wraps(cls)
    def get_instance(*args, **kwargs):
        # 双重检查锁，防止多线程竞争
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def return_to_jsonl(file_path, encoding="utf-8", ensure_ascii=False):
    def decorator(func):
        
        @wraps(func)
        def wrapper(*arg, **kwargs):
            single_result = func(*arg, **kwargs)
            error_msg = f"被装饰器的函数需要有返回，并且必须是str或dict"
            if (single_result is None):
                raise RuntimeError(error_msg)
            
            if isinstance(single_result, dict):
                single_result = json.dumps(single_result, ensure_ascii=ensure_ascii)
            elif isinstance(single_result, str):
                pass
            else:
                raise RuntimeError(error_msg)
            
            with open(file_path, "a", encoding=encoding) as f:
                f.write(single_result + "\n")
            
        return wrapper
    
    return decorator