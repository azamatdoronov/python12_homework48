# Generated by Django 4.0.5 on 2022-07-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('bakery', 'выпечка'), ('sweets', 'сладости'), ('drinks', 'напитки'), ('veggies', 'овощи'), ('other', 'Разное')], default='bakery', max_length=20, verbose_name='Категория')),
                ('p_name', models.CharField(default='No Product', max_length=50, verbose_name='Наименование товара')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание товара')),
                ('balance', models.PositiveIntegerField(verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'Список товаров',
                'db_table': 'product',
            },
        ),
    ]
