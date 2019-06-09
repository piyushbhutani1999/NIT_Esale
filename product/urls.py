from django.urls import path
from .views import product_detail_view, product_list_view, add_product


urlpatterns = [
    path("", product_list_view, name = 'product_list_view'),
    path("addproduct/",add_product, name = 'add_product'),
    path("<str:slug>/",product_detail_view, name = 'product_detail_view'),
]
