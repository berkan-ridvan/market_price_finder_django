from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'price', 'rating', 'market_name')
    list_filter = ('type', 'market_name')
    search_fields = ('title', 'description')
    list_editable = ('price', 'rating')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Ürün Bilgileri', {
            'fields': ('title', 'type', 'description', 'price', 'rating', 'market_name')
        }),
        ('Resim', {
            'fields': ('image',)
        }),
        ('Tarih', {
            'fields': ('created_at',)
        }),
    )
