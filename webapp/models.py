from django.db import models

CATEGORY_CHOICES = [('bakery', 'выпечка'), ('sweets', 'сладости'),
                    ('drinks', 'напитки'), ('veggies', 'овощи'), ('other', 'разное')]


class Product(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name="Категория")
    p_name = models.CharField(max_length=100, null=False, blank=False, default="No Product",
                              verbose_name="Имя товара")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    balance = models.IntegerField(verbose_name="Остаток")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def str(self):
        return f"{self.id}. {self.p_name}: {self.category} {self.balance} {self.price}"

    class Meta:
        db_table = "product"
        verbose_name = "товар"
        verbose_name_plural = "Список товаров"
