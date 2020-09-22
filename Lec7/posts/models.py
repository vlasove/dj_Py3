from django.db import models

# Create your models here.
# Модель данных - описание способов хранения и представления данных внутри программы.

class Post(models.Model):
    text = models.TextField() # TextField() - неогранич поле для хранения текста
