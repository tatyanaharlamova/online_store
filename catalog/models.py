from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание товара",
        null=True,
        blank=True,
    )
    preview = models.ImageField(
        upload_to="products/photo",
        verbose_name="Изображение",
        help_text="Добавьте изображение товара",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию товара",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.PositiveIntegerField(verbose_name="Цена", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]


class Contact(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя",
    )
    phone = models.CharField(
        max_length=50,
        verbose_name="Телефон",
        null=True,
        blank=True,
    )
    message = models.TextField(
        verbose_name="Сообщение",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
