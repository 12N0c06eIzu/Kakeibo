from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse  # @UnresolvedImport
from notes.models import Kakeibo
from notes.forms import NotesForm
from pip._internal import req
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
    # フォーム入力後「登録」ボタンを押下すると詳細画面を開く
    if req.method == 'POST':
        form = NotesForm(req.POST)
        
        if form.is_valid():
            kakeibo = form.save(commit=False)
            kakeibo.save()
            return redirect(notes_detail, id = kakeibo.pk)
        
    else:
        form = NotesForm()
        
    return render(req, "notes/note_new.html", {'form': form})

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
def notes_edit(req, id):
    # 家計簿オブジェクトを取得する。
    kakeibo = get_object_or_404(Kakeibo, pk=id)
    
    if req.method == "POST":
        form = NotesForm(req.POST, instance=kakeibo)
        
        if form.is_valid():
            form.save()
            return redirect("notes_detail", id=kakeibo.id)
        
    else:
        form = NotesForm(instance=kakeibo)
            
    return render(req, 'notes/note_edit.html', {'form': form} )

