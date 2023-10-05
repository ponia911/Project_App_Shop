from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse

class Category(models.Model):

    object = None
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    def get_absolute_path(self):
        return reverse('shop:product_index_by_category', cargs=[self.slug])

class Meta:
    ordering = ('name',)
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_path(self):
        return reverse('shop:product_about', args=[self.slug])

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

        def __str__(self):
            return self.name

#class Comment(models.Model):
#    text = models.TextField()
#    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#    product = models.ForeignKey(Product, on_delete=models.CASCADE)

