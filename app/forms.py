from django.forms import ModelForm,Textarea
from .models import Memo
from django import forms

class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = ['title', 'text']

widgets = {
            'title': forms.Textarea(attrs={'rows':40, 'cols':150}),
        }

