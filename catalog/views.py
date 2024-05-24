from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product, Contact


class ProductListView(ListView):
    """
    Контроллер, который отвечает за отображение списка продуктов
    """
    model = Product


class ProductDetailView(DetailView):
    """
    Контроллер, который отвечает за отображение информации о конкретном продукте
    """
    model = Product


class ContactCreateView(CreateView):
    """
    Контроллер, который отвечает за отображение контактной информации
    """
    model = Contact
    fields = (
        "name",
        "phone",
        "message",
    )
    success_url = reverse_lazy("catalog:contacts")
