# Сайта для шаринга лучших мест на карте

Сайт позволяет отображать точки интереса на карте с фотографиями и описанием. 

## Переменные окружения .env

Часть настроек проекта берётся из переменных окружения.
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
```
python .\manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
```
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE_URL` — однострочный адрес к базе данных, например: `sqlite:///db.sqlite3`. Больше информации в [документации](https://github.com/jacobian/dj-database-url#url-schema)
. Это позволяет легко переключаться между базами данных: PostgreSQL, MySQL, SQLite — без разницы, нужно лишь подставить нужный адрес.
- Настройки секьюрности (для прода):
  - `SECURE_HSTS_SECONDS`
  - `SECURE_HSTS_INCLUDE_SUBDOMAINS`
  - `SECURE_SSL_REDIRECT`
  - `SESSION_COOKIE_SECURE`
  - `CSRF_COOKIE_SECURE`
  - `SECURE_HSTS_PRELOAD`
  
## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`  

## Загрузка данных
Реализована возможность загрузки данных с помощью json файла.
```
python manage.py load_place -j place.json
```
`place.json` - любой локальный или сетевой файл вида:
```
{
	title: string,
	imgs: [
		link,
	],
	description_short: text
	description_long: html,
	coordinates: {
		lng: float,
		lat: float
	}
}
```
## Пример реализации
[pythonanywhere](https://tarodo.pythonanywhere.com/)