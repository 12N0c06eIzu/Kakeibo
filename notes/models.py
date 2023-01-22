from django.db import models
from django.conf import settings

# Create your models here.
"""
家計簿を管理するクラス
・タイトル
・金額 
・タグ マスタに登録されたCodeを入れる。
・取引日 日付
・入出フラグ : MoneyIOクラスから選択する。
・作成日 日付
・更新日 日付
"""
class Kakeibo(models.Model):
    class MoneyIO(models.IntegerChoices):
        入金 = 1
        出金 = 0
    
    title = models.CharField('タイトル', max_length=128)
    money = models.IntegerField('金額')
    tag = models.CharField('タグ', blank=True, max_length=30)
    trading_dt = models.DateTimeField('取引日')
    io_flag = models.IntegerField(choices=MoneyIO.choices)
    created_dt = models.DateTimeField('作成日', auto_now=True)
    updated_dt = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title
