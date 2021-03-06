"""project_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from apps.task_test.views import CityAreaViewset, ProductItemBaseViewset, ProductItemEnterpriseViewset, \
                                 EnterpriseViewset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

router = routers.DefaultRouter()
router.register(r'api/districts', CityAreaViewset)
router.register(r'api/nomenclature', ProductItemBaseViewset)
router.register(r'api/product_items', ProductItemEnterpriseViewset)
router.register(r'api/organizations', EnterpriseViewset)

urlpatterns += router.urls
