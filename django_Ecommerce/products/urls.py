from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('' , views.product_list, name='product_list'),
    path('<slug:category_slug>/' , views.product_list , name='product_list_by_category'),
    path('product/<int:id>/<lug:slug>/' , views.product_details , name='product_detail'),
]