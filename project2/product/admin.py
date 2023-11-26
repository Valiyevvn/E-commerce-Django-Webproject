from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import Category,Product,Images,Comment
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = Images
    extra= 5

#class CategoryAdmin(admin.ModelAdmin):
    #list_display = ['title','status','image_tag']
    #list_filter = ['status']
    #readonly_fields = ('image_tag',)

from django.utils.html import format_html

class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','amount','status','image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status','category']
    inlines = [ProductImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','product','image_tag',]
    readonly_fields = ('image_tag',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','product','user','status']
    list_filter = ['status']
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)
