
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',]
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

#def image_show(self, obj):
#    if obj.image:
#        return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
#    return "None"
#image_show.__name__ = "Картинка"


