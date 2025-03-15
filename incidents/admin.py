from django.contrib import admin
from .models import Incident

# Register your models here.
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id_servicio', 'created')
    readonly_fields = ('created', 'updated')

admin.site.register(Incident, IncidentAdmin)