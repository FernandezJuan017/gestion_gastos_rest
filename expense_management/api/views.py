from rest_framework import generics
from expense_management.models import Category
from expense_management.api.serializers import CategorySerializer

#Categories
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer