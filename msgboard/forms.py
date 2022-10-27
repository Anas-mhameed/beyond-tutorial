from django import forms
from .models import Message

# create your form here 


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('author', 'text')
