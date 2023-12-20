from django.contrib import admin
from .models import Product, Category, Gender, ProductType, SubCategory

# Register your models here
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )     

class ProductTypeAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class GenderAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
