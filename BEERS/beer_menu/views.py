# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from beer_menu.serializers import (ContactsSerializer, 
                          Type_beerSerializer, 
                          ProviderSerializer, 
                          ManufacturerSerializer, 
                          BeerSerializer, )
from beer_menu.models import (Contacts, Type_beer, Provider,  Manufacturer, Beer)



@api_view(['GET', 'POST'])
def contacts_list(request):
    if request.method == 'POST':
        serializer = ContactsSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    contacts = Contacts.objects.all()
    serializer = ContactsSerializer(contacts, many = True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def contact_detail(request, pk):
    contact = Contacts.object.get(pk=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = ContactsSerializer(contact, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    serializer = ContactsSerializer(contact)
    return Response(serializer.data)



