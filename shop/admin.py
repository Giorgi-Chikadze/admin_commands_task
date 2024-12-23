from django.contrib import admin
from shop.models import Item, Category, Tag


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


class TagInline(admin.StackedInline):
    model = Item.tags.through
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']
    ordering = ['name']
    inlines = [ItemInline]   


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')
    search_fields = ['name', 'description']
    ordering = ['-price']
    inlines = [TagInline]


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

