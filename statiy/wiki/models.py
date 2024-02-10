from django.contrib.auth import get_user_model
from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    owner = models.ForeignKey(get_user_model(), verbose_name='Пользователь',on_delete=models.CASCADE)


    def __str__(self):
        return self.title

