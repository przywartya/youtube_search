from django import forms
from .models import Comment

class SearchForm(forms.Form):
    query = forms.CharField(label="", required=True, max_length=60)

class CommentForm(forms.ModelForm):
    content = forms.CharField(required=False, label="", 
                                widget=forms.Textarea(attrs={
                                'placeholder': 'Your comment here...',
                                }))

    class Meta:
        model = Comment
        fields = ["content","rating"]