from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse  # @UnresolvedImport
from notes.models import Kakeibo
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
    # 一覧取得コード
    kakeibo = Kakeibo.objects.all()
    # Viewに渡すように準備する。
    context = {"kakeibos": kakeibo}
    return render(req, "notes/top.html", context)
    

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
def notes_detail(req, id):
    kakeibo = get_object_or_404(Kakeibo, pk=id)
    return render(req, 'notes/note_detail.html', {'kakeibo': kakeibo} )


"""
url: /notes/{id}/edit/
method: get
function: ノートの編集
"""
def notes_edit(self, id):
    pass
