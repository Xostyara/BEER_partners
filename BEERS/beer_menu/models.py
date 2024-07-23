from django.db import models

# Create your models here.


class Beer(models.Model): 
    "Таблица с видами пива"
    name = models.CharField(max_length = 100)
    
    type_beer= models.CharField(max_length= 20)  # потом сделать связку с таблицей типов пива (
    # крафтовое, лагер и т.д. или тянуть из справочника)
    
    # поставщик
    provider = models.CharField(max_length = 100)   # потом сделать связку с таблицей Поставщиков (для стандартизации)
    
    # производитель
    manufacturer = models.CharField(max_length = 100)   # потом сделать связку с таблицей Производителей (для стандартизации)
    
    description = models.TextField()       # описание

    density = models.TextField() # Плотность

    fortress = models.TextField() # крепость

    color = models.TextField() # Цвет

    bitterness = models.TextField() # Горечь

    fortress_in_procent = models.TextField()  # Крепость в процентах

    taste = models.TextField()  # вкус

    date_publication = models.DateField(auto_now_add=True)  # дата создания

    photo = models.ImageField()   # фотография/картинка
    
#     1) название
# 2) поставщик
# 3) производитель
# 4) описание
# 5) характеристики 
#     а) Плотность 
#     б) Крепость 
#     в) Цвет 
#     г) Горечь
# 6) крепость (алкоголь в %) 
# 7) ВКУС - описание 