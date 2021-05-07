from django.contrib import admin
from import_export import resources
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone', 'product_id')

from import_export import resources
class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer


admin.site.register(FileUpload)
