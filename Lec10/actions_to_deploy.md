* Установить git : ```https://git-scm.com/download/win```
* Создать удаленный репозиторий на ```github.com``` с вашим проектом
* Устновить HerokuCLI: ```https://devcenter.heroku.com/articles/heroku-cli```
* Создать учетную запись на ```https://dashboard.heroku.com/apps```
* Выполнить в командной строчке запрос ```heroku login```

web: gunicorn proj.wsgi --log-file -
* Создаем ```Procfile``` с содержимым ```web: gunicorn <name>.wsgi --log-file -```
* ```pipenv install gunicorn``` для доступа к логированию из проекта
* ```pipenv install whitenoise``` для внутреннего кэширования statiс-объектов
* В ```setting.py``` -> ```ALLOWED_HOSTS = ["*"]```
* Затем в ```settings.py``` -> 
```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_FILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```
* Выполним ```git add .``` -> ```git commit -m "ready for Heroku"``` -> ```git push```


* ```heroku create```
* Затем связываем git репозиторий с данным приложением ```heroku git:remote -a afternoon-savannah-91288``` , где ```afternoon-savannah-91288``` - уникальное имя вашего приложения.
* Отправить изменения на heroku -> ```git push heroku master```

* Хотим запустить наше приложение на бесплатном единственном сервере (самом слабом):
```heroku ps:scale web=1```