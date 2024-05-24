from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
]
