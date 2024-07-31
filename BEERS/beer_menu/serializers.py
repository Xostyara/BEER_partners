from rest_framework import serializers

from .models import Contacts, Type_beer, Provider, Manufacturer, Beer


class ContactsSerializer(serializers.ModelSerializer):
    """Сериализатор модели Контакты/Contacts"""
    class Meta:
        model = Contacts
        # Указываем поля модели, с которыми будет работать сериализатор;
        # поля модели, не указанные в перечне, сериализатор будет игнорировать.
        # Для перечисления полей можно использовать список или кортеж.
        fields = ('id', 
                  'surname', 
                  'name', 
                  'otchwstvo', 
                  'job_title', 
                  'phone',
                  'email',
        )

class Type_beerSerializer(serializers.ModelSerializer):
    """Сериализатор модели типы пива"""
    class Meta:
        model = Type_beer
        fields = ('id',
                  'key',
                  'type',
        )

class ProviderSerializer(serializers.ModelSerializer):
    """Сериализатор модели Поставщики"""
    class Meta:
        model =  Provider
        fields = ('id',
                  'name_provider',
                  'INN',
                  'number_of_agreement',
                  'active',
                  'contact',
        )

class ManufacturerSerializer(serializers.ModelSerializer):
    """Сериализатор модели Производители"""
    class Meta:
        model = Manufacturer
        fields = ('id',
                  'name_manufacturer', 
                  'country',
                  'city',
                  )

class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ('id',
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
                  'photo',
                  'active',
                  )