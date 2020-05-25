from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import Company


class CompanyAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
