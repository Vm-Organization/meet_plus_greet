![Screenshot_1](https://github.com/Vm-Organization/meet_plus_greet/assets/101522861/870e461e-e64e-4341-b2a4-f28133711cc4)

Meet plus Greet project
=============
# Worldwide Service for VIP in Airports  
https://nataliatkachuk.pythonanywhere.com/  

### Python Django Postgres JQuery HTML CSS

Realised functional:
-----------
- Registration and authorization, including by Google account (using allauth)
- Personal account
- Saving passengers data
- Quick airport search
- Booking in three steps (using django-authocomplete-light, formtools wizard)
- Booking history and active bookings
- Booking confirm, pay and cancel
- Sending email to user and manager about new booking (using signals)
- Sending messages in Telegram; telegram-bot for support (does not connected for now)
- HTML, CSS, few pages and some animation

Install for Windows
------------
- клонируем репозиторий себе
- создаем виртуальное окружение
- активируем виртуальное окружение
- меняем текущую директорию
- устанавливаем зависимости
  
``` bash
  git clone https://github.com/Vm-Organization/meet_plus_greet
  cd meet_plus_greet
  python -m venv venv
  venv\scripts\activate
  cd mpg
  pip install -r requirements.txt
```
.env.example заменить на .env, запустить postgres, создать в нем базу meet_and_greet с параметрами как в .env   

Run
------
- проводим миграции
- запускаем сервер
``` bash
  python manage.py migrate
  python manage.py runserver
```   
- запускаем бот
``` bash
  python manage.py bot
```   
To create superuser (admin):
```bash
  python manage.py createsuperuser
```
При переходе во вкладку /admin можно залогиниться с админа

Developers
-----------

https://github.com/Dashajuu fullstack  
https://github.com/DimerGGG backend  
https://github.com/Uks130322 backend
