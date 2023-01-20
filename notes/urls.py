'''
Created on 2023/01/13

@author: hayashirikuto
'''
import notes.views as notes_root
from Kakeibo.urls import path

"""
・新しくViewファイルを追加したときはimportをしてください
import ViewFile as hoge
・viewsに新しい関数を追加したときは必ず追加して下さい
path("", ),
・親玉になるアプリのurls.pyにImportして呼び出してください。
"""


urlpatterns = [
    path('new/', notes_root.notes_new, name='notes_new'),
    path('<int:id>/', notes_root.notes_detail, name='notes_detail'),
    path('<int:id>/edit/', notes_root.notes_edit, name='notes_edit'),
]
