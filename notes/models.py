import uuid
from django.db import models
# Create your models here.


class Tag(models.Model):
    """
    Kakeiboモデルにあるtagの外部キー
    １取引に１つ紐づける取引の種別
    """
    tag_code = models.UUIDField(
        'タグUUID', primary_key=True, default=uuid.uuid4, editable=False)
    tag_name = models.CharField('タグ名称', blank=True, max_length=30, unique=True)

    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.tag_name


class Kakeibo(models.Model):
    """
    家計簿を管理するクラス
    ・タイトル
    ・金額
    ・タグ マスタに登録されたCodeを入れる。Tagマスタを参照している。
    ・取引日 日付
    ・入出フラグ : MoneyIOクラスから選択する。
    ・作成日 日付
    ・更新日 日付
    """

    list = [
        ("0", "出金"),
        ("1", "入金"),
    ]

    title = models.CharField('タイトル', max_length=128)
    money = models.IntegerField('金額')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    trading_dt = models.DateTimeField('取引日')
    io_flag = models.CharField('入払区分', max_length=1,  choices=list)
    created_dt = models.DateTimeField('作成日', auto_now=True)
    updated_dt = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title
