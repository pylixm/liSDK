# -*- coding:utf-8 -*-
"""
# Author pylixm
# Created at 2016/3/29
"""
from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter

dev_token = "S=s1:U=9249d:E=15b19f82be2:C=153c246fed0:P=1cd:A=en-devtoken:V=2:H=f8e54a1b3d2a811ca3b44dea19daec28"
client = EvernoteClient(token=dev_token)
noteStore = client.get_note_store()
print noteStore
# 获取笔记本
notebooks = noteStore.listNotebooks()
for book in notebooks:
    print book.guid
    print book.name
    # 获取笔记本下的笔记
    notefilter = NoteFilter()
    notefilter.write(book)

    for note in noteStore.findNotes(notefilter, 0, 100):
        print note