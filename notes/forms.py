"""
HTMLフォームの生成、値のValidationに利用できる。
"""

from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms

from notes.models import Kakeibo


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
        widgets = {
            'trading_dt': DatePickerInput(),
            }
        
