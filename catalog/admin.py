from django.contrib import admin

from .models import Store, Category, Product


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "store",
    )

    list_filter = (
        "store",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "store",
        "category",
        "price",
        "stock",
        "available",
    )

    list_filter = (
        "store",
        "category",
        "available",
    )

    search_fields = (
        "name",
        "description",
    )

    list_editable = (
        "price",
        "stock",
        "available",
    )