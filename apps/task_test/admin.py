from django.contrib import admin
from django.db import models
from django.forms import NumberInput, Textarea
from nested_admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline
from .models import *

common_field_overrides = {
    models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 90})},
}


class CityAreaAdmin(admin.ModelAdmin):
    """
    Район города в админке
    """
    list_display = ['id', 'title', ]
    list_display_links = ['id', 'title', ]
    search_fields = ['id', 'title']
    readonly_fields = ['id', ]
    fields = ['id', 'title', ]


class TradeCategoryAdmin(admin.ModelAdmin):
    """
    Торговая категория в админке
    """
    list_display = ['id', 'title', ]
    list_display_links = ['id', 'title', ]
    search_fields = ['id', 'title']
    readonly_fields = ['id', ]
    fields = ['id', 'title', ]


class ProductTitleAdmin(admin.ModelAdmin):
    """
    Названия товаров в админке
    """
    formfield_overrides = common_field_overrides
    list_display = ['id', 'title', ]
    list_display_links = ['id', 'title', ]
    search_fields = ['id', 'title']
    readonly_fields = ['id', ]
    fields = ['id', 'title', ]


class ProductItemBaseAdmin(admin.ModelAdmin):
    """
    Единица товара отдельным списком
    """
    list_display = ['id', 'title', 'category', ]
    list_display_links = ['id', 'title', 'category', ]
    fields = ['id', 'title', 'category', ]
    readonly_fields = ['id', ]
    autocomplete_fields = ['title', 'category', ]
    search_fields = ['title', 'category']


class ProductItemInline(NestedTabularInline):
    """
    Единица товара в контексте предприятия
    """
    formfield_overrides = {
        models.DecimalField: {'widget': NumberInput(attrs={'step': 1, })},
    }
    model = ProductItemEnterpriseModel
    fields = ['product', 'price', ]
    autocomplete_fields = ['product', ]
    extra = 1


class EnterpriseAdmin(NestedModelAdmin):
    """
    Предприятие в админке, как отдельный список
    """
    formfield_overrides = common_field_overrides
    list_display = ['id', 'title', 'network_belonged', ]
    list_display_links = ['id', 'title', ]
    fields = ['id', 'title', 'network_belonged', 'city_areas', 'description', ]
    readonly_fields = ['id', ]
    search_fields = ['title', 'network_belonged', 'city_areas', ]
    autocomplete_fields = ['network_belonged', 'city_areas', ]
    inlines = [ProductItemInline, ]


class EnterpriseInline(NestedStackedInline):
    """
    Предприятие в админке, как вложение в Сеть предприятий
    """
    formfield_overrides = common_field_overrides
    model = EnterpriseModel
    extra = 1
    inlines = [ProductItemInline, ]
    fields = ['title', 'network_belonged', 'city_areas', 'description', ]
    autocomplete_fields = ['network_belonged', 'city_areas', ]


class TradeNetworkAdmin(NestedModelAdmin):
    """
    Сеть предприятий в админке
    """
    list_display = ['id', 'title', ]
    list_display_links = ['id', 'title', ]
    search_fields = ['title']
    readonly_fields = ['id', ]
    fields = ['id', 'title', ]
    inlines = [EnterpriseInline, ]


admin.site.register(CityAreaModel, CityAreaAdmin)
admin.site.register(TradeCategoryModel, TradeCategoryAdmin)
admin.site.register(ProductTitleModel, ProductTitleAdmin)
admin.site.register(ProductItemBaseModel, ProductItemBaseAdmin)
admin.site.register(EnterpriseModel, EnterpriseAdmin)
admin.site.register(TradeNetworkModel, TradeNetworkAdmin)
