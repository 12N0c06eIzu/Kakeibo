from django.test import TestCase
from django.urls import resolve

import notes.views as notes_views
# Create your tests here.
class TopViewTest(TestCase):
    """
    ・test_を接頭辞につけること
    ・PyDocで先頭に「テスト内容_テスト番号４桁　どういったテストか」を記載すること
        ・V：View関係
    """
    
    """
    # V_0001 Viewの接続に成功する。
    """
    def test_top_return_200(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
    
    """
    # V_0002 ViewからContentsが帰ってくる。
    """
    def test_top_return_content(self):
        res = self.client.get("/")
        self.assertNotEqual(res.content, None)
    
    """
    # V_0003 View newのルーティングテスト
    """
    def test_resolve_notes_new(self):
        found = resolve("/notes/new/")
        self.assertEqual(notes_views.notes_new,found.func) 
           
    """
    # V_0004 View detailのルーティングテスト
    """
    def test_resolve_notes_detail(self):
        found = resolve("/notes/1/")
        self.assertEqual(notes_views.notes_detail,found.func)    
        
    """
    # V_0005 View editのルーティングテスト
    """
    def test_resolve_notes_edit(self):
        found = resolve("/notes/1/edit/")
        self.assertEqual(notes_views.notes_edit,found.func)



    