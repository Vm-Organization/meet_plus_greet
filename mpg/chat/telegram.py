import telepot
import os
from dotenv import load_dotenv, find_dotenv
import sys
import time
from telepot.loop import MessageLoop

load_dotenv(find_dotenv())

token = os.getenv('TG_TOKEN')
my_id = os.getenv('TG_ID')
# print(bot.getMe())  # to get info including TG ID
telegram_bot = telepot.Bot(token)


def send_message(text):
    telegram_bot.sendMessage(my_id, text, parse_mode='Markdown')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    return content_type, chat_type, chat_id


# MessageLoop(telegram_bot, handle).run_as_thread()
