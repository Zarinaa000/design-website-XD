from django.db import models
from django.contrib.auth.models import User

# Service - услуга
class Service(models.Model):
    #CharField(max_lenght - 25)
    #IntegerField()
    #DataField()
    #DateTimeField()
    #FilePathField() - путь до файла

    service_title = models.CharField(max_length= 100) # название продукта
    service_price = models.FloatField() # цена продукта
    service_Description = models.TextField() # описание продукта
    service_image = models.ImageField() # картинка продукта
    service_quantity = models.IntegerField() # кол-во продукта

    def __str__(self):
        return f'{self.service_title}'
    
    















# Create your models here.
