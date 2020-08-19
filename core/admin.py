from django.contrib import admin
#from import_export.admin import ImportExportModelAdmin
from .models import Contato

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone']


admin.site.register(Contato, ContatoAdmin)
