from django_filters.rest_framework import FilterSet
from django_filters import CharFilter, RangeFilter
from .models import EnterpriseModel

__all__ = ('EnterpriseFilter', )


class EnterpriseFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', distinct=True)
    product_title = CharFilter(field_name='products__product__title__title', lookup_expr='iexact', distinct=True)
    product_category = CharFilter(field_name='products__product__category__title', lookup_expr='icontains', distinct=True)
    product_price = RangeFilter(field_name='products__price', distinct=True)

    class Meta:
        model = EnterpriseModel
        fields = ['title', 'city_areas', ]
