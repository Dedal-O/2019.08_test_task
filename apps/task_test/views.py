from rest_framework import viewsets
from .serializers import *
from .models import EnterpriseModel, CityAreaModel, ProductItemBaseModel, ProductItemEnterpriseModel
from .filters import *

__all__ = ('CityAreaViewset', 'EnterpriseViewset', 'ProductItemBaseViewset', )


class CityAreaViewset(viewsets.ModelViewSet):
    """
    Viewset для API, модель Район города
    """
    queryset = CityAreaModel.objects.all()
    serializer_class = CityAreaSerializer


class EnterpriseViewset(viewsets.ModelViewSet):
    """
    Viewset для API, модель Предприятие
    """
    queryset = EnterpriseModel.objects.all()
    serializer_class = EnterpriseSerializer
    filterset_class = EnterpriseFilter


class ProductItemBaseViewset(viewsets.ModelViewSet):
    """
    Viewset для API, модель Товар в номенклатуре
    """
    queryset = ProductItemBaseModel.objects.all()
    serializer_class = ProductItemBaseSerializer


class ProductItemEnterpriseViewset(viewsets.ModelViewSet):
    """
    Viewset для API, модель Товарная Единица в контексте предприятия
    """
    queryset = ProductItemEnterpriseModel.objects.all()
    serializer_class = ProductItemEnterpriseSerializer
