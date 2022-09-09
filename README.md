## Технологии
Проект создан с помощью технологий:
* Python 3.8
* Django 4.1.1
	
## Установка и запуск проекта

- `python3 -m venv venv` - создать виртуальное окружение
- `source venv/bin/activate` - войти в виртуальное окружение
- `pip install -r requirements.txt` - установить зависимости
- `docker-compose up -d` - поднять базу данных PostgreSQL (если Вы не используете Docker, установите PostgreSQL 
с официального сайта)
- `python manage.py migrate` - применить миграции к базе данных
- `python manage.py loaddata dbdata.json` - закинуть данные в базу данных
- `python manage.py runserver` - запуск сервера
