from rest_framework import serializers
from expense_management.models import Category_Type, Category

#Category Type
class CategoryTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category_Type
        fields = '__all__'
        
#Category
class CategorySerializer(serializers.ModelSerializer):
    #type = CategoryTypeSerializer()
    class Meta:
        model = Category
        fields = '__all__' #['id', 'name', 'description', 'type', 'parent_category']
        
        
        
    
   
    