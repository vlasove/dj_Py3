* 0) Установка утилиты для создания окружений ```pip install pipenv```
* 1) Сбрка окружения ```pipenv shell```
* 2) Установка зависимостей ```pipenv install django```
* 3) Запуск проекта ```django-admin startproject <project_name> .```
* 4) Инициализация приложения  ```python manage.py startapp <app_name>```
* 5) Установка приложения для проекта ```settings.py -> INSTALLED_APPS = ["<app_name>.apps...."]```
* 6) Не забудем указать путь до всех шаблонов ```'DIRS': [os.path.join(BASE_DIR, 'templates')]``` + создать директорию ```templates``` в корне проекта.


***Mиграция модели*** - применение всех сгенерированных SQL запросов к БД.

***Подготовка миграции*** - генерация SQL запросов.