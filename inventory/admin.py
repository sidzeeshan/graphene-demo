from django.contrib import admin
from inventory.models import Product, Family, Location, Transaction
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class FamilyResource(resources.ModelResource):

    class Meta:
        model = Family


class FamilyAdmin(ImportExportModelAdmin):
    resource_class = FamilyResource


admin.site.register(Family, FamilyAdmin)


class LocationResource(resources.ModelResource):

    class Meta:
        model = Location


class LocationAdmin(ImportExportModelAdmin):
    resource_class = LocationResource


admin.site.register(Location, LocationAdmin)


class ProductResource(resources.ModelResource):

    class Meta:
        model = Product


class ProductAdmin(ImportExportModelAdmin):
    raw_id_fields = ['family', 'location']
    search_fields = ['id']
    resource_class = ProductResource


admin.site.register(Product, ProductAdmin)


class TransactionResource(resources.ModelResource):

    class Meta:
        model = Transaction


class TransactionAdmin(ImportExportModelAdmin):
    raw_id_fields = ['product']
    search_fields = ['id']
    list_filter = ('reason', ('date', DateRangeFilter))
    resource_class = TransactionResource


admin.site.register(Transaction, TransactionAdmin)
