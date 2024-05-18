import json

from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    """
    Контроллер, который отвечает за отображение домашней страницы
    """
    product = Product.objects.all()
    context = {'products': product}
    return render(request, "products_list.html", context)


def contacts(request):
    """
    Контроллер, который отвечает за отображение контактной информации
    """
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        contacts_dict = {"name": name, "phone": phone, "message": message[:]}

        with open("contacts.json", "w") as file:
            json.dump(contacts_dict, file, ensure_ascii=False, indent=4)

    return render(request, 'contacts.html')


def products_detail(request, pk):
    """
    Контроллер, который отвечает за отображение информации о конкретном продукте
    """
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products_detail.html', context)
