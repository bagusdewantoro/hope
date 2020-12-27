from django.contrib import admin
from .models import Product, Size, Type, StockLog


admin.site.register(Size)
admin.site.register(Type)

#===================================================================
@admin.register(StockLog)
class StockLogAdmin(admin.ModelAdmin):
    list_display = ('product', 'production_date', 'quantity', 'sold', 'price')

#===================================================================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'product_size', 'figure1_preview', 'figure2_preview')

    # tampilkan gambar di admin:
    readonly_fields = ('figure1_preview', 'figure2_preview')

    def figure1_preview(self, obj):
        return obj.figure1_preview
    figure1_preview.short_description = 'Image 1'
    figure1_preview.allow_tags = True

    def figure2_preview(self, obj):
        return obj.figure2_preview
    figure2_preview.short_description = 'Image 2'
    figure2_preview.allow_tags = True
