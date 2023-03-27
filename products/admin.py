from django.contrib import admin
from .models import Category, Product, Contact

admin.site.register(Category)
admin.site.register(Product)


class ContactAdmin(admin.ModelAdmin):
    list_display = 'name', 'phone_number', 'processed', 'data_added',
    list_editable = 'processed',


admin.site.register(Contact, ContactAdmin)
