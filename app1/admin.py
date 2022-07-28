from django.contrib import admin
from .models import Pro, Product, Signup

admin.site.register(Product)
admin.site.register(Signup)
admin.site.register(Pro)

# Register your models here

class Proadmin(admin.ModelAdmin):
    list_display=['Name', 'Price', 'Des', 'Review']
    list_filter=['Name', 'Price', 'Des', 'Review']
#admin.site.register(Proadmin)
