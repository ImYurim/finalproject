from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import Company, Patent


class CompanyAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


class PatentAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Patent, PatentAdmin)
