from django.db import models
from django.urls import reverse


class Category(models.Model):
    object = None
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)


def __str__(self):
    return self.name


def get_absolute_path(self):
    return reverse('shop:product_index_by_category', cargs=[self.slug])


class Meta:
    ordering = ('name',)
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'


class Product(models.Model):
    objects = None
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=100, db_index=True, verbose_name='Ссылк')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обнавлен')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_path(self):
        return reverse('shop:product_about', args=[self.id, self.slug])

    def __str__(self):
        return self.name

# class Comment(models.Model):
#    text = models.TextField()
#    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#    product = models.ForeignKey(Product, on_delete=models.CASCADE)
