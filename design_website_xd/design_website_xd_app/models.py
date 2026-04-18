from django.db import models
from django.contrib.auth.models import User
from transliterate import translit

# Service - услуга
class Service(models.Model):
    #CharField(max_lenght - 25)
    #IntegerField()
    #DataField()
    #DateTimeField()
    #FilePathField() - путь до файла

    catalog_types = (
        ('human_image_design', 'дизайн имидж человека'), 
        ('graphic', 'графический'), 
        ('architectural', 'архитектурный'), 
        ('art_design', 'арт-дизайн'),
    )

    def user_directory_path(instance, filename):
        title = str(translit(value = instance.title, language_code = 'ru', reversed = True))
        id = str(instance.id)
        return f'services/{id}_{title}/{filename}'

    title = models.CharField(max_length= 100) # название продукта
    price = models.FloatField() # цена продукта
    description = models.TextField() # описание продукта
    image = models.ImageField(default='none', upload_to=user_directory_path) # картинка продукта
    image2 = models.ImageField(default='none', upload_to=user_directory_path) # картинка продукта
    quantity = models.IntegerField() # кол-во продукта
    catalog_type = models.CharField(max_length = 100, choices = catalog_types)

    def __str__(self):
        return f'{self.id}. {self.title}' 
