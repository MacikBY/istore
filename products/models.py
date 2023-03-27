from django.db import models
from django.urls import reverse




class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', unique=True, max_length=255)
    image = models.ImageField(verbose_name='Фотография', upload_to='photos/category/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=255)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    is_available = models.BooleanField(verbose_name='Есть на складе', default=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фотография', upload_to='photos/product/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('price',)

    def get_absolute_url(self):
        print(reverse(viewname='product_detail', kwargs={'pk': self.pk}))
        return reverse(viewname='product_detail', kwargs={'pk': self.pk})


class Contact(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=13, unique=True)
    processed = models.BooleanField(verbose_name='Обработано', default=False)
    data_added = models.DateTimeField(verbose_name='Дата заявки', auto_now_add=True)

    def __str__(self):
        return f'{self.name}----{self.phone_number}'

    class Meta:
        verbose_name = 'Заявка на обратный звонок'
        verbose_name_plural = 'Заявки на обратный звонок'
        ordering = ('data_added',)
