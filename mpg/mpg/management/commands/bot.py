from django.core.management import BaseCommand
from telepot.loop import MessageLoop

from chat.telegram import telegram_bot, handle


class Command(BaseCommand):

    def handle(self, *args, **options):
        MessageLoop(telegram_bot, handle).run_as_thread()
