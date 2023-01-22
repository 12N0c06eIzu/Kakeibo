from django.contrib import admin
from notes.models import Kakeibo
# Register your models here.

# KakeiboがAdminインタフェースを持つことをAdminに伝える。
admin.site.register(Kakeibo)
