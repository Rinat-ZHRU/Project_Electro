from django.contrib import admin
from products_app.models import Branch, Category, Product, Brand, Main_Category

admin.site.register(Branch)
admin.site.register(Category)
admin.site.register(Main_Category)
admin.site.register(Product)
admin.site.register(Brand)

