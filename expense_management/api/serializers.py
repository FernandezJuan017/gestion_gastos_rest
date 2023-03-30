from rest_framework import serializers
from expense_management.models import Category
from django_enum_choices.fields import EnumChoiceField

#Category
class CategorySerializer(serializers.ModelSerializer):
    #type = serializers.SerializerMethodField()
    #type = serializers.CharField(source='type.value')
    type = serializers.ChoiceField(source = 'type.value' ,choices=[(choice.value, choice.name) for choice in Category.TypeCategory])
    class Meta:
        model = Category
        fields = '__all__'
        
    def get_type(self, obj):
        return obj.get_type_display()
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.parent_category = validated_data.get('parent_category', instance.parent_category)

        # Manejo del campo 'type'
        str_type = str(validated_data.get('type', '').get('value'))
    
        if str_type and len(str_type) > 0 :
            print(Category.TypeCategory.INGRESOS)
            print(str(Category.TypeCategory.INGRESOS.GASTOS.value))
                   
            
            if str_type.upper() == Category.TypeCategory.INGRESOS.value:
                print(str_type)
                instance.type = Category.TypeCategory.INGRESOS
            elif str_type.upper() == Category.TypeCategory.GASTOS.value:
                print(str_type)
                instance.type = Category.TypeCategory.GASTOS
                
        instance.save()
        return instance
    