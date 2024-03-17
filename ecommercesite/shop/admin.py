from django.contrib import admin
from .models import Products, Order

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "XYZ Shop"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

    list_display = ('name', 'price', 'discount_price', 'category', 'image',)
    search_fields = ('name', 'category',)
    actions = ('change_category_to_default',)
    list_editable = ('discount_price',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
