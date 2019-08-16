# Generated by Django 2.2.4 on 2019-08-16 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityAreaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='area_title')),
            ],
            options={
                'verbose_name': 'city_area',
                'verbose_name_plural': 'city_areas',
            },
        ),
        migrations.CreateModel(
            name='EnterpriseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='enterprise_title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('city_areas', models.ManyToManyField(to='task_test.CityAreaModel', verbose_name='city_areas')),
            ],
            options={
                'verbose_name': 'enterprise',
                'verbose_name_plural': 'enterprises',
            },
        ),
        migrations.CreateModel(
            name='ProductTitleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='product_title')),
            ],
            options={
                'verbose_name': 'product_title',
                'verbose_name_plural': 'products_titles',
            },
        ),
        migrations.CreateModel(
            name='TradeCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='trade_category_title')),
            ],
            options={
                'verbose_name': 'trade_category',
                'verbose_name_plural': 'trade_categories',
            },
        ),
        migrations.CreateModel(
            name='TradeNetworkModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='trade_network_title')),
            ],
            options={
                'verbose_name': 'trade_network',
                'verbose_name_plural': 'trade_networks',
            },
        ),
        migrations.CreateModel(
            name='ProductItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default='0.0', verbose_name='price')),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task_test.EnterpriseModel', verbose_name='enterprise')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task_test.ProductTitleModel', verbose_name='product_title')),
            ],
            options={
                'verbose_name': 'product_item',
                'verbose_name_plural': 'product_items',
            },
        ),
        migrations.AddField(
            model_name='enterprisemodel',
            name='network_belonged',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task_test.TradeNetworkModel', verbose_name='trade_network'),
        ),
    ]
