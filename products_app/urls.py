from django.urls import path
from products_app.views import ProductViewSet, BrandViewSet, BranchViewSet, CategoryViewSet, MainCategoryViewSet

urlpatterns = [
    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}, name='Подкатегории')),
    path('main_category/', MainCategoryViewSet.as_view({'get': 'list', 'post': 'create'}, name='Категории')),
    path('brand/', BrandViewSet.as_view({'get': 'list', 'post': 'create'}, name='Бренды')),
    path('branch/', BranchViewSet.as_view({'get': 'list', 'post': 'create'}, name='Филиалы')),
    path('product/', ProductViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'}, name='Товары')),
    path('product/<int:pk>/', ProductViewSet.as_view(
        {
            'get': 'retrieve',
            'delete': 'destroy',
            'put': 'update'
        },
        name='Товар по ID'
         )),

]