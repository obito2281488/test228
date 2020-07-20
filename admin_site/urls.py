from django.urls import path

from .views import CategoryCreate, categories

urlpatterns = [
    path('categories/create', CategoryCreate.as_view(), name="categories.create"),
    path('categories', categories, name="categories"),
]