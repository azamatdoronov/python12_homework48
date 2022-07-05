# Generated by Django 4.0.5 on 2022-07-05 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'разное'), ('bakery', 'выпечка'), ('sweets', 'сладости'), ('drinks', 'напитки'), ('veggies', 'овощи')], default='other', max_length=20, verbose_name='Категория'),
        ),
    ]
