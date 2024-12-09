from django.contrib import admin
from .models import Category, Product

admin.site.registser(Category)

admin.site.registser(Product)
