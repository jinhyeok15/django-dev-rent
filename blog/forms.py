from django import forms
from .models import Page


class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['title', 'content']
    title = forms.CharField(max_length=50, label='제목')
    content = forms.CharField(widget=forms.Textarea, label='내용')
