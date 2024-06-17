Meet plus Greet project
=============
# Worldwide Service for VIP in Airports  

Install for Windows
------------
- клонируем репозиторий себе
- создаем виртуальное окружение
- активируем виртуальное окружение
- меняем текущую директорию
- устанавливаем зависимости
  
``` bash
  git clone https://github.com/Vm-Organization/meet_plus_greet
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
