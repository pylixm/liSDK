# 印象笔记SDK（2016-3-29 add）

## 安装

    pip install evernote

结构： 

    .
    ├── __init__.py
    ├── api
    │   ├── __init__.py
    │   └── client.py
    └── edam
        ├── __init__.py
        ├── error
        │   ├── __init__.py
        │   ├── constants.py
        │   └── ttypes.py
        ├── limits
        │   ├── __init__.py
        │   ├── constants.py
        │   └── ttypes.py
        ├── notestore
        │   ├── __init__.py
        │   ├── constants.py
        │   ├── NoteStore.py
        │   └── ttypes.py
        ├── type
        │   ├── __init__.py
        │   ├── constants.py
        │   └── ttypes.py
        └── userstore
            ├── __init__.py
            ├── constants.py
            ├── ttypes.py
            └── UserStore.py

## 目录说明：

- `api` 目录如sdk入口，可初始化一个 `evernote` 对象用来获取 `userstore` `notestore` 等

- `edam` 使用python语言封装了 `evernote` 的各接口函数。函数名和其他语言相通。

- `edam` 中各子目录对应 `evernote` 中的各模块，使用时可从此处 import 。 


