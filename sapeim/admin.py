from django.contrib import admin
from sapeim import models


@admin.register(models.Element)
class ElementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Bland)
class BlandAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ElementType)
class ElementTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('documento',)


@admin.register(models.Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DetallePrestamo)
class DetallePrestamoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    pass
