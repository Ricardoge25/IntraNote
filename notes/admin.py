from django.contrib import admin
from .models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')

admin.site.register(Note, NoteAdmin)