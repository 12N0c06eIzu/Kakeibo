from django import forms

from notes.models import Kakeibo

"""
HTMLフォームの生成、値のValidationに利用できる。
"""
class NotesForm(forms.ModelForm):
    class Meta:
        model = Kakeibo
        fields = (
            'title', 
            'money', 
            'tag', 
            'trading_dt', 
            'io_flag'
            )
        