from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_categories_from_cache():
    """
    Получение категорий из кэша. Если кэш пуст,то получение из БД.
    """
    if not CACHE_ENABLED:
        return Category.objects.all()
    else:
        key = 'categories_list'
        categories = cache.get(key)
        if categories is not None:
            return categories
        else:
            categories = Category.objects.all()
            cache.set(key, categories)
            return categories
