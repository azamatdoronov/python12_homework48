# Generated by Django 4.0.5 on 2022-08-23 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_order_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('order_list', 'Просмотр заказов')], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
