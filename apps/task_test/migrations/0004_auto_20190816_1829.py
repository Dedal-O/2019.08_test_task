# Generated by Django 2.2.4 on 2019-08-16 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_test', '0003_productitemmodel_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItemBaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='task_test.TradeCategoryModel', verbose_name='trade_category')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task_test.ProductTitleModel', verbose_name='product_title')),
            ],
            options={
                'verbose_name': 'product_item',
                'verbose_name_plural': 'product_items',
            },
        ),
        migrations.CreateModel(
            name='ProductItemEnterpriseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default='0.0', max_digits=11, verbose_name='price')),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task_test.EnterpriseModel', verbose_name='enterprise')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task_test.ProductItemBaseModel', verbose_name='product_item')),
            ],
            options={
                'verbose_name': 'product_item_enterprise',
                'verbose_name_plural': 'product_enterprise',
            },
        ),
        migrations.DeleteModel(
            name='ProductItemModel',
        ),
    ]
