from django.urls import path
from expense_management.api.views import CategoryList, CategoryGetUpdate, CategoryCreate

urlpatterns = [
    path('categories', CategoryList.as_view(), name='categories'),
    path('category', CategoryCreate.as_view(), name = 'category-create'),
    path('category/<int:pk>',CategoryGetUpdate.as_view(), name='category-get-update')
]
