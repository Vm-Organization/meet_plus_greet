from django.shortcuts import render
from django.views.generic import TemplateView

from chat.forms import MessageForm
from chat.models import Chat
from chat.telegram import telegram_bot, send_message


# Create your views here.
class ChatView(TemplateView):
    template_name = 'chat.html'
    from_class = MessageForm
    model = Chat

    def post(self):
        instance = self.model.objects.get_or_create(user=self.request.user)
        form = self.from_class(self.request.POST)
        if form.is_valid():
            form.save()
        instance.messages['user'] = form.cleaned_data['message']
        instance.save()
        send_message(form.cleaned_data['message'])
