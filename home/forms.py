from django import forms
"""from .models import Comment"""

"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')"""


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Тема')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)



