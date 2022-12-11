from __future__ import unicode_literals
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.
# admin.site.register(emp_status)
admin.site.register(emp_shift)
admin.site.register(emp_statustype)
# admin.site.register(emp)
admin.site.register(Csv)
admin.site.register(record_delete)
admin.site.register(record_created)




class BookAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name','emp_shift')
admin.site.register(emp, BookAdmin)



# class StudentResource(resources.ModelResource):
#     class Meta:
#         model = emp_status

# class StudentAdmin(ImportExportModelAdmin):
#    resource_class = StudentResource

# admin.site.register(emp_status,StudentAdmin,BookAdmin)


# class ProductResource(resources.ModelResource):

#     class Meta:
#         model = emp_status
#         exclude = ('id',)


# class ProductExportImportAdmin(ImportExportModelAdmin):
#     resource_class = ProductResource


# class ProductAdmin(admin.ModelAdmin):
#     search_fields = ['emp', 'Date','status']

# admin.site.register(emp_status, ProductAdmin, ProductExportImportAdmin)



class ProductResource(resources.ModelResource):

    class Meta:
        model = emp_status
        fields  = ('emp__emp_name', 'Date','status__status')
        exclude = ('id')


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProductResource
    list_display = ('emp', 'Date','status')
    search_fields = ['emp']

admin.site.register(emp_status, ProductAdmin)