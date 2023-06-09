from django.contrib import admin
from .models import Category, Product, Review, ProductSize


class ProductSizeInline(admin.TabularInline):
    model = ProductSize


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "image",
    )

    ordering = ("sku",)
    inlines = [ProductSizeInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'comment')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
