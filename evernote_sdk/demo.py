# -*- coding:utf-8 -*-
"""
# Author pylixm
# Created at 2016/3/29
"""
from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter
from evernote.edam.type import ttypes as Types
from evernote.api.client import NoteStore

####### 认证 ###############################
dev_token = "S=s1:U=9249d:E=15b19f82be2:C=153c246fed0:P=1cd:A=en-devtoken:V=2:H=f8e54a1b3d2a811ca3b44dea19daec28"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username

### 获取笔记本 #############################
client = EvernoteClient(token=dev_token)
noteStore = client.get_note_store()
# 获取笔记本
notebooks = noteStore.listNotebooks()
for book in notebooks:
    print book.guid
    print book.name

### 获取笔记本中的笔记及tags ########################
client = EvernoteClient(token=dev_token)
note_store = client.get_note_store()

filter = NoteStore.NoteFilter()
#filter.notebookGuid = nb_guid # 指定notebook guid

spec = NoteStore.NotesMetadataResultSpec()
spec.includeTitle = True

noteList = noteStore.findNotes(dev_token, filter, 0, 100)
notes = noteList.notes
for note in notes:
    print note.title
    tag_guids = note.tagGuids
    if tag_guids is not None:
        for tag_guid in tag_guids:
            tag = note_store.getTag(dev_token, tag_guid)
            print tag.name, tag_guid

### 创建笔记 ######################################
client = EvernoteClient(token=dev_token)
noteStore = client.get_note_store()
note = Types.Note()
note.title = "I'm a test note!"
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>Hello, world!</en-note>'
note.tagNames = ['创建标签1', '创建标签2'] #
#note.notebookGuid =  #
note = noteStore.createNote(note)

### 更新笔记 ###################################3#
client = EvernoteClient(token=dev_token)
noteStore = client.get_note_store()
note = noteStore.getNote(guid='xx')
note.title = '修改测试'
note = noteStore.updateNote(note)