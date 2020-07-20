from django import forms

class CategoryCreateForm(forms.Form):
    title = forms.CharField(max_length=100, label='Имя')
    description = forms.CharField(widget=forms.Textarea, label='Описание', required=False)
    image = forms.FileField()
    is_visible = forms.BooleanField(label='Категория видна людям', required=False)