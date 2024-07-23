from django.db import models

from .directorys import BEER_TYPE_CHOICES, GRADE_CHOICES
# Create your models here.


class Provider(models.Model):
    """Таблица с информацией о поставщике"""

    name_provider = models.CharField(max_length = 100, 
                                verbose_name='Название компании')
    INN = models.CharField(max_length=15,
                       verbose_name='ИНН'
                       )
    number_of_agreement = models.CharField(max_length=50,
                                           verbose_name='Номер договора'
                                           )


class Manufacturer(models.Model):
    """Таблица с информацией о поставщике"""
    name_manufacturer = models.CharField(max_length = 100, 
                                verbose_name='Название производителя')
    country = models.CharField(max_length = 100, 
                                verbose_name='Страна')
    city = models.CharField(max_length = 50, 
                                verbose_name='Город')
    
    


class Beer(models.Model): 
    "Таблица с видами пива"
    name = models.CharField(max_length = 100,
                            verbose_name='Название'
                            )
    
    type_beer= models.CharField(max_length=1, 
                               choices=BEER_TYPE_CHOICES,
                               verbose_name='Тип пива',
                                )  # потом сделать связку с таблицей типов пива (
    # крафтовое, лагер и т.д. или тянуть из справочника)
    
    # поставщик
    provider = models.CharField(max_length = 100, 
                                verbose_name='Поставщик'
                                )   # потом сделать связку с таблицей Поставщиков (для стандартизации)
    
    # производитель
    manufacturer = models.CharField(max_length = 100,
                                    verbose_name='Производитель'
                                    )   # потом сделать связку с таблицей Производителей (для стандартизации)
    # volume = models.FloatField(verbose_name="Объем в литрах", blank=True)
    # price = models.CharField(max_length = 5,
    #                          verbose_name='Цена', 
    #                          blank=True
    #                          )
    
    description = models.TextField(verbose_name='Описание')       

    density = models.CharField(max_length=1, 
                               choices=GRADE_CHOICES,
                               verbose_name='Плотность от 1 до 5'
                               ) 

    fortress = models.TextField(max_length=1, 
                               choices=GRADE_CHOICES,
                               verbose_name='Крепость от 1 до 5'
                               ) 

    color = models.TextField(max_length=1, 
                             choices=GRADE_CHOICES,
                             verbose_name='Цвет от 1 до 5'
                             ) 

    bitterness = models.TextField(max_length=1, 
                                  choices=GRADE_CHOICES,
                                  verbose_name='Горечь от 1 до 5'
                                  ) 

    alcohol = models.TextField(verbose_name='Алкоголь в %') 

    taste = models.TextField(verbose_name='Описание вкуса')  

    date_publication = models.DateField(auto_now_add=True, 
                                        verbose_name="дата создания"
                                        )  

    photo = models.ImageField(verbose_name='Фото')   # фотография/картинка
    
    active = models.BooleanField(default= False, 
                                verbose_name='В наличии'
                                ) #  - true/false
    
