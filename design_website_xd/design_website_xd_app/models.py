from django.db import models
from django.contrib.auth.models import User

# Service - услуга
class Service(models.Model):
    #CharField(max_lenght - 25)
    #IntegerField()
    #DataField()
    #DateTimeField()
    #FilePathField() - путь до файла

    title = models.CharField(max_length= 100) # название продукта
    price = models.FloatField() # цена продукта
    description = models.TextField() # описание продукта
    image = models.ImageField() # картинка продукта
    quantity = models.IntegerField() # кол-во продукта

    def __str__(self):
        return f'{self.id}. {self.title}'
