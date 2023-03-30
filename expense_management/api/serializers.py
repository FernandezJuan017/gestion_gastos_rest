from rest_framework import serializers
from expense_management.models import Category

#Category
class CategorySerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'
        
    def get_type(self, obj):
        return obj.get_type_display()
    