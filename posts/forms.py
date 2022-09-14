from django import forms
from .models import Post

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        #fields  = '__all__'
        #fields = ['title', 'content', 'active', 'image']
        exclude = ['author']
        