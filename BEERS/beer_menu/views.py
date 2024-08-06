# views.py
from rest_framework import viewsets 
from beer_menu.serializers import (ContactsSerializer, 
                          TypeBeerSerializer, 
                          ProviderSerializer, 
                          ManufacturerSerializer, 
                          BeerSerializer, )
from beer_menu.models import (Contacts, Type_beer, Provider,  Manufacturer, Beer)


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class TypeBeerViewSet(viewsets.ModelViewSet):
    queryset = Type_beer.objects.all()
    serializer_class = TypeBeerSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class BeerViewSet(viewsets.ModelViewSet):
    queryset =  Beer.objects.all()
    serializer_class = BeerSerializer