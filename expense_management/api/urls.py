from django.urls import path
from expense_management.api.views import CategoryList

urlpatterns = [
    path('categories',CategoryList.as_view(), name='categories')
]
