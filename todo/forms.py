from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={"size":50}))

    class Meta:
        model = Todo
        fields = ['content', 'done']