from django.db import models
from django.utils.translation import gettext_lazy as _


__all__ = ('CityAreaModel', 'TradeCategoryModel', 'TradeNetworkModel', 'ProductTitleModel', 'EnterpriseModel',
           'ProductItemBaseModel', 'ProductItemEnterpriseModel', )


class CityAreaModel(models.Model):
    """
    Район города
    """
    title = models.CharField(max_length=255, verbose_name=_('area_title'), unique=True, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('city_area')
        verbose_name_plural = _('city_areas')


class TradeCategoryModel(models.Model):
    """
    Категория товаров
    """
    title = models.CharField(max_length=255, verbose_name=_('trade_category_title'), unique=True, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('trade_category')
        verbose_name_plural = _('trade_categories')


class TradeNetworkModel(models.Model):
    """
    Сеть предприятий
    """
    title = models.CharField(max_length=255, verbose_name=_('trade_network_title'), unique=True, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('trade_network')
        verbose_name_plural = _('trade_networks')


class ProductTitleModel(models.Model):
    """
    Товар, а точнее название
    """
    title = models.CharField(max_length=255, verbose_name=_('product_title'), unique=True, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product_title')
        verbose_name_plural = _('products_titles')


class EnterpriseModel(models.Model):
    """
    Предприятие
    """
    title = models.CharField(verbose_name=_('enterprise_title'), max_length=255, blank=False, null=False)
    description = models.TextField(verbose_name=_('description'), blank=True, null=True)
    network_belonged = models.ForeignKey(to='TradeNetworkModel', verbose_name=_('trade_network'),
                                         blank=False, null=False, on_delete=models.PROTECT)
    city_areas = models.ManyToManyField(to='CityAreaModel', verbose_name=_('city_areas'))

    def __str__(self):
        return f"{self.network_belonged} - {self.title}"

    class Meta:
        verbose_name = _('enterprise')
        verbose_name_plural = _('enterprises')


class ProductItemBaseModel(models.Model):
    """
    Товар для номенклатуры
    """
    title = models.ForeignKey(to='ProductTitleModel', verbose_name=_('product_title'), on_delete=models.PROTECT,
                              blank=False, null=False)
    category = models.ForeignKey(to='TradeCategoryModel', verbose_name=_('trade_category'), on_delete=models.PROTECT,
                                 blank=False, null=False)

    def __str__(self):
        return f"{self.title}, {self.category}"

    class Meta:
        verbose_name = _("product_unit")
        verbose_name_plural = _("product_units")
        unique_together = ('title', 'category', )


class ProductItemEnterpriseModel(models.Model):
    """
    Товарная единица (согласно ТЗ - один и тот же товар продаётся у разных предприятий по разным ценам)
    """
    product = models.ForeignKey(to='ProductItemBaseModel', verbose_name=_("product_item"), on_delete=models.PROTECT,
                                blank=False, null=False)

    price = models.DecimalField(verbose_name=_('price'), default='0.0', max_digits=11, decimal_places=2,
                                blank=False, null=False)
    enterprise = models.ForeignKey(to='EnterpriseModel', verbose_name=_('enterprise'), on_delete=models.PROTECT,
                                   related_name='products', blank=False, null=False, )

    def __str__(self):
        return f"{self.product}, {self.price} ({self.enterprise})"

    class Meta:
        verbose_name = _("product_item")
        verbose_name_plural = _("product_items")
