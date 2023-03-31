from rest_framework import serializers
from expense_management.models import Category
from django_enum_choices.fields import EnumChoiceField

#Category
class CategorySerializer(serializers.ModelSerializer):
    #type = serializers.SerializerMethodField()
    #type = serializers.CharField(source='type.value')
    type = serializers.ChoiceField(source = 'type.value' ,choices=[(choice.value, choice.name) for choice in Category.TypeCategory])
    #type = serializers.ChoiceField(choices=[(choice.name, choice.value) for choice in Category.TypeCategory])

    class Meta:
        model = Category
        fields = '__all__' #['id', 'name', 'description', 'type', 'parent_category']
        
    def get_type(self, obj):
        return obj.get_type_display()
    
    def getCategoryType(strType: str):
        #Si no puede retornar un TypeCategory, devuelve un string vacio
        #valor_por_defecto = ""
        
        if len(strType) > 0:
            if strType.upper() == Category.TypeCategory.INGRESOS.value:
                return Category.TypeCategory.INGRESOS
            elif strType.upper() == Category.TypeCategory.GASTOS.value:
                return Category.TypeCategory.GASTOS
            
        return Category.TypeCategory.INGRESOS
    
    def create(self, validated_data):
        str_type = str(validated_data.pop('type').get('value'))

        type_value = CategorySerializer.getCategoryType(str_type)
   
        category = Category.objects.create(type=type_value, **validated_data)
        return category
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.parent_category = validated_data.get('parent_category', instance.parent_category)

        # Manejo del campo 'type'
        str_type = str(validated_data.get('type', '').get('value'))
    
        if str_type and len(str_type) > 0 :
                   
            if str_type.upper() == Category.TypeCategory.INGRESOS.value:
                instance.type = Category.TypeCategory.INGRESOS
            elif str_type.upper() == Category.TypeCategory.GASTOS.value:
                instance.type = Category.TypeCategory.GASTOS
                
        instance.save()
        return instance
    
   
    