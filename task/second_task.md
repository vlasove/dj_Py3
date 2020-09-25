# Техническое задание
### На разработку простейшего сервиса

В этот раз вам необходимо реализовать базовый функционал для сервиса по написанию отзывов по фильмам.
Сервис устроен по аналогии с ```https://github.com/vlasove/dj_Py3/tree/master/Lec9```.

Единственные отличия:
* Пользовательская модель имеет поле ```phone_number = models.CharField(max_length=25)``` для хранения номера телефона юзера.
* Модель объектов устроена следующим образом:
```
# Модель обзора на конкретный фильм
class FilmReview(models.Model):
    film_name = models.CharField(max_length=256)  # название фильма
    actors = models.TextField() # список актеров
    date = models.DateTimeField(auto_now_add=True) # время написания отзыва
    body = models.TextField() # тело отзыва
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
       
    ) # автор обзора

    def __str__(self):
        pass
        #code here

    def get_absolute_url(self):
        pass
        #code here


# Модель комментария для обзора на фильм
class ReviewComment(models.Model):
    post = models.ForeignKey(
        FilmReview, 
        on_delete=models.CASCADE, 
        related_name='reviews',
    )
    review_comment = models.CharField(max_length=250)
    author =  models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
    ) 
    date = models.DateTimeField(auto_now_add=True) # время написания коммента

    def __str__(self):
        # code here

    def get_absolute_url(self):
        # code here
```

* Отображение объектов Film на страницах включает в себя :```film_name, actors, date, body, author```
* Отображения комментариев включает в себя: ```review_comment, author, date```

Решение сформировать в виде проектной директориии на ```github.com```.