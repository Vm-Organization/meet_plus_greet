from django import forms

from chat.models import Chat


class MessageForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Chat
        fields = '__all__'