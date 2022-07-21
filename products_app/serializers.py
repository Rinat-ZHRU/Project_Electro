from rest_framework import serializers
from products_app.models import Product, Branch, Brand, Category, Main_Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # все поля

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'  # все поля

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'  # все поля

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # все поля

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Main_Category
        fields = '__all__'  # все поля