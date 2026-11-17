from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Genero, Editorial, Autor, Libro, Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Datos adicionales", {"fields": ("telefono", "fecha_nacimiento")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Datos adicionales", {"fields": ("telefono", "fecha_nacimiento")}),
    )

admin.site.register(Genero)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Libro)