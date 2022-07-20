
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products_app.urls')),
    # path('brand/', include('products_app.urls')),
    # path('branch/', include('products_app.urls')),
    # path('category/', include('products_app.urls')),
]
