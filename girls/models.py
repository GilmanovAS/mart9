from django.db import models

# Create your models here.

class Question(models.Model):
    slug = models.CharField(max_length=20)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=100)
    dig1 = models.IntegerField

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural= 'Вопросы'

    def __str__(self):
        return self.slug

