from django.contrib import admin
from .models import Product, Category, Gender, ProductType, SubCategory

# Register your models here
class ProductAdmin(admin.ModelAdmin):
        fieldsets = (
            (None, {
                'fields': (
                    'sku',
                    ('name', 'product_description'),
                    ('price', 'discount_price'),
                    'image')
            }),
                ('Category Selections', {
                    'classes': ('collapse',),
                    'fields': (
                        'gender',
                        'category',
                        'sub_category',
                        'product_type',
                        ),
            }),
        )


        list_display = (
            'price',
            'discount_price',
            'sku',
            'name',
            'product_description',
            'image',
            )

        ordering = ('sku',)



class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
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
