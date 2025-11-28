from django.contrib import admin

from django.contrib import admin
from .models import Product, UserProfile

# Configuración de administración para Productos
class ProductAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista
    list_display = ('name', 'price', 'stock', 'category')

    # Campo de Búsqueda 
    search_fields = ('name', 'category')

    # Opciones de Filtro 
    list_filter = ('category', 'stock')

# Configuración de administración para Usuarios
class UserProfileAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista
    list_display = ('email', 'name', 'role', 'created_at')

    # Campo de Búsqueda 
    search_fields = ('email', 'name', 'role')

    # Opciones de Filtro 
    list_filter = ('role', 'created_at')

# Registrar los modelos 
admin.site.register(Product, ProductAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
