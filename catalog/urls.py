from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView,
                           ContactCreateView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
]
