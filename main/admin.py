from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] #какие категории будут отображаться
    prepopulated_fields = { #фильтры по которым можно будет фильтровать наши продукты
        'slug' : ('name', )
        }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created_at', 'updated_at'] #то что отображаеться в категории продукты
    list_filter = ['available', 'created_at', 'updated_at', 'category'] #фильтры в админке

    list_editable = ['price', 'available']
    prepopulated_fields = { 
        'slug' : ('name', )
        }