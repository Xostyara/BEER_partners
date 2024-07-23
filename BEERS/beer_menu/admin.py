from django.contrib import admin

# Register your models here.
from .models import Beer, Provider, Manufacturer

class ProviderAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 
                    'name_provider',
                    'INN',
                    'number_of_agreement',
                    )
    search_fields = ('name_provider',
                    'INN',
                    'number_of_agreement',
                    ) 


class ManufacturerAdmin(admin.ModelAdmin):
    
    list_display = ('pk', 
                    'name_manufacturer',
                    'country',
                    'city',
                    )
    search_fields = ('name_manufacturer',
                    'country',
                    'city',
                    ) 
    

class BeerAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk',
                    'name', 
                    'type_beer', 
                    'provider', 
                    'manufacturer', 
                    'description',
                    'density',
                    'fortress',
                    'color',
                    'bitterness',
                    'alcohol',
                    'taste',
                    'date_publication',
                    'photo',
                    'active',
                    ) 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name', 
                    'type_beer',
                    'manufacturer'
                    ) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('name',) 


admin.site.register(Provider, ProviderAdmin) 
admin.site.register(Manufacturer, ManufacturerAdmin) 
admin.site.register(Beer, BeerAdmin) 

