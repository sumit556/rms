from rest_framework import serializers
from .models import *

# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
    
#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        # fields = '__all__'
        # fields = ['id', 'name']
        
    def save(self, **kwargs):
        validated_data = self.validated_data
        total = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
        if total > 0:
            raise serializers.ValidationError({
                "details":"The Category with this name is already exists."
            })
        category = self.Meta.model(**validated_data)
        return category
        
        
class FoodSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source = 'category'
    )
    class Meta:
        model = Food
        fields = ['id', 'name', 'price', 'price_with_tax', 'category_id', 'category']
        
    def get_price_with_tax(self, food:Food):
        return food.price * 0.13 + food.price