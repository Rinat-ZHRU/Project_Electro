from django.db import models


class Branch(models.Model):  # филиалы
    """Филиалы"""
    branch_name = models.CharField(max_length=250)  # наименование филиала
    br_address = models.CharField(max_length=255)
    br_email = models.EmailField()
    br_telephone = models.CharField(max_length=100)
    br_image = models.ImageField(null=True, blank=True)  # фото филиала

    class Meta:
        ordering = ['branch_name']
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return self.branch_name


class Category(models.Model):
    """Категории"""
    category_name = models.CharField(max_length=250)  # наименование категории
    category_description = models.TextField(null=True, blank=True)  # описание категории

    class Meta:
        ordering = ['category_name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    """Бренды товаров"""
    brand_name = models.CharField(max_length=50, null=True)
    brand_description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['brand_name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    """Товары"""
    UNIT_METER = 'м'
    UNIT_NUMBERS = 'шт'

    UNIT_CHOICES = (
        (UNIT_METER, 'метр'),
        (UNIT_NUMBERS, 'штук'),
    )

    name = models.CharField(max_length=250)  # наименование товара
    description = models.TextField(null=True, blank=True)  # описание товара
    price = models.DecimalField(max_digits=8, decimal_places=2)  # цена
    sale = models.DecimalField(max_digits=2, decimal_places=0)   # скидка
    number = models.DecimalField(max_digits=8, decimal_places=2)  # количество товара
    unit = models.CharField(max_length=6, choices=UNIT_CHOICES)
    image = models.ImageField(null=True, blank=True)  # изображение
    available = models.BooleanField(default=True)  # наличие
    created = models.DateTimeField(auto_now_add=True)  # дата создания
    updated = models.DateTimeField(auto_now=True)  #  дата обновления
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)  # один ко многим филиалы к товарам
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # категории к товарам
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # бренды к товарам

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name