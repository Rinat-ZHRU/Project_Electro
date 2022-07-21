from django.db import models


class Main_Category(models.Model):
    """Категории"""
    main_category_name = models.CharField('Главная категория', max_length=250)
    main_category_description = models.TextField('Описание', null=True, blank=True)  # описание категории
    image = models.ImageField('Фото', null=True, blank=True)  # изображение

    class Meta:
        ordering = ['main_category_name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def clean(self):
        self.main_category_name = self.main_category_name.capitalize()  # исправление букв на первую заглавную

    def __str__(self):
        return self.main_category_name


class Category(models.Model):
    """Подкатегории"""
    category_name = models.CharField('Подкатегория', max_length=250)  # наименование категории
    category_description = models.TextField('Описание', null=True, blank=True)  # описание категории
    image = models.ImageField('Фото', null=True, blank=True)  # изображение
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE)  # подкатегории к категориям

    class Meta:
        ordering = ['category_name']
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def clean(self):
        self.category_name = self.category_name.capitalize()  # исправление букв на первую заглавную

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    """Бренды товаров"""
    brand_name = models.CharField('Название бренда', max_length=50, null=True)
    brand_description = models.TextField('Описание бренда', null=True, blank=True)
    image = models.ImageField('Фото', null=True, blank=True)  # изображение


    class Meta:
        ordering = ['brand_name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    """Товары"""

    UNIT_CHOICES = (          # выборка
        ('метры', 'м'),
        ('штуки', 'шт'),
    )

    name = models.CharField('Наименование товара', max_length=250)  # наименование товара
    description = models.TextField('Описание товара', null=True, blank=True)  # описание товара
    price = models.DecimalField('Цена товара', max_digits=8, decimal_places=2)  # цена
    sale = models.DecimalField('Скидка', max_digits=2, decimal_places=0)   # скидка
    number = models.DecimalField('Количество', max_digits=8, decimal_places=2)  # количество товара
    unit = models.CharField('Единица измерения', max_length=6, choices=UNIT_CHOICES)
    image = models.ImageField('Фото', null=True, blank=True)  # изображение
    available = models.BooleanField('Наличие', default=True)  # наличие
    created = models.DateTimeField('Дата создания', auto_now_add=True)  # дата создания
    updated = models.DateTimeField('Дата обновления', auto_now=True)  #  дата обновления
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # категории к товарам
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # бренды к товарам

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Branch(models.Model):  # филиалы
    """Филиалы"""
    branch_name = models.CharField('Название филиала', max_length=250)
    br_address = models.CharField('Адрес филиала', max_length=255)
    br_email = models.EmailField('Электронная почта')
    br_telephone = models.CharField('Телефоны', max_length=100)
    br_image = models.ImageField('Фото', null=True, blank=True)

    class Meta:
        ordering = ['branch_name']
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return self.branch_name