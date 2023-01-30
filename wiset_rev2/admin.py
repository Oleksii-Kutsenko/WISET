from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "category",
        "in_fridge",
        "season_start",
        "season_end",
    )
    list_filter = (
        "category",
        "in_fridge",
    )
    ordering = ("in_fridge",)
    search_fields = (
        "name",
        "category",
    )
