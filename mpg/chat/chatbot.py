from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
import sys
import configparser

# Загрузка конфигурации из config.ini с указанием кодировки
config = configparser.ConfigParser()
with open('config.ini', 'r', encoding='utf-8') as configfile:
    config.read_file(configfile)

TELEGRAM_TOKEN = config['DEFAULT']['TELEGRAM_TOKEN']
WELCOME_MESSAGE = config['DEFAULT']['WELCOME_MESSAGE']

# Словарь для хранения пользователей и их сообщений
user_messages = {}

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username or update.message.from_user.full_name
    chat_id = update.message.chat_id
    user_messages[user_id] = {'chat_id': chat_id, 'username': user_name}
    await update.message.reply_text(WELCOME_MESSAGE)

# Функция для обработки текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username or update.message.from_user.full_name
    message_text = update.message.text

    # Проверка, является ли сообщение ответом на другое сообщение
    if update.message.reply_to_message:
        original_message = update.message.reply_to_message.text
        print(f"Ответ на сообщение: {original_message}")
    else:
        print("Новое сообщение, для ответа используйте форму - айди_чата: сообщение ")

    # Сохранение последнего сообщения пользователя и его имени
    if user_id not in user_messages:
        user_messages[user_id] = {'chat_id': update.message.chat_id, 'username': user_name}
    user_messages[user_id]['last_message'] = message_text

    # Вывод сообщения пользователя в терминал зеленым шрифтом
    print(f"\033[92mСообщение от {user_id} ({user_name}): {message_text}\033[0m")

    # Ответ пользователю
    await update.message.reply_text("Спасибо за сообщение!")

# Функция для отправки сообщения пользователю от имени бота
async def send_user_message(user_id: int, text: str, bot) -> None:
    if user_id in user_messages:
        await bot.send_message(chat_id=user_messages[user_id]['chat_id'], text=text)
    else:
        print(f"Ошибка: не удалось найти пользователя с ID {user_id} для ответа.")

# Функция для чтения ответов из терминала
def read_terminal_input(loop, bot):
    while True:
        line = sys.stdin.readline().strip()
        if line:
            try:
                user_id_str, response_text = line.split(':', 1)
                user_id = int(user_id_str.strip())
                response_text = response_text.strip()
                future = asyncio.run_coroutine_threadsafe(send_user_message(user_id, response_text, bot), loop)
                future.result()  # ждём завершения coroutine
            except ValueError as e:
                print(f"Ошибка обработки ввода: {e}")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    # Создание объекта приложения
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Обработчик команды /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Обработчик текстовых сообщений
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    application.add_handler(message_handler)

    # Получаем текущий цикл событий
    loop = asyncio.get_event_loop_policy().get_event_loop()

    # Запуск задачи чтения терминала в отдельном потоке
    executor = loop.run_in_executor(None, read_terminal_input, loop, application.bot)

    # Запуск бота
    application.run_polling()
