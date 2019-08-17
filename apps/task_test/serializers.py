from rest_framework import serializers
from .models import ProductItemEnterpriseModel, ProductItemBaseModel, EnterpriseModel, CityAreaModel


__all__ = ('ProductItemEnterpriseSerializer', 'ProductItemBaseSerializer', 'EnterpriseSerializer',
           'CityAreaSerializer', )


class CityAreaSerializer(serializers.ModelSerializer):
    """
    Район города - для API
    """
    class Meta:
        model = CityAreaModel
        fields = '__all__'


class ProductItemBaseSerializer(serializers.ModelSerializer):
    """
    Подготовка модели Товара из номенклатуры для работы с API
    """
    title = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = ProductItemBaseModel
        fields = '__all__'


class ProductItemEnterpriseSerializer(serializers.ModelSerializer):
    """
    Полный список товаров, присутствующих в карточках Предприятий
    """
    product = serializers.StringRelatedField()
    enterprise = serializers.StringRelatedField()

    class Meta:
        model = ProductItemEnterpriseModel
        fields = '__all__'


class EnterpriseSerializer(serializers.ModelSerializer):
    """
    Подготовка модели предприятие для работы с API
    """
    network_belonged = serializers.StringRelatedField()
    city_areas = serializers.StringRelatedField(many=True)
    products = ProductItemEnterpriseSerializer(many=True, read_only=True)

    class Meta:
        model = EnterpriseModel
        fields = '__all__'
