from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import CategorySerializer
from rest_framework.serializers import ValidationError
# Create your views here.
@api_view(['Get','POST'])
def category_list(request):
    if request.method=='GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # data =  request.data
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response({
            'details':"New category added."
        })
        
        
@api_view(['GET','DELETE', 'PUT'])       
def category_details(request, id):
    category = Category.objects.get(id = id)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        total = OrderItem.objects.filter(food__category = category).count()
        if total > 0:
            raise ValidationError({
                "detail":"The food of this category exists in the order."
            })
        category.delete()
        return Response({
            "details":"Category deleted."
        })
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data = request.data)
        print(request.data.get('name'))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    
        
        
        