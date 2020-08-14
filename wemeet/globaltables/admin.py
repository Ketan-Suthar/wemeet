from django.contrib import admin
from .models import BoardType, Role, DefaultRole
# Register your models here.


@admin.register(BoardType)
class BoardTypeAdmin(admin.ModelAdmin):
	list_display = ['boardTypeId', 'boardType']



@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = ['boardTypeId', 'roleId', 'role']



@admin.register(DefaultRole)
class DefaultRoleAdmin(admin.ModelAdmin):
	list_display = ['boardType', 'role']


