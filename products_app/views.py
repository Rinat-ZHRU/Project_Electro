from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from products_app.models import Product, Brand, Branch, Category
from products_app.serializers import ProductSerializer, CategorySerializer, BranchSerializer, BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    lookup_field = 'pk'
    ordering_fields = ['name']
    search_fields = ['name']
    filterset_fields = ['name']

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset =Branch.objects.all().order_by('id')
    serializer_class = BranchSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
