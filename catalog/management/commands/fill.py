import json

from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """
        Получение данных из фикстур с категориями
        """
        with open("categories.json", encoding='utf-8') as file:
            categories = json.load(file)
            return categories

    @staticmethod
    def json_read_products():
        """
        Получение данных из фикстур с продуктами
        """
        with open("products.json", encoding='utf-8') as file:
            products = json.load(file)
            return products

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'], name=category['fields']['name'],
                         description=category['fields']["description"])
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product['pk'], name=product['fields']['name'], description=product["fields"]["description"],
                        category=Category.objects.get(pk=product["fields"]["category"]),
                        price=product["fields"]["price"], created_at=product["fields"]["created_at"],
                        updated_at=product["fields"]["updated_at"]))
        Product.objects.bulk_create(product_for_create)
