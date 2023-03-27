from django.urls import path
from .views import get_home, get_product, filter_category

urlpatterns = [
    path('', get_home, name='home'),
    path('<int:cat_pk>/', filter_category, name='filter_cat'),
    path('product/<int:pk>', get_product, name='product_detail'),
]
