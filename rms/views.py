from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

# Create your views here.

class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def destroy(self, request, pk):
        category = Category.objects.get(pk = pk)
        total = OrderItem.objects.filter(food__category = category).count()
        if total > 0:
            raise ValidationError({
            "detail":"The food of this category exists in the order."
    })
        category.delete()
        return Response({
            "details":"Category deleted."
    }, status = status.HTTP_404_NOT_FOUND)
        
class Foodviewset(ModelViewSet):
    queryset = Food.objects.select_related('category').all()
    serializer_class = FoodSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']



# class CategoryView(ListAPIView, CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    # def get(self, request):
    #     category = Category.objects.all()
    #     serializer = CategorySerializer(category, many = True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = CategorySerializer(data = request.data)
    #     serializer.is_valid(raise_exception= True)
    #     serializer.save()
    #     return Response({
    #         'details':"New category added."
    #     }, status = status.HTTP_201_CREATED)
        
        
        
# class CategoryDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = 'pk'
    
    
    
    
    # def get(self, request, id):
    #        category = Category.objects.get(id = id)
    #        serializer = CategorySerializer(category)
    #        return Response(serializer.data) 
    
    # def put(self, request, id):
    #         category = Category.objects.get(id = id)
    #         serializer = CategorySerializer(category, data = request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)
        
    # 
             
# @api_view(['Get','POST'])
# def category_list(request):
#     if request.method=='GET':
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # data =  request.data
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception= True)
#         serializer.save()
#         return Response({
#             'details':"New category added."
#         })
        
        
# @api_view(['GET','DELETE', 'PUT'])       
# def category_details(request, id):
#     category = Category.objects.get(id = id)
#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         total = OrderItem.objects.filter(food__category = category).count()
#         if total > 0:
#             raise ValidationError({
#                 "detail":"The food of this category exists in the order."
#             })
#         category.delete()
#         return Response({
#             "details":"Category deleted."
#         })
#     elif request.method == 'PUT':
#         serializer = CategorySerializer(category, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
        
    
        
        
        