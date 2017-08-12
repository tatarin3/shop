# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('customer_name', models.CharField(max_length=64, null=True, default=None, blank=True)),
                ('customer_email', models.EmailField(max_length=254, null=True, default=None, blank=True)),
                ('customer_phone', models.CharField(max_length=32, null=True, default=None, blank=True)),
                ('comments', models.TextField(blank=True, null=True, default=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
            },
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(to='products.Product', null=True, blank=True, default=None)),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'verbose_name': 'Товар',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=24, null=True, default=None, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Статусы',
                'verbose_name': 'Статус',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(to='orders.Status'),
        ),
    ]
