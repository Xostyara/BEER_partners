from django.db import models

from .directorys import BEER_TYPE_CHOICES, GRADE_CHOICES
# Create your models here.



class Type_beer(models.Model):
    """Справочник с типами пива"""
    # id = models.AutoField(primary_key=True)

    key = models.CharField(max_length= 1,
                           verbose_name="Ключ" )
    
    type = models.CharField(max_length= 30,
                            verbose_name="Тип пива")

class Provider(models.Model):
    """Таблица с информацией о поставщике"""
    # id = models.AutoField(primary_key=True)

    name_provider = models.CharField(max_length = 100, 
                                verbose_name='Название компании')
    INN = models.CharField(max_length=15,
                       verbose_name='ИНН'
                       )
    number_of_agreement = models.CharField(max_length=50,
                                           verbose_name='Номер договора'
                                           )
    active = models.BooleanField(default=False, 
                                 verbose_name="Статус поставщика")

class Contacts(models.Model):
    """Справочник контактов поставщика"""
    # id = models.AutoField(primary_key=True)

    surname = models.CharField(max_length=30,
                               verbose_name="Фамилия"
                               )
    
    name = models.CharField(max_length= 30,
                            verbose_name="Имя"
                            )
    
    otchestvo = models.CharField(max_length=30, 
                                 verbose_name="Отчество"
                                 )
    
    job_title = models.CharField(max_length= 30, 
                                 verbose_name="Должность"
                                 )
    
    phone = models.CharField(max_length= 14, 
                             verbose_name="Телефон"
                             )
    
    email = models.EmailField(verbose_name="Почта"
                              )
    
    provider = models.ForeignKey(Provider, 
                                on_delete=models.CASCADE, 
                                blank=True, 
                                null=True, 
                                related_name='Contacts'
                                )


class Manufacturer(models.Model):
    """Таблица с информацией о производителе"""
    # id = models.AutoField(primary_key=True)

    name_manufacturer = models.CharField(max_length = 100, 
                                verbose_name='Название производителя')
    country = models.CharField(max_length = 100, 
                                verbose_name='Страна')
    city = models.CharField(max_length = 50, 
                                verbose_name='Город')
    
    
class Beer(models.Model): 
    "Таблица с видами пива"
    # id = models.AutoField(primary_key=True)

    name = models.CharField(max_length = 100,
                            verbose_name='Название'
                            )
    
    type_beer= models.ForeignKey(Type_beer, 
                                 on_delete=models.SET_NULL, 
                                 blank=True, 
                                 null=True, 
                                 related_name="type_beer")
            
    # поставщик
    provider = models.ForeignKey(Provider, 
                                 on_delete=models.SET_NULL,
                                 blank=True, 
                                 null=True, 
                                 related_name="beers",
                                 )
        
            # производитель
    manufacturer = models.ForeignKey(Manufacturer, 
                                     on_delete=models.SET_NULL,
                                     blank=True, 
                                     null=True,  
                                     related_name="Manufacturers",
                                     )
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

    # date_publication = models.DateField(auto_now_add=True, 
    #                                     verbose_name="дата создания"
    #                                     )  

    photo = models.ImageField(verbose_name='Фото')   # фотография/картинка
    
    active = models.BooleanField(default= False, 
                                verbose_name='В наличии'
                                ) #  - true/false
    
