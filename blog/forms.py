from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
                               attrs={
                                   "placeholder": "Blog here something..",
                                   "class": "textarea is-success is-medium",
                               }
                           ),
                           label="",
                           )

    class Meta:
        model = Blog
        exclude = ("user", )
