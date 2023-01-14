from django.test import TestCase, Client, RequestFactory  # @UnresolvedImport
from django.urls import resolve  # @UnresolvedImport
from django.contrib.auth import get_user_model

import notes.views as notes_views
from notes.models import Kakeibo
from notes.views import top

# UserModelを定義する。
UserModel = get_user_model()

# Create your tests here.
class TestUtil():
    def setUp(self):
        # self.user = self.createUser()
        self.kakeibo = self.createKakeibo()
        
    def createUser(self):
        return UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
            )
        
    def createKakeibo(self):
        return Kakeibo.objects.create(
            title="title1",
            money=100,
            trading_dt='2022-12-31 00:00:00',
            tag="1",
            io_flag="0")

class NotesTopViewTest(TestCase):
    """
    ・test_を接頭辞につけること
    ・PyDocで先頭に「テスト内容_テスト番号４桁　どういったテストか」を記載すること
        ・V：View関係
    """
    
    """
    # V_1001 Viewの接続に成功する。
    """
    def test_top_return_200(self):
        res = self.client.get("/")
        self.assertContains(res, "toppage", status_code=200)
    
    """
    # V_1002 ViewからContentsが帰ってくる。
    """
    def test_top_return_content(self):
        res = self.client.get("/")
        self.assertTemplateUsed(res, "notes/top.html")

    """
    # V_1003 ViewにKakeibo.titleが使用されている確認する。
    """
    def test_top_return_title(self):
        # 家計簿オブジェクトを用意する。
        kakeibo = TestUtil().createKakeibo()
        
        res = self.client.get("/")
        # title
        self.assertContains(res, kakeibo.title, status_code=200)
        
class NotesNewViewTest(TestCase):
    """
    # V_2001 View newのルーティングテスト
    """
    def test_resolve_notes_new(self):
        found = resolve("/notes/new/")
        self.assertEqual(notes_views.notes_new,found.func) 
         
class NotesDetailViewTest(TestCase):
    TestUtil().setUp()
    """
    # V_3001 View detailのルーティングテスト
    """
    def test_notes_detail_resolve(self):
        found = resolve("/notes/1/")
        self.assertEqual(notes_views.notes_detail,found.func)    
    
    """
    # V_3002 VIew テンプレートを使っている確認テスト
    """
    def test_notes_detail_return_content(self):
        # 家計簿オブジェクトを用意する。
        kakeibo = TestUtil().createKakeibo()
        
        res = self.client.get("/notes/%s/"  % kakeibo.id)
        self.assertTemplateUsed(res, "notes/note_detail.html")
        
    """
    # V_3003 View タイトルが帰ってくる。
    """
    def test_notes_detail_return_title(self):
        # 家計簿オブジェクトを用意する。
        kakeibo = TestUtil().createKakeibo()
        
        res = self.client.get("/notes/%s/" % kakeibo.id)
        self.assertContains(res, kakeibo.title, status_code=200)

class NotesEditViewTest(TestCase):
    """
    # V_4001 View editのルーティングテスト
    """
    def test_resolve_notes_edit(self):
        found = resolve("/notes/1/edit/")
        self.assertEqual(notes_views.notes_edit,found.func)

    

    