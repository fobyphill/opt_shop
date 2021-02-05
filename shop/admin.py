from django.contrib import admin
from .models import user

def set_active_user(modeladmin, request, queryset):
    queryset.update(is_active=True)
set_active_user.short_description = "Сделать активными"

def set_passive_user(modeladmin, request, queryset):
    queryset.update(is_active=False)
set_passive_user.short_description = "Сделать неактивными"

# class ActivePassiveListFilter(admin.SimpleListFilter):
#     title = ("Модерация")
#     parameter_name = 'is_acive'

class ListAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'is_active']
    ordering = ['is_active']
    list_filter = ('is_active',)
    actions = [set_active_user, set_passive_user]
    search_fields = ['first_name', 'last_name',]

admin.site.register(user, ListAdmin)

