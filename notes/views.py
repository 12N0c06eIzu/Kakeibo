from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
Viewを返すための関数を記載するPythonファイルです。

追加する上でのルール
・PyDocで関数の機能、Get or Post、ルートについて記載する。
-- 以下コピーすると良いです。
url: 
method: 
function: 
"""

"""
url: /
method: get
function: 一覧表示
"""
def top(req):
    return HttpResponse(b"hello world")
    

"""
url:　/notes/new/
method: get
function: ノートの新規作成フォームの表示
"""

def notes_new(req):
    pass

"""
url: /notes/{id}/
method: get
function: ノートの閲覧
"""
def notes_detail(self, id):
    pass

"""
url: /notes/{id}/edit/
method: get
function: ノートの編集
"""
def notes_edit(self, id):
    pass
