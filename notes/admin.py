from django.contrib import admin
from notes.models import Kakeibo, Tag
# Register your models here.

# KakeiboがAdminインタフェースを持つことをAdminに伝える。
admin.site.register(Kakeibo)
admin.site.register(Tag)
